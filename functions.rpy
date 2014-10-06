## this file declares all the functions used in the engine

init -6 python:
    if 'mouseup_2' in config.keymap['hide_windows']:
        config.keymap['hide_windows'].remove('mouseup_2')
    if 'h' in config.keymap['hide_windows']:
        config.keymap['hide_windows'].remove('h')
    if 'mouseup_3' in config.keymap['game_menu']:
        config.keymap['game_menu'].remove('mouseup_3')

    import math
    from copy import deepcopy

    def get_modified_damage(damage,faction):
        #implementing difficulty setting.
        Difficulty = store.Difficulty #to be safe
        
        if Difficulty == 0: #VNmode
            if faction == 'Player':
                damage = int(damage * 0.25)
            else:
                damage = int(damage * 4)

        elif Difficulty == 1: #Casual mode
            if faction == 'Player':
                damage = int(damage * 0.50)
            else:
                damage = int(damage * 2)

        elif Difficulty == 2: #Ensign
            if faction == 'Player':
                damage = int(damage * 0.75)
            else:
                damage = int(damage * 1.33)

        elif Difficulty == 3: #Captain
            pass
            # if faction == 'Player':
                # damage = int(damage * 1.0)
            # else:
                # damage = int(damage * 1.0)
                
        elif Difficulty == 4: #Hard
            if faction == 'Player':
                damage = int(damage * 1.33)
            else:
                damage = int(damage * 0.75)
                
        elif Difficulty == 5: #Space Whale Mode
            if faction == 'Player':
                damage = int(damage * 1.45)
            else:
                damage = int(damage * 0.66)
        
        return damage
    
    def reset_upgrades(ship):
        if ship == None:
            return
        money_returned = 0
        upgrades = ship.upgrades
        for key in upgrades:
            name,level,increase,cost,multiplier = upgrades[key]
            if level > 1:
                for count in range(level-1):
                    cost = int(cost / float(multiplier) )
                    money_returned += cost
                    new_value = getattr(ship,key)-increase
                    setattr(ship,key,new_value)
        tempship = deepcopy(ship)
        tempship.__init__()
        ship.upgrades = tempship.upgrades
        BM.money += money_returned

    def process_upgrade(ship, upgrade):
        name,level,increase,cost,multiplier = ship.upgrades[upgrade]
        if BM.money >= cost:  #sanity check
            renpy.music.play('sound/upgrade_purchase.ogg',channel = 'sound1')
            BM.money -= cost
            new_value = getattr(ship,upgrade)+increase
            setattr(ship,upgrade,new_value)
            level += 1
            cost = int(cost * multiplier)
            ship.upgrades[upgrade] = [name,level,increase,cost,multiplier]
            BM.active_upgrade = ship.upgrades[upgrade]
        else:
            renpy.music.play('sound/Voice/Chigara/Others Line 4.ogg',channel = 'chivoice')
        

    def reverse_upgrade(ship, upgrade):
        name,level,increase,cost,multiplier = ship.upgrades[upgrade]
        level -= 1
        cost = int(round(cost / multiplier))
        BM.money += int(cost * 0.8)
        new_value = getattr(ship,upgrade)-increase
        setattr(ship,upgrade,new_value)
        ship.upgrades[upgrade] = [name,level,increase,cost,multiplier]
        BM.active_upgrade = ship.upgrades[upgrade]

    def buy_upgrades():
        renpy.show_screen('upgrade')
        active = True
        renpy.music.play('sound/Voice/Chigara/Others Line 1.ogg',channel = 'chivoice')
        
        while active:
            result = ui.interact()

            if result[0] == 'quit':
                renpy.hide_screen('upgrade')
                
                voicelist = [
                    'sound/Voice/Chigara/Others Line 2.ogg',
                    'sound/Voice/Chigara/Others Line 3.ogg'
                    ]
                renpy.music.play(renpy.random.choice(voicelist),channel = 'chivoice')
                
                
                
                for ship in player_ships:
                    ship.hp = ship.max_hp
                    ship.en = ship.max_en
                    ship.missiles = ship.max_missiles
                active = False
                return

            elif result[0] == 'reset':
                reset_upgrades(BM.selected)

            elif result != None:
                if result[0] == '+':
                    process_upgrade(BM.selected, result[1])
                    
                elif result[0] == '-':
                    reverse_upgrade(BM.selected, result[1])
                    renpy.music.play('sound/upgrade_sell.ogg',channel = 'sound2')
                

    def battlemode():
        BM.battlemode = True
        config.rollback_enabled = False

    def VNmode():
        BM.battlemode = False
        config.rollback_enabled = True

    def instant_win():
        temp_list = enemy_ships[:]
        for ship in temp_list:
            ship.destroy(sunrider,no_animation=True)
            if ship.boss:
                return

    def apply_modifier(target,modifier,magnitude,duration, cumulative = False):
        """attempts to apply a buff or a curse and return True on success, False on failure"""
        if target == None:
            return False
        if not hasattr(target,'modifiers'):
            return False
        
        if cumulative:
            current_magnitude, current_duration = target.modifiers[modifier]
            magnitude += current_magnitude
            duration += current_duration  #not sure if this is wanted
            target.modifiers[modifier] = [magnitude,duration]
            return True
        
        if magnitude > 0:  #I may have to make a better check at some point
            #buffs
            if modifier in target.modifiers:
                if target.modifiers[modifier][0] > magnitude:
                    return False
                elif target.modifiers[modifier][0] == magnitude:
                    if target.modifiers[modifier][1] >= duration:
                        return False
        else:
            #curses
            if modifier in target.modifiers:
                if target.modifiers[modifier][0] < magnitude:
                    return False
                elif target.modifiers[modifier][0] == magnitude:
                    if target.modifiers[modifier][1] >= duration:
                        return False
        target.modifiers[modifier] = [magnitude,duration]
        return True

    def clean_grid():
        BM.grid = []
        BM.ships = []
        BM.covers = []
        store.enemy_ships = []

        for a in range(GRID_SIZE[0]):
                BM.grid.append([False]*GRID_SIZE[1])
        for ship in player_ships:
            BM.ships.append(ship)
            #should not be needed, as location should be set during each mission init
