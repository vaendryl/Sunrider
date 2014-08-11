  
label skirmish_battle:
    python:
        store.tempmoney = BM.money
        store.tempcmd = BM.cmd
        enemy_ships = []
        destroyed_ships = []
        BM.mission = 'skirmish'
        BM.xadj.value = 872
        BM.yadj.value = 370 
        store.zoomlevel = 0.65
        BM.phase = 'formation'
        BM.show_grid = False
        battlemode()
        BM.remove_mode = False #when True player can click on units and delete them quickly
        for ship in player_ships:
            ship.location = None

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Dusty_Universe.ogg"
    
    hide screen deck0
    show screen battle_screen
    show screen player_unit_pool_collapsed
    show screen enemy_unit_pool_collapsed
    
    if not BM.seen_skirmish:
        show screen skirmishhelp
        $ BM.seen_skirmish = True
    
    call missionskirmish       
    
    python:
        BM.phase = 'Player'
        BM.mission = 'skirmishbattle'
    
    call battle_start
    
    python:
        BM.cmd = store.tempcmd
        BM.money = store.tempmoney
    jump dispatch
    return
    
label missionskirmishbattle:

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump missionskirmishbattle #loop back
    else:
        pass #continue down

    # jump dispatch
    return    
    
label missionskirmish:
    python:
        result = ui.interact()
        
        if result == True or result == False:
            # show_message('wtf is a bool returned?') #had some trouble with this at some point. still not sure what caused it.
            renpy.jump('missionskirmish')
        
        elif result == 'start' or result == 'quit':
            if result == 'start':
                if len(enemy_ships) == 0:
                    show_message('Please add at least 1 enemy ship')
                    renpy.jump('missionskirmish')
            
                player_ship_present = False
                for ship in player_ships:
                    if ship.location != None:
                        player_ship_present = True
                
                if not player_ship_present:
                    show_message('Please add at least 1 player ship')
                    renpy.jump('missionskirmish')
        
            renpy.hide_screen('player_unit_pool_collapsed')
            renpy.hide_screen('enemy_unit_pool_collapsed')
            renpy.hide_screen('player_unit_pool')
            renpy.hide_screen('enemy_unit_pool')
            renpy.hide_screen('mousefollow')
            renpy.hide_screen('battle_screen')
            renpy.hide_screen('store_union') #seems like it has trouble staying closed? 
            BM.battlemode = False
            
            if result == 'quit':
                clean_battle_exit()
                renpy.jump('dispatch')
                
        elif result == 'remove':
            if BM.remove_mode:
                BM.remove_mode = False
            else:
                BM.remove_mode = True
        
        elif result[0] == 'playermusic':
            PlayerTurnMusic = result[1]
            show_message('Player music was changed')

        elif result[0] == 'enemymusic':
            EnemyTurnMusic = result[1]
            
        elif result[0] == "zoom":
            zoom_handling(result,BM)
            
        elif result == "next ship":
            templist = []
            for ship in player_ships:
                if ship.location == None:
                    templist.append(ship)
                    
            if BM.selected == None:
                if len(templist) > 0:
                    BM.select_ship(templist[0])                
            else:
                if BM.selected.location != None:
                    set_cell_available(BM.selected.location) 
                index = templist.index(BM.selected)
                if index == (len(templist)-1):
                    index = 0
                else:
                    index += 1
                BM.select_ship(templist[index])
                    
            if BM.selected != None:
                BM.targetwarp = True
                renpy.show_screen('mousefollow')
                BM.selected.location = None
            
        elif result == 'deselect':
            #if you picked up an enemy unit that was already put down right clicking should delete it entirely
            #player ships automatically return to the blue pool to be placed again later.
            if BM.selected != None:
                if BM.selected in enemy_ships:
                    BM.ships.remove(BM.selected)
                    enemy_ships.remove(BM.selected)
            BM.targetwarp = False
            renpy.hide_screen('mousefollow')                
            BM.unselect_ship(BM.selected)
            
        elif result[0] == 'selection':
            # this result can be from one of the imagebuttons in the pool screens or returned from
            # MouseTracker because a hex with a unit in it was clicked.
            selected_ship = result[1]
            
            if BM.remove_mode:
                if selected_ship.location != None:
                    if selected_ship.faction != 'Player':
                        if selected_ship in enemy_ships:
                            BM.ships.remove(selected_ship)
                            enemy_ships.remove(selected_ship)
                            set_cell_available(selected_ship.location)
                    else:
                        set_cell_available(selected_ship.location)
                        selected_ship.location = None
                        
                    
            else:
                BM.targetwarp = True
                renpy.show_screen('mousefollow')
                
                if selected_ship.faction == 'Player':
                    BM.select_ship(selected_ship)
                else:
                    if selected_ship.location != None:
                        BM.select_ship(selected_ship)
                        if selected_ship in enemy_ships:
                            BM.ships.remove(BM.selected)
                            enemy_ships.remove(BM.selected)
                    else:
                        BM.selected = deepcopy(selected_ship) #breaks alias
                        BM.selected.weapons = BM.selected.default_weapon_list
                        
            if BM.selected != None:
                if BM.selected.location != None:
                    set_cell_available(BM.selected.location)           
                BM.selected.location = None
                
            
        elif result[0] == 'warptarget':
            # returned from MouseTracker if you click on an empty hex when BM.warptarget == True.
            if BM.selected != None:
                new_location = result[1]
                set_cell_available(new_location,True)
                
                if BM.selected.faction != 'Player':
                    enemy_ships.append(BM.selected)
                    BM.ships.append(BM.selected)               
                
                BM.selected.location = new_location
                
                if BM.selected.faction != 'Player' and pygame.key.get_mods() != 0:
                    BM.selected = deepcopy(BM.selected) #breaks alias                    
                else:
                    BM.targetwarp = False
                    renpy.hide_screen('mousefollow')                
                    BM.unselect_ship(BM.selected)
            
            sort_ship_list()

    
    
    if BM.battlemode:   #whenever this is set to False battle ends.
        jump missionskirmish #loop back
    else:
        pass #continue down

    return
    
    
