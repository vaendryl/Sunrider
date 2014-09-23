  
label skirmish_battle:
    python:
        store.tempmoney = BM.money
        store.tempcmd = BM.cmd
        store.temprockets = store.sunrider.rockets
        store.temprepair_drones = store.sunrider.repair_drones
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
    
    call mission_skirmish       
    
    python:
        BM.phase = 'Player'
        BM.mission = 'skirmishbattle'
        update_stats()
    
    call battle_start
    
    python:
        BM.cmd = store.tempcmd
        BM.money = store.tempmoney
        store.sunrider.rockets = store.temprockets
        store.sunrider.repair_drones = store.temprepair_drones
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
    
label mission_skirmish:
    $ BM.skirmish_phase()
        
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission_skirmish #loop back
    else:
        pass #continue down
    # jump dispatch
    return            
        
        

    return