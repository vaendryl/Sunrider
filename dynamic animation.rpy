  

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

    if hasattr(BM.target, 'sprites'):
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
