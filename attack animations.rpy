############################################SUNRIDER ATTACK ANIMATIONS START
label atkanim_sunrider_kinetic:

    $renpy.show_screen('show_background',_layer='master')

    show sunrider_side:
        xpos 0.5 ypos 0.5


    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Attacking Kinetic 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Attacking Kinetic 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Ava/Ava Attacking Kinetic 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Ava/Ava Attacking Kinetic 4.ogg"

    show ava uniform alt order angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform alt order angry:
        ease 1.5 alpha 0

    show layer master at shake1
    show sunrider_side kineticrear with dissolveflash
    show sunrider_kineticround1:
        xpos 1180 ypos 455
        linear 0.15 xpos 2150 ypos 430
    show sunrider_side with dissolveflash
    play sound1 'sound/railgun.ogg'
    pause 0.05

    show layer master at shake1
    show sunrider_side kineticrear with dissolveflash
    show sunrider_kineticround2:
        xpos 1180 ypos 450
        linear 0.15 xpos 2150 ypos 425
    play sound2 'sound/railgun.ogg'
    pause 0.2

    show layer master at shake1
    show sunrider_side kineticfront with dissolveflash
    show sunrider_kineticround3:
        xpos 1300 ypos 465
        linear 0.15 xpos 2150 ypos 420
    show sunrider_side with dissolveflash
    play sound1 'sound/railgun.ogg'
    pause 0.05

    show layer master at shake1
    show sunrider_side kineticfront with dissolveflash
    show layer master at shake1
    show sunrider_kineticround4:
        xpos 1300 ypos 460
        linear 0.15 xpos 2150 ypos 415
    play sound2 'sound/railgun.ogg'
    pause 0.05
    show sunrider_side with dissolvequick

    pause 0.5
    return

label atkanim_sunrider_laser:


    $renpy.show_screen('show_background',_layer='master')
    show sunrider_side:
        xpos 0.5 ypos 0.5


    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Attacking Lasers 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Attacking Lasers 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Ava/Ava Attacking Lasers 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Ava/Ava Attacking Lasers 4.ogg"


    show ava uniform alt order angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.75
    play sound2 'sound/Laser 1.ogg'

    show ava uniform alt order angry:
        ease 1.5 alpha 0

    show sunrider_side_laserfront:
        xpos 0.5 ypos 0.5
    show sunrider_side_laserback behind sunrider_side:
        xpos 0.5 ypos 0.5
    with laserwipe

    hide sunrider_side_laserfront
    hide sunrider_side_laserback
    with laserwipe

    pause 0.5
    return

label atkanim_sunrider_missile:

    hide screen battle_screen

    $renpy.show_screen('show_background',_layer='master')
    show sunrider_side:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Attacking Missiles 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Attacking Missiles 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Ava/Ava Attacking Missiles 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Ava/Ava Attacking Missiles 4.ogg"


    show ava uniform alt order angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.75
    show ava uniform alt order angry:
        ease 1.5 alpha 0

    pause 0.25
    play sound2 'sound/missilelaunch.ogg'
    show sunrider_missile1:
        yanchor 50 xanchor 240 xpos 600 ypos 470
        linear 1.1 xpos 2040 ypos 5
    show sunrider_missile2:
        yanchor 50 xanchor 240 xpos 600 ypos 480
        linear 1.1 xpos 2040 ypos 25

    pause 0.13

    show sunrider_missile3:
        yanchor 50 xanchor 240 xpos 860 ypos 480
        linear 0.95 xpos 2040 ypos 100
    show sunrider_missile4:
        yanchor 50 xanchor 240 xpos 900 ypos 480
        linear 0.95 xpos 2040 ypos 130
    show sunrider_missile_trail with sunridermissilewipe
    hide sunrider_missile_trail with dissolve
    pause 0.5

    return

label atkanim_sunrider_pulse:

    hide screen battle_screen

    $renpy.show_screen('show_background',_layer='master')
    show sunrider_side:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,2)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Attacking Lasers 3.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Attacking Lasers 4.ogg"

    show ava uniform alt order angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform alt order angry:
        ease 1.5 alpha 0

    play sound1 "sound/laser.wav"
    show sunrider_side pulsefront with dissolveflash

    show sunrider_pulse1:
        xpos 1345 ypos 515
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse2:
        xpos 1390 ypos 518
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse1b behind sunrider_side:
        xpos 1298 ypos 452
        linear 0.15 xpos 2150 ypos 452
    show sunrider_pulse2b behind sunrider_side:
        xpos 1338 ypos 459
        linear 0.15 xpos 2150 ypos 459
    show sunrider_side with dissolveflash

    play sound2 "sound/laser.wav"
    show sunrider_side pulsefront with dissolveflash
    show sunrider_pulse3:
        xpos 1345 ypos 515
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse4:
        xpos 1390 ypos 518
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse3b behind sunrider_side:
        xpos 1298 ypos 452
        linear 0.15 xpos 2150 ypos 452
    show sunrider_pulse4b behind sunrider_side:
        xpos 1338 ypos 459
        linear 0.15 xpos 2150 ypos 459
    show sunrider_side with dissolveflash

    play sound3 "sound/laser.wav"
    show sunrider_side pulsefront with dissolveflash
    show sunrider_pulse5:
        xpos 1345 ypos 515
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse6:
        xpos 1390 ypos 518
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse5b behind sunrider_side:
        xpos 1298 ypos 452
        linear 0.15 xpos 2150 ypos 452
    show sunrider_pulse6b behind sunrider_side:
        xpos 1338 ypos 459
        linear 0.15 xpos 2150 ypos 459
    show sunrider_side with dissolveflash

    play sound4 "sound/laser.wav"
    show sunrider_side pulserear with dissolveflash
    show sunrider_pulse1:
        xpos 700 ypos 583
        linear 0.3 xpos 2150 ypos 583
    show sunrider_pulse2:
        xpos 740 ypos 573
        linear 0.3 xpos 2150 ypos 573
    show sunrider_side with dissolveflash

    play sound5 "sound/laser.wav"
    show sunrider_side pulserear with dissolveflash
    show sunrider_pulse3:
        xpos 700 ypos 583
        linear 0.3 xpos 2150 ypos 583
    show sunrider_pulse4:
        xpos 740 ypos 573
        linear 0.3 xpos 2150 ypos 573
    show sunrider_side with dissolveflash

    play sound6 "sound/laser.wav"
    show sunrider_side pulserear with dissolveflash
    show sunrider_pulse5:
        xpos 700 ypos 583
        linear 0.3 xpos 2150 ypos 583
    show sunrider_pulse6:
        xpos 740 ypos 573
        linear 0.3 xpos 2150 ypos 573
    show sunrider_side with dissolveflash

    play sound7 "sound/laser.wav"
    show sunrider_side pulserear with dissolveflash
    show sunrider_pulse7:
        xpos 700 ypos 583
        linear 0.3 xpos 2150 ypos 583
    show sunrider_pulse8:
        xpos 740 ypos 573
        linear 0.3 xpos 2150 ypos 573
    show sunrider_side with dissolveflash

    play sound8 "sound/laser.wav"
    show sunrider_side pulsefront with dissolveflash
    show sunrider_pulse1:
        xpos 1345 ypos 515
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse2:
        xpos 1390 ypos 518
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse1b behind sunrider_side:
        xpos 1298 ypos 452
        linear 0.15 xpos 2150 ypos 452
    show sunrider_pulse2b behind sunrider_side:
        xpos 1338 ypos 459
        linear 0.15 xpos 2150 ypos 459
    show sunrider_side with dissolveflash

    play sound9 "sound/laser.wav"
    show sunrider_side pulsefront with dissolveflash
    show sunrider_pulse3:
        xpos 1345 ypos 515
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse4:
        xpos 1390 ypos 518
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse3b behind sunrider_side:
        xpos 1298 ypos 452
        linear 0.15 xpos 2150 ypos 452
    show sunrider_pulse4b behind sunrider_side:
        xpos 1338 ypos 459
        linear 0.15 xpos 2150 ypos 459
    show sunrider_side with dissolveflash

    play sound1 "sound/laser.wav"
    show sunrider_side pulsefront with dissolveflash
    show sunrider_pulse5:
        xpos 1345 ypos 515
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse6:
        xpos 1390 ypos 518
        linear 0.15 xpos 2150 ypos 515
    show sunrider_pulse5b behind sunrider_side:
        xpos 1298 ypos 452
        linear 0.15 xpos 2150 ypos 452
    show sunrider_pulse6b behind sunrider_side:
        xpos 1338 ypos 459
        linear 0.15 xpos 2150 ypos 459
    show sunrider_side with dissolveflash

    play sound2 "sound/laser.wav"
    show sunrider_side pulserear with dissolveflash
    show sunrider_pulse1:
        xpos 700 ypos 583
        linear 0.3 xpos 2150 ypos 583
    show sunrider_pulse2:
        xpos 740 ypos 573
        linear 0.3 xpos 2150 ypos 573
    show sunrider_side with dissolveflash

    play sound3 "sound/laser.wav"
    show sunrider_side pulserear with dissolveflash
    show sunrider_pulse3:
        xpos 700 ypos 583
        linear 0.3 xpos 2150 ypos 583
    show sunrider_pulse4:
        xpos 740 ypos 573
        linear 0.3 xpos 2150 ypos 573
    show sunrider_side with dissolveflash

    play sound4 "sound/laser.wav"
    show sunrider_side pulserear with dissolveflash
    show sunrider_pulse5:
        xpos 700 ypos 583
        linear 0.3 xpos 2150 ypos 583
    show sunrider_pulse6:
        xpos 740 ypos 573
        linear 0.3 xpos 2150 ypos 573
    show sunrider_side with dissolveflash

    pause 0.5
    return

label atkanim_sunrider_assault:

    $renpy.show_screen('show_background',_layer='master')
    show sunrider_side:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Attacking Kinetic 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Flak Intercept 1.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Ava/Ava Flak Intercept 2.ogg"

    show ava uniform alt order angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform alt order angry:
        ease 1.5 alpha 0

    python:
        flak_positions1 = [
            (830,420),
            (880,387),
            (1040,387),
            (1100,387),
            (1160,387),
            ]
        Flak1 = FlakShield("gameplay/Animations/Sunrider/flakbullet.png",flak_positions1,5000,dispersion=2, angle=80, interval=0.15)

        flak_positions2 = [
            (810,420),
            (860,387),
            (1020,387),
            (1080,387),
            (1140,387),
            ]
        Flak2 = FlakShield("gameplay/Animations/Sunrider/flakbullet.png",flak_positions2,5000,dispersion=2, angle=80, interval=0.15)

    play sound "sound/Flak.ogg"

    $ Flak1.show()
    show sunrider_side flak1
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak1
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak1
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak1
    pause 0.01
    show sunrider_side
    pause 0.01
    $ Flak1.stop()
    $ Flak2.show()
    show sunrider_side flak2
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak2
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak2
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak2
    pause 0.01
    show sunrider_side
    pause 0.01
    $ Flak2.stop()
    $ Flak1.start()
    show sunrider_side flak1
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak1
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak1
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak1
    pause 0.01
    show sunrider_side
    pause 0.01
    $ Flak1.stop()
    $ Flak2.start()
    show sunrider_side flak2
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak2
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak2
    pause 0.01
    show sunrider_side
    pause 0.01
    show sunrider_side flak2
    pause 0.01
    show sunrider_side
    $ Flak2.stop()

    pause 0.5

    return

label atkanim_sunrider_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show sunrider_side:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Attacking Missiles 2.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Attacking Missiles 3.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Ava/Ava Attacking Missiles 4.ogg"

    show ava uniform alt order angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.75
    show ava uniform alt order angry:
        ease 1.5 alpha 0

    pause 0.25

    play sound "sound/missilelaunch.ogg"

    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 500 ypos 738
        pause 0.1
        linear 1.2 xpos 2140 ypos 728

    show sunrider_rockettrail with sunriderrocketwipe
    hide sunrider_rockettrail with dissolve
    pause 0.1

    return

#####################################################################SUNRIDER HIT ANIMATIONS

label hitanim_sunrider_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show sunrider_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound1 "sound/missilefly.ogg"

    show sunrider_missilehit1:
        xpos 1440 ypos 0 alpha 0
        pause 0.4
        alpha 1
        linear 0.7 xpos 620 ypos 480
        alpha 0

    show sunrider_missilehit2:
        alpha 0 xpos 1640 ypos 0
        pause 0.3
        alpha 1
        linear 0.7 xpos 740 ypos 560
        alpha 0

    show sunrider_missilehit3:
        xpos 1750 ypos 0 alpha 0
        pause 0.2
        alpha 1
        linear 0.7 xpos 920 ypos 500
        alpha 0

    show sunrider_missilehit4:
        xpos 1930 ypos 0 alpha 0
        pause 0.1
        alpha 1
        linear 0.7 xpos 1010 ypos 540
        alpha 0

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1(pausetime=0.9,repeats=12)
    show sunrider_missileexplode1:
        alpha 0
        pause 0.9
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    show sunrider_missileexplode2:
        alpha 0
        pause 1
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    show sunrider_missileexplode3:
        alpha 0
        pause 1.1
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    pause 0.15

    show sunrider_missiletrail_hit with sunridermissilehitwipe
    hide sunrider_missiletrail_hit with dissolve

    call hit_sunrider

    pause 0.3

    return

label hitanim_sunrider_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show sunrider_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 540
        linear 0.25 xpos 590 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show sunrider_kinetichit1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 540
        linear 0.25 xpos 910 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show sunrider_kinetichit2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    pause 0.25

    call hit_sunrider

    pause 0.5

    return

label hitanim_sunrider_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show sunrider_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show sunrider_laserhitexplode:
        alpha 0
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show sunrider_laserhit behind sunrider_laserhitexplode with enemy_laserhitwipe
    hide sunrider_laserhit behind sunrider_laserhitexplode with enemy_laserhitwipe

    call hit_sunrider

    pause 0.5

    return

label hitanim_sunrider_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show sunrider_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master
    show sunrider_pulse1:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    call hit_sunrider

    pause 1

    return

label hitanim_sunrider_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show sunrider_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rockethit:
        alpha 0
        pause 0.1
        alpha 1
        xpos 1940 ypos 620
        linear 0.7 xpos 560 ypos 620
        alpha 0

    play sound "sound/explosion4.ogg"

    show layer master at shake2(pausetime=1,repeats=8)
    show sunrider_rockethitexplode:
        alpha 0
        pause 1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0

    pause 0.1

    show sunrider_rockethittrail with sunriderhitrocketwipe
    hide sunrider_rockethittrail with dissolve

    call hit_sunrider

    pause 0.5

    return

label hitanim_sunrider_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show sunrider_side:
        xpos 0.5 ypos 0.5

    play sound "sound/Flak.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode12:
        xpos 0.41 ypos 0.52 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode13:
        xpos 0.81 ypos 0.17 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode14:
        xpos 0.37 ypos 0.63 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0

    call hit_sunrider

    pause 0.2

    return

label miss_sunrider:

    show layer master

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,6)

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show sunrider_side behind miss:
        xpos 0.5 ypos 0.5

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava No Damage 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava No Damage 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Ava/Ava No Damage 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Ava/Ava No Damage 4.ogg"
    if Random == 5:
        play avavoice "sound/Voice/Ava/Ava No Damage 5.ogg"
    if Random == 6:
        play avavoice "sound/Voice/Ava/Ava No Damage 6.ogg"

    show ava uniform handonhip mad:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform handonhip mad:
        ease 1.5 alpha 0

    pause 2

    return

label attacksuccess_sunrider:

    show layer master

    $ Random = renpy.random.randint(1,7)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Attack Success 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Attack Success 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Ava/Ava Attack Success 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Ava/Ava Attack Success 4.ogg"
    if Random == 5:
        play avavoice "sound/Voice/Ava/Ava Attack Success 5.ogg"
    if Random == 6:
        play avavoice "sound/Voice/Ava/Ava Attack Success 6.ogg"
    if Random == 7:
        play avavoice "sound/Voice/Ava/Ava Attack Success 7.ogg"

    show ava uniform fistup yes:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform fistup yes:
        ease 1.5 alpha 0

    pause
    return

label attackfail_sunrider:

    show layer master

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Missing Attack 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Missing Attack 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Ava/Ava Missing Attack 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Ava/Ava Missing Attack 4.ogg"
    if Random == 5:
        play avavoice "sound/Voice/Ava/Ava Missing Attack 5.ogg"

    show ava uniform alt neutral angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform alt neutral angry:
        ease 1.5 alpha 0

    pause 0.5
    return

label hit_sunrider:

    show layer master

    if sunrider.hp >= sunrider.max_hp * 0.8:
        play avavoice "sound/Voice/Ava/Ava Damage 1.ogg"
    if sunrider.hp < sunrider.max_hp * 0.8 and sunrider.hp >= sunrider.max_hp * 0.6:
        play avavoice "sound/Voice/Ava/Ava Damage 2.ogg"
    if sunrider.hp < sunrider.max_hp * 0.6 and sunrider.hp >= sunrider.max_hp * 0.4:
        play avavoice "sound/Voice/Ava/Ava Damage 3.ogg"
    if sunrider.hp < sunrider.max_hp * 0.4 and sunrider.hp >= sunrider.max_hp * 0.2:
        play avavoice "sound/Voice/Ava/Ava Damage 4.ogg"
    if sunrider.hp < sunrider.max_hp * 0.2:
        play avavoice "sound/Voice/Ava/Ava Damage 5.ogg"

    show ava uniform alt neutral angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform alt neutral angry:
        ease 1.5 alpha 0

    pause

    return

label order_begin:

    scene black

    play sound "sound/Sword Shing 2.ogg"

    show executiveorder:
        zoom 20 xalign 0.5 yalign 0.5
        ease 0.5 zoom 1
        block:
            xpos 0.5
            pause 0.01
            xpos 0.53
            pause 0.01
            xpos 0.47
            repeat 5

    play kayvoice "sound/Voice/Shields/Cpt Shields 1.ogg"

    show captain_order 1:
        xpos 1.3 alpha 0
        parallel:
            ease 1.0 xpos 0.6
        parallel:
            ease 0.5 alpha 1
            ease 0.5 alpha 0

    pause

label atkanim_sunrider_vanguard:

    scene black

    play music "Music/March_of_Immortals.ogg" noloop fadeout 1.5
    play sound "sound/Sword Shing 2.ogg"
    play kayvoice "sound/Voice/Shields/Cpt Shields 1.ogg"

    show executiveorder:
        zoom 5 xalign 0.5 yalign 0.5
        ease 0.4 zoom 1
        block:
            ease 0.02 xpos 0.52
            ease 0.04 xpos 0.48
            ease 0.02 xpos 0.5
            repeat 8
    pause 0.4
    play sound1 "sound/drum.ogg"

    pause 1.0

    play kayvoice "sound/Voice/Shields/Cpt Shields 13.ogg"

    scene vanguard1 with dissolve:
        xalign 0.5 yalign 0.5

    show captain_order 1:
        xpos 1.0 alpha 0
        ease 0.5 xpos 0.5 alpha 1

    pause 2.0

    play kayvoice "sound/Voice/Shields/Cpt Shields 14.ogg"

    pause 1.0

    play sound "sound/vanguard cannon.ogg"

    scene vanguard2:
        xalign 0.5 yalign 0.5
    show captain_order 2:
        alpha 0 xpos 0.5 alpha 1
        pause 1.0
        ease 0.5 alpha 0
    with dissolve

    pause 0.5

    scene vanguard3 with dissolve:
        xalign 0.5 yalign 0.5
        ease 0.4 zoom 0.7
        block:
            ease 0.02 xpos 0.51
            ease 0.04 xpos 0.49
            ease 0.02 xpos 0.5
            repeat 10

    pause 1.5

    return

label die_sunrider:

    $renpy.show_screen('show_background',_layer='master')

    show sunrider_side:
        xpos 0.5 ypos 0.5

    play avavoice "sound/Voice/Ava/Ava Destroyed 1.ogg"

    show ava uniform altneutral surpriseshout:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15

    pause 4.2

    play avavoice "sound/Voice/Ava/Ava Destroyed 2.ogg"

    show ava uniform altneutral surpriseshout:
        ease 1.5 alpha 0

    pause 2.0

    play sound2 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode2:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound3 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode3:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound4 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode4:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound5 "sound/explosion2.ogg"
    show layer master at shake1
    show sunrider_explode5:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound5 "sound/explosion2.ogg"
    show layer master at shake1
    show sunrider_explode6:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.8

    play sound6 "sound/explosion4.ogg"
    show layer master
    scene white with dissolve
    stop music fadeout 1.5

    pause 1.0

    scene badend

    return

########################################################################PACT MISSILE FRIGATE ATTACK ANIMATIONS


label atkanim_pactmissilefrigate_missile:

    $renpy.show_screen('show_background',_layer='master')

    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5

    pause 0.01

    play sound "sound/missile.ogg"

    show pactmissilefrigate_missile1:
        xpos 1240 ypos 380 alpha 0
        pause 0.55
        alpha 1
        linear 0.6 xpos -400 ypos 380

    show pactmissilefrigate_missile2:
        xpos 1240 ypos 448 alpha 0
        pause 0.57
        alpha 1
        linear 0.6 xpos -400 ypos 448

    show pactmissilefrigate_missile3:
        xpos 1240 ypos 508 alpha 0
        pause 0.59
        alpha 1
        linear 0.6 xpos -400 ypos 508

    show pactmissilefrigate_missile4:
        xpos 1240 ypos 673 alpha 0
        pause 0.61
        alpha 1
        linear 0.6 xpos -400 ypos 673

    pause 0.25

    show pactmissilefrigate_missiletrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_missilewipe
    hide pactmissilefrigate_missiletrail with dissolve

    pause 0.1

    return

