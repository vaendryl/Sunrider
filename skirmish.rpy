
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

    call mission_skirmish

    python:
        BM.phase = 'Player'
        BM.mission = 'skirmish_battle'

    call battle_start

    python:
        BM.cmd = store.tempcmd
        BM.money = store.tempmoney
    jump dispatch
    return

label mission_skirmish_battle:

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission_skirmish_battle #loop back
    else:
        pass #continue down

    # jump dispatch
    return

label mission_skirmish:
    python:
        BM.result = ui.interact()

        if BM.result == True or BM.result == False:
            # show_message('wtf is a bool returned?') #had some trouble with this at some point. still not sure what caused it.
            renpy.jump('mission_skirmish')
        else:
            BM.skirmish_dispatcher[BM.result[0]]()

    if BM.battlemode:   #whenever this is set to False battle ends.
        jump mission_skirmish #loop back
    else:
        pass #continue down

    return