#            x,y = ship.location
#            BM.grid[x-1][y-1] = True


    def get_acc(weapon, attacker, target, guess = False, range_reduction = 0): #calculate the chance to hit an enemy ship
        accuracy = weapon.accuracy

        #upgrades modify the base stat
        if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
            accuracy *= attacker.kinetic_acc
        if weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
            accuracy *= attacker.energy_acc
        if weapon.wtype == 'Missile' or weapon.wtype == 'Rocket':
            pass
        if weapon.wtype == 'Melee':
            accuracy *= attacker.melee_acc

        #subtract the targets evasion from accuracy but only when it's not a support skill and the AI isn't guessing CTH.
        if not weapon.wtype == 'Support' and not guess:
            accuracy -= (target.evasion * ( 100 + target.modifiers['evasion'][0] ) / 100 )

        #an acc. buff is added as a flat bonus
        if not weapon.wtype == 'Support' or weapon.wtype == 'Curse':
            accuracy += attacker.modifiers['accuracy'][0]

        #accuracy degrades over distance based on a weapon stat. missiles and rockets usually degrade much more slowly
        accuracy += 50 - (weapon.acc_degradation * (max(get_ship_distance(attacker,target) - range_reduction,1)))

        #environmental effects are added
        accuracy *= BM.environment['accuracy'] / 100.0

        if accuracy > 100: return 100
        if accuracy < 0.0: return 0
        return int(accuracy)

    def get_cell_available(location):
        '''Returns True is a space is free - False if it is not'''
        if location != None:
            a,b = location
            X,Y = GRID_SIZE
            if a > 0 and a <= X and b > 0 and b <= Y:
                try:
                    if BM.grid[a-1][b-1]:
                        return False
                    else:
                        return True
                except:
                    return False
            else:
                return False #out of bounds is not available
        else:
            return False #None location is not free. failsafes.
            
    def get_player_ships_in_battle():
        result = []
        for ship in player_ships:
            if ship.location != None:
                result.append(ship)
        return result
    
    
    
    def set_cell_available(location, available=False):
        #False means available(empty/nil), True means occupied
        if location != None:
            a,b = location
            X,Y = GRID_SIZE
            if a > 0 and a <= X and b > 0 and b <= Y:
                BM.grid[a-1][b-1] = available
            else:
                if config.developer:
                    raise Exception("tried to set availability on a hex that does not exist")
                else:
                    pass  #not sure if I should raise an exception or not


    def show_message(message,xpos=0.5,ypos=0.7,pause = MESSAGE_PAUSE):
        """briefly show some text on screen"""
        renpy.hide_screen('message')
        renpy.show_screen('message', message=message,xpos=xpos,ypos=ypos)
        try:
            renpy.pause(pause)            
        except:
            pass
        renpy.hide_screen('message')

    def calculate_vector(location1,location2):  #target location, current location
        if location1[0]-location2[0] == 0:
            x = 0
        else:
            x = (location1[0]-location2[0]) / abs(location1[0]-location2[0])
        if location1[1]-location2[1] == 0:
            y = 0
        else:
            y=(location1[1]-location2[1])/abs(location1[1]-location2[1])
        return (x,y)

    def get_distance(location1, location2):
        if location1 == None or location2 == None: return 999
        cubic1 = convert_to_cubic(location1)
        cubic2 = convert_to_cubic(location2)
        result = cubic_distance(cubic1, cubic2)
        return result

    def get_ship_distance(ship1,ship2):
        if ship1 == None or ship2 == None: return 999
        if ship1.location == None or ship2.location == None: return 999
        cubic1 = convert_to_cubic(ship1.location)
        cubic2 = convert_to_cubic(ship2.location)
        result = cubic_distance(cubic1, cubic2)
        return result
    
    def real_damage(weapon,parent):
        if weapon == None or parent == None:
            return 0
        wtype = weapon_type(weapon)
        if wtype == 'Kinetic':
            return int(weapon.damage*parent.kinetic_dmg)
        elif wtype == 'Energy':
            return int(weapon.damage*parent.energy_dmg)
        elif wtype == 'Missile':
            return int(weapon.damage*parent.missile_dmg)
        elif wtype == 'Melee':
            return int(weapon.damage*parent.melee_dmg)
        else:
            return 0


    def update_stats():
          #first update the shields
          #we loop through all ships and then loop through all ships again
          #we then check if the first ships is in range of the 2nd one
          #if they are, the shield generation value of the 2nd gets added to the total shield value of the first
          #we also update armor (to match damage levels) while we are at it.
          #the font color is also updated to show a value is buffed or not from baseline

        for ship1 in player_ships:
            try:
                if ship1.modifiers['energy regen'][0] == -100:
                    ship1.en = 0
            except:
                ship1.modifiers['energy regen'] = (0,0)
            ship1.shields = 0
            for ship2 in player_ships:
                if get_ship_distance(ship1,ship2) <= ship2.shield_range:
                    actual_generation = ship2.shield_generation
                    try:
                        mod,duration = ship2.modifiers['shield_generation']
                    except:
                        ship2.modifiers['shield_generation'] = [0,0]
                        mod,duration = (0,0)
                    if mod != 0: actual_generation += mod
                    if actual_generation < 0: actual_generation = 0
                    ship1.shields += actual_generation
            if ship1.shields > 100: ship1.shields = 100
            ship1.shield_color = '000'
            if ship1.shields > ship1.shield_generation: ship1.shield_color = '070'
            ship1.update_armor()
        for ship1 in enemy_ships:
            try:
                if ship1.modifiers['energy regen'][0] == -100:
                    ship1.en = 0
            except:
                ship1.modifiers['energy regen'] = (0,0)
            ship1.shields = 0
            for ship2 in enemy_ships:
                if ship2.shield_generation > 0:
                    if get_ship_distance(ship1,ship2) <= ship2.shield_range:
                        actual_generation = ship2.shield_generation
                        try:
                            mod,duration = ship2.modifiers['shield_generation']
                        except:
                            ship2.modifiers['shield_generation'] = [0,0]
                            mod,duration = ship2.modifiers['shield_generation']
                        if mod != 0:
                            actual_generation += mod
                        if actual_generation < 0:
                            actual_generation = 0
                        ship1.shields += actual_generation
            if ship1.shields > 100: ship1.shields = 100
            ship1.shield_color = '000'
            if ship1.shields > ship1.shield_generation: ship1.shield_color = '070'
            ship1.update_armor()

    def weapon_type(weapon):
        if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
            return 'Kinetic'
        elif weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
            return 'Energy'
        elif weapon.wtype == 'Missile' or weapon.wtype == 'Rocket':
            return 'Missile'
        elif weapon.wtype == 'Melee':
            return 'Melee'
        else:
            return 'notype'

    def add_new_vars():
        firstvars = deepcopy(AllVariables().__dict__)
        for key in firstvars:
            if not hasattr(store,key) or getattr(store,key) == None:
                setattr(store,key,firstvars[key])

    def reset_classes():
        """experimental save file compatibility keeper
        this reruns the __init__() function of every relevant class in the game
        so that newly added fields can be added to classes from an old save file.
        deepcopy() is used because creating an alias is exactly what's not needed here"""