label hitanim_pactmissilefrigate_kinetic:   ##############PACT MISSILE FRIGATE HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show pactmissilefrigate_kinetichit1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show pactmissilefrigate_kinetichit2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmissilefrigate_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp(damage_delay = 1.0)

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show pactmissilefrigate_hitmissileexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show pactmissilefrigate_hitmissileexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmissilefrigate_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"
    show layer master at shake2(pausetime=0.2,repeats=6)
    show pactmissilefrigate_hitlaserexplode:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe
    hide pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmissilefrigate_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show sunrider_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmissilefrigate_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 0 ypos 570
        linear 1.1 xpos 1160 ypos 570
        alpha 0


    show layer master at shake2(pausetime=1,repeats=8)
    if sunrider.weapons[3].damage == 800:
        play sound1 "sound/explosion5.ogg"
        show pactmissilefrigate_rocketexplode:
            xpos 0.5 ypos 0.5 alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        
    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 1
            ease 0.05 alpha 1.0 zoom 1.0 
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show pactmissilefrigate_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_rockethitwipe

    show pactmissilefrigate_rockettrail:
        ease 1.0 alpha 0
    
    if sunrider.weapons[3].damage == 1200:
        pause 1.5
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmissilefrigate_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"
    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"
    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"
    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"
    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"
    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"
    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode12:
        xpos 0.41 ypos 0.52 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"
    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode13:
        xpos 0.81 ypos 0.17 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode14:
        xpos 0.37 ypos 0.63 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmissilefrigate_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return


label die_pactmissilefrigate: ###################################MISSILE FRIGATE DEATH

    $renpy.show_screen('show_background',_layer='master')

    show pactmissilefrigate_side:
        xpos 0.5 ypos 0.5


    play sound1 "sound/explosion1.ogg"
    show layer master at shake1
    show pactmissilefrigate_die1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound2 "sound/explosion1.ogg"
    show layer master at shake1
    show pactmissilefrigate_die2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    play sound3 "sound/explosion4.ogg"
    hide pactmissilefrigate_side
    show pactmissilefrigate_die3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_pactmissilefrigate: #############################PACT MISSILE FRIGATE MISS

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show pactmissilefrigate_side behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label atkanim_blackjack_assault: ########################BLACK JACK ATTACK ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play avavoice "sound/Voice/Asaga/Asaga Kinetic 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Asaga/Asaga Kinetic 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Asaga/Asaga Kinetic 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Asaga/Asaga Kinetic 4.ogg"

    show blackjack:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show asaga plugsuit point happy:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit point happy:
        ease 1.5 alpha 0

    play sound "sound/mech1.ogg"
    show blackjack assault with dissolve

    pause 0.3

    play sound1 "sound/machinegun.ogg"

    show blackjack_assaultflash1:
        alpha 0
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.1
            ease 0.025 alpha 0
            pause 0.15
            repeat (4)

    show blackjack_assaultflash2:
        alpha 0
        pause 0.30
        block:
            ease 0.025 alpha 1
            pause 0.1
            ease 0.025 alpha 0
            pause 0.15
            repeat (4)

    pause 1.5

    return

label atkanim_blackjack_laser:

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play avavoice "sound/Voice/Asaga/Asaga Lasers 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Asaga/Asaga Lasers 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Asaga/Asaga Lasers 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Asaga/Asaga Lasers 4.ogg"

    show blackjack:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show asaga plugsuit point happy:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit point happy:
        ease 1.5 alpha 0

    pause 0.8

    play sound "sound/mech1.ogg"
    show blackjack laser with dissolve

    play sound1 "sound/Laser 1.ogg"

    show blackjack_laser1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.1 alpha 1
        pause 0.4
        ease 0.1 alpha 0

    pause 0.1
    show blackjack_laser2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.1 alpha 1
        pause 0.4
        ease 0.1 alpha 0

    pause 0.1
    show blackjack_laser3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.1 alpha 1
        pause 0.4
        ease 0.1 alpha 0

    pause 0.1
    show blackjack_laser4:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.1 alpha 1
        pause 0.4
        ease 0.1 alpha 0

    pause 0.8

    return

label atkanim_blackjack_missile:

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play avavoice "sound/Voice/Asaga/Asaga Missiles 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Asaga/Asaga Missiles 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Asaga/Asaga Missiles 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Asaga/Asaga Missiles 4.ogg"

    show blackjack:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show asaga plugsuit point happy:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit point happy:
        ease 1.5 alpha 0
    pause 0.8

    play sound "sound/mech1.ogg"
    show blackjack missile with dissolve

    pause 0.1

    play sound1 "sound/missile.ogg"

    show blackjack_missile1:
        alpha 0
        pause 0.3
        xpos 680 ypos 315 alpha 1
        linear 0.7 xpos 2200 ypos 20

    show blackjack_missile2:
        alpha 0
        pause 0.3
        xpos 675 ypos 348 alpha 1
        linear 0.7 xpos 2200 ypos 70

    show blackjack_missile3:
        alpha 0
        pause 0.3
        xpos 870 ypos 320 alpha 1
        linear 0.7 xpos 2400 ypos 20

    show blackjack_missile4:
        alpha 0
        pause 0.3
        xpos 802 ypos 680 alpha 1
        linear 0.7 xpos 2200 ypos 410

    show blackjack_missile5:
        alpha 0
        pause 0.3
        xpos 815 ypos 730 alpha 1
        linear 0.7 xpos 2200 ypos 460

    show blackjack_missiletrail with blackjack_missilewipe
    hide blackjack_missiletrail with dissolve

    pause 0.1

    return

label atkanim_blackjack_pulse:

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play avavoice "sound/Voice/Asaga/Asaga Lasers 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Asaga/Asaga Lasers 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Asaga/Asaga Lasers 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Asaga/Asaga Lasers 4.ogg"

    show blackjack:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show asaga plugsuit point happy:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit point happy:
        ease 1.5 alpha 0

    pause 0.8

    play sound "sound/mech1.ogg"
    show blackjack pulse with dissolve

    pause 0.1

    play sound1 "sound/laser.wav"
    show blackjack_pulseflash1:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse1:
        xpos 1230 ypos 460
        linear 0.1 xpos 2200 ypos 480

    pause 0.06

    play sound2 "sound/laser.wav"
    show blackjack_pulseflash2:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse2:
        xpos 1260 ypos 445
        linear 0.1 xpos 2200 ypos 465

    pause 0.06

    play sound3 "sound/laser.wav"
    show blackjack_pulseflash1:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse3:
        xpos 1230 ypos 460
        linear 0.1 xpos 2200 ypos 480

    pause 0.06

    play sound4 "sound/laser.wav"
    show blackjack_pulseflash2:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse4:
        xpos 1260 ypos 445
        linear 0.1 xpos 2200 ypos 465

    pause 0.06

    play sound5 "sound/laser.wav"
    show blackjack_pulseflash1:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse5:
        xpos 1230 ypos 460
        linear 0.1 xpos 2200 ypos 480

    pause 0.06

    play sound6 "sound/laser.wav"
    show blackjack_pulseflash2:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse6:
        xpos 1260 ypos 445
        linear 0.1 xpos 2200 ypos 465

    pause 0.06

    play sound7 "sound/laser.wav"
    show blackjack_pulseflash1:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse7:
        xpos 1230 ypos 460
        linear 0.1 xpos 2200 ypos 480

    pause 0.06

    play sound8 "sound/laser.wav"
    show blackjack_pulseflash2:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse8:
        xpos 1260 ypos 445
        linear 0.1 xpos 2200 ypos 465

    pause 0.1

    play sound9 "sound/laser.wav"
    show blackjack_pulseflash1:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse1:
        xpos 1230 ypos 460
        linear 0.1 xpos 2200 ypos 480

    pause 0.06

    play sound1 "sound/laser.wav"
    show blackjack_pulseflash2:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse2:
        xpos 1260 ypos 445
        linear 0.1 xpos 2200 ypos 465

    pause 0.06

    play sound2 "sound/laser.wav"
    show blackjack_pulseflash1:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse3:
        xpos 1230 ypos 460
        linear 0.1 xpos 2200 ypos 480

    pause 0.06

    play sound3 "sound/laser.wav"
    show blackjack_pulseflash2:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse4:
        xpos 1260 ypos 445
        linear 0.1 xpos 2200 ypos 465

    pause 0.06

    play sound4 "sound/laser.wav"
    show blackjack_pulseflash1:
        alpha 0
        ease 0.06 alpha 1
        ease 0.06 alpha 0

    show blackjack_pulse5:
        xpos 1230 ypos 460
        linear 0.1 xpos 2200 ypos 480

    pause 0.5

    return

label atkanim_blackjack_melee:

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play avavoice "sound/Voice/Asaga/Asaga Melee 1.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Asaga/Asaga Melee 2.ogg"
    if Random == 3:
        play avavoice "sound/Voice/Asaga/Asaga Melee 3.ogg"
    if Random == 4:
        play avavoice "sound/Voice/Asaga/Asaga Melee 4.ogg"

    show blackjack:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show asaga plugsuit point happy:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit point happy:
        ease 1.5 alpha 0

    pause 0.8

    play sound "sound/mech1.ogg"
    show blackjack melee with dissolve

    pause 0.5

    play sound1 "sound/boasters.ogg"

    show blackjack melee:
        xpos 0.5 ypos 0.5
        ease 1.0 xpos 2.0 ypos -1.0

    pause 1.4

    return

label hitanim_blackjack_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show blackjack:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 520 xzoom -1
        linear 0.25 xpos 972 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 460 xzoom -1
        linear 0.25 xpos 705 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    pause 0.5

    call hit_blackjack

    return

label hitanim_blackjack_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show blackjack:
        xpos 0.5 ypos 0.5

    pause 0.05

    play sound "sound/missilefly.ogg"

    show blackjack_hitmissile1:
        alpha 0 xpos 1350 ypos 0 zoom 1.2
        pause 0.4
        alpha 1
        linear 0.5 xpos 550 ypos 490
        alpha 0

    show blackjack_hitmissile2:
        alpha 0 xpos 1540 ypos 0 zoom 1.2
        pause 0.3
        alpha 1
        linear 0.5 xpos 700 ypos 530
        alpha 0

    show blackjack_hitmissile3:
        alpha 0 xpos 1650 ypos 0 zoom 1.2
        pause 0.2
        alpha 1
        linear 0.5 xpos 880 ypos 500
        alpha 0

    show blackjack_hitmissile4:
        alpha 0 xpos 1825 ypos 0 zoom 1.2
        pause 0.1
        alpha 1
        linear 0.6 xpos 950 ypos 540
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit1:
        alpha 0 xpos 0.4 ypos 0.5
        pause 0.8
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit2:
        alpha 0 xpos 0.35 ypos 0.45
        pause 0.9
        alpha 1
        ease 1 alpha 0

    pause 0.05

    show blackjack_hitmissiletrail with sunridermissilehitwipe
    hide blackjack_hitmissiletrail with dissolve

    pause 0.1

    call hit_blackjack

    return

label hitanim_blackjack_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show blackjack:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.4 ypos 0.5 xzoom -1
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    play sound "sound/explosion1.ogg"

    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.4 ypos 0.5  xzoom -1
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show blackjack_hitlaser behind piratebomber_laserhitexplode2 with enemy_laserhitwipe
    hide blackjack_hitlaser with enemy_laserhitwipe

    pause 0.5

    call hit_blackjack

    return

label hitanim_blackjack_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show blackjack:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show blackjack_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show blackjack_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    play sound3 "sound/explosion3.ogg"

    show blackjack_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 1

    call hit_blackjack

    return

label hitanim_blackjack_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show blackjack:
        xpos 0.5 ypos 0.5

    show piratebomber_hitrocket:
        xpos 3000 ypos 490 xzoom -1
        pause 0.5
        linear 0.6 xpos 1010 ypos 490
        alpha 0

    show layer master at shake2(pausetime=1.1,repeats=8)
    show blackjack_rocketexplode:
        alpha 0
        pause 1.1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0
    
    pause 0.7

    play sound "sound/explosion4.ogg"

    show blackjack_rockettrail behind piratebomber_hitrocket with enemy_laserhitwipe
    hide blackjack_rockettrail with dissolve

    pause 0.5

    call hit_blackjack

    return

label hitanim_blackjack_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show blackjack:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.2

    call hit_blackjack

    return

label hitanim_blackjack_melee:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show blackjack:
        xpos 0.5 ypos 0.5

    show havoc melee:
        xpos 2.0 ypos 0.8
        ease 1.5 xpos 0.1 ypos 0.5

    pause 0.9

    play sound "sound/Sword Shing 2.ogg"

    show melee_overlay:
        xzoom -1
    with meleehit

    pause 0.1

    hide melee_overlay with dissolvequick

    pause 0.2

    show havoc melee:
        xpos 0.1 ypos 0.5
        ease 1.0 xpos -1.0 ypos -1.0

    pause 0.3

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.4 ypos 0.5 xzoom -1 zoom 1.2
        ease 1.2 alpha 0

    pause 0.1

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5 xzoom -1 zoom 1.2
        ease 1.2 alpha 0

    pause 0.5

    call hit_blackjack

    return

label miss_blackjack:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show blackjack behind miss:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,6)

    if Random == 1:
        play asavoice "sound/Voice/Asaga/Asaga No Damage 1.ogg"
    if Random == 2:
        play asavoice "sound/Voice/Asaga/Asaga No Damage 2.ogg"
    if Random == 3:
        play asavoice "sound/Voice/Asaga/Asaga No Damage 3.ogg"
    if Random == 4:
        play asavoice "sound/Voice/Asaga/Asaga No Damage 4.ogg"
    if Random == 5:
        play asavoice "sound/Voice/Asaga/Asaga No Damage 5.ogg"
    if Random == 6:
        play asavoice "sound/Voice/Asaga/Asaga No Damage 6.ogg"

    show asaga plugsuit handsonhips grin:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit handsonhips grin:
        ease 1.5 alpha 0

    pause 2

    return

label attacksuccess_blackjack:

    show layer master

    $ Random = renpy.random.randint(1,6)

    if Random == 1:
        play asavoice "sound/Voice/Asaga/Asaga Success 1.ogg"
    if Random == 2:
        play asavoice "sound/Voice/Asaga/Asaga Success 2.ogg"
    if Random == 3:
        play asavoice "sound/Voice/Asaga/Asaga Success 3.ogg"
    if Random == 4:
        play asavoice "sound/Voice/Asaga/Asaga Success 4.ogg"
    if Random == 5:
        play asavoice "sound/Voice/Asaga/Asaga Success 5.ogg"
    if Random == 6:
        play asavoice "sound/Voice/Asaga/Asaga Success 6.ogg"

    show asaga plugsuit vpose:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit vpose:
        ease 1.5 alpha 0

    pause
    return

label attackfail_blackjack:

    show layer master

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play asavoice "sound/Voice/Asaga/Asaga Miss 1.ogg"
    if Random == 2:
        play asavoice "sound/Voice/Asaga/Asaga Miss 2.ogg"
    if Random == 3:
        play asavoice "sound/Voice/Asaga/Asaga Miss 3.ogg"
    if Random == 4:
        play asavoice "sound/Voice/Asaga/Asaga Miss 4.ogg"
    if Random == 5:
        play asavoice "sound/Voice/Asaga/Asaga Miss 5.ogg"

    show asaga plugsuit handsonhips frown:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit handsonhips frown:
        ease 1.5 alpha 0

    pause
    return

label hit_blackjack:

    show layer master

    if blackjack.hp >= blackjack.max_hp * 0.8:
        play asavoice "sound/Voice/Asaga/Asaga Damage 1.ogg"
    if blackjack.hp < blackjack.max_hp * 0.8 and blackjack.hp >= blackjack.max_hp * 0.6:
        play asavoice "sound/Voice/Asaga/Asaga Damage 2.ogg"
    if blackjack.hp < blackjack.max_hp * 0.6 and blackjack.hp >= blackjack.max_hp * 0.4:
        play asavoice "sound/Voice/Asaga/Asaga Damage 3.ogg"
    if blackjack.hp < blackjack.max_hp * 0.4 and blackjack.hp >= blackjack.max_hp * 0.2:
        play asavoice "sound/Voice/Asaga/Asaga Damage 4.ogg"
    if blackjack.hp < blackjack.max_hp * 0.2:
        play asavoice "sound/Voice/Asaga/Asaga Damage 5.ogg"

    show asaga plugsuit handsonhips frown onlayer screens:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit handsonhips frown onlayer screens:
        ease 1.5 alpha 0

    pause

    return

label die_blackjack:

    $renpy.show_screen('show_background',_layer='master')

    show blackjack:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play asavoice "sound/Voice/Asaga/Asaga Retreat 1.ogg"
    if Random == 2:
        play asavoice "sound/Voice/Asaga/Asaga Retreat 2.ogg"
    if Random == 3:
        play asavoice "sound/Voice/Asaga/Asaga Retreat 3.ogg"
    if Random == 4:
        play asavoice "sound/Voice/Asaga/Asaga Retreat 4.ogg"
    if Random == 5:
        play asavoice "sound/Voice/Asaga/Asaga Retreat 5.ogg"

    show asaga plugsuit armscrossed sad:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show asaga plugsuit armscrossed sad:
        ease 1.5 alpha 0

    pause 1.0

    show blackjack:
        ease 0.5 xpos -0.5 ypos -1.0
    with dissolvequick

    pause

    return


label atkanim_liberty_laser: ########################LIBERTY ATTACK ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play chivoice "sound/Voice/Chigara/Attack With Lasers Line 1.ogg"
    if Random == 2:
        play chivoice "sound/Voice/Chigara/Attack With Lasers Line 2.ogg"
    if Random == 3:
        play chivoice "sound/Voice/Chigara/Attack With Lasers Line 3.ogg"
    if Random == 4:
        play chivoice "sound/Voice/Chigara/Attack With Lasers Line 4.ogg"

    show liberty:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show chigara plugsuit altneutral shout:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show chigara plugsuit altneutral shout:
        ease 1.5 alpha 0

    pause 0.8

    play sound "sound/mech1.ogg"
    show liberty laser with dissolve

    pause 0.3

    show liberty_laserflash1 with dissolve

    play sound "sound/Laser 1.ogg"

    show liberty_laserflash2 behind liberty_laserflash1 with laserwipe
    hide liberty_laserflash2 behind liberty_laserflash1 with laserwipe

    pause 0.5

    return

label hitanim_liberty_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show liberty:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 520 xzoom -1
        linear 0.25 xpos 972 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 460 xzoom -1
        linear 0.25 xpos 705 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    pause 0.5

    call hit_liberty

    return

label hitanim_liberty_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show liberty:
        xpos 0.5 ypos 0.5

    pause 0.05

    play sound "sound/missilefly.ogg"

    show blackjack_hitmissile1:
        alpha 0 xpos 1350 ypos 0 zoom 1.2
        pause 0.4
        alpha 1
        linear 0.5 xpos 550 ypos 490
        alpha 0

    show blackjack_hitmissile2:
        alpha 0 xpos 1540 ypos 0 zoom 1.2
        pause 0.3
        alpha 1
        linear 0.5 xpos 700 ypos 530
        alpha 0

    show blackjack_hitmissile3:
        alpha 0 xpos 1650 ypos 0 zoom 1.2
        pause 0.2
        alpha 1
        linear 0.5 xpos 880 ypos 500
        alpha 0

    show blackjack_hitmissile4:
        alpha 0 xpos 1825 ypos 0 zoom 1.2
        pause 0.1
        alpha 1
        linear 0.6 xpos 950 ypos 540
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit1:
        alpha 0 xpos 0.4 ypos 0.5
        pause 0.8
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit2:
        alpha 0 xpos 0.35 ypos 0.45
        pause 0.9
        alpha 1
        ease 1 alpha 0

    pause 0.05

    show blackjack_hitmissiletrail with sunridermissilehitwipe
    hide blackjack_hitmissiletrail with dissolve

    pause 0.1

    call hit_liberty

    return

label hitanim_liberty_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show liberty:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.4 ypos 0.5 xzoom -1
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    play sound "sound/explosion1.ogg"

    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.4 ypos 0.5  xzoom -1
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show blackjack_hitlaser behind piratebomber_laserhitexplode2 with enemy_laserhitwipe
    hide blackjack_hitlaser with enemy_laserhitwipe

    pause 0.5

    call hit_liberty

    return

label hitanim_liberty_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show liberty:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show blackjack_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show blackjack_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    play sound3 "sound/explosion3.ogg"

    show blackjack_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 1

    call hit_liberty

    return

label hitanim_liberty_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show liberty:
        xpos 0.5 ypos 0.5

    show piratebomber_hitrocket:
        xpos 3000 ypos 490 xzoom -1
        pause 0.5
        linear 0.6 xpos 1010 ypos 490
        alpha 0

    show layer master at shake2(pausetime=1.1,repeats=8)
    show blackjack_rocketexplode:
        alpha 0
        pause 1.1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0
    
    pause 0.7

    play sound "sound/explosion4.ogg"

    show blackjack_rockettrail behind piratebomber_hitrocket with enemy_laserhitwipe
    hide blackjack_rockettrail with dissolve

    pause 0.5

    call hit_liberty

    return

label hitanim_liberty_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show liberty:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.2

    call hit_liberty

    return

label miss_liberty:

    $renpy.show_screen('show_background',_layer='master')

    show chigara plugsuit handonchest happy:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show chigara plugsuit handonchest happy:
        ease 1.5 alpha 0

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show liberty behind miss:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,6)

    if Random == 1:
        play chivoice "sound/Voice/Chigara/No Damage Line 1.ogg"
    if Random == 2:
        play chivoice "sound/Voice/Chigara/No Damage Line 2.ogg"
    if Random == 3:
        play chivoice "sound/Voice/Chigara/No Damage Line 3.ogg"
    if Random == 4:
        play chivoice "sound/Voice/Chigara/No Damage Line 4.ogg"
    if Random == 5:
        play chivoice "sound/Voice/Chigara/No Damage Line 5.ogg"
    if Random == 6:
        play chivoice "sound/Voice/Chigara/No Damage Line 6.ogg"

    pause 2

    return

label attacksuccess_liberty:

    show layer master

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play chivoice "sound/Voice/Chigara/Successful Attack Line 1.ogg"
    if Random == 2:
        play chivoice "sound/Voice/Chigara/Successful Attack Line 2.ogg"
    if Random == 3:
        play chivoice "sound/Voice/Chigara/Successful Attack Line 3.ogg"

    show chigara plugsuit handonchest happy:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show chigara plugsuit handonchest happy:
        ease 1.5 alpha 0

    pause
    return

