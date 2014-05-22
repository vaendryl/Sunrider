## This file declares all the classes in the battle engine
# 1) battle manager class
# 2) status displayable class
# 3) Action objects (these gets activated when you click a button)
# 4) battleship blueprint class
# 5) Weapon blueprint class
# 6) library (specific ships/weapons)


init -5:
    image vanguard_cannon:
        'Battle UI/sunrider vanguard.jpg'
#        xcenter ycenter

init -2 python:

        ##here the Battle class gets defined. it forms the core and spine of the entire combat engine.
        ##it gets initialized into an instance called BM, short for battlemanager
    class Battle(store.object): # handles managing a list of all battle units, handles turns and manages enemy AI
        def __init__(self):
            self.save_version = config.version
            self.ships = []
            self.covers = []
            self.missiles = []
            self.selected = None
            self.hovered = None
            self.target = None
            self.selectedmode = False
            self.targetingmode = False
            self.moving = False
            self.phase = 'Player'
            self.weaponhover = None
            self.active_weapon = None
            self.mission = 1
            self.turn_count = 1
            self.grid = []
            self.cmd = 0
            self.vanguard = False
            self.money = 0
            self.showing_orders = False
            self.orders = {
                'FULL FORWARD':[500,'full_forward'],
                'REPAIR DRONES':[500,'repair_drones'],
                'VANGUARD CANNON':[1500,'vanguard_cannon'],
                }
            self.order_used = False
              #environment modififiers are initialized here and can be changed later
            self.environment = {
                'accuracy':100,
                'turndamage':0,
                'damage':0,
                'energyregen':0,
                }
            self.battlemode = False
            self.edgescroll = (0,0)
            self.xadj = ui.adjustment() #used by the viewport in the battlescreen
            self.yadj = ui.adjustment()
            self.draggable = True
              #stores a matrix of the grid to keep track of what spots are free. False is free, True is occupied
            for a in range(GRID_SIZE[0]):
                self.grid.append([False]*GRID_SIZE[1])
            self.battle_bg = "Background/space{!s}.jpg".format(renpy.random.randint(1,9))

        def select_ship(self,ship,play_voice = True):
            self.selectedmode = True
            self.selected = ship
            if ship.faction == 'Player' and play_voice:
                a = renpy.random.randint(0,len(ship.selection_voice)-1)
                renpy.music.play('sound/Voice/{}'.format(ship.selection_voice[a]),channel = ship.voice_channel)
                del a
            renpy.show_screen('commands')
            ship.movement_tiles = get_movement_tiles(ship)

        def unselect_ship(self,ship):
            renpy.hide_screen('commands')
            self.selectedmode = False
            self.selected = None
            self.targetingmode = False
            ship.movement_tiles = []

        def start(self):
            battlemode(self)
            update_stats()  #used to update some attributes like armor and shields
            renpy.show_screen('battle_screen')
            renpy.jump('mission{}'.format(self.mission))

        def battle(self):
            #battle_screen should be shown, and ui.interact waits for your input. 'result' stores the value return from the Return actionable in the screen
            result = ui.interact()

            #sanity check
            for ship in BM.ships:
                if ship.hp <= 0:
                    destroyed_ships.append(ship)
                    if ship in player_ships:
                        player_ships.remove(ship)
                    if ship in enemy_ships:
                        enemy_ships.remove(ship)
                    if ship in BM.ships:
                        BM.ships.remove(ship)

            if result == 'anime':
                try:
                    renpy.call_in_new_context('atkanim_blackjack_melee') #'atkanim_blackjack_melee')
                except:
                    show_message('animation label does not exist!')

            if result == 'cheat':
                BM.cmd = 99999
                for ship in player_ships:
                    ship.en = 9999

            if result == 'I WIN':
                instant_win()

            if result == 'deselect':
                if self.active_weapon != None:
                    self.active_weapon = None
                    self.targetingmode = False
                    self.weaponhover = None
                elif self.selected != None:
                    self.unselect_ship(self.selected)
                else:
                    pass

            if result == "next ship":
                if self.selected == None:
                    self.select_ship(sunrider)
                    return
                if self.selected != None and len(player_ships) > 1:
                    if self.selected.faction == 'Player':
                        index = player_ships.index(self.selected)
                        if index == (len(player_ships)-1):
                            index = 0
                        else:
                            index += 1
                        self.select_ship(player_ships[index])

            if result == "previous ship":
                if self.selected != None and len(player_ships) > 1:
                    if self.selected.faction == 'Player':
                        index = player_ships.index(self.selected)
                        if index == 0:
                            index = len(player_ships)-1
                        else:
                            index -= 1
                        self.select_ship(player_ships[index])

            if result[0] == "zoom":
                zoom_handling(result,self) #see funtion.rpy how this is handled. it took a LONG time to get it to a point I am happy with
                if self.selectedmode: self.selected.movement_tiles = get_movement_tiles(self.selected)

            if result[0] == 'selection':  #this means you clicked on a ship, which could mean various things depending on circumstance.
                self.target = result[1]
                self.hovered = None

                #if no ship is currently selected select the ship that was just clicked on.
                if self.selected == None:
                    self.select_ship(self.target)
                    return

                #you do not have a weapon active.
                if not self.targetingmode:

                    #did you select the active ship?
                    if self.target == self.selected:
                        self.unselect_ship(self.selected)
                    else:
                        self.select_ship(self.target)
                    return

                #you do have a weapon active.
                else:
                    weapon = self.active_weapon
                    self.targetingmode = False

                    #did you click the currently selected ship?
                    if self.target == self.selected:
                        if weapon.wtype == 'Support':
                            pass  #you clicked your selected ship with a support weapon active. do not end the method.
                        else:
                            self.unselect_ship(result[1])
                            return #do end the method. this is important.

                    #did you click an ally?
                    elif self.target.faction == 'Player':
                        if weapon.wtype == 'Support':
                            if self.target.cth <= 0:
                                self.draggable = False
                                renpy.say('Ava','It\'s hopeless, captain!')
                                self.draggable = True
                                self.targetingmode = True #try again
                                return #do end the method, this is important.
                            else:
                                #you clicked an ally unit with a support weapon active. do not end the method.
                                pass
                        else:
                            self.select_ship(self.target)
                            return

                    #you clicked an enemy with an active weapon.
                    else:

                        #check if you can hit the target. if not, let the player know he's stupid.
                        if self.target.cth <= 0:
                            self.draggable = False
                            renpy.say('Ava','It\'s hopeless, captain!')
                            self.draggable = True
                            return #do end the method, this is important.
                        else:
                            BM.attacker = BM.selected
                            if self.active_weapon.wtype == 'Curse':
                                weapon.fire(self.selected,self.target)
                                self.active_weapon = None
                                self.weaponhover = None

                                return

                            if self.active_weapon.wtype == 'Melee':
                                pass #do not show the atkanim, because there aren't any for melee.
                            else:
                                try:
                                    renpy.call_in_new_context('atkanim_{}_{}'.format(self.selected.animation_name,self.active_weapon.wtype.lower()))
                                except:
                                    show_message('missing animation. "atkanim_{}_{}" does\'t seem to exist'.format(self.selected.animation_name,self.active_weapon.wtype.lower()))

                #up till now nothing ended the method meaning it's okay to fire the weapon at the target - be it support or not.
                result = weapon.fire(self.selected,self.target)
                self.target.receive_damage(result,self.selected,weapon.wtype)
                self.selected.movement_tiles = get_movement_tiles(self.selected)
                update_stats()
                self.active_weapon = None
                self.weaponhover = None
                return

            if result[0] == 'move': #this means you clicked on one of the blue squares indicating you want to move somewhere
                self.selected.move_ship(result[1],self) #result[1] is the new location to move towards
                update_stats()

            if result == 'FULL FORWARD':
                if self.cmd >= 500:
                    self.cmd -= 500
                    show_message('All ships gain 20% damage and 15% accuracy!')
                    for ship in player_ships:
                        if ship.modifiers['accuracy'][0] <= 15:
                            ship.modifiers['accuracy'] = [15,5]
                        if ship.modifiers['damage'][0] <= 20:
                            ship.modifiers['damage'] = [20,5]

                    random_ship = player_ships[renpy.random.randint(0,len(player_ships)-1)]
                    random_voice = renpy.random.randint(0,len(random_ship.buffed_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(random_ship.buffed_voice[random_voice]),channel = random_ship.voice_channel)
                    for ship in player_ships:
                        ship.getting_buff = True
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    renpy.pause(1)
                    for ship in player_ships:
                        ship.getting_buff = False
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')

                else:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')

            if result == 'REPAIR DRONES':
                if self.cmd >= 500:
                    self.cmd -= 500

                    show_message('The Sunrider restored 50% of her hull integrity!')
                    sunrider.hp += int(sunrider.max_hp * 0.5)
                    if sunrider.hp > sunrider.max_hp: sunrider.hp = sunrider.max_hp
                    sunrider.getting_buff = True
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    a = renpy.random.randint(0,len(sunrider.buffed_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(sunrider.buffed_voice[a]),channel = sunrider.voice_channel)
                    del a
                    renpy.pause(1)
                    sunrider.getting_buff = False
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                else:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')

            if result == 'VANGUARD CANNON':
                if self.cmd >= 1500:
                    self.cmd -= 1500
                    renpy.music.play('Music/March_of_Immortals.ogg')
                    renpy.call_in_new_context('atkanim_sunrider_vanguard')
                    BM.vanguard = True
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    renpy.pause(1)
                    store.damage = 800
                    store.hit_count = 1
                    store.total_armor_negation = 0
                    store.total_shield_negation = 0
                    templist = enemy_ships[:]
                    for ship in templist:
                        if ship.location[1] == sunrider.location[1]:
                            if ship.location[0]-sunrider.location[0] >=0:
                                if ship.location[0]-sunrider.location[0] <=7:
                                    if ship in enemy_ships and self.battlemode: #it's possible the ship was already deleted because of the boss being killed
                                        BM.target = ship
                                        ship.receive_damage(800,sunrider,'Vanguard')
                    BM.vanguard = False
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')

                else:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')

            if result[0] == 'hover': #you are hovering over one of the weapon buttons
                self.weaponhover = result[1]
                if self.weaponhover.wtype == 'Support':
                    for ship in player_ships:
                        ship.cth = get_acc(result[1], BM.selected, ship)
                else:
                    ignore_evasion = False
                    if self.weaponhover.wtype == 'Curse':
                        ignore_evasion = True

                    for ship in enemy_ships:
                        ship.cth = get_acc(result[1], BM.selected, ship, ignore_evasion)

            if result[0] == 'weapon_fire': #you actually clicked on one of the weapon buttons
                if self.selected.en < result[1].energy_use: #sanity check. the button should not even be clickable
                    show_message('DEBUG: Not enough energy!')
                    return

                if result[1].wtype == 'Support':
                    if result[1].self_buff:
                        result[1].fire(BM.selected,BM.selected)
                        return

                self.targetingmode = True   #displays targeting info over enemy_ships
                self.active_weapon = result[1]
                self.weaponhover = BM.active_weapon
                return

            if result == 'endturn':
                self.end_player_turn()

            if len(enemy_ships) == 0 and self.battlemode: #check if there are enemy_ships remaining.
                renpy.hide_screen('commands')
                self.battle_end()
                renpy.hide_screen('battle_screen')


            if len(player_ships) == 0:  #all player units destroyed!
                self.battlemode = False #this ends the battle loop
                VNmode()
                renpy.hide_screen('battle_screen')
                renpy.hide_screen('commands')

            return

#ending the battle - reset values for next battle
        def battle_end(self, lost = False):
            self.battlemode = False #this ends the battle loop
            if self.selected != None: self.unselect_ship(self.selected)

            if not lost:
                renpy.music.stop()
                renpy.music.play('Music/Posthumus_Regium_Finale.ogg', loop = False)
                renpy.hide_screen('commands')
                self.draggable = False
                renpy.show_screen('victory')
                renpy.pause(3.0)
                renpy.hide_screen('victory')

                repair_cost = 0
                total_money = 0
                for ship in destroyed_ships:
                    if ship.faction == 'Player':
                        repair_cost += int(ship.max_hp * 0.2)
                    else:
                        total_money += ship.money_reward

                for ship in player_ships:
                    repair_cost += int((ship.max_hp - ship.hp)*0.1)

                net_gain = int(total_money - repair_cost)
                self.money += int(net_gain)
                self.cmd += int((net_gain*10)/BM.turn_count)

                renpy.show_screen('victory2')
                renpy.pause(1)
                renpy.hide_screen('victory2')
                self.draggable = True

            self.turn_count = 1
            self.ships = []
            self.selectedmode = False


            VNmode() #return to visual novel mode. this mostly just restored scrolling rollback
            for ship in destroyed_ships:
                if ship.faction == 'Player':
                    player_ships.append(ship)
                    self.ships.append(ship)
            for ship in player_ships:
                self.ships.append(ship)
            for ship in player_ships:
                ship.en = ship.max_en
                ship.hp = ship.max_hp
                ship.hate = 100
                ship.total_damage = 0
                ship.total_missile_damage = 0
                ship.total_kinetic_damage = 0
                ship.total_energy_damage = 0
                ship.missiles = ship.max_missiles
                for modifier in ship.modifiers:
                    ship.modifiers[modifier] = [0,0]

            #reset the entire grid to empty and BM.ships with only the player_ships list
            clean_grid()
            BM.covers = []

            renpy.block_rollback()

#ending a turn
        def end_player_turn(self):
            renpy.hide_screen('commands')
            self.selected = None #some sanity checking
            self.order_used = False
            self.target = None
            self.moving = False
            self.selectedmode = False
            self.targetingmode = False
            self.active_weapon = None
            self.turn_count += 1
            renpy.music.play(EnemyTurnMusic)
            renpy.call_in_new_context('endofturn')

            for ship in self.ships:
                ship.flak_effectiveness = 100
                ship.en = ship.max_en

            self.enemy_AI() #call the AI to take over

            for ship in self.ships:
                ship.flak_effectiveness = 100
                ship.en = ship.max_en

        def enemy_AI(self):

              ##lead ships don't care about looking for other ships for protection
              ##other ships come to them! instead, lead ships typically go on the
              ##offensive, dragging allies along.
            self.lead_ships = []
            total_defense = 0
            for eship in enemy_ships:
                total_defense += eship.shield_generation + eship.flak + eship.armor
            average_defense = total_defense / float(len(enemy_ships))

              ##because I assume  most of the time there will be many mooks and only
              ##a few high defense ships the few that are are definitely above average.
              ##this method is very dynamic and doesn't rely on blueprint flags.
            for eship in enemy_ships:
                defense = eship.shield_generation + eship.flak + eship.armor
                if defense > average_defense:
                    self.lead_ships.append(eship)

                ##the lead ships are heaving a go first
            for eship in self.lead_ships:
                eship.en = eship.max_en
                eship.lbl = im.MatrixColor(eship.blbl,im.matrix.brightness(0.3))
                renpy.pause(0.3)
                eship.AI()
                eship.lbl = eship.blbl


            for ship in enemy_ships:
                #now all the not-lead ships take their turn
                if ship not in self.lead_ships:
                    ship.en = ship.max_en
                    ship.lbl = im.MatrixColor(ship.blbl,im.matrix.brightness(0.3))
                    renpy.pause(0.3)
                    ship.AI()
                    ship.lbl = ship.blbl
            renpy.music.play(PlayerTurnMusic)
            renpy.call_in_new_context('endofturn')
            self.active_weapon = None  #I forget, why is this needed?
            self.selected = None
            self.selectedmode = False

    ## Displayables ##
    #none anymore

    ##blueprints##

      #this class is the basis of all unit types in the game. these values are the default one if none are specified.
    class Battleship(store.object):
        def __init__(self):
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = -1
            self.shield_color = '000'
            self.max_hp = 200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.repair = 0
            self.flak = 0
            self.flak_range = 1
            self.flak_effectiveness = 100
            self.flak_used = False
            self.fireing_flak = False
            self.morale = 100
            self.enemies = {}
            self.hate = 100 #this is actually how much the enemy hates you. aka threat
            self.attraction = 0 #AI uses this. ships that provide lots of cover attract others
            self.fear = {
                'kinetics':20,
                'missiles':20,
                'energy':20,
                }
            self.kinetic_dmg = 1  #normal damage at start. increased by upgrades
            self.kinetic_acc = 1
            self.kinetic_cost = 1
            self.energy_dmg = 1
            self.energy_acc = 1
            self.energy_cost = 1
            self.missile_dmg = 1
            self.missile_acc = 1
            self.missile_cost = 1
            self.melee_dmg = 1
            self.melee_acc = 1
            self.melee_cost = 1
            #[display name, level,increase/upgrade,upgrade cost,cost multiplier]
            self.upgrades = {
                'max_hp':['Hull Plating',1,100,100,1.5],
                'max_en':['Energy Reactor',1,5,200,1.4],
                'move_cost':['Move Cost',1,-1,100,2.5],
                'evasion':['Evasion',1,5,500,2.5],
                'kinetic_dmg':['Kinetic Damage',1,0.05,100,1.5],
                'kinetic_acc':['Kinetic Accuracy',1,0.05,100,1.5],
                'kinetic_cost':['Kinetic Energy Cost',1,-0.05,100,2.0],
                'energy_dmg':['Energy Damage',1,0.05,100,1.5],
                'energy_acc':['Energy Accuracy',1,0.05,100,1.5],
                'energy_cost':['Energy Energy Cost',1,-0.05,100,2.0],
                'missile_dmg':['Missile Damage',1,0.05,100,1.5],
                'missile_acc':['Missile Accuracy',1,0.05,100,1.5],
                'missile_cost':['Missile Energy Cost',1,-0.05,100,2.0],
                'max_missiles':['Missile Storage',1,1,500,3],
                'melee_dmg':['Melee Damage',1,0.05,100,1.5],
                'melee_acc':['Melee Accuracy',1,0.05,100,1.5],
                'melee_cost':['Melee Energy Cost',1,-0.05,100,2.0],
                'shield_generation':['Shield Power',1,5,500,2],
                'shield_range':['Shield Range',1,1,1000,5],
                'flak':['Flak',1,5,500,2],
                'base_armor':['Armor',1,5,500,2],
                'repair':['Repair Crew',1,50,500,2]
                }
            self.total_damage = 0  #refers to damage done, not taken. used by AI
            self.total_kinetic_damage = 0
            self.total_missile_damage = 0
            self.total_energy_damage = 0
            self.base_armor = 10
            self.armor = self.base_armor
            self.armor_color = '000'
            self.weapons = []
            self.max_weapons = 9
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.move_cost = 50
            self.cmd_reward = 100
            self.money_reward = 100
            self.cth = 0
            self.getting_buff = False
            self.getting_curse = False
            self.boss = False
            self.location = (1,1)
            self.movement_tiles = []
            self.portrait = None
            self.death_animation = 'no_animation'  #the default death animation: none.
            self.miss_animation = 'no_animation' #gets called when this ship avoids getting hit
            self.id = 0 #used to identify enemy_ships more easily
              #modifiers list temporary (de)buffs.
              #these values represent the strength of the modifier and the number of turns it stays in effect
            self.modifiers = {
                'accuracy':[0,0],
                'move_cost':[0,0],
                'evasion':[0,0],
                'damage':[0,0],
                'armor':[0,0],
                'shield':[0,0],
                'flak':[0,0],
                'energy':[0,0],
                'stealth':[0,0],
                }

        def receive_damage(self,damage,attacker,wtype):
            BM.attacker = attacker

            if damage == 'no energy':
                renpy.say('ERROR','the {} does not have the energy for this attack'.format(self.name))
            elif damage == 'no ammo':
                renpy.say('ERROR','the {} does not have enough ammo for this attack'.format(self.name))
            elif damage == 'miss':
                if wtype == 'Melee':
                    store.damage = damage
                    renpy.call_in_new_context('melee_attack_player')
                else:
                    try:
                        renpy.call_in_new_context('miss_{}'.format(self.animation_name)) #show the miss animation
                    except:
                        show_message('missing animation. "miss_{}" does\'t seem to exist'.format(self.animation_name))
            else:

                #handle healing
                if wtype == 'Support':
                    self.hp += int(damage)
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    return

                #implementing difficulty setting.
                if Difficulty == 0:
                    if self.faction == 'Player':
                        damage = int(damage * 0.25)
                    else:
                        damage = int(damage * 4)

                if Difficulty == 1:
                    if self.faction == 'Player':
                        damage = int(damage * 0.75)
                    else:
                        damage = int(damage * 1.33)

                if Difficulty == 3:
                    if self.faction == 'Player':
                        damage = int(damage * 1.33)
                    else:
                        damage = int(damage * 0.75)


                #havoc isn't allowed to die in the first turn
                if self.name == 'Havoc' and BM.turn_count == 1 and damage > self.hp:
                    try:
                        renpy.call_in_new_context('miss_{}'.format(self.animation_name)) #show the miss animation
                    except:
                        show_message('missing animation. "miss_{}" does\'t seem to exist'.format(self.animation_name))
                    return

                  #collect and store data used by the AI
                attacker.total_damage += damage
                if wtype == 'Missile' or wtype == 'Rocket':
                    attacker.total_missile_damage += damage
                      #high levels of fear (of a damage type) changes AI behavior
                    self.fear['missiles'] += damage / 10
                if wtype == 'Kinetic' or wtype == 'Assault':
                    attacker.total_kinetic_damage += damage
                    self.fear['kinetics'] += damage / 10
                if wtype == 'Laser' or wtype == 'Pulse':
                    attacker.total_energy_damage += damage
                    self.fear['energy'] += damage / 10

                store.damage = damage #the global variant is used by the health_animation screen
                attacker.hate += damage*0.5  #damaging enemies increases how likely they are to target you
                self.hate -= damage  #getting damaged lowers your threat back down
                if self.hate < 100: self.hate = 100
                BM.target = self

                  #if the attack hits, show the hit animation of the target based on weapon type

                if wtype == 'Melee':
                    renpy.call_in_new_context('melee_attack_player')
                else:
                    try:
                        renpy.call_in_new_context('hitanim_{}_{}'.format(self.animation_name,wtype.lower()))
                    except:
                        show_message('missing animation. "hitanim_{}_{}" doesn\'t seem to exist'.format(self.animation_name,wtype.lower()))

                self.hp -= damage
                if self.hp <= 0:
                    self.destroy(attacker)

        def destroy(self,attacker,no_animation = False):
              #first take care of some AI data tracking stuff
              #destroying enemy ships increases hate, but lowers enemy moral too
            if not self.faction == 'Player':
                attacker.hate += self.max_hp*0.3
                attacker.target = None
                for eship in enemy_ships:
                    if get_ship_distance(self,eship) <= 4:
                        eship.morale -= 20

            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            destroyed_ships.append(self)
            if self in enemy_ships:
                enemy_ships.remove(self)
            if self in player_ships:
                player_ships.remove(self)
                if len(player_ships) == 0:
                    renpy.jump('gameover')
            a = self.location[0]-1  #make the next line of code a little shorter
            b = self.location[1]-1
            BM.grid[a][b] = False #tell the BM that the old cell is now free again
            if self in BM.ships:
                BM.ships.remove(self)
            if self.boss:
                BM.battle_end()

        def register_weapon(self, weapon):
            if len(self.weapons) >= self.max_weapons:
                raise IndexError('ERROR: too many weapons assigned to the {}'.format(self.name))
            else:
                self.weapons.append(weapon)

        def remove_weapon(self, weapon):
            if weapon in self.weapons:
                self.weapons.remove(weapon)

        def set_location(self,xnew,ynew):
            a,b = self.location
            BM.grid[a-1][b-1] = False
            BM.grid[xnew-1][ynew-1] = True
            self.location = (xnew,ynew)

#AI estimate damage
        def AI_estimate_damage(self,pship,en = 0):  #part of the AI
            if en == 0: en = self.en
            #renpy.log('starting estimating damage on {}'.format(pship.name))

            pship.damage_estimation = [None,0,0] #weapon,estimation,priority
              #cycle through all the weapons and find out which one is likely to be most
              #effective for each player ship
            for weapon in self.weapons:
                #renpy.log('checking the effect of {}'.format(weapon.name))

                if self.en >= weapon.energy_use:
                    accuracy = get_acc(weapon,self,pship,guess=True)
                    if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
                        estimation = (weapon.damage-pship.armor*2)*weapon.shot_count*accuracy / 100.0
                        priority = estimation * (pship.hate/100.0)/50.0
                        #renpy.log('I estimate that {} would do {!s} damage on {}'.format(weapon.name,int(estimation),pship.name))
                        #renpy.log('based on hate I give this ship a priority of {}'.format(priority))
                        if pship.damage_estimation[2] < priority:
                            pship.damage_estimation = [weapon,int(estimation),priority]
                    if weapon.wtype == 'Missile' or weapon.wtype == 'Rocket':
                        if weapon.uses_missiles and self.missiles <= 0:
                            estimation = 0
                        elif weapon.uses_rockets and self.rockets <= 0:
                            estimation = 0
                        else:
                            estimation = (weapon.damage-pship.armor)*weapon.shot_count*accuracy / 100.0
                            estimation = estimation * (100 - pship.flak) / 100.0
                              #arbitrary compensation for not calculating flak defense perfectly
                              #also, missiles cost ammo and probably shouldn't be spammed.
                            estimation *= 0.85
                            priority = estimation * (pship.hate/100.0)/50.0
                            #renpy.log('I estimate that {} would do {!s} damage on {}'.format(weapon.name,int(estimation),pship.name))
                            #renpy.log('based on hate I give this ship a priority of {}'.format(priority))
                            if pship.damage_estimation[1] < estimation:
                                pship.damage_estimation = [weapon,int(estimation),priority]
                    if weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
                        estimation = (weapon.damage-pship.armor)*weapon.shot_count*accuracy / 100.0
                        estimation = estimation * (100 - pship.shields) / 100.0
                        priority = estimation * (pship.hate/100.0)/50.0
                        #renpy.log('I estimate that {} would do {!s} damage on {}'.format(weapon.name,int(estimation),pship.name))
                        #renpy.log('based on hate I give this ship a priority of {}'.format(priority))
                        if pship.damage_estimation[1] < estimation:
                            pship.damage_estimation = [weapon,int(estimation),priority]
                    if weapon.wtype == 'Melee':
                        if pship.stype == "Ryder":
                            estimation = (weapon.damage-pship.armor*2)*weapon.shot_count*accuracy / 100.0
                        else:
                            estimation = 0
                        priority = estimation * (pship.hate/100.0)/50.0
                        #renpy.log('I estimate that {} would do {!s} damage on {}'.format(weapon.name,int(estimation),pship.name))
                        #renpy.log('based on hate I give this ship a priority of {}'.format(priority))
                        if pship.damage_estimation[2] < priority:
                            pship.damage_estimation = [weapon,int(estimation),priority]
            if pship.damage_estimation[0] == None:
                pass
                #renpy.log('all weapons can do no damage')
            else:
                pass
                #renpy.log('I conclude that {} has the highest damage({!s}) and a priority of {!s}'.format(pship.damage_estimation[0].name,pship.damage_estimation[1],pship.damage_estimation[2]))
#            if pship.name == 'sunrider': pship.damage_estimation[2] = pship.damage_estimation[2] * 0.75

#AI attacks
        def AI_attack_target(self,pship,weapon):
            update_stats()
            BM.attacker = self
            BM.target = pship
            if weapon.wtype == 'Melee':
                pass
            else:
                try:
                    renpy.call_in_new_context('atkanim_{}_{}'.format(self.animation_name,weapon.wtype.lower()))
                except:
                    show_message('missing animation. "atkanim_{}_{}" does\'t seem to exist'.format(self.animation_name,weapon.wtype.lower()))
            damage = weapon.fire(self,pship)
            pship.receive_damage(damage,self,weapon.wtype)
            update_stats()

#basic loop
        def AI_basic_loop(self):
            #renpy.log('{} starting AI_basic_loop'.format(self.name))
            #renpy.log('I have {} energy'.format(self.en))

              ##create some damage estimates
            for pship in player_ships:
                self.AI_estimate_damage(pship)
                  ##first, if we can finish off an enemy in one hit we will try.
                if pship.hp < pship.damage_estimation[1]:
                    self.AI_attack_target(pship,pship.damage_estimation[0])
                    #renpy.log('I took an attack of opportunity against {}'.format(pship.name))
                      ##loop again and see what to do with the rest of the ships EN power
                    return

              ##find the target we can do the most damage on right now
            best_target = [None,None,0,0] #ship,weapon,estimate,priority
            for pship in player_ships:
                 ##damage_estimation[0] is the weapon
                 ##damage_estimation[1] is the amount of expected damage
                if pship.damage_estimation[2] > best_target[3]:
                    best_target = [pship,pship.damage_estimation[0],pship.damage_estimation[1],pship.damage_estimation[2]]
            if best_target[0] == None:
                pass
                #renpy.log('no good target was found')
            else:
                pass
                #renpy.log('best target is {} with an estimate of {!s} and a priority of {!s}'.format(best_target[0].name,best_target[2],best_target[3]))

              ##find out if there isn't an ally around that could boost our defenses
              ##I want to change this so that it calculates how attractive each cell on the map is.
            most_attractive_ship = [None,0]
            if len(enemy_ships) > 1:
                if self not in BM.lead_ships:
                    for eship in enemy_ships:
                        if not self == eship:
                            attraction = 1
                            distance = get_ship_distance(self,eship)
                            if eship.shield_generation > self.shields:
                                attraction += (eship.shields - self.shields)*self.fear['energy']*0.1
                            if eship.flak > self.flak:
                                attraction += (eship.flak - self.flak)*self.fear['missiles'] *0.1
                            eship.attraction = attraction / (distance*distance/2.0)
                            #renpy.log('the {} is judged to have an attraction of {!s}'.format(eship.name,attraction))
                            #renpy.log('modified by distance it is {!s}'.format(eship.attraction))
                    for eship in enemy_ships:
                        if eship.attraction > most_attractive_ship[1]:
                            most_attractive_ship = [eship,eship.attraction]
                    #renpy.log('the most attractive ship weighed by distance is {} at {!s} attraction'.format(most_attractive_ship[0].name,int(most_attractive_ship[1])))

            #check if this ship can use melee attacks
            can_melee = False
            for weapon in self.weapons:
                if weapon.wtype == 'Melee':
                    can_melee = True

            if can_melee:
                minimum_damage = 100
            else:
                minimum_damage = 10

              ##decide whether to shoot or to move
            if best_target[0] == None or most_attractive_ship[1] < 5000 and best_target[2] < minimum_damage:
                #renpy.log('decided on moving towards an enemy ship')
                if best_target[0] == None:
                    pass
                    #renpy.log('because I can not do any damage from here')
                else:
                    pass
                    #renpy.log('because most attractive is at {!s}'.format(most_attractive_ship[1]))
                    #renpy.log('and best target damage estimation is at {!s}'.format(best_target[2]))

                  ##find the enemy ships you want to move towards
                priority_target = [None,0]
                can_melee = False
                for weapon in self.weapons:
                    if weapon.wtype == 'Melee':
                        can_melee = True

                for ship in player_ships:
                    distance = get_ship_distance(self,ship)
                    if ship.stype == 'Ryder' and can_melee:
                        priority = 10*(ship.hate/100+10) / (distance*distance/2.0)
                    else:
                        priority = (ship.hate/100+10) / (distance*distance/2.0)
                    if  priority > priority_target[1]:
                        priority_target = [ship,priority]
                self.target = priority_target[0]
                self.AI_move_towards(self.target)
                #renpy.log('I am going after the {} because of its weighted priority of {!s}'.format(priority_target[0].name,priority_target[1]))
                return

            elif best_target[3] > most_attractive_ship[1]:
                #renpy.log('attacking the {} because of its high priority of {!s}'.format(best_target[0].name,best_target[3]))
                ##attack ship
                BM.target = best_target[0]
                self.AI_attack_target(best_target[0],best_target[1])
                return

            elif most_attractive_ship[1] < best_target[3] and self.en >= self.move_cost:
                #renpy.log('moving to ally {} because of its high attractiveness of {!s}'.format(most_attractive_ship[0].name,most_attractive_ship[1]))
                ##move towards support ship
                self.AI_move_towards(most_attractive_ship[0],melee_distance=True)
                return

            else:
                if best_target[0] == None:
                    return
                else:
                      #just attack whatever as it seems to be the only thing left we can do.
                    BM.target = best_target[0]
                    self.AI_attack_target(best_target[0],best_target[1])
                    return

#AI move towards
        def AI_move_towards(self, target, melee_distance = False):
            old_spot = self.location
            final_spot = self.location #going to iterate over this
            max_move_distance = self.en/self.move_cost
            travel_distance = get_ship_distance(self,target)

            if melee_distance == False:
                if target.stype == 'Ryder':
                    for weapon in self.weapons:
                        if weapon.wtype == 'Melee':
                            melee_distance = True

            if max_move_distance == 0:
                return

            for a in range(1,GRID_SIZE[0]+1):
                for b in range(1,GRID_SIZE[1]+1):
                     #checks if this spot is free
                    if BM.grid[a-1][b-1] == False:
                          #check if have the EN to move here
                        if get_distance((a,b),self.location) <= max_move_distance:
                            distance_target = get_distance((a,b),target.location)
                              #unless specifically allowed, we don't want to end up right next to a target
                            if distance_target == 1 and not melee_distance: distance_target = 999
                              #check if this spot is closer to the target than the final_spot
                            if distance_target <= get_distance(final_spot,target.location):
                                distance_self = get_distance((a,b),self.location)
                                  #check if this spot is not stupid far from self
                                  #i.e. the spot behind the target is just as far from the target
                                  #as the one in front of it
                                if distance_self <= travel_distance:
                                    travel_distance = distance_self
                                    final_spot = (a,b)

            ##TO DO: take into account how dangerous spots are. this will NEVER end....
            if old_spot == final_spot:  #calling move_ship() when not needed can lead to double counter attacks.
                return
            else:
                self.move_ship(final_spot,BM)
            return

#AI START
        def AI(self):
            #renpy.log('{} starting AI'.format(self.name))
            #renpy.log('I have {} energy'.format(self.en))
            if self in BM.lead_ships:
                pass
                #renpy.log('I am a lead ship!')

            self.target = None
            BM.selected = self
            self.AI_running = True
            while self.AI_running:
                starting_en = self.en
                #if self.target == None: ##I need to get back to this
                self.AI_basic_loop()
                if starting_en == self.en:
                      ##no (more) engine power was (/could be) used so we quit the AI
                    self.AI_running = False
                    return

        def move_ship(self, new_location,bm):
              ##play voices based on backwards or forwards motion
            if self.faction == 'Player':
                if self.location[0] > new_location[0]: #going west
                    a = renpy.random.randint(0,len(self.movebackward_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(self.movebackward_voice[a]),channel = self.voice_channel)
                    del a
                if self.location[0] < new_location[0]: #going east
                    a = renpy.random.randint(0,len(self.moveforward_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(self.moveforward_voice[a]),channel = self.voice_channel)
                    del a

            bm.selectedmode = False #this disables showing movement tiles
            renpy.hide_screen('commands')
            self.en -= self.move_cost * get_distance(self.location,new_location)
            a = self.location[0]-1  #make the next line of code a little shorter
            b = self.location[1]-1
            bm.grid[a][b] = False #tell the BM that the old cell is now free again
            self.current_location = self.location #store a temporary location
            vector = calculate_vector(new_location,self.location) #get what direction to go to
            self.next_location = (self.location[0]+vector[0],self.location[1]+vector[1])
            self.location = None #this makes the imagebutton of this ship not be displayed on battle_screen
            bm.moving = True
            anti_stall = 0
            while bm.moving:
#
                result = ui.interact()
                if result[0] == 'timer': #this gets returned every half second or so when ships are moving from grid to grid
                    if self.next_location == new_location:
                        self.location = new_location #we have arrived
                        bm.selected = None #completely deselect unit
                        bm.moving = False #stop the loop
                        bm.grid[new_location[0]-1][new_location[1]-1] = True #tell the BM the new cell is occupied
                    else:
                        self.current_location = self.next_location
                        vector = calculate_vector(new_location,self.current_location)
                        self.next_location = (self.current_location[0]+vector[0],self.current_location[1]+vector[1])

                #this probably shouldn't take 15 loops. if it does, something bad is happening
                anti_stall += 1
                if anti_stall == 15:
                    show_message('debug: infinite loop detected while moving. breaking off....')
                    bm.moving = False

            ## BLIND SIDE ATTACKS
            if self.faction == 'Player' and self.modifiers['stealth'][0] != 100:
                for enemy in enemy_ships:
                    if get_ship_distance(self,enemy) == 1 and self in player_ships: #if next to enemy and -not dead-
                        counter = None
                        for weapon in enemy.weapons:
                            if weapon.wtype == 'Assault':
                                counter = weapon
                        if counter != None:
                            if enemy.en >= counter.energy_use:
                                show_message('COUNTER ATTACK!')
                                enemy.AI_attack_target(self,counter)
            else:
                for ship in player_ships:
                    if ship.name != 'Phoenix': #enemy phoenix is immune to counter attacks without having to buff itself.
                        if get_ship_distance(self,ship) == 1 and self in enemy_ships: #if next to enemy and -not dead-
                            counter = None
                            for weapon in ship.weapons:
                                if weapon.wtype == 'Assault':
                                    counter = weapon
                            if counter != None:
                                if ship.en >= counter.energy_use:
                                    show_message('COUNTER ATTACK!')
                                    update_stats()
                                    try:
                                        renpy.call_in_new_context('atkanim_{}_{}'.format(ship.animation_name,counter.wtype.lower()))
                                    except:
                                        show_message('missing animation. "atkanim_{}_{}" does\'t seem to exist'.format(ship.animation_name,counter.wtype.lower()))
                                    damage = counter.fire(ship,self)
                                    self.receive_damage(damage,ship,counter.wtype)



            bm.select_ship(self, play_voice = False) #you can control your ship again




        ### Weapon Blueprints ###
    class Weapon(store.object): #superclass of all weapon objects
        def __init__(self):
            self.damage = 0
            self.uses_missiles = False
            self.uses_rockets = False
            self.energy_use = 0
            self.acc_degradation = 15
            self.wtype = ''
            self.shot_count = 1
            self.accuracy = 100




        ## Laser ##
    class Laser(Weapon): #starter laser weapon and parent of all other lasers
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 300
            self.energy_use = 100
            self.wtype = 'Laser'
            self.name = 'Basic Laser'
            self.lbl = 'Battle UI/button_laser.png'

        def fire(self, parent, target): #firing lasers!
            update_armor(target)
            energy_cost = int(self.energy_use * parent.energy_cost)
            if parent.en < energy_cost:  #energy handling
                return 'no energy'
            else:
                parent.en -= energy_cost
            accuracy = get_acc(self, parent, target)

                ## actual damage calculation
            total_damage = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            store.hit_count = 0

            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(self.shot_count):
                if renpy.random.randint(0,100) > accuracy:
                    pass #you missed!
                else:
                    damage = self.damage * parent.energy_dmg * renpy.random.triangular(0.8,1.2)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    damage -= target.armor
                    if damage <= 1: damage = 1
                    store.total_armor_negation += target.armor
                    if target.shields > 0:
                        damage = damage * (100 - target.shields) / 100.0
                        store.total_shield_negation += int(damage * target.shields / 100.0)
                    if damage <= 1: damage = 1
                    total_damage += int(damage)
                    store.hit_count += 1

            if total_damage > 0:
                return total_damage
            else:
                return 'miss'

        ## GUNZ ##
    class Kinetic(Weapon): #starter Kinetic weapon
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 150
            self.shot_count = 4
            self.energy_use = 50
            self.accuracy = 50
            self.wtype = 'Kinetic'
            self.name = 'Basic Guns'
            self.lbl = 'Battle UI/button_kinetic.png'

        def fire(self, parent, target): #firing gunz!
            update_armor(target)

            energy_cost = int(self.energy_use * parent.kinetic_cost)
            if parent.en < energy_cost:  #energy handling
                return 'no energy'
            else:
                parent.en -= energy_cost

            accuracy = get_acc(self, parent, target)
            if accuracy == 0: return 'miss'

            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0

            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(self.shot_count):
                if renpy.random.randint(1,100) > accuracy:
                    pass #you missed!
                else:
                    damage = self.damage * parent.kinetic_dmg * renpy.random.triangular(0.8,1.2)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if damage < target.armor *2:
                        store.total_armor_negation += damage -1
                    else:
                        store.total_armor_negation += target.armor *2
                    damage -= target.armor * 2
                    if damage <= 1: damage = 1 #it's rpg tradition you still do 1 damage against a big armored enemy :)
                    total_damage += damage
                    store.hit_count += 1
            if total_damage == 0: return 'miss'
            return int(total_damage)


        ## Missiles ##
    class Missile(Weapon): #starter Missile weapon
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 60    #multiplied by shot count
            self.energy_use = 30
            self.uses_missiles = True
            self.ammo_use = 1
            self.accuracy = 60
            self.acc_degradation = 5
            self.wtype = 'Missile'
            self.name = 'Basic Missiles'
            self.type = 'standard'
            self.shot_count = 8
            self.eccm = 0
            self.lbl = 'Battle UI/button_missile.png'

        def fire(self, parent, target):
            update_armor(target)

            energy_cost = int(self.energy_use * parent.missile_cost)
            if parent.en < energy_cost:  #energy handling
                return 'no energy'
            else:
                parent.en -= energy_cost

            if self.uses_missiles:
                if self.ammo_use > parent.missiles:
                    return 'no ammo'
                else:
                    parent.missiles -= self.ammo_use

            if self.uses_rockets:
                if self.ammo_use > parent.rockets:
                    return 'no ammo'
                else:
                    parent.en -= self.energy_use
                    parent.rockets -= self.ammo_use

            accuracy = get_acc(self, parent, target)
            BM.selectedmode = False

            missile = MissileSprite(parent,target, self.damage,self.shot_count,self.type)
            BM.missiles.append(missile)
            vector = calculate_vector(target.location,missile.location) #get what direction to go to
            missile.next_location = missile.location[0]+(vector[0]/2.0),missile.location[1]+(vector[1]/2.0)

            moving = True
            while moving:
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                renpy.pause(0.1)
                missile.location = missile.next_location

                for ship in BM.ships:
                    if not ship.faction == missile.parent.faction and ship.flak > 0:
                        if not ship.flak_used:
                            if get_ship_distance(missile,ship) <= (ship.flak_range+0.5):
                                ship.fireing_flak = True
                                renpy.hide_screen('battle_screen')
                                renpy.show_screen('battle_screen')
                                renpy.pause(0.1)
                                if ship == target:

                                    ##attempt to show the assault hit animation if it has it.
                                    try:
                                        renpy.call_in_new_context('atkanim_{}_assault'.format(ship.animation_name))
                                    except:
                                        pass

                                missile.flak_intercept(ship)
                                if missile.shot_count == 0:
                                    BM.missiles.remove(missile)
                                    moving = False
                                    ship.fireing_flak = False
                                    for ship in BM.ships:
                                        ship.flak_used = False
                                    return 'miss'
                                renpy.hide_screen('battle_screen')
                                renpy.show_screen('battle_screen')
                                renpy.pause(0.1)
                                ship.fireing_flak = False
                if get_ship_distance(missile,target) <= 0.5:
                    moving = False
                    BM.missiles.remove(missile)
                else:
                    missile.next_location = missile.location[0]+(vector[0]/2.0),missile.location[1]+(vector[1]/2.0)
                    vector = calculate_vector(target.location,missile.location) #get what direction to go to
                    missile.next_location = missile.location[0]+(vector[0]/2.0),missile.location[1]+(vector[1]/2.0)

            for ship in BM.ships:
                ship.flak_used = False

            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0

            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(missile.shot_count):
                if renpy.random.randint(0,100) <= accuracy:
                    damage = self.damage * parent.missile_dmg * renpy.random.triangular(0.8,1.2)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    damage -= target.armor
                    if damage <= 1: damage = 1
                    store.total_armor_negation += target.armor
                    total_damage += damage
                    store.hit_count += 1
            if total_damage == 0: return 'miss'
            return int(total_damage)


          ##this class is the missile shown on screen when missiles are fired##
    class MissileSprite(store.object):
        def __init__(self,parent,target,damage=60,shot_count=8,type='standard'):
            self.location = parent.location
            self.parent = parent
            self.target = target
            a = (parent.location[0] - target.location[0])*192
            b = (parent.location[1] - target.location[1])*120
              #calculate the angle between the attacker and the target
            self.angle = math.degrees(math.atan2(a,b))
            self.damage = damage
            self.shot_count = shot_count
            self.type = type
            self.lbl = im.Rotozoom('Battle UI/map missile (2).png',self.angle,1.0)
            self.eccm = 0
            self.flak_degradation = 3  #this is how much flak effectiveness gets reduced by each missile
            self.next_location = None

        def flak_intercept(self,interceptor):
            shots_remaining = self.shot_count
            interceptor.flak_used = True
            effective_flak = (interceptor.flak-self.eccm)*interceptor.flak_effectiveness/100.0
            for shot in range(self.shot_count):
                if renpy.random.randint(0,100) <= effective_flak:
                    shots_remaining -= 1
            if self.shot_count > shots_remaining:
                shot_down = self.shot_count - shots_remaining
                if shot_down == 1:
                    show_message('1 missile was shot down!')
                else:
                    show_message('{} missiles were shot down!'.format(shot_down))
            interceptor.flak_effectiveness -= (self.shot_count * self.flak_degradation)
            self.shot_count = shots_remaining


    class Melee(Weapon):
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 400    #multiplied by shot count
            self.energy_use = 50
            self.ammo_use = 1
            self.accuracy = 140
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'  #lol
            self.type = 'Melee'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_melee.png'

        def fire(self, parent, target):
            update_armor(target)

            energy_cost = int(self.energy_use * parent.melee_cost)
            if parent.en < energy_cost:  #energy handling
                return 'no energy'
            else:
                parent.en -= energy_cost

            accuracy = get_acc(self, parent, target)
            if accuracy == 0: return 'miss'
            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            for shot in range(self.shot_count):
                if renpy.random.randint(0,100) > accuracy:
                    pass #you missed!
                else:
                    damage = self.damage * parent.melee_dmg * renpy.random.triangular(0.8,1.2)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if damage < target.armor *2:
                        store.total_armor_negation += damage -1
                    else:
                        store.total_armor_negation += target.armor *2
                    damage -= target.armor * 2
                    if damage <= 1: damage = 1 #it's rpg tradition you still do 1 damage against a big armored enemy :)
                    total_damage += damage
                    store.hit_count += 1
            if total_damage == 0: return 'miss'
            return int(total_damage)


    class Support(store.object):
        def __init__(self):
            self.repair = False
            self.self_buff = False #if true this skill automatically casts on self only
            self.damage = 0 #also used to repair
            self.uses_missiles = False
            self.uses_rockets = False
            self.energy_use = 60
            self.wtype = 'Support'
            self.modifies = '' #what modifier key will it affect. e.g. 'accuracy'
            self.buff_strength = 0 #how many points does it increase a stat?
            self.buff_duration = 1

            #effective range is 3 cells away and always hits
            self.accuracy = 350
            self.acc_degradation = 100

            self.name = 'Empty Support Skill'
            self.shot_count = 1
            self.lbl = ''

        def fire(self,parent,target):

            #energy  management
            if parent.en < self.energy_use:
                return 'no energy'
            else:
                parent.en -= self.energy_use

            if self.self_buff:
                target = parent

            #if this is a healing skill
            if self.repair:
                healing = self.damage * renpy.random.triangular(0.8,1.2)
                if self.wtype == 'Support':
                    target.getting_buff = True
                else:
                    target.getting_curse = True
                BM.selectedmode = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                if not target == parent and target.faction == 'Player':
                    a = renpy.random.randint(0,len(target.buffed_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(target.buffed_voice[a]),channel = target.voice_channel)
                    del a
                renpy.pause(1)
                target.getting_buff = False
                target.getting_curse = False
                BM.selectedmode = True
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                return healing

            #if it's a buff
            else:
                target.modifiers[self.modifies] = [self.buff_strength,self.buff_duration]
                if self.wtype == 'Support':
                    target.getting_buff = True
                else:
                    target.getting_curse = True
                BM.selectedmode = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                if not target == parent and target.faction == 'Player':
                    a = renpy.random.randint(0,len(target.buffed_voice)-1)
                    renpy.music.play('sound/Voice/{}'.format(target.buffed_voice[a]),channel = target.voice_channel)
                    del a
                renpy.pause(1)
                target.getting_buff = False
                target.getting_curse = False
                BM.selectedmode = True
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                return 0

    class Curse(Support):
        def __init__(self):
            Support.__init__(self)
            self.wtype = 'Curse'

    class GravityGun(store.object):
        def __init__(self):
            self.repair = False
            self.self_buff = False #if true this skill automatically casts on self only
            self.damage = 0 #also used to repair
            self.uses_missiles = False
            self.uses_rockets = False
            self.energy_use = 60
            self.wtype = 'Curse'
            self.modifies = '' #what modifier key will it affect. e.g. 'accuracy'
            self.buff_strength = 0 #how many points does it increase a stat?
            self.buff_duration = 1

            #effective range is 3 cells away and always hits
            self.accuracy = 640
            self.acc_degradation = 100

            self.name = 'Gravity Gun'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_gravity.png'

        def fire(self,parent,target):

            if parent.en < self.energy_use:
                return
            parent.en -= self.energy_use
            BM.selectedmode = True

            target_faction = target.faction
            target_weapons = target.weapons

            target.faction = 'Player'
            target.weapons = []

            BM.select_ship(target, play_voice = False)
            target.movement_tiles = get_movement_tiles(target,1)

            looping = True
            cancel = False

            while looping:
                result = ui.interact()
                if result[0] == 'move':
                    target.faction = target_faction
                    target.move_ship(result[1],BM) #result[1] is the new location to move towards
                    looping = False
                if result == 'deselect':
                    cancel = True
                    looping = False

            target.en += target.move_cost
            target.faction = target_faction
            target.weapons = target_weapons
            BM.select_ship(parent, play_voice = False)
            parent.movement_tiles = get_movement_tiles(parent)
            return





    class Cover(store.object):
        def __init__(self,location = (1,1)):
            self.location = location
            self.cover_chance = 25 #percentage chance of blocking an incoming attack
            self.max_hp = 500
            self.hp = self.max_hp
            self.label = 'Battle UI/asteroid cover.png'
            self.angle = renpy.random.randint(1,360)

        def receive_damage(self,damage):
            self.hp -= damage
            if self.hp <=0: self.destroy()

        def destroy(self):
            if self in BM.covers:
                BM.covers.remove(self)
                show_message('The asteroid was destroyed!')
                renpy.pause(0.5)


         ### WEAPONFIRE PARTICLE GENERATOR ###
    class FlakShield(object): #created for us by RenpyTom! thanks man!

        def __init__(self, d, generators, speed, angle=135, interval=0.05, dispersion=0):

            # The displayable we use.
            self.d = Transform(d, rotate=angle-90)
            # Are we running?
            self.running = True
            # A list of bullets that are in the air at
            # the moment.
            self.bullets = [ ]
            # The time the next bullets should be shot at.
            self.next_shot = None
            # The interval between shots.
            self.interval = interval
            # The locations of flak generators as (x, y) tuples.
            self.generators = generators
            # The angle bullets appear at.
            self.angle = angle
            # The dispersion between bullet angles.
            self.dispersion = dispersion
            # The speed of a bullet.
            self.speed = speed
            # The sprite manager.
            self.manager = SpriteManager(self.update)

        def update(self, st):
            if self.next_shot is None:
                self.next_shot = st
            if self.next_shot < st - 10 * self.interval:
                self.next_shot = st - 10 * self.interval

            # Generate shots.
            while self.next_shot <= st:
                if self.running:
                    for startx, starty in self.generators:
                            angle = (self.angle + renpy.random.uniform(-self.dispersion, self.dispersion)) / 180.0 * math.pi
                            xdt = 1.0 * self.speed * math.sin(angle)
                            ydt = 1.0 * self.speed * -math.cos(angle)
                            sprite = self.manager.create(self.d)
                            self.bullets.append((
                                self.next_shot,
                                startx,
                                starty,
                                xdt,
                                ydt,
                                sprite))
                self.next_shot += self.interval

            new_bullets = [ ]
            for b in self.bullets:
                startt, startx, starty, xdt, ydt, sprite = b
                t = st - startt
                sprite.x = startx + xdt * t
                sprite.y = starty + ydt * t
                if sprite.x < 0 or sprite.x > self.manager.width:
                    sprite.destroy()
                    continue
                if sprite.y < 0 or sprite.y > self.manager.height:
                    sprite.destroy()
                    continue
                new_bullets.append(b)

            self.bullets = new_bullets
            return 0

        def show(self):
            ui.layer('master')
            ui.add(self.manager)
            ui.close()

        def hide(self):
            ui.layer('master')
            ui.remove(self.manager)
            ui.close()

        def start(self):
            """
            Starts shooting flak.
            """
            self.running = True

        def stop(self):
            """
            Stops shooting flak.
            """
            self.running = False














