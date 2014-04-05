#these labels are called by combat code
image work_in_progress 'gameplay/work-in-progress-hi.png':
    xcenter ycenter
image black = Solid((0, 0, 0, 255))

label no_animation: #defunct
    scene black with dissolve
    show work_in_progress
    pause 0.5
    return

transform shake(time=0.5,repeats=20): #defunct?
    xalign 0.5 yalign 0.5
    pause time
    block:
        ease 0.01 xpos 0.51
        ease 0.02 xpos 0.49
        ease 0.01 xpos 0.5
        repeat repeats

label endofturn:
    show screen battle_screen
    $update_stats()

    if not BM.phase == 'Player':
        play sound 'sound/battle.wav'
        show sunrider_phase onlayer screens zorder 50
        pause TURN_SPEED
        play sound 'sound/drum.ogg'
        hide sunrider_phase onlayer screens zorder 50 with dissolve
        $ BM.phase = 'Player'
    elif BM.phase == 'Player' and enemy_ships[0].faction == 'PACT':
        play sound 'sound/battle.wav'
        show PACT_phase onlayer screens zorder 50
        pause TURN_SPEED
        play sound 'sound/drum.ogg'
        hide PACT_phase onlayer screens zorder 50 with dissolve
        $ BM.phase = 'PACT'
    elif BM.phase == 'Player' and enemy_ships[0].faction == 'Pirate':
        play sound 'sound/battle.wav'
        show Pirate_phase onlayer screens zorder 50
        pause TURN_SPEED
        play sound 'sound/drum.ogg'
        hide Pirate_phase onlayer screens zorder 50 with dissolve
        $ BM.phase = 'Pirate'

    $update_modifiers() #update buffs and curses

    return



label battle_start:
    play music PlayerTurnMusic
    $battlemode(BM)
    $renpy.take_screenshot()
    $renpy.save('battlestart')
    $BM.xadj.value = 872
    $BM.yadj.value = 370
    python:
        for ship in player_ships:
            ship.hp = ship.max_hp
            ship.en = ship.max_en
    $BM.start()


    return

label sunrider_destroyed:
    hide screen commands
    hide screen battle_screen
    scene badend

    menu:
        "Try Again":
            jump tryagain

        "Load Saved Game":
            jump loadsavedgame

    return

label loadsavedgame:
    show screen load
    pause
    jump sunrider_destroyed
    return

label battle:
    $BM.battle()
    if BM.battlemode == True:
        jump battle
    else:
        return

label tryagain:
    $renpy.load('battlestart')
    pause
    $show_message('this should never show up')
    pause
    return

label after_load:
    return