label attackfail_liberty:

    show layer master

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play asavoice "sound/Voice/Chigara/Attack Miss Line 1.ogg"
    if Random == 2:
        play asavoice "sound/Voice/Chigara/Attack Miss Line 2.ogg"
    if Random == 3:
        play asavoice "sound/Voice/Chigara/Attack Miss Line 3.ogg"

    show chigara plugsuit altneutral sad:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show chigara plugsuit altneutral sad:
        ease 1.5 alpha 0

    pause
    return

label hit_liberty:

    show layer master

    if liberty.hp >= liberty.max_hp * 0.8:
        play chivoice "sound/Voice/Chigara/Damage Line 1.ogg"
    if liberty.hp < liberty.max_hp * 0.8 and liberty.hp >= liberty.max_hp * 0.6:
        play chivoice "sound/Voice/Chigara/Damage Line 2.ogg"
    if liberty.hp < liberty.max_hp * 0.6 and liberty.hp >= liberty.max_hp * 0.4:
        play chivoice "sound/Voice/Chigara/Damage Line 3.ogg"
    if liberty.hp < liberty.max_hp * 0.4 and liberty.hp >= liberty.max_hp * 0.2:
        play chivoice "sound/Voice/Chigara/Damage Line 4.ogg"
    if liberty.hp < liberty.max_hp * 0.2:
        play chivoice "sound/Voice/Chigara/Damage Line 5.ogg"

    show chigara plugsuit palmsup surprise:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show chigara plugsuit palmsup surprise:
        ease 1.5 alpha 0

    pause

    return

label die_liberty:

    $renpy.show_screen('show_background',_layer='master')

    show liberty:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play chivoice "sound/Voice/Chigara/Retreat Line 1.ogg"
    if Random == 2:
        play chivoice "sound/Voice/Chigara/Retreat Line 1.ogg"
    if Random == 3:
        play chivoice "sound/Voice/Chigara/Retreat Line 1.ogg"
    if Random == 4:
        play chivoice "sound/Voice/Chigara/Retreat Line 1.ogg"
    if Random == 5:
        play chivoice "sound/Voice/Chigara/Retreat Line 1.ogg"

    show chigara plugsuit altneutral sad:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show chigara plugsuit altneutral sad:
        ease 1.5 alpha 0

    pause 1.0

    show liberty:
        ease 0.5 xpos -0.5 ypos -1.0
    with dissolvequick

    pause

    return

label atkanim_seraphim_kinetic:########################SERAPHIM ATTACK ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,11)

    if Random == 1:
        play solvoice "sound/Voice/Sola/Attack 1.ogg"
    if Random == 2:
        play solvoice "sound/Voice/Sola/Attack 2.ogg"
    if Random == 3:
        play solvoice "sound/Voice/Sola/Attack 3.ogg"
    if Random == 4:
        play solvoice "sound/Voice/Sola/Attack 4.ogg"
    if Random == 5:
        play solvoice "sound/Voice/Sola/Attack 5.ogg"
    if Random == 6:
        play solvoice "sound/Voice/Sola/Attack 6.ogg"
    if Random == 7:
        play solvoice "sound/Voice/Sola/Attack 7.ogg"
    if Random == 8:
        play solvoice "sound/Voice/Sola/Attack 8.ogg"
    if Random == 9:
        play solvoice "sound/Voice/Sola/Attack 9.ogg"
    if Random == 10:
        play solvoice "sound/Voice/Sola/Attack 10.ogg"
    if Random == 11:
        play solvoice "sound/Voice/Sola/Attack 11.ogg"

    show seraphim:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show sola plugsuit altneutral neutral:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show sola plugsuit altneutral neutral:
        ease 1.5 alpha 0

    pause 0.8

    play sound "sound/mech1.ogg"
    show seraphim kinetic with dissolve

    play sound1 "sound/Sola Sniper.ogg"

    pause 0.5
    show seraphim_charge1 with dissolve
    pause 0.6

    show layer master at shake1(pausetime=0.1)

    show seraphim_charge2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.1 alpha 1
        pause 0.1
        ease 0.1 alpha 0 zoom 1.5
    show seraphim_bullet:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.1
        alpha 1.0
        ease 0.2 xpos 2.0 ypos 2.0

    pause 0.8

    return

label hitanim_seraphim_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show seraphim:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 520 xzoom -1
        linear 0.25 xpos 972 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 460 xzoom -1
        linear 0.25 xpos 705 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    pause 0.5

    call hit_seraphim

    return

label hitanim_seraphim_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show seraphim:
        xpos 0.5 ypos 0.5

    pause 0.05

    play sound "sound/missilefly.ogg"

    show blackjack_hitmissile1:
        alpha 0 xpos 1350 ypos 0 zoom 1.2
        pause 0.4
        alpha 1
        linear 0.5 xpos 550 ypos 490
        alpha 0

    show blackjack_hitmissile2:
        alpha 0 xpos 1540 ypos 0 zoom 1.2
        pause 0.3
        alpha 1
        linear 0.5 xpos 700 ypos 530
        alpha 0

    show blackjack_hitmissile3:
        alpha 0 xpos 1650 ypos 0 zoom 1.2
        pause 0.2
        alpha 1
        linear 0.5 xpos 880 ypos 500
        alpha 0

    show blackjack_hitmissile4:
        alpha 0 xpos 1825 ypos 0 zoom 1.2
        pause 0.1
        alpha 1
        linear 0.6 xpos 950 ypos 540
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit1:
        alpha 0 xpos 0.4 ypos 0.5
        pause 0.8
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit2:
        alpha 0 xpos 0.35 ypos 0.45
        pause 0.9
        alpha 1
        ease 1 alpha 0

    pause 0.05

    show blackjack_hitmissiletrail with sunridermissilehitwipe
    hide blackjack_hitmissiletrail with dissolve

    pause 0.1

    call hit_seraphim

    return

label hitanim_seraphim_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show seraphim:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.4 ypos 0.5 xzoom -1
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    play sound "sound/explosion1.ogg"

    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.4 ypos 0.5  xzoom -1
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show blackjack_hitlaser behind piratebomber_laserhitexplode2 with enemy_laserhitwipe
    hide blackjack_hitlaser with enemy_laserhitwipe

    pause 0.5

    call hit_seraphim

    return

label hitanim_seraphim_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show seraphim:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show blackjack_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show blackjack_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    play sound3 "sound/explosion3.ogg"

    show blackjack_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 1

    call hit_seraphim

    return

label hitanim_seraphim_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show seraphim:
        xpos 0.5 ypos 0.5

    show piratebomber_hitrocket:
        xpos 3000 ypos 490 xzoom -1
        pause 0.5
        linear 0.6 xpos 1010 ypos 490
        alpha 0

    show layer master at shake2(pausetime=1.1,repeats=8)
    show blackjack_rocketexplode:
        alpha 0
        pause 1.1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0
    
    pause 0.7

    play sound "sound/explosion4.ogg"

    show blackjack_rockettrail behind piratebomber_hitrocket with enemy_laserhitwipe
    hide blackjack_rockettrail with dissolve

    pause 0.5

    call hit_seraphim

    return

label hitanim_seraphim_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show seraphim:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.2

    call hit_seraphim

    return

label miss_seraphim:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show seraphim behind miss:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play solvoice "sound/Voice/Sola/Evade 1.ogg"
    if Random == 2:
        play solvoice "sound/Voice/Sola/Evade 2.ogg"
    if Random == 3:
        play solvoice "sound/Voice/Sola/Evade 3.ogg"
    if Random == 4:
        play solvoice "sound/Voice/Sola/Evade 4.ogg"
    if Random == 5:
        play solvoice "sound/Voice/Sola/Evade 5.ogg"

    show sola plugsuit altneutral neutral:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show sola plugsuit altneutral neutral:
        ease 1.5 alpha 0

    pause 2

    return

label attacksuccess_seraphim:

    show layer master

    play solvoice "sound/Voice/Sola/Hit 1.ogg"

    show sola plugsuit altneutral neutral:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show sola plugsuit altneutral neutral:
        ease 1.5 alpha 0

    pause
    return

label attackfail_seraphim:

    show layer master

    play solvoice "sound/Voice/Sola/Miss 1.ogg"

    show sola plugsuit altneutral neutral:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show sola plugsuit altneutral neutral:
        ease 1.5 alpha 0

    pause
    return

label hit_seraphim:

    show layer master

    if seraphim.hp >= seraphim.max_hp * 0.8:
        play solvoice "sound/Voice/Sola/Damaged 1.ogg"
    if seraphim.hp < seraphim.max_hp * 0.8 and seraphim.hp >= seraphim.max_hp * 0.6:
        play solvoice "sound/Voice/Sola/Damaged 2.ogg"
    if seraphim.hp < seraphim.max_hp * 0.6 and seraphim.hp >= seraphim.max_hp * 0.4:
        play solvoice "sound/Voice/Sola/Damaged 3.ogg"
    if seraphim.hp < seraphim.max_hp * 0.4 and seraphim.hp >= seraphim.max_hp * 0.2:
        play solvoice "sound/Voice/Sola/Damaged 4.ogg"
    if seraphim.hp < seraphim.max_hp * 0.2:
        play solvoice "sound/Voice/Sola/Damaged 5.ogg"

    show sola plugsuit altneutral neutral onlayer screens:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show sola plugsuit altneutral neutral onlayer screens:
        ease 1.5 alpha 0

    pause

    return

label die_seraphim:

    $renpy.show_screen('show_background',_layer='master')

    show seraphim:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play solvoice "sound/Voice/Sola/Die 1.ogg"
    if Random == 2:
        play solvoice "sound/Voice/Sola/Die 2.ogg"
    if Random == 3:
        play solvoice "sound/Voice/Sola/Die 3.ogg"
    if Random == 4:
        play solvoice "sound/Voice/Sola/Die 4.ogg"
    if Random == 5:
        play solvoice "sound/Voice/Sola/Die 5.ogg"

    show sola plugsuit altneutral neutral:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show sola plugsuit altneutral neutral:
        ease 1.5 alpha 0

    pause 1.0

    show seraphim:
        ease 0.5 xpos -0.5 ypos -1.0
    with dissolvequick

    pause

    return


label atkanim_piratebomber_missile: ##########################PIRATE BOMBER ATTACK ANIMATIONS


    $renpy.show_screen('show_background',_layer='master')

    show piratebomber:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    pause 0.2

    play sound1 "sound/MechHeavy.ogg"

    show piratebomber missile with dissolve

    pause 0.1

    play sound "sound/missile.ogg"

    show piratebomber_missile1:
        xpos 950 ypos 251 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos -105

    show piratebomber_missile2:
        xpos 920 ypos 260 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos -125

    show piratebomber_missile3:
        xpos 1187 ypos 254 alpha 0
        pause 0.35
        alpha 1
        linear 0.6 xpos -300 ypos -160

    show piratebomber_missile4:
        xpos 1172 ypos 271 alpha 0
        pause 0.35
        alpha 1
        linear 0.6 xpos -300 ypos -180

    show piratebomber_missile5:
        xpos 948 ypos 608 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos 250

    show piratebomber_missile6:
        xpos 1128 ypos 698 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos 300

    show piratebomber_missiletrial with piratebomber_missilewipe
    hide piratebomber_missiletrial with dissolve

    pause 0.1

    return

label atkanim_piratebomber_rocket:

    $renpy.show_screen('show_background',_layer='master')

    show piratebomber:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    pause 0.5

    play sound1 "sound/MechHeavy.ogg"
    show piratebomber rocket with dissolve

    pause 0.5

    show piratebomber norocket

    play sound "sound/missilelaunch.ogg"
    show piratebomber_rocket1:
        xpos 0.5 ypos 0.5
        linear 0.5 xpos -0.4 ypos 0.22

    show piratebomber_rocket2:
        xpos 0.5 ypos 0.5
        linear 0.5 xpos -0.4 ypos 0.22

    pause 1

    return

label atkanim_piratebomber_assault:

    $renpy.show_screen('show_background',_layer='master')

    show piratebomber:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    pause 0.5

    play sound1 "sound/MechHeavy.ogg"
    show piratebomber assault with dissolve

    pause 0.3

    play sound "sound/machinegun.ogg"
    show piratebomber_assaultflash1:
        alpha 0
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    show piratebomber_assaultflash2:
        alpha 0
        pause 0.30
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    pause 1.5

    return

label hitanim_piratebomber_kinetic: ##########################PIRATE BOMBER HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp


    show piratebomber:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.6 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebomber_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratebomber:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0 zoom 1.2
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0 zoom 1.2
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0 zoom 1.2
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0 zoom 1.2
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebomber_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratebomber:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"
    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhittrail behind piratebomber_laserhitexplode with pactmissilefrigate_laserhitwipe
    hide piratebomber_laserhittrail with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebomber_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show piratebomber:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebomber_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratebomber:
        xpos 0.5 ypos 0.5

    pause 0.1
    show piratebomber_hitrocket:
        xpos -200 ypos 440
        linear 0.4 xpos 1010 ypos 448
        alpha 0

    if sunrider.weapons[3].damage == 800:
        show layer master at shake2(pausetime=0.4,repeats=8)
        play sound "sound/explosion4.ogg"
        show pactmissilefrigate_die3:
            xpos 0.5 ypos 0.5 alpha 0
            pause 0.4
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0

    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 0.4
            ease 0.4 alpha 1.0 zoom 1.5
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show piratebomber_hitrockettrail behind piratebomber_hitrocket:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_laserhitwipe
    show piratebomber_hitrockettrail:
        ease 1.0 alpha 0

    if sunrider.weapons[3].damage == 1200:
        pause 3.0
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebomber_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratebomber:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebomber_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show piratebomber:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label die_piratebomber:

    $renpy.show_screen('show_background',_layer='master')

    show piratebomber:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion1.ogg"
    show layer master at shake1
    show piratebomber_die1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound2 "sound/explosion1.ogg"
    show layer master at shake1
    show piratebomber_die2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound3 "sound/explosion4.ogg"
    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide piratebomber
    show piratebomber_die3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_piratebomber:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show piratebomber behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label atkanim_pactcruiser_kinetic: ################################# PACT CRUISER KINETIC

    $renpy.show_screen('show_background',_layer='master')

    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.2

    show layer master at shake1
    show pactcruiser_kineticflash1:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show pactcruiser_kineticbullet1:
        xpos 801 ypos 437
        linear 0.15 xpos -200 ypos 350
    play sound1 'sound/explosion1.ogg'
    pause 0.05

    show layer master at shake1
    show pactcruiser_kineticflash1:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show pactcruiser_kineticbullet2:
        xpos 808 ypos 425
        linear 0.15 xpos -200 ypos 362
    play sound2 'sound/explosion1.ogg'
    pause 0.2

    show layer master at shake1
    show pactcruiser_kineticflash2:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show pactcruiser_kineticbullet3:
        xpos 923 ypos 419
        linear 0.15 xpos -200 ypos 300
    play sound1 'sound/explosion1.ogg'
    pause 0.05

    show layer master at shake1
    show pactcruiser_kineticflash2:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show layer master at shake1
    show pactcruiser_kineticbullet4:
        xpos 927 ypos 410
        linear 0.15 xpos -200 ypos 290
    play sound2 'sound/explosion1.ogg'
    pause 0.05

    pause 0.5
    return

label atkanim_pactcruiser_assault:

    $renpy.show_screen('show_background',_layer='master')
    show pactcruiser_side:
        xpos 0.5 ypos 0.5
    pause 0.5

    python:
        flak_positions1 = [
            (816,451),
            (897,451),
            (1272,432)
            ]
        Flak1 = FlakShield("gameplay/Animations/PACTCruiser/flakbullet.png",flak_positions1,5000,dispersion=2, angle=290, interval=0.15)

        flak_positions2 = [
            (792,451),
            (835,451),
            (1238,432)
            ]
        Flak2 = FlakShield("gameplay/Animations/PACTCruiser/flakbullet.png",flak_positions2,5000,dispersion=2, angle=290, interval=0.15)

    play sound "sound/Flak.ogg"

    $ Flak1.show()
    show pactcruiser_flakflash1
    pause 0.01
    hide pactcruiser_flakflash1
    pause 0.01
    show pactcruiser_flakflash1
    pause 0.01
    hide pactcruiser_flakflash1
    pause 0.01
    show pactcruiser_flakflash1
    pause 0.01
    hide pactcruiser_flakflash1
    pause 0.01
    show pactcruiser_flakflash1
    pause 0.01
    hide pactcruiser_flakflash1
    pause 0.01
    $ Flak1.stop()
    $ Flak2.show()
    show pactcruiser_flakflash2
    pause 0.01
    hide pactcruiser_flakflash2
    pause 0.01
    show pactcruiser_flakflash2
    pause 0.01
    hide pactcruiser_flakflash2
    pause 0.01
    show pactcruiser_flakflash2
    pause 0.01
    hide pactcruiser_flakflash2
    pause 0.01
    show pactcruiser_flakflash2
    pause 0.01
    hide pactcruiser_flakflash2
    pause 0.01
    $ Flak2.stop()
    $ Flak1.start()
    show pactcruiser_flakflash1
    pause 0.01
    hide pactcruiser_flakflash1
    pause 0.01
    show pactcruiser_flakflash1
    pause 0.01
    hide pactcruiser_flakflash1
    pause 0.01
    show pactcruiser_flakflash1
    pause 0.01
    hide pactcruiser_flakflash1
    pause 0.01
    show pactcruiser_flakflash1
    pause 0.01
    hide pactcruiser_flakflash1
    pause 0.01
    $ Flak1.stop()
    $ Flak2.start()
    show pactcruiser_flakflash2
    pause 0.01
    hide pactcruiser_flakflash2
    pause 0.01
    show pactcruiser_flakflash2
    pause 0.01
    hide pactcruiser_flakflash2
    pause 0.01
    show pactcruiser_flakflash2
    pause 0.01
    hide pactcruiser_flakflash2
    pause 0.01
    show pactcruiser_flakflash2
    pause 0.01
    hide pactcruiser_flakflash2
    pause 0.01
    $ Flak2.stop()

    pause 0.5

    return

label atkanim_pactcruiser_laser:

    $renpy.show_screen('show_background',_layer='master')
    show pactcruiser_side:
        xpos 0.5 ypos 0.5
    play sound2 'sound/legion_laser.ogg'

    pause 0.001

    show pactcruiser_laserfront:
        xpos 0.5 ypos 0.5
    show pactcruiser_laserback behind pactcruiser_side:
        xpos 0.5 ypos 0.5
    with enemy_laserhitwipe

    hide pactcruiser_laserfront
    hide pactcruiser_laserback
    with enemy_laserhitwipe

    pause 0.5
    return

label hitanim_pactcruiser_kinetic:   ##############PACT CRUISER HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcruiser_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show pactmissilefrigate_hitmissileexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show pactmissilefrigate_hitmissileexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcruiser_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show pactmissilefrigate_hitlaserexplode:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe
    hide pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcruiser_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show sunrider_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcruiser_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 0 ypos 570
        linear 1.1 xpos 1160 ypos 570
        alpha 0


    show layer master at shake2(pausetime=1,repeats=8)
    if sunrider.weapons[3].damage == 800:
        play sound1 "sound/explosion5.ogg"
        show pactmissilefrigate_rocketexplode:
            xpos 0.5 ypos 0.5 alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        
    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 1
            ease 0.05 alpha 1.0 zoom 1.0 
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show pactmissilefrigate_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_rockethitwipe

    show pactmissilefrigate_rockettrail:
        ease 1.0 alpha 0
    
    if sunrider.weapons[3].damage == 1200:
        pause 1.5
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 1.5
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcruiser_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcruiser_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return


label die_pactcruiser: ###################################PACT CRUISER DEATH

    $renpy.show_screen('show_background',_layer='master')

    show pactcruiser_side:
        xpos 0.5 ypos 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide pactcruiser_side
    show pactcruiser_dead3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_pactcruiser:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show pactcruiser_side behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label atkanim_pactbattleship_kinetic: ################################# PACT BATTLESHIP BEGIN

    $renpy.show_screen('show_background',_layer='master')

    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.2

    show layer master at shake1
    show pactbattleship_kineticflash1:
        alpha 0
        ease 0.1 alpha 1
        ease 0.1 alpha 0
    show pactbattleship_kineticbullet1:
        xpos 360 ypos 440
        linear 0.15 xpos -500 ypos 360
    play sound1 'sound/explosion1.ogg'
    pause 0.1

    show layer master at shake1
    show pactbattleship_kineticflash2:
        alpha 0
        ease 0.1 alpha 1
        ease 0.1 alpha 0
    show pactbattleship_kineticbullet2:
        xpos 460 ypos 430
        linear 0.15 xpos -400 ypos 340
    play sound2 'sound/explosion1.ogg'
    pause 0.1

    show layer master at shake1
    show pactbattleship_kineticflash3:
        alpha 0
        ease 0.1 alpha 1
        ease 0.1 alpha 0
    show layer master at shake1
    show pactbattleship_kineticbullet3:
        xpos 700 ypos 420
        linear 0.15 xpos -320 ypos 330
    play sound3 'sound/explosion1.ogg'
    pause 0.1

    pause 0.5
    return