label formationphase:  #pretty much a copy of missionskirmish but I can't be bothered merging these 2 right now
    python:
        result = ui.interact()
        
        if result == 'start':
        
            #check if there are still player units that are not placed
            unplaced_units = False
            for ship in player_ships:
                if ship.location == None:
                    unplaced_units = True
            if unplaced_units:
                show_message('there are still ships you have not placed!')
            else:
                renpy.hide_screen('player_unit_pool_collapsed')
                renpy.hide_screen('enemy_unit_pool_collapsed')
                renpy.hide_screen('player_unit_pool')
                renpy.hide_screen('enemy_unit_pool')
                renpy.hide_screen('mousefollow')
                BM.phase = 'Player'
                renpy.jump('mission{}'.format(BM.mission))
            
        elif result[0] == "zoom":
            zoom_handling(result,BM)
            
        elif result == "next ship":
            templist = []
            for ship in player_ships:
                if ship.location == None:
                    templist.append(ship)
                    
            if BM.selected == None:
                if len(templist) > 0:
                    BM.select_ship(templist[0])                
            else:
                if BM.selected.location != None:
                    set_cell_available(BM.selected.location) 
                index = templist.index(BM.selected)
                if index == (len(templist)-1):
                    index = 0
                else:
                    index += 1
                BM.select_ship(templist[index])
                    
            if BM.selected != None:
                BM.targetwarp = True
                renpy.show_screen('mousefollow')
                BM.selected.location = None
                   
        
        elif result == 'deselect':
            #if you picked up an enemy unit that was already put down right clicking should delete it entirely
            #player ships automatically return to the blue pool to be placed again later.
            if BM.selected != None:
                if BM.selected in enemy_ships:
                    BM.ships.remove(BM.selected)
                    enemy_ships.remove(BM.selected)
            BM.targetwarp = False
            renpy.hide_screen('mousefollow')                
            BM.unselect_ship(BM.selected)
            
        elif result[0] == 'selection':
            # this result can be from one of the imagebuttons in the pool screens or returned from
            # MouseTracker because a hex with a unit in it was clicked.
            selected_ship = result[1]
            
            if selected_ship.faction == 'Player':
                BM.targetwarp = True
                renpy.show_screen('mousefollow')
                BM.select_ship(selected_ship)           
                    
                if BM.selected.location != None:
                    set_cell_available(BM.selected.location)           
                BM.selected.location = None
                
            
        elif result[0] == 'warptarget':
            # returned from MouseTracker if you click on an empty hex when BM.warptarget == True.
            if BM.selected != None:
                new_location = result[1]
                
                #when setting up before a mission you can't put your ships farther to the right than column 7
                if new_location[0] > BM.formation_range:
                    show_message('too far infield')
                else:               
                    set_cell_available(new_location,True) #passing True actually sets it unavailable
                    
                    if BM.selected.faction != 'Player':
                        enemy_ships.append(BM.selected)
                        BM.ships.append(BM.selected)               
                    
                    BM.selected.location = new_location
                    
                    if BM.selected.faction != 'Player' and pygame.key.get_mods() != 0:
                        BM.selected = deepcopy(BM.selected) #breaks alias                    
                    else:
                        BM.targetwarp = False
                        renpy.hide_screen('mousefollow')                
                        BM.unselect_ship(BM.selected)                        

    if BM.battlemode:   #whenever this is set to False battle ends.
        jump formationphase #loop back
    else:
        pass #continue down

    return 