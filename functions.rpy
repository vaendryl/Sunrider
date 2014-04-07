## this file declares all the functions used in the engine

init -6 python:
    if 'mouseup_2' in config.keymap['hide_windows']:
        config.keymap['hide_windows'].remove('mouseup_2')
    if 'h' in config.keymap['hide_windows']:
        config.keymap['hide_windows'].remove('h')
    if 'mouseup_3' in config.keymap['game_menu']:
        config.keymap['game_menu'].remove('mouseup_3')


    import math
    #import random

    def battlemode(bm):  #as it turns out, modifying the keymap doesn't seem to do ANYTHING in runtime
#        if 'mousedown_4' in config.keymap['rollback']:
#            config.keymap['rollback'].remove('mousedown_4')
#        if 'K_PAGEUP' in config.keymap['rollback']:
#            config.keymap['rollback'].remove('K_PAGEUP')
#        if 'mousedown_5' in config.keymap['rollforward']:
#            config.keymap['rollforward'].remove('mousedown_5')
#        if 'K_PAGEDOWN' in config.keymap['rollforward']:
#            config.keymap['rollforward'].remove('K_PAGEDOWN')
#        if 'mouseup_2' in config.keymap['hide_windows']:
#            config.keymap['hide_windows'].remove('mouseup_2')
#        if 'h' in config.keymap['hide_windows']:
#            config.keymap['hide_windows'].remove('h')
        bm.battlemode = True
        config.rollback_enabled = False

    def VNmode():
#        try:
#            config.keymap['rollback'].append('mousedown_4')
#            config.keymap['rollforward'].append('mousedown_5')
#            config.keymap['K_PAGEUP'].append('mousedown_4')
#            config.keymap['K_PAGEDOWN'].append('mousedown_5')
#            config.keymap['hide_windows'].append('mouseup_2')
#            config.keymap['hide_windows'].append('h')
#        except:
#            pass
        BM.battlemode = False
        config.rollback_enabled = True

    def instant_win():
        temp_list = enemy_ships[:]
        for ship in temp_list:
            ship.destroy(sunrider,no_animation=True)
            if ship.boss:
                return

    def get_acc(weapon, attacker, target, guess = False): #calculate the chance to hit an enemy ship
        accuracy = (weapon.accuracy + attacker.modifiers['accuracy'][0])
        accuracy += 50 - (weapon.acc_degradation * get_ship_distance(attacker,target))
        if not weapon.wtype == 'Support' or guess:
            accuracy -= (target.evasion + target.modifiers['evasion'][0])
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
        result = abs(ship1.location[0] - ship2.location[0])
        result += abs(ship1.location[1] - ship2.location[1])
        return result

    def update_armor(parent):
        parent.armor = (parent.base_armor + parent.modifiers['armor'][0]) * parent.hp / parent.max_hp

    def update_stats():
          #first update the shields
          #we loop through all ships and then loop through all ships again
          #we then check if the first ships is in range of the 2nd one
          #if they are, the shield generation value of the 2nd gets added to the total shield value of the first
          #we also update armor (to match damage levels) while we are at it.
          #the font color is also updated to show a value is buffed or not from baseline
        for ship1 in player_ships:
            ship1.shields = 0
            for ship2 in player_ships:
                if ship2.shield_generation > 0:
                    if get_ship_distance(ship1,ship2) <= ship2.shield_range:
                        ship1.shields += ship2.shield_generation
            if ship1.shields > 100: ship1.shields = 100
            ship1.shield_color = '000'
            if ship1.shields > ship1.shield_generation: ship1.shield_color = '070'
            update_armor(ship1)
            ship1.armor_color = '000'
            if ship1.armor < ship1.base_armor: ship1.armor_color = '700'
        for ship1 in enemy_ships:
            ship1.shields = 0
            for ship2 in enemy_ships:
                if ship2.shield_generation > 0:
                    if get_ship_distance(ship1,ship2) <= ship2.shield_range:
                        ship1.shields += ship2.shield_generation
            if ship1.shields > 100: ship1.shields = 100
            ship1.shield_color = '000'
            if ship1.shields > ship1.shield_generation: ship1.shield_color = '070'
            update_armor(ship1)
            ship1.armor_color = '000'
            if ship1.armor < ship1.base_armor: ship1.armor_color = '700'

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
        if BM.grid[location[0]-1][location[1]-1]:
            raise Exception('DEBUG: {} can not be created because the location is not free!'.format(ship_class.name))
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

    def get_movement_tiles(ship):
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
                            show_message('the ' +ship.name+ ' lost it\'s buff to it\'s ' +key+ '!')
                            renpy.pause(0.5)
                        else:
                            ship.modifiers[key][1] -= 1



    def game_over():
        renpy.hide_screen('game_over_gimmick')
        renpy.show_screen('game_over_gimmick')