label atkanim_pactbattleship_assault:

    $renpy.show_screen('show_background',_layer='master')
    show pactbattleship_side:
        xpos 0.5 ypos 0.5
    pause 0.5

    python:
        flak_positions1 = [
            (539,428),
            (591,424),
            (691,405),
            (736,402)
            ]
        Flak1 = FlakShield("gameplay/Animations/PACTBattleship/flakbullet.png",flak_positions1,4000,dispersion=5, angle=285, interval=0.15)

        flak_positions2 = [
            (561,424),
            (632,417),
            (668,410),
            (745,399)
            ]
        Flak2 = FlakShield("gameplay/Animations/PACTBattleship/flakbullet.png",flak_positions2,4000,dispersion=5, angle=285, interval=0.15)

    play sound "sound/Flak.ogg"

    $ Flak1.show()
    show pactbattleship_flakflash1
    pause 0.01
    hide pactbattleship_flakflash1
    pause 0.01
    show pactbattleship_flakflash1
    pause 0.01
    hide pactbattleship_flakflash1
    pause 0.01
    show pactbattleship_flakflash1
    pause 0.01
    hide pactbattleship_flakflash1
    pause 0.01
    show pactbattleship_flakflash1
    pause 0.01
    hide pactbattleship_flakflash1
    pause 0.01
    $ Flak1.stop()
    $ Flak2.show()
    show pactbattleship_flakflash2
    pause 0.01
    hide pactbattleship_flakflash2
    pause 0.01
    show pactbattleship_flakflash2
    pause 0.01
    hide pactbattleship_flakflash2
    pause 0.01
    show pactbattleship_flakflash2
    pause 0.01
    hide pactbattleship_flakflash2
    pause 0.01
    show pactbattleship_flakflash2
    pause 0.01
    hide pactbattleship_flakflash2
    pause 0.01
    $ Flak2.stop()
    $ Flak1.start()
    show pactbattleship_flakflash1
    pause 0.01
    hide pactbattleship_flakflash1
    pause 0.01
    show pactbattleship_flakflash1
    pause 0.01
    hide pactbattleship_flakflash1
    pause 0.01
    show pactbattleship_flakflash1
    pause 0.01
    hide pactbattleship_flakflash1
    pause 0.01
    show pactbattleship_flakflash1
    pause 0.01
    hide pactbattleship_flakflash1
    pause 0.01
    $ Flak1.stop()
    $ Flak2.start()
    show pactbattleship_flakflash2
    pause 0.01
    hide pactbattleship_flakflash2
    pause 0.01
    show pactbattleship_flakflash2
    pause 0.01
    hide pactbattleship_flakflash2
    pause 0.01
    show pactbattleship_flakflash2
    pause 0.01
    hide pactbattleship_flakflash2
    pause 0.01
    show pactbattleship_flakflash2
    pause 0.01
    hide pactbattleship_flakflash2
    pause 0.01
    $ Flak2.stop()

    pause 0.5

    return

label atkanim_pactbattleship_laser:

    $renpy.show_screen('show_background',_layer='master')
    show pactbattleship_side:
        xpos 0.5 ypos 0.5
    play sound2 'sound/legion_laser.ogg'

    pause 0.001

    show pactbattleship_laserfront:
        xpos 0.5 ypos 0.5
    show pactbattleship_laserback behind pactbattleship_side:
        xpos 0.5 ypos 0.5
    with enemy_laserhitwipe

    hide pactbattleship_laserfront
    hide pactbattleship_laserback
    with enemy_laserhitwipe

    pause 0.5
    return

label atkanim_pactbattleship_missile:

    $renpy.show_screen('show_background',_layer='master')

    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.01

    play sound "sound/missile.ogg"

    show pactbattleship_missile1:
        xpos 945 ypos 470 alpha 0
        pause 0.69
        alpha 1
        linear 0.6 xpos -400 ypos 0

    show pactbattleship_missile2:
        xpos 1015 ypos 465 alpha 0
        pause 0.67
        alpha 1
        linear 0.6 xpos -400 ypos -40

    show pactbattleship_missile3:
        xpos 1100 ypos 455 alpha 0
        pause 0.65
        alpha 1
        linear 0.6 xpos -400 ypos -80

    pause 0.25

    show pactbattleship_missiletrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_missilewipe
    hide pactbattleship_missiletrail with dissolve

    pause 0.1

    return

label atkanim_pactbattleship_rocket:

    $renpy.show_screen('show_background',_layer='master')

    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.01

    play sound "sound/missilelaunch.ogg"

    show pactbattleship_rocket:
        xpos 500 ypos 520 alpha 0
        pause 0.9
        alpha 1
        linear 0.6 xpos -400 ypos 520

    pause 0.25

    show pactbattleship_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_missilewipe
    hide pactbattleship_rockettrail with dissolve

    pause 0.1

    return

label hitanim_pactbattleship_kinetic:   ##############PACT CRUISER HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbattleship_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show pactmissilefrigate_hitmissileexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show pactmissilefrigate_hitmissileexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbattleship_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show pactmissilefrigate_hitlaserexplode:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe
    hide pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbattleship_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show sunrider_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbattleship_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 0 ypos 570
        linear 1.1 xpos 1160 ypos 570
        alpha 0


    show layer master at shake2(pausetime=1,repeats=8)
    if sunrider.weapons[3].damage == 800:
        play sound1 "sound/explosion5.ogg"
        show pactmissilefrigate_rocketexplode:
            xpos 0.5 ypos 0.5 alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        
    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 1
            ease 0.05 alpha 1.0 zoom 1.0 
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show pactmissilefrigate_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_rockethitwipe

    show pactmissilefrigate_rockettrail:
        ease 1.0 alpha 0
    
    if sunrider.weapons[3].damage == 1200:
        pause 1.5
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 1.5
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbattleship_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbattleship_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return


label die_pactbattleship: ###################################PACT CRUISER DEATH

    $renpy.show_screen('show_background',_layer='master')

    show pactbattleship_side:
        xpos 0.5 ypos 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead1 zorder 1:
        alpha 0 zoom 1.2
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead2 zorder 1:
        alpha 0 zoom 1.2
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75
    show white:
        alpha 0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0

    play sound "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide pactbattleship_side
    show pactcruiser_dead3:
        alpha 0 zoom 1.5
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_pactbattleship:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show pactbattleship_side behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label atkanim_ryuviancruiser_kinetic: ################################# RYUVIAN CRUISER KINETIC

    $renpy.show_screen('show_background',_layer='master')

    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master at shake1
    show ryuviancruiser_kineticflash1:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show ryuviancruiser_kineticround1:
        xpos 580 ypos 354
        linear 0.15 xpos -400 ypos 350
    play sound1 'sound/explosion1.ogg'
    pause 0.05

    show layer master at shake1
    show ryuviancruiser_kineticflash_back1 behind ryuviancruiser_side:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show ryuviancruiser_kineticround2 behind ryuviancruiser_side:
        xpos 580 ypos 329
        linear 0.15 xpos -400 ypos 325
    play sound2 'sound/explosion1.ogg'
    pause 0.2

    show layer master at shake1
    show ryuviancruiser_kineticflash2:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show ryuviancruiser_kineticround3:
        xpos 580 ypos 354
        linear 0.15 xpos -400 ypos 350
    play sound1 'sound/explosion1.ogg'
    pause 0.05

    show layer master at shake1
    show ryuviancruiser_kineticflash_back2 behind ryuviancruiser_side:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show ryuviancruiser_kineticround4 behind ryuviancruiser_side:
        xpos 580 ypos 329
        linear 0.15 xpos -400 ypos 325
    play sound2 'sound/explosion1.ogg'

    pause 0.5
    return

label atkanim_ryuviancruiser_missile:

    $renpy.show_screen('show_background',_layer='master')
    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5
    pause 0.1
    play sound2 'sound/missile.ogg'

    show ryuviancruiser_missile1:
        xpos 846 ypos 445 alpha 0
        pause 0.45
        alpha 1
        linear 0.55 xpos -300 ypos 50

    show ryuviancruiser_missile2:
        xpos 1100 ypos 445 alpha 0
        pause 0.4
        alpha 1
        linear 0.55 xpos -300 ypos -20

    show ryuviancruiser_missile3:
        xpos 1200 ypos 445 alpha 0
        pause 0.4
        alpha 1
        linear 0.55 xpos -300 ypos -30

    pause 0.001

    show ryuviancruiser_missiletrail:
        xalign 0.5 yalign 0.5
    with pactmissilefrigate_missilewipe
    hide ryuviancruiser_missiletrail with dissolve

    return

label hitanim_ryuviancruiser_kinetic:   ##############PACT CRUISER HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_ryuviancruiser_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show pactmissilefrigate_hitmissileexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show pactmissilefrigate_hitmissileexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_ryuviancruiser_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show pactmissilefrigate_hitlaserexplode:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe
    hide pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_ryuviancruiser_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show sunrider_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_ryuviancruiser_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 0 ypos 570
        linear 1.1 xpos 1160 ypos 570
        alpha 0


    show layer master at shake2(pausetime=1,repeats=8)
    if sunrider.weapons[3].damage == 800:
        play sound1 "sound/explosion5.ogg"
        show pactmissilefrigate_rocketexplode:
            xpos 0.5 ypos 0.5 alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        
    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 1
            ease 0.05 alpha 1.0 zoom 1.0 
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show pactmissilefrigate_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_rockethitwipe

    show pactmissilefrigate_rockettrail:
        ease 1.0 alpha 0
    
    if sunrider.weapons[3].damage == 1200:
        pause 1.5
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_ryuviancruiser_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
    
    return

label hitanim_ryuviancruiser_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return


label die_ryuviancruiser:

    $renpy.show_screen('show_background',_layer='master')

    show ryuviancruiser_side:
        xpos 0.5 ypos 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide ryuviancruiser_side
    show pactcruiser_dead3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_ryuviancruiser:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show ryuviancruiser_side behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label atkanim_havoc_missile: ##########################HAVOC ATTACK ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')

    show havoc:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play cosvoice "sound/Voice/Cosette/Cosette Missiles Attack 1.ogg"
    if Random == 2:
        play cosvoice "sound/Voice/Cosette/Cosette Missiles Attack 2.ogg"
    if Random == 3:
        play cosvoice "sound/Voice/Cosette/Cosette Missiles Attack 3.ogg"

    show cosette plugsuit point evilsmile:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show cosette plugsuit point evilsmile:
        ease 1.5 alpha 0
    pause 0.8

    play sound1 "sound/MechHeavy.ogg"
    show havoc missile with dissolve

    pause 0.1

    play sound2 "sound/missile.ogg"

    show havoc_missile1:
        xpos 1025 ypos 225 alpha 0
        pause 0.3
        alpha 1
        linear 0.6 xpos -300 ypos -150

    show havoc_missile2:
        xpos 1052 ypos 223 alpha 0
        pause 0.3
        alpha 1
        linear 0.6 xpos -300 ypos -147

    show havoc_missile3:
        xpos 1280 ypos 243 alpha 0
        pause 0.2
        alpha 1
        linear 0.6 xpos 0 ypos -150

    show havoc_missile4:
        xpos 1290 ypos 230 alpha 0
        pause 0.2
        alpha 1
        linear 0.6 xpos 0 ypos -163

    show havoc_missile5:
        xpos 1025 ypos 608 alpha 0
        pause 0.35
        alpha 1
        linear 0.6 xpos -300 ypos 210

    show havoc_missile6:
        xpos 1233 ypos 715 alpha 0
        pause 0.35
        alpha 1
        linear 0.6 xpos -300 ypos 250

    show havoc_missiletrial with pactmissilefrigate_missilewipe
    hide havoc_missiletrial with dissolve

    pause 0.1

    return

label atkanim_havoc_rocket:

    $renpy.show_screen('show_background',_layer='master')

    show havoc:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play cosvoice "sound/Voice/Cosette/Cosette Missiles Attack 1.ogg"
    if Random == 2:
        play cosvoice "sound/Voice/Cosette/Cosette Missiles Attack 2.ogg"
    if Random == 3:
        play cosvoice "sound/Voice/Cosette/Cosette Missiles Attack 3.ogg"

    show cosette plugsuit point evilsmile:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show cosette plugsuit point evilsmile:
        ease 1.5 alpha 0
    pause 0.8

    play sound1 "sound/MechHeavy.ogg"

    show havoc rocket with dissolve

    pause 0.5

    play sound2 "sound/missilelaunch.ogg"

    show havoc norocket

    show havoc_rocket1:
        xpos 0.5 ypos 0.5
        linear 0.5 xpos -0.6 ypos 0.3

    pause 0.08

    show havoc_rocket2:
        xpos 0.5 ypos 0.5
        linear 0.5 xpos -0.6 ypos 0.3

    pause 0.08

    show havoc_rocket3:
        xpos 0.5 ypos 0.5
        linear 0.5 xpos -0.6 ypos 0.3

    pause 0.08

    show havoc_rocket4:
        xpos 0.5 ypos 0.5
        linear 0.5 xpos -0.6 ypos 0.3

    pause 1

    return

label atkanim_havoc_assault:

    $renpy.show_screen('show_background',_layer='master')

    show havoc:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play cosvoice "sound/Voice/Cosette/Cosette Kinetic Attack 1.ogg"
    if Random == 2:
        play cosvoice "sound/Voice/Cosette/Cosette Kinetic Attack 1.ogg"
    if Random == 3:
        play cosvoice "sound/Voice/Cosette/Cosette Kinetic Attack 3.ogg"
    if Random == 4:
        play cosvoice "sound/Voice/Cosette/Cosette Kinetic Attack 4.ogg"

    show cosette plugsuit point evilsmile:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show cosette plugsuit point evilsmile:
        ease 1.5 alpha 0
    pause 0.8

    play sound1 "sound/MechHeavy.ogg"

    show havoc assault with dissolve

    pause 0.3

    play sound2 "sound/machinegun.ogg"

    show havoc_assaultflash1:
        alpha 0
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.03
            ease 0.025 alpha 0
            pause 0.06
            repeat (15)

    pause 1.5

    return

label atkanim_havoc_melee:

    $renpy.show_screen('show_background',_layer='master')

    show havoc:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play cosvoice "sound/Voice/Cosette/Cosette Melee Attack 1.ogg"
    if Random == 2:
        play cosvoice "sound/Voice/Cosette/Cosette Melee Attack 1.ogg"
    if Random == 3:
        play cosvoice "sound/Voice/Cosette/Cosette Melee Attack 3.ogg"
    if Random == 4:
        play cosvoice "sound/Voice/Cosette/Cosette Melee Attack 4.ogg"

    show cosette plugsuit point evilsmile:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show cosette plugsuit point evilsmile:
        ease 1.5 alpha 0
    pause 0.8

    play sound1 "sound/chainsaw.ogg"

    show havoc melee with dissolve

    pause 0.5

    play sound2 "sound/boasters.ogg"

    show havoc melee:
        xpos 0.5 ypos 0.5
        ease 1.0 xpos -2.0 ypos -1.0

    pause 1.4

    return

label hitanim_havoc_kinetic: ##########################HAVOC HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show havoc:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25
    play sound2 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.6 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
    
    return

label hitanim_havoc_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show havoc:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0 zoom 1.2
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0 zoom 1.2
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0 zoom 1.2
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0 zoom 1.2
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_havoc_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show havoc:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhittrail behind piratebomber_laserhitexplode1 with pactmissilefrigate_laserhitwipe
    hide piratebomber_laserhittrail with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_havoc_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show havoc:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3


    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_havoc_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show havoc:
        xpos 0.5 ypos 0.5

    pause 0.1
    show piratebomber_hitrocket:
        xpos -200 ypos 440
        linear 0.4 xpos 1010 ypos 448
        alpha 0

    if sunrider.weapons[3].damage == 800:
        show layer master at shake2(pausetime=0.4,repeats=8)
        play sound "sound/explosion4.ogg"
        show pactmissilefrigate_die3:
            xpos 0.5 ypos 0.5 alpha 0
            pause 0.4
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0

    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 0.4
            ease 0.4 alpha 1.0 zoom 1.5
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show piratebomber_hitrockettrail behind piratebomber_hitrocket:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_laserhitwipe
    show piratebomber_hitrockettrail:
        ease 1.0 alpha 0

    if sunrider.weapons[3].damage == 1200:
        pause 3.0
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_havoc_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show havoc:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_havoc_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show havoc:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label hitanim_havoc_melee:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show havoc:
        xpos 0.5 ypos 0.5

    show blackjack melee:
        xpos -2.0 ypos 1.0
        ease 1.5 xpos 0.9 ypos 0.5

    pause 1.0

    play sound "sound/Sword Shing 2.ogg"

    show melee_overlay:
        xzoom -1
    with meleehitreverse

    pause 0.1

    hide melee_overlay with dissolvequick

    pause 0.2

    show blackjack melee:
        xpos 0.9 ypos 0.5
        ease 1.0 xpos 2.0 ypos -1.0

    pause 0.3

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.55 ypos 0.5 zoom 1.2
        ease 1.2 alpha 0

    pause 0.1

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.55 ypos 0.5 zoom 1.2
        ease 1.2 alpha 0

    pause 0.5

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label miss_havoc:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show havoc behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label die_havoc:

    $renpy.show_screen('show_background',_layer='master')

    if BM.mission > 5:
        $renpy.show_screen('show_background',_layer='master')

        show havoc:
            xpos 0.5 ypos 0.5 xzoom -1

        pause 0.8

        show havoc:
            ease 0.5 xpos -0.5 ypos -1.0

        pause 2

        return

    show havoc:
        xpos 0.5 ypos 0.5

    show cosette plugsuit armscrossed angry with dissolve:
        xpos 0.35

    cos "Tsch... These guys aren't worth it! Fall back!"

    show havoc:
        ease 0.5 xpos -0.5 ypos -1.0
    with dissolvequick

    hide cosette with dissolve
    show ava uniform fistup yes:
        xpos 0.35
    with dissolve

    ava "Enemy ships are bugging out.  We got them!"

    show asaga plugsuit neutralalt closedeyessmile:
        xpos 0.65
    with dissolve

    asa "Whoo! That sure was exciting!"
    kay "We'll open up our hangar bay. You have permission to dock, Black Jack."

    show ava uniform armscrossed frown:
        xpos 0.35
    with dissolve

    ava "And to explain yourself."

    show asaga plugsuit neutralalt smile:
        xpos 0.65
    with dissolve

    asa "Roger that! Coming aboard!"

    hide asaga
    hide ava

    return

label atkanim_piratedestroyer_kinetic: ################################# PIRATE DESTROYER KINETIC

    $renpy.show_screen('show_background',_layer='master')

    show piratedestroyer:

    pause 0.2

    show layer master at shake1
    show piratedestroyer_kineticflash:
        alpha 0
        ease 0.1 alpha 1
        ease 0.1 alpha 0
    show piratedestroyer_kineticround1:
        xpos 1052 ypos 335
        linear 0.15 xpos -400 ypos 100
    play sound1 'sound/explosion1.ogg'
    pause 0.06
    show piratedestroyer_kineticround2:
        xpos 1060 ypos 315
        linear 0.15 xpos -392 ypos 85
    pause 0.4

    show layer master at shake1
    show piratedestroyer_kineticflash:
        alpha 0
        ease 0.1 alpha 1
        ease 0.1 alpha 0
    show piratedestroyer_kineticround3:
        xpos 1052 ypos 335
        linear 0.15 xpos -400 ypos 100
    play sound2 'sound/explosion1.ogg'
    pause 0.06
    show piratedestroyer_kineticround4:
        xpos 1060 ypos 315
        linear 0.15 xpos -392 ypos 85

    pause 0.5
    return

label atkanim_piratedestroyer_laser:

    $renpy.show_screen('show_background',_layer='master')
    show piratedestroyer:
        xpos 0.5 ypos 0.5
    pause 0.001
    play sound2 'sound/laser2.ogg'

    show piratedestroyer_laserfront:
        xpos 0.5 ypos 0.5
    show piratedestroyer_laserback behind piratedestroyer:
        xpos 0.5 ypos 0.5
    with enemy_laserhitwipe

    hide piratedestroyer_laserfront
    hide piratedestroyer_laserback
    with enemy_laserhitwipe

    pause 0.2
    return

label hitanim_piratedestroyer_kinetic:   ##############PIRATE DESTROYER HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratedestroyer:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactmissilefrigate_kinetichit1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactmissilefrigate_kinetichit2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
    return

label hitanim_piratedestroyer_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratedestroyer:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show pactmissilefrigate_hitmissileexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show pactmissilefrigate_hitmissileexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratedestroyer_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show piratedestroyer:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show pactmissilefrigate_hitlaserexplode:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe
    hide pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratedestroyer_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show piratedestroyer:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show sunrider_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratedestroyer_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratedestroyer:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 0 ypos 570
        linear 1.1 xpos 1160 ypos 570
        alpha 0


    show layer master at shake2(pausetime=1,repeats=8)
    if sunrider.weapons[3].damage == 800:
        play sound1 "sound/explosion5.ogg"
        show pactmissilefrigate_rocketexplode:
            xpos 0.5 ypos 0.5 alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        
    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 1
            ease 0.05 alpha 1.0 zoom 1.0 
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show pactmissilefrigate_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_rockethitwipe

    show pactmissilefrigate_rockettrail:
        ease 1.0 alpha 0
    
    if sunrider.weapons[3].damage == 1200:
        pause 1.5
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 1.5
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
    
    return

label hitanim_piratedestroyer_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratedestroyer:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratedestroyer_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show piratedestroyer:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label die_piratedestroyer:

    $renpy.show_screen('show_background',_layer='master')

    show piratedestroyer:
        xpos 0.5 ypos 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactmissilefrigate_die1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactmissilefrigate_die2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide piratedestroyer
    show pactmissilefrigate_die3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_piratedestroyer:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show piratedestroyer behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label atkanim_pactstation_laser:  ###################################PACT STATION ATKANIM

    $renpy.show_screen('show_background',_layer='master')
    show pactstation:
        xpos 0.5 ypos 0.5
    pause 0.1
    play sound2 'sound/legion_laser.ogg'

    show pactstation_laserfront:
        xpos 0.5 ypos 0.5
    show pactstation_laserback behind pactcruiser_side:
        xpos 0.5 ypos 0.5
    with enemy_laserhitwipe

    hide pactstation_laserfront
    hide pactstation_laserback
    with enemy_laserhitwipe

    pause 0.5
    return

label atkanim_pactstation_kinetic:

    $renpy.show_screen('show_background',_layer='master')

    show pactstation:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound1 "sound/railgun.ogg"
    show layer master at shake1
    show pactstation_kineticflash 1:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show pactstation_kineticround1:
        xpos 740 ypos 660
        linear 0.15 xpos -400 ypos 600
    show pactstation_kineticround2:
        xpos 750 ypos 460
        linear 0.15 xpos -400 ypos 400

    pause 0.1

    play sound2 "sound/railgun.ogg"
    show layer master at shake1
    show pactstation_kineticflash 2:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show pactstation_kineticround3:
        xpos 830 ypos 710
        linear 0.15 xpos -400 ypos 650
    show pactstation_kineticround4:
        xpos 910 ypos 420
        linear 0.15 xpos -400 ypos 360
    pause 0.1

    play sound3 "sound/railgun.ogg"
    show layer master at shake1
    show pactstation_kineticflash 3:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show pactstation_kineticround5:
        xpos 1310 ypos 370
        linear 0.15 xpos -400 ypos 310
    show pactstation_kineticround6:
        xpos 1420 ypos 570
        linear 0.15 xpos -400 ypos 510
    pause 0.05

    pause 0.5
    return