#        #store a list of BM.ships. deepcopy() does not create aliased variables
#        ships = deepcopy(BM.ships)

        show_message('You loaded a save file from a previous version of the game. reinitializing game data...')
        try:
            renpy.pause(1.0) #this will typically fail when a ui.interact is running, like it usually is during battle
        except:
            pass

        #copy the dict from BM
        fields = deepcopy(BM.__dict__)
        
        #add missing fields to BM
        BM.__init__()
        
        #restore the old values to the dict in BM
        for key in fields:
            if type(BM.__dict__[key]) is dict:
                dictionary = BM.__dict__[key]
                for key2 in fields[key]:
                    #only put missing keys in nested dicts
                    #this will re-add orders that are not part of the default
                    if not key2 in dictionary:
                        dictionary[key2] = fields[key][key2]
            else:
                BM.__dict__[key] = fields[key]

        #repeat same concept for basic variables inside firstvariables.rpy
        add_new_vars()
        
        #remake the BM.ships list
        BM.ships = []
        for ship in player_ships:
            BM.ships.append(ship)
        for ship in enemy_ships:
            BM.ships.append(ship)

        #going to re-init all the ships
        for ship in BM.ships:
            weapons = ship.weapons
            #re-init all the weapons to default values
            for weapon in weapons:
                weapon.__init__()

            #make a copy of the ship instance
            ship_copy = deepcopy(ship)
            #re-init the ship
            ship.__init__()
            #loop over all the keys in the dict of the copy
            for key in ship_copy.__dict__:
                ship_value = getattr(ship_copy,key)  #= hp value or upgrades dict etc
                #check if this key represents a nested dict
                if type(ship_value) is dict: #such as ship.upgrades
                    new_ship_dict = getattr(ship,key) #the default dict part of the recently reinitialized ship
                    #loop over all the keys in the dict from the copied ship
                    for key2 in ship_value:                        
                        #overwrite the default values with the ones that were there originally
                        #otherwise all upgrades would get wiped out.
                        if key2 in new_ship_dict:
                            new_ship_dict[key2] = ship_value[key2]
                else:
                    # key not a dict
                    if hasattr(ship,key):
                        setattr(ship,key, getattr(ship_copy,key) )
                        
            #restore the old weapon list
            ship.weapons = weapons

        show_message('Reinitialization complete.')
        return
        
    def update_mp():
        for variable in important_variables:
            if hasattr(store,variable):
                if getattr(mp,variable) is None:
                    setattr(mp,variable, getattr(store,variable) )
        mp.save()
        
    # def memory_leak_test():
        # for a in range(1000):
            # BM.battle_log.append('tonsofcrap')

    def time_warp_easeout(t):  ##probably never got used
        return 1.0 - math.cos(t * math.pi / 2.0)

    def get_mouse_location():
        """
        get the mouse position and return the hex location the mouse is over.
        """
        a,b = renpy.get_mouse_pos()
        yoffset = 27 * store.zoomlevel
        hexheight = HEXD * store.zoomlevel
        hexwidth = HEXW * store.zoomlevel
        # xmax,ymax = GRID_SIZE

        y = int( (b+BM.yadj.value-yoffset) / hexheight )
        if y%2==0:
            xoffset = hexwidth/2
        else:
            xoffset = 0
        x = int( (a+BM.xadj.value-xoffset) / hexwidth )
        return (x,y)
        # if x <= 0 and x >= xmax:
            # return (1,1)


    # def test_displayable():
        # pass

    def ship_position(ship):
        if ship.location is None:
            return 0

        a, b = ship.location
        return a + b * 100

    def sort_ship_list():
        BM.ships.sort(key=ship_position)

    def zoom_handling(result,bm):
        if result == None:
            return
        if bm == None:
            return
        mouse_xpos, mouse_ypos = renpy.get_mouse_pos() #such a handy function. Thanks Tom!  I use this to zoom in onto your mouse position
        if result[1] == 'in':   #fudging the mouse position a little so you zoom in further than you actually point
            if mouse_xpos > 960:
                adjusted_xpos = 960 + (mouse_xpos-960)*1.5
            else:
                adjusted_xpos = mouse_xpos - (960-mouse_xpos)*0.75
            if mouse_ypos > 540:
                adjusted_ypos = 540 + (mouse_ypos-540)*1.5
            else:
                adjusted_ypos = mouse_ypos - (540-mouse_ypos)*0.75
        else:
            adjusted_xpos = 960   #when you zoom out you do not do so based on your cursor position.
            adjusted_ypos = 540

        real_xpos = (bm.xadj.value + adjusted_xpos) / (1920*store.zoomlevel/0.5)  #this stores the position of the mouse relative to the entire battlefield
        real_ypos = (bm.yadj.value + adjusted_ypos) / (1080*store.zoomlevel/0.5)

        if result[1] == "in": #check if you scrolled up or scrolled down.
            store.zoomlevel *= (1 + ZOOM_SPEED)
            if store.zoomlevel >= 2.0: store.zoomlevel = 2.0 #set a maximum value so you can't zoom in endlessly

        elif result[1] == "out":
            store.zoomlevel *= (1 - ZOOM_SPEED)
            if store.zoomlevel <= 0.5: store.zoomlevel = 0.5

        side_distance = (1920*store.zoomlevel/0.5)*real_xpos-adjusted_xpos #I use the mousepostion that was stored at the start to calculate the new viewport position
        if side_distance < 0: side_distance = 0
        top_distance = (1080*store.zoomlevel/0.5)*real_ypos-adjusted_ypos
        if top_distance < 0: top_distance = 0

        renpy.hide_screen('battle_screen') #the zoomlevel must to be processed BEFORE I adjust the viewport location
        renpy.show_screen('battle_screen')
        bm.xadj.value = int(side_distance) #actually set the new viewport values
        bm.yadj.value = int(top_distance)

    def create_ship(ship,location=None,weapons=[]):

        #find the location
        if location != None:
            location = get_free_spot_near(location)
            if BM.grid[location[0]-1][location[1]-1]:
                return
            else:
                #indicate that the cell on the grid is occupied
                BM.grid[location[0]-1][location[1]-1]= True 
        
        #set the location
        ship.location = location
        
        #confirm the weapon list
        if weapons == None or weapons == []:
            weapons = ship.default_weapon_list
        
        #register the weapons
        for weapon in weapons:
            ship.register_weapon(weapon)
        
        #register the ship
        if ship.faction == 'Player':
            store.player_ships.append(ship)
        else:
            store.enemy_ships.append(ship)
        store.BM.ships.append(ship)
        
        #retun the a player ship for easy aliasing
        if ship.faction == 'Player':
            return ship
        else:
        
            #add newly encountered enemy ships to the list of enemies in skirmish.
            in_all_enemies = False
            for eship in store.all_enemies:
                if ship.__class__ == eship.__class__:
                    in_all_enemies = True
            if not in_all_enemies:
                store.all_enemies.append( ship.__class__() )
                store.all_enemies[-1].location = None
                    
            return

    def get_free_spot_near(location):
        radius = 0
        # don't make the radius larger than width and height of the grid
        while radius < GRID_SIZE[0] or radius < GRID_SIZE[1]:
            # get the locations in the ring at radius 'radius'
            locations = get_in_ring(location, radius)
            
            # return the first available location in the list
            for loc in locations:
                if get_cell_available(loc):
                    return loc
            # increment radius
            radius += 1
        return location
        
    def short_pause():
        #very useful combined with renpy.invoke_in_new_context
        renpy.show_screen('battle_screen')
        renpy.pause(1)
        
        
    def get_remaining_player_ships():
        count = 0
        for ship in player_ships:
            if ship.location != None:
                count += 1
        return count
    
    def clean_battle_exit():
        BM.battle_log = []
        BM.battlemode = False #this ends the battle loop
        if BM.selected != None: BM.unselect_ship(BM.selected)
        BM.targetingmode = False
        BM.weaponhover = None
        BM.hovered = None
        renpy.hide_screen('tooltips')
        BM.phase = 'Player'
        BM.turn_count = 1
        BM.active_strategy = [None,0]
        BM.ships = []
        BM.selectedmode = False
        VNmode() #return to visual novel mode. this mostly just restores scrolling rollback
        for ship in destroyed_ships:
            if ship.faction == 'Player' and not ship.mercenary:
                player_ships.append(ship)
                BM.ships.append(ship)
        for ship in player_ships:
            BM.ships.append(ship)
        for ship in player_ships:
            ship.en = ship.max_en
            ship.hp = ship.max_hp
            ship.hate = 100
            ship.total_damage = 0
            ship.total_missile_damage = 0
            ship.total_kinetic_damage = 0
            ship.total_energy_damage = 0
            ship.missiles = ship.max_missiles
            ship.location = None #this helps if you add new ships but don't know the current location of the existing ones.
            for modifier in ship.modifiers:
                ship.modifiers[modifier] = [0,0]

        #reset the entire grid to empty and BM.ships with only the player_ships list
        clean_grid()
        BM.covers = []
        renpy.hide_screen('battle_screen')
        renpy.hide_screen('commands')
        renpy.block_rollback()
        renpy.music.play("Music/Mission_Briefing.ogg") #else battle theme keeps playing after battle
        
    def get_shot_hit(accuracy,shotcount,faction):
        #fudging with actual hit chances for fun and profit  (lolhiddenmechanics)
        #for now no fudging for AI.
        if faction == 'Player' and store.Difficulty <=3 and shotcount == 1 and accuracy >50:
            RNG2 = renpy.random.randint(1,50) + renpy.random.randint(0,50)
            return RNG2 <= int(accuracy)
        elif faction == 'Player' and store.Difficulty > 3 and accuracy < 50 and shotcount == 1: #muhahaha
            RNG2 = renpy.random.randint(1,50) + renpy.random.randint(0,50)
            return RNG2 <= int(accuracy)
        else:
            return renpy.random.randint(1,100) <= accuracy  

    def test_RNG(accuracy):
        #you can use this to see the difference between the 2 ways of calculating a hit.
        hits1RN = 0
        hits2RN = 0
        
        for i in range(1000):
            if (renpy.random.randint(1,50) + renpy.random.randint(0,50)) < accuracy:
                hits2RN += 1
            if renpy.random.randint(1,100) < accuracy:
                hits1RN += 1
        
        return (hits1RN,hits2RN)
            
    
    def get_shipcount_in_list(shipname,list):
        #count number of times a ship is in a list. useful for merc counting
        if len(list) == 0: return 0
        if shipname == None: return 0

        count = 0
        for item in list:
            if shipname == item.name:
                count+=1
        return count

    def create_cover(location):
        BM.covers.append(Cover(location))
        return
        
    
    def remove_order(order):
        if order in BM.orders:
            del BM.orders[order]

    def cover_mechanic(weapon,target,accuracy):
            for cover in BM.covers:
                if cover.location == target.location:
                    if renpy.random.randint(1,100) <= cover.cover_chance:
                        show_message('the shot was blocked by an asteroid!')
                        renpy.pause(1.0)
                        total_damage = 0
                        for shot in range(weapon.shot_count):
                                total_damage += weapon.damage  #asteroid has no defenses
                        cover.receive_damage(total_damage)
                        return True
            return False


    def get_movement_tiles(ship, move_range = None):
        if ship == None: return []
        if ship.location == None: return []
        
        if move_range == None:
            move_range = int(float(ship.en) / ship.move_cost)
        if move_range > 4 : move_range = 4  #limit the max number of movement tiles on screen
        tile_locations = []
        for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
            for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                loc1 = convert_to_cubic(ship.location)
                loc2 = convert_to_cubic([a,b])
                cell_distance = cubic_distance(loc1, loc2)

                if not BM.grid[a-1][b-1] and cell_distance <= move_range:
                    xposition = dispx(a,b,zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                    yposition = dispy(a,b,zoomlevel,0.5 * ADJY) + int(zoomlevel * MOVY)
                    tile_locations.append((xposition,yposition,-cell_distance,a,b))
        return tile_locations

    def has_weapon(ship,wtype):
        """check if a ship has a weapon of a given type. the weapon type is passed as a string"""
        for weapon in ship.weapons:
            if weapon.wtype == wtype:
                return True
        return False
        
    def get_counter_attack(location, AI = False):
        """check if a location is next to an (enemy) unit that has an Assault type weapon"""
        if location == None: return False
        if AI:
            shiplist = player_ships
        else:
            shiplist = enemy_ships
        for ship in shiplist:
            if get_distance(ship.location,location) == 1:
                if has_weapon(ship,'Assault') and ship.modifiers['flak'][0] != -100:
                    return True
        return False
        
    def update_modifiers():
        """
        called when the phase changes. it ticks down modifiers and removes them when expired.
        """

        if BM.phase == 'Player':
        
            #order management
            order_expired = False
            strat,duration = BM.active_strategy
            if strat != None:
                if duration <= 1:
                    message = "{} has expired!".format(strat)
                    BM.battle_log_insert(['order'], message)
                    show_message(message)
                    order_expired = True
                    BM.active_strategy = [None,0]
                else:
                    BM.active_strategy = [strat,duration -1]
        
            #handle the actual modifiers
            for ship in player_ships:                
                for key in ship.modifiers:
                    mod_power,duration = ship.modifiers[key]
                    if mod_power != 0:
                        if duration == 1:
                            if mod_power < 0:
                                message = "{0} recovered from curse to its {1}".format(ship.name, key.replace('_', ' '))
                                BM.battle_log_insert(['support', 'debuff'], message)
                                show_message(message)
                            else:
                                if not order_expired:
                                    message = "{0} lost buff to its {1}".format(ship.name, key.replace('_', ' '))
                                    BM.battle_log_insert(['support', 'buff'], message)
                                    show_message(message)
                            ship.modifiers[key] = [0,0]
                            renpy.pause(0.5)
                        else:
                            ship.modifiers[key][1] -= 1
        else:
            for ship in enemy_ships:
                for key in ship.modifiers:
                    if ship.modifiers[key][1] > 0:
                        if ship.modifiers[key][1] == 1:
                            if ship.modifiers[key][0] < 0:
                                message = "{0} recovered from curse to its {1}".format(ship.name, key.replace('_', ' '))
                                BM.battle_log_insert(['support', 'debuff'], message)
                                show_message(message)
                            else:
                                message = "{0} recovered from curse to its {1}".format(ship.name, key.replace('_', ' '))
                                BM.battle_log_insert(['support', 'debuff'], message)
                                show_message(message)
                            ship.modifiers[key] = [0,0]
                            renpy.pause(0.5)
                        else:
                            ship.modifiers[key][1] -= 1


    def game_over():
        renpy.hide_screen('game_over_gimmick')
        renpy.show_screen('game_over_gimmick')

##conversion from offset cordinates to cubic coordinates
##makes working with hexagons easier

    #def convert_to_cubic(location):  #converts offset coordinates to cubic coordiantes
    #    r = location[0]              #works on even vertical offset
    #    q = location[1]
    #    x = q - ((r + (r % 2))/2)
    #    z = r
    #    y = (-1 * x) - z
    #    return [x,y,z]

    def convert_to_cubic(location):  #converts offset coordinates to cubic coordiantes
        r = location[0]              #works on even horizontal offset
        q = location[1]
        x = q
        z = r - ((q + (q % 2))/2)
        y = (-1 * x) - z
        return [x,y,z]

    #def convert_to_offset(location):  #converts cubic coordinates to offset coordinates
    #    x = location[0]               #works on even vertical offset
    #    y = location[1]
    #    z = location[2]
    #    q = x + (z + (z%2)) / 2
    #    r = z
    #    return [r, q]

    def convert_to_offset(location):  #converts cubic coordinates to offset coordinates
        x = location[0]               #works on even horizontal offset
        y = location[1]
        z = location[2]
        q = x
        r = z + (x + (x%2)) / 2
        return (r, q)

    def cubic_distance(location1, location2):  #calculates the distances between two cubic coordiantes
        x1 = location1[0]
        y1 = location1[1]
        z1 = location1[2]

        x2 = location2[0]
        y2 = location2[1]
        z2 = location2[2]

        result = (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))/2
        return result

    def hex_round(location):  #rounds cubic coordinates to the nearest hexagon
        x = location[0]
        y = location[1]
        z = location[2]
        rx = int(x)
        ry = int(y)
        rz = int(z)

        x_diff = abs(rx - x)
        y_diff = abs(ry - y)
        z_diff = abs(rz - z)

        if x_diff > y_diff and x_diff > z_diff:
            rx = -ry-rz
        elif y_diff > z_diff:
            ry = -rx-rz
        else:
            rz = -rx-ry

        return [rx, ry, rz]

    def interpolate_hex(location1, location2):  #creates a path between location1 and location2
        tiles = []
        loc1 = location1
        loc2 = location2
        cube1 = convert_to_cubic(loc1)
        cube2 = convert_to_cubic(loc2)
        disN = get_distance(loc1, loc2)

        if disN != 0:
            N = (1.0)/disN
            for i in range(0, disN+1):
                x = cube1[0] + (cube2[0] - cube1[0])*i*N
                y = cube1[1] + (cube2[1] - cube1[1])*i*N
                z = cube1[2] + (cube2[2] - cube1[2])*i*N
                #x = cube1[0] * (1 - float(i)/disN) + cube2[0] * float(i)/disN
                #y = cube1[1] * (1 - float(i)/disN) + cube2[1] * float(i)/disN
                #z = cube1[2] * (1 - float(i)/disN) + cube2[2] * float(i)/disN
                cuberound = hex_round([x, y, z])
                newloc = convert_to_offset(cuberound)
                if isvalid(newloc):
                    tiles.append(newloc)
        return tiles

