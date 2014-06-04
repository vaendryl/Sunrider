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

    def reset_upgrades(ship):
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

    def buy_upgrades():
        renpy.show_screen('upgrade')
        active = True
        while active:
            result = ui.interact()

            if result == 'quit':
                renpy.hide_screen('upgrade')
                for ship in player_ships:
                    ship.hp = ship.max_hp
                    ship.en = ship.max_en
                    ship.missiles = ship.max_missiles
                active = False
                return

            elif result == 'next':
                if BM.selected != None and len(player_ships) > 1:
                    index = player_ships.index(BM.selected)
                    if index == (len(player_ships)-1):
                        index = 0
                    else:
                        index += 1
                    BM.selected = player_ships[index]

            elif result == 'reset':
                reset_upgrades(BM.selected)

            elif result != None:
                ship = BM.selected #shorter
                name,level,increase,cost,multiplier = ship.upgrades[result]
                if BM.money >= cost:  #sanity check
                    BM.money -= cost
                    new_value = getattr(ship,result)+increase
                    setattr(ship,result,new_value)
                    level += 1
                    cost = int(cost * multiplier)
                    ship.upgrades[result] = [name,level,increase,cost,multiplier]

    def battlemode(bm):
        bm.battlemode = True
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

    def clean_grid():
        BM.grid = []
        BM.ships = []
        for a in range(GRID_SIZE[0]):
                BM.grid.append([False]*GRID_SIZE[1])
        for ship in player_ships:
            BM.ships.append(ship)
            #should not be needed, as location should be set during each mission init
#            x,y = ship.location
#            BM.grid[x-1][y-1] = True


    def get_acc(weapon, attacker, target, guess = False): #calculate the chance to hit an enemy ship
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
        if not weapon.wtype == 'Support' or guess:
            accuracy -= (target.evasion + target.modifiers['evasion'][0])

        #an acc. buff is added as a flat bonus
        accuracy += attacker.modifiers['accuracy'][0]

        #accuracy degrades over distance based on a weapon stat. missiles and rockets usually degrade much more slowly
        accuracy += 50 - (weapon.acc_degradation * get_ship_distance(attacker,target))

        #environmental effects are added
        accuracy *= BM.environment['accuracy'] / 100.0

        if accuracy > 100: return 100
        if accuracy < 0.0: return 0
        return int(accuracy)

    def show_message(message,xpos=0.5,ypos=0.7):
        renpy.hide_screen('message')
        renpy.show_screen('message', message=message,xpos=xpos,ypos=ypos)
        renpy.pause(MESSAGE_PAUSE)

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

    def get_distance(location1,location2):
        if location1 == None or location2 == None: return 999
        result = abs(location1[0] - location2[0])
        result += abs(location1[1] - location2[1])
        return result

    def get_ship_distance(ship1,ship2):
        if ship1 == None or ship2 == None: return 999
        if ship1.location == None or ship2.location == None: return 999
        result = abs(ship1.location[0] - ship2.location[0])
        result += abs(ship1.location[1] - ship2.location[1])
        return result

    def update_armor(parent):
        parent.armor = (parent.base_armor + parent.modifiers['armor'][0]) * parent.hp / parent.max_hp

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
            update_armor(ship1)
            ship1.armor_color = '000'
            if ship1.armor < ship1.base_armor: ship1.armor_color = '700'
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
            update_armor(ship1)
            ship1.armor_color = '000'
            if ship1.armor < ship1.base_armor: ship1.armor_color = '700'

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
        renpy.pause(1.0)

        #create a non aliased copy of BM so we can extract all the field data
        BM_copy = deepcopy(BM)
        #extracting field data
        fields = deepcopy(BM_copy.__dict__)
        #re-init the copy. this adds new fields defined in classes.rpy
        BM_copy.__init__()
        #store all the default field data into a dict
        fields = BM_copy.__dict__

        #loop over each field stored in the new dict
        for key in fields:
            #check if the fielddata itself is a dictionary (like BM.orders)
            if type(fields[key]) is dict:
                #check if the new dict already exists. add it if it does not
                try:
                    dict2 = getattr(BM,key)
                except:
                    setattr(BM,key,fields[key])
                    continue
                #create temporary dicts for easy coding
                dict1 = fields[key]
                #loop over every key in the new field list
                for key in dict1:
                    #if a new key exists, add it to the old dict. thanks to aliasing this updates the dict in BM
                    if key not in dict2:
                        dict2[key]=dict1[key]
            else:
                #test if BM has this field. if it does not, add it with default value.
                try:
                    x = getattr(BM,key)
                except:
                    setattr(BM,key,fields[key])

        #repeat same concept for basic variables inside firstvariables.rpy
        add_new_vars()

        #going to re-init all the ships
        for ship in BM.ships:
            weapons = ship.weapons
            #re-init all the weapons to default values
            for weapon in weapons:
                weapon.__init__()

            #make a copy of the ship instance
            ship_copy = deepcopy(ship)
            #re-init the copy
            ship_copy.__init__()
            #remove this copy from BM.ships as we don't want it displayed on the map etc
            del BM.ships[-1]
            #copy all the fields of the copy into a dict
            fields = ship_copy.__dict__

            #loop over all the keys in the dict
            for key in fields:
                if type(fields[key]) is dict:
                    #check if the new dict already exists. add it if it does not
                    try:
                        dict2 = getattr(ship,key)  #this will be an alias, and it needs to be.
                    except:
                        setattr(ship,key,fields[key])
                        continue
                    dict1 = fields[key]
                    #since the dict already existed, loop over every key in the new field list and update it
                    for key in dict1:
                        #if a new key exists, add it to the old dict. thanks to aliasing this updates the dict in the ship too
                        if key not in dict2:
                            dict2[key]=dict1[key]
                else:
                    #test if BM has this field. if it does not, add it with default value.
                    try:
                        x = getattr(ship,key)
                    except:
                        setattr(ship,key,fields[key])

            #restore the old weapon list
            ship.weapons = weapons

        show_message('Reinitialization complete.')
        return

    def time_warp_easeout(t):
        return 1.0 - math.cos(t * math.pi / 2.0)

    def zoom_handling(result,bm):
        mouse_xpos, mouse_ypos = renpy.get_mouse_pos() #such a handy function. Thanks Tom!  I use this to zoom in onto your mouse position
        if result[1] == 'in':   #fudging the mouseposition a little so you zoom in further than you actually point
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

    def create_ship(ship_class,location,weapons):

        if location != None:
            if BM.grid[location[0]-1][location[1]-1]:
                return