label hitanim_pactstation_kinetic:   ##############PACT STATION HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactstation:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactstation_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactstation:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show pactmissilefrigate_hitmissileexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show pactmissilefrigate_hitmissileexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactstation_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactstation:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"
    show layer master at shake2(pausetime=0.2,repeats=6)
    show pactmissilefrigate_hitlaserexplode:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe
    hide pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactstation_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactstation:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show sunrider_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactstation_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactstation:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 0 ypos 570
        linear 1.1 xpos 1160 ypos 570
        alpha 0


    show layer master at shake2(pausetime=1,repeats=8)
    if sunrider.weapons[3].damage == 800:
        play sound1 "sound/explosion5.ogg"
        show pactmissilefrigate_rocketexplode:
            xpos 0.5 ypos 0.5 alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        
    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 1
            ease 0.05 alpha 1.0 zoom 1.0 
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show pactmissilefrigate_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_rockethitwipe

    show pactmissilefrigate_rockettrail:
        ease 1.0 alpha 0
    
    if sunrider.weapons[3].damage == 1200:
        pause 1.5
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 1.5
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactstation_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactstation:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label die_pactstation: ###################################PACT CRUISER DEATH

    $renpy.show_screen('show_background',_layer='master')

    show pactstation:
        xpos 0.5 ypos 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound2 "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide pactstation
    show pactcruiser_dead3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_pactstation: #############################PACT MISSILE FRIGATE MISS

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show pactstation behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactstation_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactstation:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label atkanim_pactmook_missile: ##############################PACT MOOK ASSAULT

    $renpy.show_screen('show_background',_layer='master')

    show pactmook:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    pause 0.2

    show pactmook missile with dissolve

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmook_missileround1:
        xpos 1040 ypos 250 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos 170 ypos -100

    show pactmook_missileround2:
        xpos 1250 ypos 245 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos 420 ypos -100

    show pactmook_missileround3:
        xpos 1090 ypos 660 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos 140

    show pactmook_missileround4:
        xpos 1090 ypos 615 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos 70

    show pactmook_missileround5:
        xpos 1240 ypos 630 alpha 0
        pause 0.55
        alpha 1
        linear 0.6 xpos -300 ypos 30

    show pactmook_missiletrail with pactmissilefrigate_missilewipe
    hide pactmook_missiletrail with dissolve

    pause 0.1

    return

label atkanim_pactmook_assault:

    $renpy.show_screen('show_background',_layer='master')

    show pactmook:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    pause 0.5

    show pactmook assault with dissolve

    pause 0.3

    play sound "sound/machinegun.ogg"

    show pactmook_muzzleflash1:
        alpha 0
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    show pactmook_muzzleflash2:
        alpha 0
        pause 0.30
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    pause 1.5

    return

label atkanim_pactmook_laser:

    $renpy.show_screen('show_background',_layer='master')

    show pactmook:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    pause 0.5

    show pactmook laser with dissolve
    show pactmook_laserbeam1:
        alpha 0
        ease 0.3 alpha 1
        ease 0.7 alpha 0

    play sound "sound/Laser 1.ogg"

    show pactmook_laserbeam2 behind pactmook_laserbeam1 with enemy_laserhitwipequick
    hide pactmook_laserbeam2 behind pactmook_laserbeam1 with enemy_laserhitwipequick

    pause 0.1

    return

label hitanim_pactmook_kinetic: ##########################PACT MOOK HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactmook:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.6 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmook_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactmook:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0 zoom 1.2
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0 zoom 1.2
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0 zoom 1.2
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0 zoom 1.2
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmook_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactmook:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound1 "sound/Laser 1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhittrail behind piratebomber_laserhitexplode1 with pactmissilefrigate_laserhitwipe
    hide piratebomber_laserhittrail with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmook_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactmook:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmook_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactmook:
        xpos 0.5 ypos 0.5

    pause 0.1
    show piratebomber_hitrocket:
        xpos -200 ypos 440
        linear 0.4 xpos 1010 ypos 448
        alpha 0

    if sunrider.weapons[3].damage == 800:
        show layer master at shake2(pausetime=0.4,repeats=8)
        play sound "sound/explosion4.ogg"
        show pactmissilefrigate_die3:
            xpos 0.5 ypos 0.5 alpha 0
            pause 0.4
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0

    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 0.4
            ease 0.4 alpha 1.0 zoom 1.5
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show piratebomber_hitrockettrail behind piratebomber_hitrocket:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_laserhitwipe
    show piratebomber_hitrockettrail:
        ease 1.0 alpha 0

    if sunrider.weapons[3].damage == 1200:
        pause 3.0
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
    
    return

label hitanim_pactmook_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactmook:
        xpos 0.5 ypos 0.5


    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactmook_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactmook:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label miss_pactmook:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show pactmook behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))


    return

label die_pactmook:

    $renpy.show_screen('show_background',_layer='master')

    show pactmook:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1
    show piratebomber_die1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound2 "sound/explosion1.ogg"

    show layer master at shake1
    show piratebomber_die2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound3 "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide pactmook
    show piratebomber_die3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label atkanim_seraphimenemy_kinetic: ##############################PACT MOOK ASSAULT

    $renpy.show_screen('show_background',_layer='master')

    show seraphimenemy:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    pause 0.2

    play sound "sound/mech1.ogg"
    show seraphimenemy kinetic with dissolve

    pause 0.1

    play sound1 "sound/Sola Sniper.ogg"
    pause 0.6
    show seraphimenemy_charge1 with dissolve
    pause 0.6

    show layer master at shake1(pausetime=0.1)

    show seraphimenemy_charge2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.1 alpha 1
        pause 0.1
        ease 0.1 alpha 0 zoom 1.5
    show seraphimenemy_bullet:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.1
        alpha 1.0
        ease 0.2 xpos -2.0 ypos 4.0

    pause 0.8

    return

label hitanim_seraphimenemy_kinetic: ##########################PACT MOOK HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show seraphimenemy:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.6 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_seraphimenemy_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show seraphimenemy:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0 zoom 1.2
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0 zoom 1.2
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0 zoom 1.2
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0 zoom 1.2
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_seraphimenemy_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show seraphimenemy:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound1 "sound/Laser 1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhittrail behind piratebomber_laserhitexplode1 with pactmissilefrigate_laserhitwipe
    hide piratebomber_laserhittrail with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_seraphimenemy_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show seraphimenemy:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_seraphimenemy_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show seraphimenemy:
        xpos 0.5 ypos 0.5

    pause 0.1
    show piratebomber_hitrocket:
        xpos -200 ypos 440
        linear 0.4 xpos 1010 ypos 448
        alpha 0

    if sunrider.weapons[3].damage == 800:
        show layer master at shake2(pausetime=0.4,repeats=8)
        play sound "sound/explosion4.ogg"
        show pactmissilefrigate_die3:
            xpos 0.5 ypos 0.5 alpha 0
            pause 0.4
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0

    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 0.4
            ease 0.4 alpha 1.0 zoom 1.5
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show piratebomber_hitrockettrail behind piratebomber_hitrocket:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_laserhitwipe
    show piratebomber_hitrockettrail:
        ease 1.0 alpha 0

    if sunrider.weapons[3].damage == 1200:
        pause 3.0
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_seraphimenemy_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show seraphimenemy:
        xpos 0.5 ypos 0.5


    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_seraphimenemy_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show seraphimenemy:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label miss_seraphimenemy:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show seraphimenemy behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))


    return

label die_seraphimenemy:

    $renpy.show_screen('show_background',_layer='master')

    show seraphimenemy:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1
    show piratebomber_die1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound2 "sound/explosion1.ogg"

    show layer master at shake1
    show piratebomber_die2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound3 "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide seraphimenemy
    show piratebomber_die3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label atkanim_pirategrunt_missile: ##############################PIRATE GRUNT ASSAULT

    $renpy.show_screen('show_background',_layer='master')

    show pirategrunt:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    pause 0.2

    play sound "sound/missilefly.ogg"

    show pirategrunt missile with dissolve

    pause 0.1

    show pirategrunt_missileround1:
        xpos 1040 ypos 250 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos 170 ypos -100

    show pirategrunt_missileround2:
        xpos 1250 ypos 245 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos 420 ypos -100

    show pirategrunt_missileround3:
        xpos 1090 ypos 660 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos 140

    show pirategrunt_missileround4:
        xpos 1090 ypos 615 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos 70

    show pirategrunt_missileround5:
        xpos 1240 ypos 630 alpha 0
        pause 0.55
        alpha 1
        linear 0.6 xpos -300 ypos 30

    show pirategrunt_missiletrail with pactmissilefrigate_missilewipe
    hide pirategrunt_missiletrail with dissolve

    pause 0.1

    return

label atkanim_pirategrunt_assault:

    $renpy.show_screen('show_background',_layer='master')

    show pirategrunt:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    pause 0.5

    show pirategrunt assault with dissolve

    pause 0.3

    play sound "sound/machinegun.ogg"

    show pirategrunt_muzzleflash1:
        alpha 0
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    show pirategrunt_muzzleflash2:
        alpha 0
        pause 0.30
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    pause 1.5

    return

label atkanim_pirategrunt_laser:

    $renpy.show_screen('show_background',_layer='master')

    show pirategrunt:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    pause 0.5

    show pirategrunt laser with dissolve
    show pirategrunt_laserbeam1:
        alpha 0
        ease 0.3 alpha 1
        ease 0.7 alpha 0

    play sound1 'sound/Laser 1.ogg'

    show pirategrunt_laserbeam2 behind pirategrunt_laserbeam1 with enemy_laserhitwipequick
    hide pirategrunt_laserbeam2 behind pirategrunt_laserbeam1 with enemy_laserhitwipequick

    pause 0.5

    return

label hitanim_pirategrunt_kinetic: ##########################PIRATE GRUNT HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pirategrunt:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.6 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pirategrunt_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pirategrunt:
        xpos 0.5 ypos 0.5

    play sound "sound/missilefly.ogg"

    pause 0.1

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0 zoom 1.2
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0 zoom 1.2
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0 zoom 1.2
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0 zoom 1.2
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pirategrunt_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pirategrunt:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhittrail behind pirategrunt_laserhitexplode1 with pactmissilefrigate_laserhitwipe
    hide piratebomber_laserhittrail with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pirategrunt_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pirategrunt:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"
    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pirategrunt_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pirategrunt:
        xpos 0.5 ypos 0.5

    pause 0.1
    show piratebomber_hitrocket:
        xpos -200 ypos 440
        linear 0.4 xpos 1010 ypos 448
        alpha 0

    if sunrider.weapons[3].damage == 800:
        show layer master at shake2(pausetime=0.4,repeats=8)
        play sound "sound/explosion4.ogg"
        show pactmissilefrigate_die3:
            xpos 0.5 ypos 0.5 alpha 0
            pause 0.4
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0

    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 0.4
            ease 0.4 alpha 1.0 zoom 1.5
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show piratebomber_hitrockettrail behind piratebomber_hitrocket:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_laserhitwipe
    show piratebomber_hitrockettrail:
        ease 1.0 alpha 0

    if sunrider.weapons[3].damage == 1200:
        pause 3.0
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
    
    return

label hitanim_pirategrunt_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pirategrunt:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pirategrunt_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pirategrunt:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label miss_pirategrunt:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show pirategrunt behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))


    return

label die_pirategrunt:

    $renpy.show_screen('show_background',_layer='master')

    show pirategrunt:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1
    show piratebomber_die1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1
    show piratebomber_die2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound1 "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide pirategrunt
    show piratebomber_die3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label atkanim_piratebase_missile:  ###################################PIRATE BASE ATKANIM

    $renpy.show_screen('show_background',_layer='master')
    show piratebase:
        xpos 0.5 ypos 0.5
    pause 0.1

    show piratebase missile with dissolve

    pause 0.25
    play sound2 'sound/missilelaunch.ogg'
    show piratebase_missileround1:
        xpos 830 ypos 470 alpha 0
        pause 0.65
        alpha 1
        linear 0.65 xpos -200 ypos -120
    show piratebase_missileround2:
        xpos 815 ypos 490 alpha 0
        pause 0.65
        alpha 1
        linear 0.65 xpos -200 ypos -20
    show piratebase_missileround3:
        xpos 865 ypos 530 alpha 0
        pause 0.65
        alpha 1
        linear 0.65 xpos -200 ypos -60
    show piratebase_missileround4:
        xpos 880 ypos 500 alpha 0
        pause 0.65
        alpha 1
        linear 0.65 xpos -200 ypos 50

    show piratebase_missiletrail with piratestation_missilewipe
    hide piratebase_missiletrail with dissolve
    pause 0.5

    return

label atkanim_piratebase_kinetic:

    $renpy.show_screen('show_background',_layer='master')

    show piratebase:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound1 "sound/railgun.ogg"
    show layer master at shake1
    show piratebase_kineticflash1:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show piratebase_kineticround1:
        xpos 1020 ypos 334
        linear 0.15 xpos -200 ypos 25

    pause 0.1

    play sound2 "sound/railgun.ogg"
    show layer master at shake1
    show piratebase_kineticflash2:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show piratebase_kineticround2:
        xpos 1190 ypos 370
        linear 0.15 xpos -200 ypos 20

    pause 0.1

    play sound3 "sound/railgun.ogg"
    show layer master at shake1
    show piratebase_kineticflash3:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show piratebase_kineticround3:
        xpos 1100 ypos 530
        linear 0.15 xpos -200 ypos 200

    pause 0.1

    play sound4 "sound/railgun.ogg"
    show layer master at shake1
    show piratebase_kineticflash4:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show piratebase_kineticround4:
        xpos 1280 ypos 510
        linear 0.15 xpos -200 ypos 130

    pause 0.1

    play sound5 "sound/railgun.ogg"
    show layer master at shake1
    show piratebase_kineticflash5:
        alpha 0
        ease 0.05 alpha 1
        ease 0.05 alpha 0
    show piratebase_kineticround5:
        xpos 1400 ypos 370
        linear 0.15 xpos -200 ypos -40

    pause 0.5

    return

label atkanim_piratebase_assault:

    $renpy.show_screen('show_background',_layer='master')
    show piratebase:
        xpos 0.5 ypos 0.5
    pause 0.5

    python:
        flak_positions1 = [
            (760,702),
            (765,776),
            (768,848)
            ]
        Flak1 = FlakShield("gameplay/Animations/PACTCruiser/flakbullet.png",flak_positions1,7000,dispersion=2, angle=290, interval=0.15)

        flak_positions2 = [
            (763,733),
            (767,809),
            (761,879)
            ]
        Flak2 = FlakShield("gameplay/Animations/PACTCruiser/flakbullet.png",flak_positions2,7000,dispersion=2, angle=290, interval=0.15)

    play sound "sound/Flak.ogg"

    $ Flak1.show()
    show piratebase_assaultflash1
    pause 0.01
    hide piratebase_assaultflash1
    pause 0.01
    show piratebase_assaultflash1
    pause 0.01
    hide piratebase_assaultflash1
    pause 0.01
    show piratebase_assaultflash1
    pause 0.01
    hide piratebase_assaultflash1
    pause 0.01
    show piratebase_assaultflash1
    pause 0.01
    hide piratebase_assaultflash1
    pause 0.01
    $ Flak1.stop()
    $ Flak2.show()
    show piratebase_assaultflash2
    pause 0.01
    hide piratebase_assaultflash2
    pause 0.01
    show piratebase_assaultflash2
    pause 0.01
    hide piratebase_assaultflash2
    pause 0.01
    show piratebase_assaultflash2
    pause 0.01
    hide piratebase_assaultflash2
    pause 0.01
    show piratebase_assaultflash2
    pause 0.01
    hide piratebase_assaultflash2
    pause 0.01
    $ Flak2.stop()
    $ Flak1.start()
    show piratebase_assaultflash1
    pause 0.01
    hide piratebase_assaultflash1
    pause 0.01
    show piratebase_assaultflash1
    pause 0.01
    hide piratebase_assaultflash1
    pause 0.01
    show piratebase_assaultflash1
    pause 0.01
    hide piratebase_assaultflash1
    pause 0.01
    show piratebase_assaultflash1
    pause 0.01
    hide piratebase_assaultflash1
    pause 0.01
    $ Flak1.stop()
    $ Flak2.start()
    show piratebase_assaultflash2
    pause 0.01
    hide piratebase_assaultflash2
    pause 0.01
    show piratebase_assaultflash2
    pause 0.01
    hide piratebase_assaultflash2
    pause 0.01
    show piratebase_assaultflash2
    pause 0.01
    hide piratebase_assaultflash2
    pause 0.01
    show piratebase_assaultflash2
    pause 0.01
    hide piratebase_assaultflash2
    pause 0.01
    $ Flak2.stop()

    pause 0.5

    return

label hitanim_piratebase_kinetic:   ##############PACT STATION HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratebase:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebase_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratebase:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show pactmissilefrigate_hitmissileexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show pactmissilefrigate_hitmissileexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebase_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show piratebase:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"
    show layer master at shake2(pausetime=0.2,repeats=6)
    show pactmissilefrigate_hitlaserexplode:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe
    hide pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebase_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show piratebase:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show sunrider_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebase_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratebase:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 0 ypos 570
        linear 1.1 xpos 1160 ypos 570
        alpha 0


    show layer master at shake2(pausetime=1,repeats=8)
    if sunrider.weapons[3].damage == 800:
        play sound1 "sound/explosion5.ogg"
        show pactmissilefrigate_rocketexplode:
            xpos 0.5 ypos 0.5 alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        
    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 1
            ease 0.05 alpha 1.0 zoom 1.0 
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show pactmissilefrigate_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_rockethitwipe

    show pactmissilefrigate_rockettrail:
        ease 1.0 alpha 0
    
    if sunrider.weapons[3].damage == 1200:
        pause 1.5
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 1.5
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebase_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show piratebase:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label die_piratebase: ###################################PACT CRUISER DEATH

    $renpy.show_screen('show_background',_layer='master')

    show piratebase:
        xpos 0.5 ypos 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound2 "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide piratebase
    show pactcruiser_dead3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_piratebase: #############################PACT MISSILE FRIGATE MISS

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show piratebase behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label hitanim_piratebase_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show piratebase:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label atkanim_phoenixboaster_assault: ##########################################PHOENIX BOASTER

    $renpy.show_screen('show_background',_layer='master')

    show phoenixboaster:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    pause 0.5

    show phoenixboaster assault with dissolve

    pause 0.3

    play sound "sound/machinegun.ogg"

    show phoenixboaster_assaultflash1:
        alpha 0
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    show phoenixboaster_assaultflash2:
        alpha 0
        pause 0.25
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    show phoenixboaster_assaultflash3:
        alpha 0
        pause 0.35
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    show phoenixboaster_assaultflash4:
        alpha 0
        pause 0.45
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)
    pause 1.5

    return

label atkanim_phoenixboaster_laser:

    $renpy.show_screen('show_background',_layer='master')

    show phoenixboaster:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    pause 0.3

    play sound "sound/Laser 1.ogg"

    show phoenixboaster_laser1:
        alpha 0
        ease 0.75 alpha 1
        ease 0.75 alpha 0

    show phoenixboaster_laser2:
        alpha 0
        pause 0.2
        ease 0.75 alpha 1
        ease 0.75 alpha 0

    show phoenixboaster_laser3:
        alpha 0
        pause 0.4
        ease 0.75 alpha 1
        ease 0.75 alpha 0

    show phoenixboaster_laser4:
        alpha 0
        pause 0.6
        ease 0.75 alpha 1
        ease 0.75 alpha 0

    pause 2.0

    return

label hitanim_phoenixboaster_kinetic: ##########################PHOENIX BOOSTER HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenixboaster:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.6 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixboaster_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenixboaster:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0 zoom 1.2
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0 zoom 1.2
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0 zoom 1.2
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0 zoom 1.2
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixboaster_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show phoenixboaster:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhittrail behind piratebomber_laserhitexplode1 with pactmissilefrigate_laserhitwipe
    hide piratebomber_laserhittrail with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixboaster_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show phoenixboaster:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixboaster_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenixboaster:
        xpos 0.5 ypos 0.5

    pause 0.1
    show piratebomber_hitrocket:
        xpos -200 ypos 440
        linear 0.4 xpos 1010 ypos 448
        alpha 0

    if sunrider.weapons[3].damage == 800:
        show layer master at shake2(pausetime=0.4,repeats=8)
        play sound "sound/explosion4.ogg"
        show pactmissilefrigate_die3:
            xpos 0.5 ypos 0.5 alpha 0
            pause 0.4
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0

    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 0.4
            ease 0.4 alpha 1.0 zoom 1.5
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show piratebomber_hitrockettrail behind piratebomber_hitrocket:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_laserhitwipe
    show piratebomber_hitrockettrail:
        ease 1.0 alpha 0

    if sunrider.weapons[3].damage == 1200:
        pause 3.0
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixboaster_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenixboaster:
        xpos 0.5 ypos 0.5


    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixboaster_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show phoenixboaster:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label miss_phoenixboaster:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show phoenixboaster behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))


    return

label die_phoenixboaster:

    $renpy.show_screen('show_background',_layer='master')

    show phoenixboaster:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1
    show piratebomber_die1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound2 "sound/explosion1.ogg"

    show layer master at shake1
    show piratebomber_die2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound3 "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide phoenixboaster
    show piratebomber_die3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    show phoenixnoboaster:
        xpos 0.5 ypos 0.5
        ease 1.0 xpos -2.0 ypos -2.0

    pause 2

    show asaga plugsuit excited happy:
        xzoom -1 xpos 0.2
    with dissolve

    asa "I think we got the special unit!"

    hide asaga
    show chigara plugsuit neutral frown:
        xzoom -1 xpos 0.2
    with dissolve

    chi "No... Only its warp booster has been destroyed."

    hide chigara

    if len(store.enemy_ships) > 1:
        show ava uniform alt order angry:
            xzoom -1 xpos 0.2
        with dissolve
        ava "There's still the rest of the fleet to worry about. Take out their capital ships!"
    #else:
    #if you want her to say something else instead of nothing this would be the place to put it.

    hide ava

    return