## functions to calculate position of displayables

    def dispx(x, y, zoom, add = 0):
        xposition = 0
        if y % 2 == 0:
            xposition = int(((x + add) * HEXW + SLIDEX) * zoom)
        else:
            xposition = int(((x + add) * HEXW) * zoom)
        return xposition

    def dispy(x, y, zoom, add = 0):
        yposition = 0
        if x % 2 == 0:
            yposition = int(((y + add) * HEXD + SLIDEY) * zoom)
        else:
            yposition = int(((y + add) * HEXD) * zoom)
        return yposition

    def interpolate_grid(location1, location2): #draws a line from location1 to location2
        tiles = []
        loc1 = location1
        loc2org = location2
        mx = loc2org[0] - loc1[0] #extrapolation
        my = loc2org[1] - loc1[1]
        loc2 = [10*mx+loc2org[0],10*my+loc2org[1]]
        ystep = 0
        xstep = 0
        error = 0
        errorprev = 0
        y = loc1[1]
        x = loc1[0]
        ddx = 0
        ddy = 0
        dx = loc2[0] - loc1[0]
        dy = loc2[1] - loc1[1]
        if dy < 0:
            ystep = -1
            dy = -dy
        else:
            ystep = 1
        if dx < 0:
            xstep = -1
            dx = -dx
        else:
            xstep = 1
        ddy = 2*dy
        ddx = 2*dx
        if ddx >= ddy:
            errorprev = dx
            error = dx
            for i in range(0,dx):
                x+=xstep
                error+=ddy
                if error > ddx:
                    y+=ystep
                    error-=ddx
                    if error + errorprev < ddx:
                        if get_distance(location1,(x,y-ystep))<= 6 and isvalid((x,y-ystep)):
                            tiles.append([x,y-ystep])
                    else:
                        if get_distance(location1,(x-xstep,y))<= 6 and isvalid((x-xstep,y)):
                            tiles.append([x-xstep,y])
                if get_distance(location1,(x,y))<= 6 and isvalid((x,y)):
                    tiles.append([x,y])
                errorprev = error
        else:
            errorprev = dy
            error = dy
            for i in range(0,dy):
                y+=ystep
                error+=ddx
                if error > ddy:
                    x+=xstep
                    error-=ddy
                    if error + errorprev < ddy:
                        if get_distance(location1,(x-xstep,y))<= 6 and isvalid((x-xstep,y)):
                            tiles.append([x-xstep,y])
                    else:
                        if get_distance(location1,(x,y-ystep))<= 6 and isvalid((x,y-ystep)):
                            tiles.append([x,y-ystep])
                if get_distance(location1,(x,y))<= 6 and isvalid((x,y)):
                    tiles.append([x,y])
                errorprev = error
        return tiles

    def isvalid(location): #determines if the location in on the grid
        valid = True
        if location[0] > GRID_SIZE[0] or location[0] <=0:
            valid = False
        if location[1] > GRID_SIZE[1] or location[1] <=0:
            valid = False
        return valid
        
    def debuglog_add(text):
        if config.developer:
            BM.debug_log.append(text)
        else:
            pass

    def get_all_in_radius(location, radius):
        if radius < 0 or location == None:
            return []
        if location < 2:
            return get_all_in_radius_slow(location, radius)

        locations = []
        cx, cy, cz = convert_to_cubic(location)
        for dx in range(-radius, radius + 1):
            for dy in range(max(-radius, -dx - radius), min(radius, -dx + radius) + 1):
                dz = -dx - dy
                locations.append(convert_to_offset([cx + dx, cy + dy, cz + dz]))

        return clean_locations(list(set(locations)))

    def get_all_in_radius_slow(location, radius):
        if radius < 0 or location == None:
            return []

        locations = []
        pending = [location]
        while radius > 0:
            pending2 = []
            for loc in pending:
                x, y = loc
                pending2.append((x + 1, y))
                pending2.append((x - 1, y))
                pending2.append((x, y + 1))
                pending2.append((x, y - 1))
                if y % 2 == 0:
                    pending2.append((x + 1, y + 1))
                    pending2.append((x + 1, y - 1))
                else:
                    pending2.append((x - 1, y + 1))
                    pending2.append((x - 1, y - 1))
            locations.extend(pending)
            pending = list(set(pending2))
            for loc in locations:
                if loc in pending:
                    pending.remove(loc)
            radius -= 1
        locations.extend(pending)
        return clean_locations(list(set(locations)))

    def get_in_ring(loc, radius):
        outer = get_all_in_radius(loc, radius)
        inner = get_all_in_radius(loc, radius - 1)
        # remove all locations in the inner ring from the outer ring
        for x in inner:
            a,b = x
            if a > 1 and a < GRID_SIZE[0] and b > 1 and b < GRID_SIZE[1]:
                outer.remove(x)
        return outer   

    def clean_locations(locations):
        """
        removes all the locations that are out of bounds
        """
        if locations == None: return []
        if locations == []: return []
        
        result = []
        x,y = GRID_SIZE
        
        for location in locations:
            a,b = location
            if a > 0 and a <= x and b > 0 and b <= y:
                result.append(location)
        
        return result        