#               raise Exception('DEBUG: {} can not be created because the location is not free!'.format(ship_class.name))
            else:
                BM.grid[location[0]-1][location[1]-1]= True #indicate that the cell on the grid is occupied
        ship = ship_class
        ship.location = location
        for weapon in weapons:
            ship.register_weapon(weapon)
        if ship.faction == 'Player':
            store.player_ships.append(ship)
        else:
            store.enemy_ships.append(ship)
        if ship.faction == 'Player':
            return ship

    def create_cover(location):
        BM.covers.append(Cover(location))
        return

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
        if ship == None: return
        if move_range == None:
            move_range = int(float(ship.en) / ship.move_cost)
        if move_range > 4 : move_range = 4  #limit the max number of movement tiles on screen
        tile_locations = []
        for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
            for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                cell_distance = abs(ship.location[0]-a) + abs(ship.location[1]-b)
                if not BM.grid[a-1][b-1] and cell_distance <= move_range:
                    xposition = int((a+0.5) * 192 * zoomlevel)
                    yposition = int((b+0.5) * 120 * zoomlevel)
                    tile_locations.append((xposition,yposition,-cell_distance,a,b))
        return tile_locations

    def update_modifiers():
        if BM.phase == 'Player':
            for ship in player_ships:
                for key in ship.modifiers:
                    if ship.modifiers[key][1] > 0:
                        if ship.modifiers[key][1] == 1:
                            ship.modifiers[key] = [0,0]
                            show_message('the ' +ship.name+ ' lost it\'s buff to it\'s ' +key+ '!')
                            renpy.pause(0.5)
                        else:
                            ship.modifiers[key][1] -= 1
        else:
            for ship in enemy_ships:
                for key in ship.modifiers:
                    if ship.modifiers[key][1] > 0:
                        if ship.modifiers[key][1] == 1:
                            ship.modifiers[key] = [0,0]
                            show_message('the ' +ship.name+ ' recovered from it\'s curse to it\'s ' +key+ '!')
                            renpy.pause(0.5)
                        else:
                            ship.modifiers[key][1] -= 1

##experimental AI##
    def scan_local_area(ship):
        if ship == None:
            return

        move_range = ship.en/ship.move_cost
        cells_in_range = []

        for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
            for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                distance = get_distance(ship.location,(a,b))
                if distance <= move_range:
                    for pship in player_ships:
                        ship.AI_estimate_damage(pship)



    def game_over():
        renpy.hide_screen('game_over_gimmick')
        renpy.show_screen('game_over_gimmick')