label atkanim_pactbomber_missile: ##########################PACT BOMBER ATTACK ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')

    show pactbomber:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    pause 0.2

    play sound1 "sound/MechHeavy.ogg"

    show pactbomber missile with dissolve

    pause 0.1

    play sound "sound/missile.ogg"

    show piratebomber_missile1:
        xpos 950 ypos 251 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos -105

    show  piratebomber_missile2:
        xpos 920 ypos 260 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos -125

    show  piratebomber_missile3:
        xpos 1187 ypos 254 alpha 0
        pause 0.35
        alpha 1
        linear 0.6 xpos -300 ypos -160

    show  piratebomber_missile4:
        xpos 1172 ypos 271 alpha 0
        pause 0.35
        alpha 1
        linear 0.6 xpos -300 ypos -180

    show  piratebomber_missile5:
        xpos 948 ypos 608 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos 250

    show  piratebomber_missile6:
        xpos 1128 ypos 698 alpha 0
        pause 0.4
        alpha 1
        linear 0.6 xpos -300 ypos 300

    show pactbomber_missiletrail with piratebomber_missilewipe
    hide pactbomber_missiletrail with dissolve

    pause 0.1

    return

label atkanim_pactbomber_rocket:

    $renpy.show_screen('show_background',_layer='master')

    show pactbomber:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5 ypos 0.5

    pause 0.5

    play sound1 "sound/MechHeavy.ogg"
    show pactbomber rocket with dissolve

    pause 0.5

    show pactbomber norocket

    play sound "sound/missilelaunch.ogg"
    show pactbomber_rocketfly1:
        xpos 0.5 ypos 0.5
        linear 0.5 xpos -0.4 ypos 0.22

    show pactbomber_rocketfly2:
        xpos 0.5 ypos 0.5
        linear 0.5 xpos -0.4 ypos 0.22

    pause 1

    return

label atkanim_pactbomber_laser:

    $renpy.show_screen('show_background',_layer='master')

    show pactbomber:
        zoom 2 xpos 0.8 ypos 0.5
        ease 0.5 zoom 1 xpos 0.5

    pause 0.5

    show pactbomber laser with dissolve
    show pactbomber_laserflash:
        alpha 0
        ease 0.3 alpha 1
        ease 0.7 alpha 0

    play sound "sound/Laser 1.ogg"

    show pactbomber_laserbeam behind pactbomber_laserflash with enemy_laserhitwipequick
    hide pactbomber_laserbeam behind pactbomber_laserflash with enemy_laserhitwipequick

    pause 0.5

    return


label hitanim_pactbomber_kinetic: ##########################PIRATE BOMBER HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp


    show pactbomber:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.6 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbomber_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactbomber:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0 zoom 1.2
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0 zoom 1.2
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0 zoom 1.2
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0 zoom 1.2
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbomber_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactbomber:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"
    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhittrail behind piratebomber_laserhitexplode with pactmissilefrigate_laserhitwipe
    hide piratebomber_laserhittrail with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbomber_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactbomber:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbomber_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactbomber:
        xpos 0.5 ypos 0.5

    pause 0.1
    show piratebomber_hitrocket:
        xpos -200 ypos 440
        linear 0.4 xpos 1010 ypos 448
        alpha 0

    if sunrider.weapons[3].damage == 800:
        show layer master at shake2(pausetime=0.4,repeats=8)
        play sound "sound/explosion4.ogg"
        show pactmissilefrigate_die3:
            xpos 0.5 ypos 0.5 alpha 0
            pause 0.4
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0

    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 0.4
            ease 0.4 alpha 1.0 zoom 1.5
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show piratebomber_hitrockettrail behind piratebomber_hitrocket:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_laserhitwipe
    show piratebomber_hitrockettrail:
        ease 1.0 alpha 0

    if sunrider.weapons[3].damage == 1200:
        pause 3.0
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
    
    return

label hitanim_pactbomber_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactbomber:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactbomber_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactbomber:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label die_pactbomber:

    $renpy.show_screen('show_background',_layer='master')

    show pactbomber:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion1.ogg"
    show layer master at shake1
    show piratebomber_die1 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound2 "sound/explosion1.ogg"
    show layer master at shake1
    show piratebomber_die2 zorder 1:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75

    play sound3 "sound/explosion4.ogg"
    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide pactbomber
    show piratebomber_die3:
        alpha 0
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_pactbomber:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show pactbomber behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label hitanim_agamemnon_missile:      ######################################AGAMEMNON

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show agamemnon_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound1 "sound/missilefly.ogg"

    show sunrider_missilehit1:
        xpos 1440 ypos 0 alpha 0
        pause 0.4
        alpha 1
        linear 0.7 xpos 620 ypos 480
        alpha 0

    show sunrider_missilehit2:
        alpha 0 xpos 1640 ypos 0
        pause 0.3
        alpha 1
        linear 0.7 xpos 740 ypos 560
        alpha 0

    show sunrider_missilehit3:
        xpos 1750 ypos 0 alpha 0
        pause 0.2
        alpha 1
        linear 0.7 xpos 920 ypos 500
        alpha 0

    show sunrider_missilehit4:
        xpos 1930 ypos 0 alpha 0
        pause 0.1
        alpha 1
        linear 0.7 xpos 1010 ypos 540
        alpha 0

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1(pausetime=0.9,repeats=12)
    show sunrider_missileexplode1:
        alpha 0
        pause 0.9
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    show sunrider_missileexplode2:
        alpha 0
        pause 1
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    show sunrider_missileexplode3:
        alpha 0
        pause 1.1
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    pause 0.15

    show sunrider_missiletrail_hit with sunridermissilehitwipe
    hide sunrider_missiletrail_hit with dissolve

    call hit_agamemnon

    pause 0.3

    return

label hitanim_agamemnon_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show agamemnon_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 540
        linear 0.25 xpos 590 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show sunrider_kinetichit1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 540
        linear 0.25 xpos 910 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show sunrider_kinetichit2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    call hit_agamemnon

    pause 0.5

    return

label hitanim_agamemnon_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show agamemnon_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show sunrider_laserhitexplode:
        alpha 0
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show sunrider_laserhit behind sunrider_laserhitexplode with enemy_laserhitwipe
    hide sunrider_laserhit behind sunrider_laserhitexplode with enemy_laserhitwipe

    call hit_agamemnon

    pause 0.5

    return

label hitanim_agamemnon_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show agamemnon_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master
    show sunrider_pulse1:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    call hit_agamemnon

    pause 1

    return

label hitanim_agamemnon_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show agamemnon_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rockethit:
        alpha 0
        pause 0.1
        alpha 1
        xpos 1940 ypos 620
        linear 0.7 xpos 560 ypos 620
        alpha 0

    play sound "sound/explosion4.ogg"

    show layer master at shake2(pausetime=1,repeats=8)
    show sunrider_rockethitexplode:
        alpha 0
        pause 1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0

    pause 0.1

    show sunrider_rockethittrail with sunriderhitrocketwipe
    hide sunrider_rockethittrail with dissolve

    call hit_agamemnon

    pause 0.5

    return

label hitanim_agamemnon_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show agamemnon_side:
        xpos 0.5 ypos 0.5

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode12:
        xpos 0.41 ypos 0.52 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode13:
        xpos 0.81 ypos 0.17 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode14:
        xpos 0.37 ypos 0.63 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0

    call hit_agamemnon

    pause 0.2

    return

label miss_agamemnon:

    show layer master

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show agamemnon_side behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    return

label hit_agamemnon:

    show layer master

    $ Random = renpy.random.randint(1,2)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Others 7.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Others 8.ogg"

    show ava uniform alt neutral angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform alt neutral angry:
        ease 1.5 alpha 0

    pause

    return

label die_agamemnon:

    $renpy.show_screen('show_background',_layer='master')

    show agamemnon_side:
        xpos 0.5 ypos 0.5

    play sound2 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode2:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound3 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode3:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound4 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode4:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound5 "sound/explosion2.ogg"
    show layer master at shake1
    show sunrider_explode5:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound5 "sound/explosion2.ogg"
    show layer master at shake1
    show sunrider_explode6:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.8

    play sound6 "sound/explosion4.ogg"
    show layer master
    scene white with dissolve
    stop music fadeout 1.5

    pause 1.0

    scene badend

    return

label hitanim_mochi_missile:      ######################################MOCHI

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show mochi_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound1 "sound/missilefly.ogg"

    show sunrider_missilehit1:
        xpos 1440 ypos 0 alpha 0
        pause 0.4
        alpha 1
        linear 0.7 xpos 620 ypos 480
        alpha 0

    show sunrider_missilehit2:
        alpha 0 xpos 1640 ypos 0
        pause 0.3
        alpha 1
        linear 0.7 xpos 740 ypos 560
        alpha 0

    show sunrider_missilehit3:
        xpos 1750 ypos 0 alpha 0
        pause 0.2
        alpha 1
        linear 0.7 xpos 920 ypos 500
        alpha 0

    show sunrider_missilehit4:
        xpos 1930 ypos 0 alpha 0
        pause 0.1
        alpha 1
        linear 0.7 xpos 1010 ypos 540
        alpha 0

    play sound1 "sound/explosion1.ogg"

    show layer master at shake1(pausetime=0.9,repeats=12)
    show sunrider_missileexplode1:
        alpha 0
        pause 0.9
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    show sunrider_missileexplode2:
        alpha 0
        pause 1
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    show sunrider_missileexplode3:
        alpha 0
        pause 1.1
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    pause 0.15

    show sunrider_missiletrail_hit with sunridermissilehitwipe
    hide sunrider_missiletrail_hit with dissolve

    call hit_mochi

    pause 0.3

    return

label hitanim_mochi_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show mochi_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 540
        linear 0.25 xpos 590 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show sunrider_kinetichit1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 540
        linear 0.25 xpos 910 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show sunrider_kinetichit2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    call hit_mochi

    pause 0.5

    return

label hitanim_mochi_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show mochi_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show sunrider_laserhitexplode:
        alpha 0
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show sunrider_laserhit behind sunrider_laserhitexplode with enemy_laserhitwipe
    hide sunrider_laserhit behind sunrider_laserhitexplode with enemy_laserhitwipe

    call hit_mochi

    pause 0.5

    return

label hitanim_mochi_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show mochi_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master
    show sunrider_pulse1:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    call hit_mochi

    pause 1

    return

label hitanim_mochi_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show mochi_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rockethit:
        alpha 0
        pause 0.1
        alpha 1
        xpos 1940 ypos 620
        linear 0.7 xpos 560 ypos 620
        alpha 0

    play sound "sound/explosion4.ogg"

    show layer master at shake2(pausetime=1,repeats=8)
    show sunrider_rockethitexplode:
        alpha 0
        pause 1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0

    pause 0.1

    show sunrider_rockethittrail with sunriderhitrocketwipe
    hide sunrider_rockethittrail with dissolve

    call hit_mochi

    pause 0.5

    return

label hitanim_mochi_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show mochi_side:
        xpos 0.5 ypos 0.5

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode12:
        xpos 0.41 ypos 0.52 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode13:
        xpos 0.81 ypos 0.17 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode14:
        xpos 0.37 ypos 0.63 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0

    call hit_mochi

    pause 0.2

    return

label miss_mochi:

    show layer master

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show mochi_side behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    return

label hit_mochi:

    show layer master

    $ Random = renpy.random.randint(1,2)

    if Random == 1:
        play avavoice "sound/Voice/Ava/Ava Others 7.ogg"
    if Random == 2:
        play avavoice "sound/Voice/Ava/Ava Others 8.ogg"

    show ava uniform alt neutral angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show ava uniform alt neutral angry:
        ease 1.5 alpha 0

    pause

    return

label die_mochi:

    $renpy.show_screen('show_background',_layer='master')

    play sound2 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode2:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound3 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode3:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound4 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode4:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound5 "sound/explosion2.ogg"
    show layer master at shake1
    show sunrider_explode5:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound5 "sound/explosion2.ogg"
    show layer master at shake1
    show sunrider_explode6:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.8

    play sound6 "sound/explosion4.ogg"
    show layer master
    scene white with dissolve
    stop music fadeout 1.5

    pause 1.0

    scene badend

    return

label atkanim_phoenix_assault: ########################PHOENIX ATTACK ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play icavoice "sound/Voice/Icari/Icari Attacking Kinetic 1.ogg"
    if Random == 2:
        play icavoice "sound/Voice/Icari/Icari Attacking Kinetic 2.ogg"
    if Random == 3:
        play icavoice "sound/Voice/Icari/Icari Attacking Kinetic 3.ogg"
    if Random == 4:
        play icavoice "sound/Voice/Icari/Icari Attacking Kinetic 4.ogg"

    show phoenix:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show icari plugsuit point angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show icari plugsuit point angry:
        ease 1.5 alpha 0

    play sound "sound/mech1.ogg"
    show phoenix assault with dissolve

    pause 0.3

    play sound1 "sound/machinegun.ogg"

    show phoenix_assaultflash1:
        alpha 0
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.1
            ease 0.025 alpha 0
            pause 0.15
            repeat (4)

    show phoenix_assaultflash2:
        alpha 0
        pause 0.30
        block:
            ease 0.025 alpha 1
            pause 0.1
            ease 0.025 alpha 0
            pause 0.15
            repeat (4)

    pause 1.5

    return

label atkanim_phoenix_melee:

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play icavoice "sound/Voice/Icari/Icari Attacking Melee 1.ogg"
    if Random == 2:
        play icavoice "sound/Voice/Icari/Icari Attacking Melee 2.ogg"
    if Random == 3:
        play icavoice "sound/Voice/Icari/Icari Attacking Melee 3.ogg"
    if Random == 4:
        play icavoice "sound/Voice/Icari/Icari Attacking Melee 4.ogg"

    show phoenix:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show icari plugsuit point angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show icari plugsuit point angry:
        ease 1.5 alpha 0

    pause 0.8

    play sound "sound/mech1.ogg"
    show phoenix melee with dissolve

    pause 0.5

    play sound1 "sound/boasters.ogg"

    show phoenix melee:
        xpos 0.5 ypos 0.5
        ease 1.0 xpos 2.0 ypos -1.0

    pause 1.4

    return

label hitanim_phoenix_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenix:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 520 xzoom -1
        linear 0.25 xpos 972 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 460 xzoom -1
        linear 0.25 xpos 705 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    pause 0.5

    call hit_phoenix

    return

label hitanim_phoenix_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenix:
        xpos 0.5 ypos 0.5

    pause 0.05

    play sound "sound/missilefly.ogg"

    show blackjack_hitmissile1:
        alpha 0 xpos 1350 ypos 0 zoom 1.2
        pause 0.4
        alpha 1
        linear 0.5 xpos 550 ypos 490
        alpha 0

    show blackjack_hitmissile2:
        alpha 0 xpos 1540 ypos 0 zoom 1.2
        pause 0.3
        alpha 1
        linear 0.5 xpos 700 ypos 530
        alpha 0

    show blackjack_hitmissile3:
        alpha 0 xpos 1650 ypos 0 zoom 1.2
        pause 0.2
        alpha 1
        linear 0.5 xpos 880 ypos 500
        alpha 0

    show blackjack_hitmissile4:
        alpha 0 xpos 1825 ypos 0 zoom 1.2
        pause 0.1
        alpha 1
        linear 0.6 xpos 950 ypos 540
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit1:
        alpha 0 xpos 0.4 ypos 0.5
        pause 0.8
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit2:
        alpha 0 xpos 0.35 ypos 0.45
        pause 0.9
        alpha 1
        ease 1 alpha 0

    pause 0.05

    show blackjack_hitmissiletrail with sunridermissilehitwipe
    hide blackjack_hitmissiletrail with dissolve

    pause 0.1

    call hit_phoenix

    return

label hitanim_phoenix_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show phoenix:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.4 ypos 0.5 xzoom -1
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    play sound "sound/explosion1.ogg"

    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.4 ypos 0.5  xzoom -1
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show blackjack_hitlaser behind piratebomber_laserhitexplode2 with enemy_laserhitwipe
    hide blackjack_hitlaser with enemy_laserhitwipe

    pause 0.5

    call hit_phoenix

    return

label hitanim_phoenix_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show phoenix:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show blackjack_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show blackjack_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    play sound3 "sound/explosion3.ogg"

    show blackjack_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 1

    call hit_phoenix

    return

label hitanim_phoenix_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenix:
        xpos 0.5 ypos 0.5

    show piratebomber_hitrocket:
        xpos 3000 ypos 490 xzoom -1
        pause 0.5
        linear 0.6 xpos 1010 ypos 490
        alpha 0

    show layer master at shake2(pausetime=1.1,repeats=8)
    show blackjack_rocketexplode:
        alpha 0
        pause 1.1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0
    
    pause 0.7

    play sound "sound/explosion4.ogg"

    show blackjack_rockettrail behind piratebomber_hitrocket with enemy_laserhitwipe
    hide blackjack_rockettrail with dissolve

    pause 0.5
    
    call hit_phoenix

    return

label hitanim_phoenix_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenix:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.2

    call hit_phoenix

    return

label miss_phoenix:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show phoenix behind miss:
        xpos 0.5 ypos 0.5


    $ Random = renpy.random.randint(1,7)

    if Random == 1:
        play icavoice "sound/Voice/Icari/Icari No Damage 1.ogg"
    if Random == 2:
        play icavoice "sound/Voice/Icari/Icari No Damage 2.ogg"
    if Random == 3:
        play icavoice "sound/Voice/Icari/Icari No Damage 3.ogg"
    if Random == 4:
        play icavoice "sound/Voice/Icari/Icari No Damage 4.ogg"
    if Random == 5:
        play icavoice "sound/Voice/Icari/Icari No Damage 5.ogg"
    if Random == 6:
        play icavoice "sound/Voice/Icari/Icari No Damage 6.ogg"
    if Random == 7:
        play icavoice "sound/Voice/Icari/Icari No Damage 7.ogg"

    show icari plugsuit point angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show icari plugsuit point angry:
        ease 1.5 alpha 0

    pause 2

    return

label attacksuccess_phoenix:

    show layer master

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play icavoice "sound/Voice/Icari/Icari Successful Attack 1.ogg"
    if Random == 2:
        play icavoice "sound/Voice/Icari/Icari Successful Attack 2.ogg"
    if Random == 3:
        play icavoice "sound/Voice/Icari/Icari Successful Attack 3.ogg"
    if Random == 4:
        play icavoice "sound/Voice/Icari/Icari Successful Attack 4.ogg"
    if Random == 5:
        play icavoice "sound/Voice/Icari/Icari Successful Attack 5.ogg"

    show icari plugsuit handonhip smile:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show icari plugsuit handonhip smile:
        ease 1.5 alpha 0

    pause
    return

label attackfail_phoenix:

    show layer master

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play icavoice "sound/Voice/Icari/Icari Missing Attack 1.ogg"
    if Random == 2:
        play icavoice "sound/Voice/Icari/Icari Missing Attack 2.ogg"
    if Random == 3:
        play icavoice "sound/Voice/Icari/Icari Missing Attack 3.ogg"
    if Random == 4:
        play icavoice "sound/Voice/Icari/Icari Missing Attack 4.ogg"
    if Random == 5:
        play icavoice "sound/Voice/Icari/Icari Missing Attack 5.ogg"

    show icari plugsuit armscrossed angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show icari plugsuit armscrossed angry:
        ease 1.5 alpha 0

    pause
    return

label hit_phoenix:

    show layer master

    if phoenix.hp >= phoenix.max_hp * 0.8:
        play icavoice "sound/Voice/Icari/Icari Damaged 1.ogg"
    if phoenix.hp < phoenix.max_hp * 0.8 and phoenix.hp >= phoenix.max_hp * 0.6:
        play icavoice "sound/Voice/Icari/Icari Damaged 2.ogg"
    if phoenix.hp < phoenix.max_hp * 0.6 and phoenix.hp >= phoenix.max_hp * 0.4:
        play icavoice "sound/Voice/Icari/Icari Damaged 3.ogg"
    if phoenix.hp < phoenix.max_hp * 0.4 and phoenix.hp >= phoenix.max_hp * 0.2:
        play icavoice "sound/Voice/Icari/Icari Damaged 4.ogg"
    if phoenix.hp < phoenix.max_hp * 0.2:
        play icavoice "sound/Voice/Icari/Icari Damaged 5.ogg"

    show icari plugsuit armscrossed angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show icari plugsuit armscrossed angry:
        ease 1.5 alpha 0

    pause

    return

label die_phoenix:

    $renpy.show_screen('show_background',_layer='master')

    show phoenix:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play icavoice "sound/Voice/Icari/Icari Retreating 1.ogg"
    if Random == 2:
        play icavoice "sound/Voice/Icari/Icari Retreating 2.ogg"
    if Random == 3:
        play icavoice "sound/Voice/Icari/Icari Retreating 3.ogg"
    if Random == 4:
        play icavoice "sound/Voice/Icari/Icari Retreating 4.ogg"
    if Random == 5:
        play icavoice "sound/Voice/Icari/Icari Retreating 5.ogg"

    show icari plugsuit armscrossed angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show icari plugsuit armscrossed angry:
        ease 1.5 alpha 0

    pause 1.0

    show phoenix:
        ease 0.5 xpos -0.5 ypos -1.0
    with dissolvequick

    pause

    return

label atkanim_phoenix_assassination:

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play icavoice "sound/Voice/Icari/Icari Stealth Mode 1.ogg"
    if Random == 2:
        play icavoice "sound/Voice/Icari/Icari Stealth Mode 2.ogg"
    if Random == 3:
        play icavoice "sound/Voice/Icari/Icari Stealth Mode 3.ogg"
    if Random == 4:
        play icavoice "sound/Voice/Icari/Icari Stealth Mode 4.ogg"

    show phoenix:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show icari plugsuit point angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show icari plugsuit point angry:
        ease 1.5 alpha 0

    show phoenix:
        ease 1.0 alpha 0.1

    pause 1.5
    return

