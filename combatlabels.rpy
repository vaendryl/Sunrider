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

label test_battle:
    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []
        BM.mission = 'test'

        #create the sunrider. you only have to create a player ship once:
        sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault()]
        sunrider = create_ship(Sunrider(),(8,6),sunrider_weapons)

        blackjack_weapons = [Melee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
        blackjack = create_ship(BlackJack(),(10,5),blackjack_weapons)

        liberty_weapons = [LibertyLaser(),Repair(),AccUp(),DamageUp()]
        liberty = create_ship(Liberty(),(8,7),liberty_weapons)

        create_ship(Havoc(),(13,5),[Melee()]) #,HavocAssault(),HavocMissile(),HavocRocket()])
#        create_ship(PirateGrunt(),(13,7),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
#        create_ship(PirateGrunt(),(13,6),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
#        create_ship(PirateGrunt(),(13,8),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])

#        create_ship(PirateDestroyer(),(16,5),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
#        create_ship(PirateDestroyer(),(16,7),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Dusty_Universe.ogg"

#    $ buy_upgrades() ##testing

    jump battle_start
    return

label missiontest:

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump missiontest #loop back
    else:
        pass #continue down

    return

transform melee_atkanim(img1,img2):
    img1
    xalign 0.5 yalign 0.5
    zoom 2 xpos 0.2
    ease 0.5 zoom 1 xpos 0.5
    pause 1.3
    img2 with Dissolve(.5, alpha=True)
    pause 1.0
    xpos 0.5 ypos 0.5
    ease 1.0 xpos 2.0 ypos -1.0
    xpos -2.0 ypos 1.0
    ease 1.5 xpos 0.9 ypos 0.5
    pause 0.5
    xpos 0.9 ypos 0.5
    ease 1.0 xpos 2.0 ypos -1.0

transform melee_atkanim_enemy(img1,img2):
    img1
    xalign 0.5 yalign 0.5
    zoom 2 xpos 0.8
    ease 0.5 zoom 1 xpos 0.5
    pause 1.3
    img2 with Dissolve(.5, alpha=True)
    pause 1.0
    xpos 0.5 ypos 0.5
    ease 1.0 xpos -2.0 ypos -1.0
    xpos 2.0 ypos 1.0
    ease 1.5 xpos 0.1 ypos 0.5
    pause 0.5
    xpos 0.1 ypos 0.5
    ease 1.0 xpos -1.0 ypos -1.0


transform melee_atkanim_sprite(img1):
    img1
    yanchor 0.51 ypos 1.0
    xanchor 0.5
    zoom 0.6255
    subpixel True
    xzoom -1 xpos -0.2
    ease 0.3 xpos 0.15
    pause 0.5
    ease 1.5 alpha 0

transform melee_hitanim(img1,yy):
    pause 3.5
    img1
    yanchor 0.5 xanchor 0.5
    xpos 0.5 ypos 0.5
    linear 1.0 ypos yy

screen melee_player:
    zorder 2

    if store.damage == 'miss':
        add melee_hitanim(BM.target.sprites['standard'],-1.5)
    else:
        add melee_hitanim(BM.target.sprites['standard'],0.5)

    if BM.attacker.faction == 'Player':
        add melee_atkanim(BM.attacker.sprites['standard'],BM.attacker.sprites['melee'])
    else:
        add melee_atkanim_enemy(BM.attacker.sprites['standard'],BM.attacker.sprites['melee'])

    add melee_atkanim_sprite(BM.attacker.sprites['character'])

label melee_attack_player:
    python:
        renpy.show_screen('show_background',_layer='master')
        renpy.show_screen('melee_player',_layer='master')

        try:
            random = renpy.random.randint(0,len(BM.attacker.attack_voice)-1)
            renpy.music.play(BM.attacker.attack_voice[random],channel=BM.attacker.voice_channel)
        except:
            pass

    pause 1.3
    if BM.attacker.name == 'Havoc':
        play sound "sound/chainsaw.ogg"
    else:
        play sound "sound/mech1.ogg"
    pause 1.0 #I think dissolve effect also pauses for a little while
    play sound "sound/boasters.ogg"
    pause 1.4

    ## hitanim ##   little reason not to combine them if it's all dynamically generated anyway.

    show screen animation_hp
    pause 1.0
    play sound "sound/Sword Shing 2.ogg"


    if store.damage != 'miss':

        if BM.attacker.faction == 'Player':
            show melee_overlay onlayer screens:
                xzoom -1
            with meleehitreverse
        else:
            show melee_overlay onlayer screens:
                xzoom -1
            with meleehit

        pause 0.1
        hide melee_overlay onlayer screens with dissolvequick
        pause 0.5
        play sound1 "sound/explosion1.ogg"
        show layer master at shake2(repeats=6)

        if BM.attacker.faction == 'Player':
            show piratebomber_kinetichit2 onlayer screens:
                xpos 0.55 ypos 0.5 zoom 1.2
                ease 1.2 alpha 0
            pause 0.1
            play sound2 "sound/explosion1.ogg"
            show layer master at shake2(repeats=6)
            show piratebomber_kinetichit1 onlayer screens:
                xpos 0.55 ypos 0.5 zoom 1.2
                ease 1.2 alpha 0
        else:
            show piratebomber_kinetichit2 onlayer screens:
                xpos 0.4 ypos 0.5 xzoom -1 zoom 1.2
                ease 1.2 alpha 0
            pause 0.1
            play sound2 "sound/explosion1.ogg"
            show layer master at shake2(repeats=6)
            show piratebomber_kinetichit1 onlayer screens:
                xpos 0.4 ypos 0.5 xzoom -1 zoom 1.2
                ease 1.2 alpha 0

        pause 0.5

        if BM.attacker.faction == 'Player':
            $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
        else:
            $renpy.call('hit_{}'.format(BM.target.animation_name))
    else:
        pause 0.5
        if BM.attacker.faction == 'Player':
            $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))
        else:
            python:
                try:
                    random = renpy.random.randint(0,len(BM.attacker.no_damage_voice)-1)
                    renpy.music.play(BM.attacker.no_damage_voice[random],channel=BM.attacker.voice_channel)
                except:
                    pass

    return

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
    python:
        try:
            a = BM.order_used
        except:
            BM.order_used = False
    return