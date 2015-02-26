
label skirmish_battle:
    python:
        store.tempmoney = BM.money
        store.tempcmd = BM.cmd
        # store.temprockets = store.sunrider.rockets
        # store.temprepair_drones = store.sunrider.repair_drones
        player_ships_original = player_ships
        original_sunrider = sunrider
        player_ships = deepcopy(player_ships) #upgrades should not be permanent.
        sunrider = get_ship_from_list(player_ships, 'Sunrider')
        enemy_ships = []
        destroyed_ships = []
        clean_grid()
        BM.mission = 'skirmish'
        BM.xadj.value = 872
        BM.yadj.value = 370
        store.zoomlevel = 0.65
        BM.phase = 'formation'
        BM.selected = None
        battlemode()
        BM.remove_mode = False #when True player can click on units and delete them quickly
        for ship in player_ships:
            ship.location = None

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Dusty_Universe.ogg"

    hide screen ship_map
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
        # store.sunrider.rockets = store.temprockets
        # store.sunrider.repair_drones = store.temprepair_drones
        player_ships = player_ships_original
        sunrider = original_sunrider
        BM.mission = None
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

    # jump dispatch
    return