label atkanim_phoenixenemy_assault: ######################################PHOENIX ENEMY

    $renpy.show_screen('show_background',_layer='master')

    show phoenix:
        zoom 2 xpos 0.8 ypos 0.5 xzoom -1
        ease 0.5 zoom 1 xpos 0.5 xzoom -1

    pause 0.5

    play sound1 "sound/mechchange.ogg"

    show phoenix assault with dissolve

    pause 0.3

    play sound "sound/machinegun.ogg"

    show phoenix_assaultflash1:
        alpha 0 xzoom -1
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    show phoenix_assaultflash2:
        alpha 0 xzoom -1
        pause 0.30
        block:
            ease 0.025 alpha 1
            pause 0.06
            ease 0.025 alpha 0
            pause 0.12
            repeat (5)

    pause 1.5

    return

label hitanim_phoenixenemy_kinetic: ##########################PACT MOOK HIT ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenix:
        xpos 0.5 ypos 0.5 xzoom -1

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"
    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.6 ypos 0.5
        ease 1.2 alpha 0

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixenemy_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenix:
        xpos 0.5 ypos 0.5 xzoom -1

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0 zoom 1.2
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0 zoom 1.2
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0 zoom 1.2
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0 zoom 1.2
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixenemy_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show phoenix:
        xpos 0.5 ypos 0.5 xzoom -1

    pause 0.5

    play sound1 "sound/Laser 1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show piratebomber_laserhittrail behind piratebomber_laserhitexplode1 with pactmissilefrigate_laserhitwipe
    hide piratebomber_laserhittrail with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixenemy_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show phoenix:
        xpos 0.5 ypos 0.5 xzoom -1

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixenemy_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenix:
        xpos 0.5 ypos 0.5 xzoom -1

    pause 0.1
    show piratebomber_hitrocket:
        xpos -200 ypos 440
        linear 0.4 xpos 1010 ypos 448
        alpha 0

    if sunrider.weapons[3].damage == 800:
        show layer master at shake2(pausetime=0.4,repeats=8)
        play sound "sound/explosion4.ogg"
        show pactmissilefrigate_die3:
            xpos 0.5 ypos 0.5 alpha 0
            pause 0.4
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0

    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 0.4
            ease 0.4 alpha 1.0 zoom 1.5
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show piratebomber_hitrockettrail behind piratebomber_hitrocket:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_laserhitwipe
    show piratebomber_hitrockettrail:
        ease 1.0 alpha 0

    if sunrider.weapons[3].damage == 1200:
        pause 3.0
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0 zoom 2.0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixenemy_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show phoenix:
        xpos 0.5 ypos 0.5 xzoom -1


    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_phoenixenemy_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show phoenix:
        xpos 0.5 ypos 0.5 xzoom -1

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return

label miss_phoenixenemy:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show phoenix behind miss:
        xpos 0.5 ypos 0.5 xzoom -1

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))


    return

label die_phoenixenemy:

    $renpy.show_screen('show_background',_layer='master')

    show phoenix:
        xpos 0.5 ypos 0.5 xzoom -1

    pause 0.8

    show phoenix:
        ease 0.5 xpos -0.5 ypos -1.0

    pause 2

    return


label atkanim_bianca_assault: ########################BIANCA ATTACK ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play clavoice "sound/Voice/Claude/Kinetic 1.ogg"
    if Random == 2:
        play clavoice "sound/Voice/Claude/Kinetic 2.ogg"
    if Random == 3:
        play clavoice "sound/Voice/Claude/Kinetic 3.ogg"
    if Random == 4:
        play clavoice "sound/Voice/Claude/Kinetic 4.ogg"

    show bianca:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show claude plugsuit excited shout:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show claude plugsuit excited shout:
        ease 1.5 alpha 0

    play sound "sound/mech1.ogg"
    show bianca kinetic with dissolve

    pause 0.5

    play sound "sound/shotgun.ogg"

    show bianca_kinetic_explode:
        xpos 0.5 ypos 0.5 alpha 1.0
        ease 0.3 alpha 0.0 zoom 2.5 ypos 0.6 xpos 0.7

    pause 1.0

    return

label hitanim_bianca_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show bianca:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 520 xzoom -1
        linear 0.25 xpos 972 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 460 xzoom -1
        linear 0.25 xpos 705 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    pause 0.5

    call hit_bianca

    return

label hitanim_bianca_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show bianca:
        xpos 0.5 ypos 0.5

    pause 0.05

    play sound "sound/missilefly.ogg"

    show blackjack_hitmissile1:
        alpha 0 xpos 1350 ypos 0 zoom 1.2
        pause 0.4
        alpha 1
        linear 0.5 xpos 550 ypos 490
        alpha 0

    show blackjack_hitmissile2:
        alpha 0 xpos 1540 ypos 0 zoom 1.2
        pause 0.3
        alpha 1
        linear 0.5 xpos 700 ypos 530
        alpha 0

    show blackjack_hitmissile3:
        alpha 0 xpos 1650 ypos 0 zoom 1.2
        pause 0.2
        alpha 1
        linear 0.5 xpos 880 ypos 500
        alpha 0

    show blackjack_hitmissile4:
        alpha 0 xpos 1825 ypos 0 zoom 1.2
        pause 0.1
        alpha 1
        linear 0.6 xpos 950 ypos 540
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit1:
        alpha 0 xpos 0.4 ypos 0.5
        pause 0.8
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit2:
        alpha 0 xpos 0.35 ypos 0.45
        pause 0.9
        alpha 1
        ease 1 alpha 0

    pause 0.05

    show blackjack_hitmissiletrail with sunridermissilehitwipe
    hide blackjack_hitmissiletrail with dissolve

    pause 0.1

    call hit_bianca

    return

label hitanim_bianca_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show bianca:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.4 ypos 0.5 xzoom -1
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    play sound "sound/explosion1.ogg"

    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.4 ypos 0.5  xzoom -1
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show blackjack_hitlaser behind piratebomber_laserhitexplode2 with enemy_laserhitwipe
    hide blackjack_hitlaser with enemy_laserhitwipe

    pause 0.5

    call hit_bianca

    return

label hitanim_bianca_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show bianca:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show blackjack_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show blackjack_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    play sound3 "sound/explosion3.ogg"

    show blackjack_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 1

    call hit_bianca

    return

label hitanim_bianca_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show bianca:
        xpos 0.5 ypos 0.5

    show piratebomber_hitrocket:
        xpos 3000 ypos 490 xzoom -1
        pause 0.5
        linear 0.6 xpos 1010 ypos 490
        alpha 0

    show layer master at shake2(pausetime=1.1,repeats=8)
    show blackjack_rocketexplode:
        alpha 0
        pause 1.1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0
    
    pause 0.7

    play sound "sound/explosion4.ogg"

    show blackjack_rockettrail behind piratebomber_hitrocket with enemy_laserhitwipe
    hide blackjack_rockettrail with dissolve

    pause 0.5

    call hit_bianca

    return

label hitanim_bianca_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show bianca:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.2

    call hit_bianca

    return

label miss_bianca:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show bianca behind miss:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,7)

    if Random == 1:
        play clavoice "sound/Voice/Claude/Evade 1.ogg"
    if Random == 2:
        play clavoice "sound/Voice/Claude/Evade 2.ogg"
    if Random == 3:
        play clavoice "sound/Voice/Claude/Evade 3.ogg"
    if Random == 4:
        play clavoice "sound/Voice/Claude/Evade 4.ogg"
    if Random == 5:
        play clavoice "sound/Voice/Claude/Evade 5.ogg"
    if Random == 6:
        play clavoice "sound/Voice/Claude/Evade 6.ogg"
    if Random == 7:
        play clavoice "sound/Voice/Claude/Evade 7.ogg"

    show claude plugsuit fingerup laugh:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show claude plugsuit fingerup laugh:
        ease 1.5 alpha 0

    pause 2

    return

label attacksuccess_bianca:

    show layer master

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play clavoice "sound/Voice/Claude/Hit 1.ogg"
    if Random == 2:
        play clavoice "sound/Voice/Claude/Hit 2.ogg"
    if Random == 3:
        play clavoice "sound/Voice/Claude/Hit 3.ogg"

    show claude plugsuit excited happy:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show claude plugsuit excited happy:
        ease 1.5 alpha 0

    pause
    return

label attackfail_bianca:

    show layer master

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play clavoice "sound/Voice/Claude/Miss 1.ogg"
    if Random == 2:
        play clavoice "sound/Voice/Claude/Miss 2.ogg"
    if Random == 3:
        play clavoice "sound/Voice/Claude/Miss 3.ogg"
    if Random == 4:
        play clavoice "sound/Voice/Claude/Miss 4.ogg"

    show claude plugsuit oops teehee:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show claude plugsuit oops teehee:
        ease 1.5 alpha 0

    pause
    return

label hit_bianca:

    show layer master

    if bianca.hp >= bianca.max_hp * 0.8:
        play clavoice "sound/Voice/Claude/Damage 1.ogg"
    if bianca.hp < bianca.max_hp * 0.8 and bianca.hp >= bianca.max_hp * 0.6:
        play clavoice "sound/Voice/Claude/Damage 2.ogg"
    if bianca.hp < bianca.max_hp * 0.6 and bianca.hp >= bianca.max_hp * 0.4:
        play clavoice "sound/Voice/Claude/Damage 3.ogg"
    if bianca.hp < bianca.max_hp * 0.4 and bianca.hp >= bianca.max_hp * 0.2:
        play clavoice "sound/Voice/Claude/Damage 4.ogg"
    if bianca.hp < bianca.max_hp * 0.2:
        play clavoice "sound/Voice/Claude/Damage 5.ogg"

    show claude plugsuit excited scaredsurprise:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show claude plugsuit excited scaredsurprise:
        ease 1.5 alpha 0

    pause

    return

label die_bianca:

    $renpy.show_screen('show_background',_layer='master')

    show bianca:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play clavoice "sound/Voice/Claude/Retreat 1.ogg"
    if Random == 2:
        play clavoice "sound/Voice/Claude/Retreat 2.ogg"
    if Random == 3:
        play clavoice "sound/Voice/Claude/Retreat 3.ogg"
    if Random == 4:
        play clavoice "sound/Voice/Claude/Retreat 4.ogg"
    if Random == 5:
        play clavoice "sound/Voice/Claude/Retreat 5.ogg"

    show claude plugsuit neutral sad:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show claude plugsuit neutral sad:
        ease 1.5 alpha 0

    pause 1.0

    show bianca:
        ease 0.5 xpos -0.5 ypos -1.0
    with dissolvequick

    pause

    return

############################################ALLIANCECRUISER ATTACK ANIMATIONS START
label atkanim_alliancecruiser_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    

    show alliancecruiser_side:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play othvoice "sound/Voice/AllianceCruiser/All Hands Brace For Combat.ogg"
    if Random == 2:
        play othvoice "sound/Voice/AllianceCruiser/Firing Weapons.ogg"
    if Random == 3:
        play othvoice "sound/Voice/AllianceCruiser/Open Fire.ogg"

    pause 0.75

    show layer master at shake1
    show alliancecruiser_sidekineticrear:
        alpha 0
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show alliancecruiser_kineticround1:
        xpos 1091 ypos 390
        linear 0.15 xpos 2300 ypos 270
    play sound1 'sound/railgun.ogg'
    pause 0.05

    show layer master at shake1
    show alliancecruiser_sidekineticfront:
        alpha 0
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show alliancecruiser_kineticround2:
        xpos 1202 ypos 408
        linear 0.15 xpos 2300 ypos 310
    play sound2 'sound/railgun.ogg'
    pause 0.2

    show layer master at shake1
    show alliancecruiser_sidekineticrear:
        alpha 0
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show alliancecruiser_kineticround3:
        xpos 1091 ypos 390
        linear 0.15 xpos 2300 ypos 270
    play sound1 'sound/railgun.ogg'
    pause 0.05

    show layer master at shake1
    show alliancecruiser_sidekineticfront:
        alpha 0
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show layer master at shake1
    show alliancecruiser_kineticround4:
        xpos 1202 ypos 408
        linear 0.15 xpos 2300 ypos 310
    play sound2 'sound/railgun.ogg'

    pause 0.5
    return

label atkanim_alliancecruiser_laser:

    $renpy.show_screen('show_background',_layer='master')
    show alliancecruiser_side:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play othvoice "sound/Voice/AllianceCruiser/All Hands Brace For Combat.ogg"
    if Random == 2:
        play othvoice "sound/Voice/AllianceCruiser/Firing Weapons.ogg"
    if Random == 3:
        play othvoice "sound/Voice/AllianceCruiser/Open Fire.ogg"

    pause 0.75
    
    play sound2 'sound/Laser 1.ogg'

    show alliancecruiser_side_laserfront:
        xpos 0.5 ypos 0.5
    with laserwipe

    hide alliancecruiser_side_laserfront with laserwipe

    pause 0.5
    return

label atkanim_alliancecruiser_missile:

    hide screen battle_screen

    $renpy.show_screen('show_background',_layer='master')
    show alliancecruiser_side:
        xpos 0.5 ypos 0.5
        
    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play othvoice "sound/Voice/AllianceCruiser/All Hands Brace For Combat.ogg"
    if Random == 2:
        play othvoice "sound/Voice/AllianceCruiser/Firing Weapons.ogg"
    if Random == 3:
        play othvoice "sound/Voice/AllianceCruiser/Open Fire.ogg"

    pause 0.75
        
    play sound2 'sound/missilelaunch.ogg'
    show alliancecruiser_missile1:
        xpos 745 ypos 420
        linear 1.1 xpos 2200 ypos -20
    show alliancecruiser_missile2:
        xpos 808 ypos 420
        linear 1.1 xpos 2200 ypos 0

    show alliancecruiser_missile_trail with sunridermissilewipe
    hide alliancecruiser_missile_trail with dissolve
    pause 0.5

    return

label atkanim_alliancecruiser_assault:

    $renpy.show_screen('show_background',_layer='master')
    show alliancecruiser_side:
        xpos 0.5 ypos 0.5
        
    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play othvoice "sound/Voice/AllianceCruiser/All Hands Brace For Combat.ogg"
    if Random == 2:
        play othvoice "sound/Voice/AllianceCruiser/Firing Weapons.ogg"
    if Random == 3:
        play othvoice "sound/Voice/AllianceCruiser/Open Fire.ogg"

    pause 0.75

    python:
        flak_positions1 = [
            (1325,394),
            (1254,381),
            (1220,393),
            (1155,380),
            (958,367),
            (896,365),
            ]
        Flak1 = FlakShield("gameplay/Animations/Alliancecruiser/flakbullet.png",flak_positions1,3000,dispersion=2, angle=80, interval=0.15)

        flak_positions2 = [
            (1305,381),
            (1266,396),
            (1204,381),
            (1164,395),
            (920,366),
            (867,365),
            ]
        Flak2 = FlakShield("gameplay/Animations/Alliancecruiser/flakbullet.png",flak_positions2,3000,dispersion=2, angle=80, interval=0.15)

    play sound "sound/Flak.ogg"

    $ Flak1.show()
    show alliancecruiser_side flak1
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak1
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak1
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak1
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    $ Flak1.stop()
    $ Flak2.show()
    show alliancecruiser_side flak2
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak2
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak2
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak2
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    $ Flak2.stop()
    $ Flak1.start()
    show alliancecruiser_side flak1
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak1
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak1
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak1
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    $ Flak1.stop()
    $ Flak2.start()
    show alliancecruiser_side flak2
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak2
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak2
    pause 0.01
    show alliancecruiser_side
    pause 0.01
    show alliancecruiser_side flak2
    pause 0.01
    show alliancecruiser_side
    $ Flak2.stop()

    pause 0.5

    return

#####################################################################ALLIANCECRUISER HIT ANIMATIONS

label hitanim_alliancecruiser_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show alliancecruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    show sunrider_missilehit1:
        xpos 1440 ypos 0 alpha 0
        pause 0.4
        alpha 1
        linear 0.7 xpos 620 ypos 480
        alpha 0

    show sunrider_missilehit2:
        alpha 0 xpos 1640 ypos 0
        pause 0.3
        alpha 1
        linear 0.7 xpos 740 ypos 560
        alpha 0

    show sunrider_missilehit3:
        xpos 1750 ypos 0 alpha 0
        pause 0.2
        alpha 1
        linear 0.7 xpos 920 ypos 500
        alpha 0

    show sunrider_missilehit4:
        xpos 1930 ypos 0 alpha 0
        pause 0.1
        alpha 1
        linear 0.7 xpos 1010 ypos 540
        alpha 0

    show layer master at shake1(pausetime=0.9,repeats=12)
    show sunrider_missileexplode1:
        alpha 0
        pause 0.9
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    show sunrider_missileexplode2:
        alpha 0
        pause 1
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    show sunrider_missileexplode3:
        alpha 0
        pause 1.1
        ease 0.2 alpha 1
        pause 0.2
        ease 2 alpha 0

    pause 0.15

    play sound1 "sound/explosion1.ogg"

    show sunrider_missiletrail_hit with sunridermissilehitwipe    
    hide sunrider_missiletrail_hit with dissolve

    call hit_alliancecruiser

    pause 0.3

    return

label hitanim_alliancecruiser_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show alliancecruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 540
        linear 0.25 xpos 590 ypos 540
        alpha 0

    pause 0.25

    play sound "sound/explosion1.ogg"

    show layer master at shake2
    show sunrider_kinetichit1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0
    show sunrider_kineticround2:
        xpos 2140 ypos 540
        linear 0.25 xpos 910 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"
    
    show layer master at shake2
    show sunrider_kinetichit2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0
        
    pause 0.25

    call hit_alliancecruiser

    pause 0.5

    return

label hitanim_alliancecruiser_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show alliancecruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show sunrider_laserhitexplode:
        alpha 0
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show sunrider_laserhit behind sunrider_laserhitexplode with enemy_laserhitwipe
    hide sunrider_laserhit behind sunrider_laserhitexplode with enemy_laserhitwipe

    call hit_alliancecruiser

    pause 0.5

    return

label hitanim_alliancecruiser_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show alliancecruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master
    show sunrider_pulse1:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 1940 ypos 550
        linear 0.15 xpos 1050 ypos 550
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 1940 ypos 420 alpha 1
        linear 0.15 xpos 570 ypos 420
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 1940 ypos 650 alpha 1
        linear 0.15 xpos 380 ypos 650
        alpha 0

    play sound "sound/explosion3.ogg"

    show sunrider_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1
    
    pause 0.25

    call hit_alliancecruiser

    pause 1

    return

label hitanim_alliancecruiser_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show alliancecruiser_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rockethit:
        alpha 0
        pause 0.1
        alpha 1
        xpos 1940 ypos 620
        linear 0.7 xpos 560 ypos 620
        alpha 0

    play sound "sound/explosion4.ogg"

    show layer master at shake2(pausetime=1,repeats=8)
    show sunrider_rockethitexplode:
        alpha 0
        pause 1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0

    pause 0.1

    show sunrider_rockethittrail with sunriderhitrocketwipe
    hide sunrider_rockethittrail with dissolve

    call hit_alliancecruiser

    pause 0.5

    return

label hitanim_alliancecruiser_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show alliancecruiser_side:
        xpos 0.5 ypos 0.5

    play sound "sound/Flak.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode12:
        xpos 0.41 ypos 0.52 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode13:
        xpos 0.81 ypos 0.17 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode14:
        xpos 0.37 ypos 0.63 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0

    call hit_alliancecruiser

    pause 0.2

    return

label miss_alliancecruiser:

    show layer master

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show alliancecruiser_side behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    return

label attacksuccess_alliancecruiser:
    
    pause
    return

label attackfail_alliancecruiser:

    return

label hit_alliancecruiser:

    $ Random = renpy.random.randint(1,3)

    if Random == 1:
        play othvoice "sound/Voice/AllianceCruiser/Hull Breaches Reported.ogg"
    if Random == 2:
        play othvoice "sound/Voice/AllianceCruiser/Reroute Emergency Power.ogg"
    if Random == 3:
        play othvoice "sound/Voice/AllianceCruiser/Were Taking Fire.ogg"

    pause

    return


label die_alliancecruiser:

    $renpy.show_screen('show_background',_layer='master')

    show alliancecruiser_side:
        xpos 0.5 ypos 0.5
        
    play othvoice "sound/Voice/AllianceCruiser/Abandon Ship.ogg"
    
    pause 1.0

    play sound2 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode2:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound3 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode3:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound4 "sound/explosion1.ogg"
    show layer master at shake1
    show sunrider_explode4:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.4

    play sound5 "sound/explosion2.ogg"
    show layer master at shake1
    show sunrider_explode5:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound5 "sound/explosion4.ogg"
    show layer master at shake1
    hide alliancecruiser_side
    show sunrider_explode6:
        alpha 0
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0
        
    pause 1.0

    return


label atkanim_pactcarrier_assault: ##########################################PACT CARRIER

    $renpy.show_screen('show_background',_layer='master')
    show pactcarrier_side:
        xpos 0.5 ypos 0.5
    pause 0.5

    python:
        flak_positions1 = [
            (748,429),
            (787,424),
            (836,429),
            (908,412),
            (1005,429),
            (1040,428)
            ]
        Flak1 = FlakShield("gameplay/Animations/AllianceCruiser/flakbullet.png",flak_positions1,3000,dispersion=5, angle=285, interval=0.15)

        flak_positions2 = [
            (733,430),
            (770,424),
            (810,420),
            (852,425),
            (967,412),
            (920,412),
            (987,430),
            (1027,428)
            ]
        Flak2 = FlakShield("gameplay/Animations/AllianceCruiser/flakbullet.png",flak_positions2,3000,dispersion=5, angle=285, interval=0.15)

    play sound "sound/Flak.ogg"

    $ Flak1.show()
    show pactcarrier_side flak1
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak1
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak1
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak1
    pause 0.01
    show pactcarrier_side
    pause 0.01
    $ Flak1.stop()
    $ Flak2.show()
    show pactcarrier_side flak2
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak2
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak2
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak2
    pause 0.01
    show pactcarrier_side
    pause 0.01
    $ Flak2.stop()
    $ Flak1.start()
    show pactcarrier_side flak1
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak1
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak1
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak1
    pause 0.01
    show pactcarrier_side
    pause 0.01
    $ Flak1.stop()
    $ Flak2.start()
    show pactcarrier_side flak2
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak2
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak2
    pause 0.01
    show pactcarrier_side
    pause 0.01
    show pactcarrier_side flak2
    pause 0.01
    show pactcarrier_side
    $ Flak2.stop()

    pause 0.5

    return

label hitanim_pactcarrier_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactcarrier_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos -200 ypos 520
        linear 0.25 xpos 968 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode1:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos -200 ypos 460
        linear 0.25 xpos 1235 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show pactcruiser_kineticexplode2:
        xpos 0.5 ypos 0.5
        ease 1.2 alpha 0
        
    pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))
    
    return

label hitanim_pactcarrier_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactcarrier_side:
        xpos 0.5 ypos 0.5

    pause 0.1

    play sound "sound/missilefly.ogg"

    show pactmissilefrigate_hitmissile1:
        alpha 0 xpos 543 ypos 0
        pause 0.35
        alpha 1
        linear 0.5 xpos 1350 ypos 480
        alpha 0

    show pactmissilefrigate_hitmissile2:
        alpha 0 xpos 353 ypos 0
        pause 0.25
        alpha 1
        linear 0.5 xpos 1190 ypos 520
        alpha 0

    show pactmissilefrigate_hitmissile3:
        alpha 0 xpos 243 ypos 0
        pause 0.15
        alpha 1
        linear 0.5 xpos 1000 ypos 460
        alpha 0

    show pactmissilefrigate_hitmissile4:
        alpha 0 xpos 64 ypos 0
        pause 0.05
        alpha 1
        linear 0.5 xpos 910 ypos 510
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show pactmissilefrigate_hitmissileexplode1:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.9
        alpha 1
        ease 1 alpha 0

    show pactmissilefrigate_hitmissileexplode2:
        alpha 0 xpos 0.5 ypos 0.5
        pause 1
        alpha 1
        ease 1 alpha 0

    pause 0.15

    show pactmissilefrigate_hitmissiletrail with pactmissilefrigate_missilehitwipe
    hide pactmissilefrigate_hitmissiletrail with dissolve

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcarrier_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactcarrier_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show pactmissilefrigate_hitlaserexplode:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe
    hide pactmissilefrigate_hitlaser behind pactmissilefrigate_hitlaserexplode with pactmissilefrigate_laserhitwipe

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcarrier_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactcarrier_side:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show sunrider_pulse1:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse1b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0
    pause 0.05
    show sunrider_pulse2b:
        xpos 0 ypos 540
        linear 0.15 xpos 940 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show sunrider_pulse3:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse3b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0
    pause 0.05
    show sunrider_pulse4b:
        xpos 0 ypos 460 alpha 1
        linear 0.15 xpos 1180 ypos 460
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show sunrider_pulse5:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse5b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0
    pause 0.05
    show sunrider_pulse6b:
        xpos 0 ypos 550 alpha 1
        linear 0.15 xpos 1380 ypos 550
        alpha 0

    play sound3 "sound/explosion3.ogg"

    show pactmissilefrigate_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1
    
    pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcarrier_rocket: #(damage):

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactcarrier_side:
        xpos 0.5 ypos 0.5

    pause 0.1
    show sunrider_rocket:
        yanchor 98 xanchor 400 xpos 0 ypos 570
        linear 1.1 xpos 1160 ypos 570
        alpha 0


    show layer master at shake2(pausetime=1,repeats=8)
    if sunrider.weapons[3].damage == 800:
        play sound1 "sound/explosion5.ogg"
        show pactmissilefrigate_rocketexplode:
            xpos 0.5 ypos 0.5 alpha 0
            pause 1
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        
    if sunrider.weapons[3].damage == 1200:
        play sound1 "sound/quantumtorpedo.ogg"
        show quantumtorpedo:
            alpha 0 zoom 0
            pause 1
            ease 0.05 alpha 1.0 zoom 1.0 
            parallel:
                ease 3.0 rotate 360
            parallel:
                pause 2.0
                ease 1.0 zoom 0.0

    pause 0.1

    show pactmissilefrigate_rockettrail:
        xpos 0.5 ypos 0.5
    with pactmissilefrigate_rockethitwipe

    show pactmissilefrigate_rockettrail:
        ease 1.0 alpha 0
    
    if sunrider.weapons[3].damage == 1200:
        pause 1.5
        play sound2 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_rocketexplode:
            xpos 0.4 ypos 0.5 alpha 0
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.1
        play sound3 "sound/explosion5.ogg"
        show layer master at shake2
        show pactmissilefrigate_die1:
            xpos 0.55 ypos 0.52 alpha 0 zoom 1.5
            ease 0.1 alpha 1
            pause 0.5
            ease 0.5 alpha 0
        pause 0.25

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcarrier_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show pactcarrier_side:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    $renpy.call('attacksuccess_{}'.format(BM.attacker.animation_name))

    return

label hitanim_pactcarrier_vanguard:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show pactcarrier_side:
        xpos 0.5 ypos 0.5

    pause 0.5

    play sound "sound/vanguard cannon laser.ogg"

    show layer master at shake2(pausetime=0.2,repeats=6)
    show layer master at shake2(pausetime=0.5,repeats=6)
    show layer master at shake2(pausetime=0.8,repeats=6)
    show layer master at shake2(pausetime=1.1,repeats=6)

    play sound1 "sound/explosion1.ogg"

    show hitanim_vanguard_explode1:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode2:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.5
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode3:
        alpha 0 xalign 0.5 yalign 0.5
        pause 0.8
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_explode4:
        alpha 0 xalign 0.5 yalign 0.5
        pause 1.1
        ease 0.1 alpha 1
        ease 2 alpha 0

    show hitanim_vanguard_beam behind pactmissilefrigate_hitlaserexplode with laserwipe

    play sound2 "sound/explosion2.ogg"

    pause 1.5

    return


label die_pactcarrier:

    $renpy.show_screen('show_background',_layer='master')

    show pactcarrier_side:
        xpos 0.5 ypos 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead1 zorder 1:
        alpha 0 zoom 1.2
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.5

    play sound "sound/explosion1.ogg"

    show layer master at shake1
    show pactcruiser_dead2 zorder 1:
        alpha 0 zoom 1.2
        ease 0.2 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    pause 0.75
    show white:
        alpha 0
        ease 0.3 alpha 1.0
        ease 0.3 alpha 0

    play sound "sound/explosion4.ogg"

    show layer master at shake2(shakeinterval=0.1,repeats=10)
    hide pactcarrier_side
    show pactcruiser_dead3:
        alpha 0 zoom 1.5
        ease 0.4 alpha 1
        pause 0.5
        ease 1.5 alpha 0

    pause 2

    return

label miss_pactcarrier:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show pactcarrier_side behind miss:
        xpos 0.5 ypos 0.5

    pause 2

    $renpy.call('attackfail_{}'.format(BM.attacker.animation_name))

    return

label atkanim_paladin_assault: ########################PALADIN ATTACK ANIMATIONS

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play kryvoice "sound/Voice/Kryska/Attacking Kinetic 1.ogg"
    if Random == 2:
        play kryvoice "sound/Voice/Kryska/Attacking Kinetic 2.ogg"
    if Random == 3:
        play kryvoice "sound/Voice/Kryska/Attacking With Laser 3.ogg"
    if Random == 4:
        play kryvoice "sound/Voice/Kryska/Attacking With Laser 2.ogg"

    show paladin:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show kryska plugsuit salute angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show kryska plugsuit salute angry:
        ease 1.5 alpha 0

    play sound "sound/mech1.ogg"
    show paladin assault with dissolve

    pause 0.3

    play sound1 "sound/machinegun.ogg"

    show paladin_assaultflash1:
        alpha 0
        pause 0.15
        block:
            ease 0.025 alpha 1
            pause 0.1
            ease 0.025 alpha 0
            pause 0.15
            repeat (4)

    show paladin_assaultflash2:
        alpha 0
        pause 0.30
        block:
            ease 0.025 alpha 1
            pause 0.1
            ease 0.025 alpha 0
            pause 0.15
            repeat (4)

    pause 1.5

    return

label atkanim_paladin_missile:

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play kryvoice "sound/Voice/Kryska/Attacking With Missile 1.ogg"
    if Random == 2:
        play kryvoice "sound/Voice/Kryska/Attacking With Missile 2.ogg"
    if Random == 3:
        play kryvoice "sound/Voice/Kryska/Attacking With Missile 3.ogg"
    if Random == 4:
        play kryvoice "sound/Voice/Kryska/Attacking With Missile 4.ogg"

    show paladin:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show kryska plugsuit salute angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show kryska plugsuit salute angry:
        ease 1.5 alpha 0
    pause 0.8

    play sound "sound/mech1.ogg"
    show paladin missile with dissolve

    pause 0.1

    play sound1 "sound/missile.ogg"

    show blackjack_missile1:
        alpha 0
        pause 0.3
        xpos 680 ypos 345 alpha 1
        linear 0.7 xpos 2215 ypos 35

    show blackjack_missile2:
        alpha 0
        pause 0.3
        xpos 675 ypos 378 alpha 1
        linear 0.7 xpos 2215 ypos 85

    show blackjack_missile3:
        alpha 0
        pause 0.3
        xpos 870 ypos 350 alpha 1
        linear 0.7 xpos 2415 ypos 35

    show blackjack_missile4:
        alpha 0
        pause 0.3
        xpos 802 ypos 735 alpha 1
        linear 0.7 xpos 2215 ypos 455

    show blackjack_missile5:
        alpha 0
        pause 0.3
        xpos 815 ypos 785 alpha 1
        linear 0.7 xpos 2215 ypos 490

    show paladin_missiletrail with blackjack_missilewipe
    hide paladin_missiletrail with dissolve

    pause 0.1

    return

label atkanim_paladin_kinetic:

    $renpy.show_screen('show_background',_layer='master')

    $ Random = renpy.random.randint(1,4)

    if Random == 1:
        play kryvoice "sound/Voice/Kryska/Attacking Kinetic 1.ogg"
    if Random == 2:
        play kryvoice "sound/Voice/Kryska/Attacking Kinetic 2.ogg"
    if Random == 3:
        play kryvoice "sound/Voice/Kryska/Attacking Kinetic 3.ogg"
    if Random == 4:
        play kryvoice "sound/Voice/Kryska/Attacking Kinetic 4.ogg"

    show paladin:
        zoom 2 xpos 0.2
        ease 0.5 zoom 1 xpos 0.5

    show kryska plugsuit salute angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show kryska plugsuit salute angry:
        ease 1.5 alpha 0

    play sound "sound/mech1.ogg"
    show paladin kinetic with dissolve

    pause 0.5

    play sound "sound/shotgun.ogg"
    show layer master at shake2
    show paladin_kineticflash1:
        xpos 0.5 ypos 0.5 alpha 1.0
        ease 0.3 alpha 0.0 zoom 2.5 ypos 0.8

    pause 0.1
    play sound1 "sound/shotgun.ogg"
    show layer master at shake2
    show paladin_kineticflash2:
        xpos 0.5 ypos 0.5 alpha 1.0
        ease 0.3 alpha 0.0 zoom 2.5 ypos 1.0
    pause 0.1
    
    play sound2 "sound/shotgun.ogg"
    show layer master at shake2
    show paladin_kineticflash3:
        xpos 0.5 ypos 0.5 alpha 1.0
        ease 0.3 alpha 0.0 zoom 2.5 ypos 1.0
    pause 0.1
    
    play sound3 "sound/shotgun.ogg"
    show layer master at shake2
    show paladin_kineticflash4:
        xpos 0.5 ypos 0.5 alpha 1.0
        ease 0.3 alpha 0.0 zoom 2.5 ypos 0.8

    pause 1.0

    return

label hitanim_paladin_kinetic:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show paladin:
        xpos 0.5 ypos 0.5

    pause 0.5

    show sunrider_kineticround1:
        xpos 2140 ypos 520 xzoom -1
        linear 0.25 xpos 972 ypos 540
        alpha 0

    pause 0.25

    play sound1 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit2:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    show sunrider_kineticround2:
        xpos 2140 ypos 460 xzoom -1
        linear 0.25 xpos 705 ypos 480
        alpha 0

    pause 0.25

    play sound2 "sound/explosion1.ogg"

    show layer master at shake2(repeats=6)
    show piratebomber_kinetichit1:
        xpos 0.4 ypos 0.5 xzoom -1
        ease 1.2 alpha 0

    pause 0.5

    call hit_paladin

    return

label hitanim_paladin_missile:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show paladin:
        xpos 0.5 ypos 0.5

    pause 0.05

    play sound "sound/missilefly.ogg"

    show blackjack_hitmissile1:
        alpha 0 xpos 1350 ypos 0 zoom 1.2
        pause 0.4
        alpha 1
        linear 0.5 xpos 550 ypos 490
        alpha 0

    show blackjack_hitmissile2:
        alpha 0 xpos 1540 ypos 0 zoom 1.2
        pause 0.3
        alpha 1
        linear 0.5 xpos 700 ypos 530
        alpha 0

    show blackjack_hitmissile3:
        alpha 0 xpos 1650 ypos 0 zoom 1.2
        pause 0.2
        alpha 1
        linear 0.5 xpos 880 ypos 500
        alpha 0

    show blackjack_hitmissile4:
        alpha 0 xpos 1825 ypos 0 zoom 1.2
        pause 0.1
        alpha 1
        linear 0.6 xpos 950 ypos 540
        alpha 0

    play sound "sound/explosion1.ogg"

    show layer master at shake2(pausetime=0.9, repeats=12)
    show piratebomber_kinetichit1:
        alpha 0 xpos 0.4 ypos 0.5
        pause 0.8
        alpha 1
        ease 1 alpha 0

    show piratebomber_kinetichit2:
        alpha 0 xpos 0.35 ypos 0.45
        pause 0.9
        alpha 1
        ease 1 alpha 0

    pause 0.05

    show blackjack_hitmissiletrail with sunridermissilehitwipe
    hide blackjack_hitmissiletrail with dissolve

    pause 0.1

    call hit_paladin

    return

label hitanim_paladin_laser:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show paladin:
        xpos 0.5 ypos 0.5

    pause 0.5

    show layer master at shake2(pausetime=0.2,repeats=6)
    show piratebomber_laserhitexplode2:
        alpha 0 xpos 0.4 ypos 0.5 xzoom -1
        pause 0.2
        ease 0.1 alpha 1
        ease 2 alpha 0

    play sound "sound/explosion1.ogg"

    show piratebomber_laserhitexplode1:
        alpha 0 xpos 0.4 ypos 0.5  xzoom -1
        pause 0.3
        ease 0.1 alpha 1
        ease 2 alpha 0

    show blackjack_hitlaser behind piratebomber_laserhitexplode2 with enemy_laserhitwipe
    hide blackjack_hitlaser with enemy_laserhitwipe

    pause 0.5

    call hit_paladin

    return

label hitanim_paladin_pulse:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp
    show paladin:
        xpos 0.5 ypos 0.5

    pause 0.5    ## salvo 1

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 540
        linear 0.15 xpos 760 ypos 540
        alpha 0

    play sound1 "sound/explosion3.ogg"

    show blackjack_pulsehit1:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2  ## salvo 2

    show layer master
    show blackjack_pulse5:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse6:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse7:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0
    pause 0.05
    show blackjack_pulse8:
        xpos 1920 ypos 350 alpha 1
        linear 0.15 xpos 640 ypos 350
        alpha 0

    play sound2 "sound/explosion3.ogg"

    show blackjack_pulsehit2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 0.2   #salvo 3

    show layer master
    show blackjack_pulse1:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse2:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse3:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    pause 0.05
    show blackjack_pulse4:
        xpos 1920 ypos 370 alpha 1
        linear 0.15 xpos 850 ypos 370
        alpha 0
    play sound3 "sound/explosion3.ogg"

    show blackjack_pulsehit3:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1 alpha 0
    show layer master at shake1

    pause 1

    call hit_paladin

    return

label hitanim_paladin_rocket:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show paladin:
        xpos 0.5 ypos 0.5

    show piratebomber_hitrocket:
        xpos 3000 ypos 490 xzoom -1
        pause 0.5
        linear 0.6 xpos 1010 ypos 490
        alpha 0

    show layer master at shake2(pausetime=1.1,repeats=8)
    show blackjack_rocketexplode:
        alpha 0
        pause 1.1
        ease 0.1 alpha 1
        pause 0.5
        ease 0.5 alpha 0
    
    pause 0.7

    play sound "sound/explosion4.ogg"

    show blackjack_rockettrail behind piratebomber_hitrocket with enemy_laserhitwipe
    hide blackjack_rockettrail with dissolve

    pause 0.5

    call hit_paladin

    return

label hitanim_paladin_assault:

    $renpy.show_screen('show_background',_layer='master')
    show screen animation_hp

    show paladin:
        xpos 0.5 ypos 0.5

    play sound1 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode1:
        xpos 0.32 ypos 0.62 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode2:
        xpos 0.62 ypos 0.57 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound2 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode3:
        xpos 0.74 ypos 0.14 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master
    show pactmissilefrigate_flakexplode4:
        xpos 0.82 ypos 0.47 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound3 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode5:
        xpos 0.20 ypos 0.80 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound4 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode6:
        xpos 0.58 ypos 0.72 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode7:
        xpos 0.72 ypos 0.12 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound5 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode8:
        xpos 0.80 ypos 0.44 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound6 "sound/explosion3.ogg"

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode9:
        xpos 0.38 ypos 0.85 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    play sound7 "sound/explosion3.ogg"

    show layer master
    show pactmissilefrigate_flakexplode10:
        xpos 0.24 ypos 0.39 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.1

    show layer master at shake1(shakeinterval=0.5, repeats=6)
    show pactmissilefrigate_flakexplode11:
        xpos 0.38 ypos 0.35 alpha 0
        ease 0.05 alpha 1
        pause 0.2
        ease 1.8 alpha 0
    pause 0.2

    call hit_paladin

    return

label miss_paladin:

    $renpy.show_screen('show_background',_layer='master')

    show miss:
        xpos 0.5 ypos 0.5
        ease 3 ypos 0.3 alpha 0

    show paladin behind miss:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,6)

    if Random == 1:
        play kryvoice "sound/Voice/Kryska/No Damage 1.ogg"
    if Random == 2:
        play kryvoice "sound/Voice/Kryska/No Damage 2.ogg"
    if Random == 3:
        play kryvoice "sound/Voice/Kryska/No Damage 3.ogg"
    if Random == 4:
        play kryvoice "sound/Voice/Kryska/No Damage 4.ogg"
    if Random == 5:
        play kryvoice "sound/Voice/Kryska/No Damage 5.ogg"
    if Random == 6:
        play kryvoice "sound/Voice/Kryska/No Damage 6.ogg"

    show kryska plugsuit handonhip focussmile:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show kryska plugsuit handonhip focussmile:
        ease 1.5 alpha 0

    pause 2

    return

label attacksuccess_paladin:

    show layer master

    $ Random = renpy.random.randint(1,6)

    if Random == 1:
        play kryvoice "sound/Voice/Kryska/After Successful Attack 2.ogg"
    if Random == 2:
        play kryvoice "sound/Voice/Kryska/After Successful Attack 3.ogg"
    if Random == 3:
        play kryvoice "sound/Voice/Kryska/After Successful Attack 4.ogg"
    if Random == 4:
        play kryvoice "sound/Voice/Kryska/After Successful Attack 5.ogg"
    if Random == 5:
        play kryvoice "sound/Voice/Kryska/After Successful Attack 6.ogg"
    if Random == 6:
        play kryvoice "sound/Voice/Kryska/After Successful Attack 7.ogg"

    show kryska plugsuit salute confidentsmile:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show kryska plugsuit salute confidentsmile:
        ease 1.5 alpha 0

    pause
    return

label attackfail_paladin:

    show layer master

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play kryvoice "sound/Voice/Kryska/After Missing Attack 1.ogg"
    if Random == 2:
        play kryvoice "sound/Voice/Kryska/After Missing Attack 2.ogg"
    if Random == 3:
        play kryvoice "sound/Voice/Kryska/After Missing Attack 3.ogg"
    if Random == 4:
        play kryvoice "sound/Voice/Kryska/After Missing Attack 4.ogg"
    if Random == 5:
        play kryvoice "sound/Voice/Kryska/After Missing Attack 5.ogg"

    show kryska plugsuit altneutral frown:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show kryska plugsuit altneutral frown:
        ease 1.5 alpha 0

    pause
    return

label hit_paladin:

    show layer master

    if paladin.hp >= paladin.max_hp * 0.8:
        play kryvoice "sound/Voice/Kryska/Damaged 1.ogg"
    if paladin.hp < paladin.max_hp * 0.8 and paladin.hp >= paladin.max_hp * 0.6:
        play kryvoice "sound/Voice/Kryska/Damaged 2.ogg"
    if paladin.hp < paladin.max_hp * 0.6 and paladin.hp >= paladin.max_hp * 0.4:
        play kryvoice "sound/Voice/Kryska/Damaged 3.ogg"
    if paladin.hp < paladin.max_hp * 0.4 and paladin.hp >= paladin.max_hp * 0.2:
        play kryvoice "sound/Voice/Kryska/Damaged 4.ogg"
    if paladin.hp < paladin.max_hp * 0.2:
        play kryvoice "sound/Voice/Kryska/Damaged 5.ogg"

    show kryska plugsuit armscrossed angry onlayer screens:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show kryska plugsuit armscrossed angry onlayer screens:
        ease 1.5 alpha 0

    pause

    return

label die_paladin:

    $renpy.show_screen('show_background',_layer='master')

    show paladin:
        xpos 0.5 ypos 0.5

    $ Random = renpy.random.randint(1,5)

    if Random == 1:
        play kryvoice "sound/Voice/Kryska/Retreating 1.ogg"
    if Random == 2:
        play kryvoice "sound/Voice/Kryska/Retreating 2.ogg"
    if Random == 3:
        play kryvoice "sound/Voice/Kryska/Retreating 3.ogg"
    if Random == 4:
        play kryvoice "sound/Voice/Kryska/Retreating 4.ogg"
    if Random == 5:
        play kryvoice "sound/Voice/Kryska/Retreating 5.ogg"

    show kryska plugsuit armscrossed angry:
        xzoom -1 xpos -0.2
        ease 0.3 xpos 0.15
    pause 0.5
    show kryska plugsuit armscrossed angry:
        ease 1.5 alpha 0

    pause 1.0

    show paladin:
        ease 0.5 xpos -0.5 ypos -1.0
    with dissolvequick

    pause

    return
