#################################################MAP MOVEMENT

label dispatch:


    #dissolve to black so that previous scene doesn't briefly appear when going to new scene
    window hide
#    scene Solid((0, 0, 0, 255))
    with dissolve

    hide screen store_missile
    hide screen store_rocket


    if captaindeck == 0:
        window hide
        $ renpy.transition(dissolve)
        show screen deck0
        $ ui.interact()

    if captaindeck == 1:
        window hide
        $ renpy.transition(dissolve)
        show screen deck1
        $ ui.interact()

    if captaindeck == 2:
        window hide
        $ renpy.transition(dissolve)
        show screen deck2
        $ ui.interact()


screen deck0:

    tag ship_map

    imagemap:
        ground "Menu/deck0_inactive.jpg"
        hover "Menu/deck0_hover.jpg"
        idle "Menu/deck0.jpg"

        hotspot (1610, 858, 310, 70):
            action Show("deck1", dissolve)
        hotspot (1610, 960, 310, 70):
            action Show("deck2", dissolve)


    frame:##################################### CAPTAIN'S QUARTERS
        xmaximum 300
        xpos 500
        ypos 400
        background None

        vbox:
            if ava_location == "captainsloft":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(ava_event)
                    idle "Menu/ava_button.png"
                    hover "Menu/ava_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if asa_location == "captainsloft":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(asa_event)
                    idle "Menu/asa_button.png"
                    hover "Menu/asa_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if chi_location == "captainsloft":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(chi_event)
                    idle "Menu/chi_button.png"
                    hover "Menu/chi_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if ica_location == "captainsloft":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(ica_event)
                    idle "Menu/ica_button.png"
                    hover "Menu/ica_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if cla_location == "captainsloft":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(cla_event)
                    idle "Menu/cla_button.png"
                    hover "Menu/cla_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if sol_location == "captainsloft":
                imagebutton:
                    action Jump(sol_event)
                    idle "Menu/sol_button.png"
                    hover "Menu/sol_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if kry_location == "captainsloft":
                imagebutton:
                    action Jump(kry_event)
                    idle "Menu/kry_button.png"
                    hover "Menu/kry_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if pro_location == "captainsloft":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if cal_location == "captainsloft":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(cal_event)
                    idle "Menu/cal_button.png"
                    hover "Menu/cal_button_hover.png"
                    activate_sound "Sound/click.mp3"


    frame:##################################### SICKBAY
        xmaximum 400
        xpos 750
        ypos 525
        background None

        vbox:
            if ava_location == "sickbay":
                imagebutton:
                    #xpos 1140 ypos 595
                    action Jump(ava_event)
                    idle "Menu/ava_button.png"
                    hover "Menu/ava_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if asa_location == "sickbay":
                imagebutton:
                    #xpos 1140 ypos 595
                    action Jump(asa_event)
                    idle "Menu/asa_button.png"
                    hover "Menu/asa_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if ica_location == "sickbay":
                imagebutton:
                    action Jump(ica_event)
                    idle "Menu/ica_button.png"
                    hover "Menu/ica_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if chi_location == "sickbay":
                imagebutton:
                    #xpos 1140 ypos 595
                    action Jump(chi_event)
                    idle "Menu/chi_button.png"
                    hover "Menu/chi_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if cla_location == "sickbay":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(cla_event)
                    idle "Menu/cla_button.png"
                    hover "Menu/cla_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if sol_location == "sickbay":
                imagebutton:
                    action Jump(sol_event)
                    idle "Menu/sol_button.png"
                    hover "Menu/sol_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if kry_location == "sickbay":
                imagebutton:
                    action Jump(kry_event)
                    idle "Menu/kry_button.png"
                    hover "Menu/kry_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if pro_location == "sickbay":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
                    activate_sound "Sound/click.mp3"


    frame:##################################### MESS HALL
        xmaximum 400
        xpos 1150
        ypos 380
        background None

        vbox:
            if ava_location == "messhall":
                imagebutton:
                    #xpos 1250 ypos 480
                    action Jump(ava_event)
                    idle "Menu/ava_button.png"
                    hover "Menu/ava_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if asa_location == "messhall":
                imagebutton:
                    #xpos 1250 ypos 480
                    action Jump(asa_event)
                    idle "Menu/asa_button.png"
                    hover "Menu/asa_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if chi_location == "messhall":
                imagebutton:
                    #xpos 1250 ypos 480
                    action Jump(chi_event)
                    idle "Menu/chi_button.png"
                    hover "Menu/chi_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if ica_location == "messhall":
                imagebutton:
                    #xpos 1250 ypos 480
                    action Jump(ica_event)
                    idle "Menu/ica_button.png"
                    hover "Menu/ica_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if cla_location == "messhall":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(cla_event)
                    idle "Menu/cla_button.png"
                    hover "Menu/cla_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if sol_location == "messhall":
                imagebutton:
                    action Jump(sol_event)
                    idle "Menu/sol_button.png"
                    hover "Menu/sol_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if kry_location == "messhall":
                imagebutton:
                    action Jump(kry_event)
                    idle "Menu/kry_button.png"
                    hover "Menu/kry_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if pro_location == "messhall":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
                    activate_sound "Sound/click.mp3"

screen deck1:

    tag ship_map

    imagemap:
        ground "Menu/deck1_inactive.jpg"
        hover "Menu/deck1_hover.jpg"
        idle "Menu/deck1.jpg"

        hotspot (1610, 758, 310, 70):
            action Show("deck0", dissolve)
        hotspot (1610, 960, 310, 70):
            action Show("deck2", dissolve)

    frame:##################################### BRIDGE
        xmaximum 300
        xpos 620
        ypos 440
        background None

        vbox:

            if ava_location == "bridge":
                imagebutton:
                    #xpos 660 ypos 470
                    action Jump(ava_event)
                    idle "Menu/ava_button.png"
                    hover "Menu/ava_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if asa_location == "bridge":
                imagebutton:
                    #xpos 660 ypos 470
                    action Jump(asa_event)
                    idle "Menu/asa_button.png"
                    hover "Menu/asa_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if chi_location == "bridge":
                imagebutton:
                    #xpos 660 ypos 470
                    action Jump(chi_event)
                    idle "Menu/chi_button.png"
                    hover "Menu/chi_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if ica_location == "bridge":
                imagebutton:
                    #xpos 660 ypos 470
                    action Jump(ica_event)
                    idle "Menu/ica_button.png"
                    hover "Menu/ica_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if cla_location == "bridge":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(cla_event)
                    idle "Menu/cla_button.png"
                    hover "Menu/cla_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if sol_location == "bridge":
                imagebutton:
                    action Jump(sol_event)
                    idle "Menu/sol_button.png"
                    hover "Menu/sol_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if kry_location == "bridge":
                imagebutton:
                    action Jump(kry_event)
                    idle "Menu/kry_button.png"
                    hover "Menu/kry_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if pro_location == "bridge":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if gal_location == "bridge":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(gal_event)
                    idle "Menu/gal_button.png"
                    hover "Menu/gal_button_hover.png"
                    activate_sound "Sound/click.mp3"


    frame:##################################### ENGINEERING
        xmaximum 300
        xpos 1000
        ypos 350
        background None

        vbox:

            if ava_location == "engineering":
                imagebutton:
                    #xpos 1080 ypos 520
                    action Jump(ava_event)
                    idle "Menu/ava_button.png"
                    hover "Menu/ava_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if asa_location == "engineering":
                imagebutton:
                    #xpos 1080 ypos 520
                    action Jump(asa_event)
                    idle "Menu/asa_button.png"
                    hover "Menu/asa_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if chi_location == "engineering":
                imagebutton:
                    #xpos 1080 ypos 520
                    action Jump(chi_event)
                    idle "Menu/chi_button.png"
                    hover "Menu/chi_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if ica_location == "engineering":
                imagebutton:
                    #xpos 1080 ypos 520
                    action Jump(ica_event)
                    idle "Menu/ica_button.png"
                    hover "Menu/ica_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if cla_location == "engineering":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(cla_event)
                    idle "Menu/cla_button.png"
                    hover "Menu/cla_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if sol_location == "engineering":
                imagebutton:
                    action Jump(sol_event)
                    idle "Menu/sol_button.png"
                    hover "Menu/sol_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if kry_location == "engineering":
                imagebutton:
                    action Jump(kry_event)
                    idle "Menu/kry_button.png"
                    hover "Menu/kry_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if pro_location == "engineering":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
                    activate_sound "Sound/click.mp3"

    frame:##################################### LAB
        xmaximum 300
        xpos 1170
        ypos 440
        background None

        vbox:
            if ava_location == "lab":
                imagebutton:
                    #xpos 1240 ypos 520
                    action Jump(ava_event)
                    idle "Menu/ava_button.png"
                    hover "Menu/ava_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if asa_location == "lab":
                imagebutton:
                    #xpos 1240 ypos 520
                    action Jump(asa_event)
                    idle "Menu/asa_button.png"
                    hover "Menu/asa_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if chi_location == "lab":
                imagebutton:
                    #xpos 1240 ypos 520
                    action Jump(chi_event)
                    idle "Menu/chi_button.png"
                    hover "Menu/chi_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if ica_location == "lab":
                imagebutton:
                    action Jump(ica_event)
                    idle "Menu/ica_button.png"
                    hover "Menu/ica_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if cla_location == "lab":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(cla_event)
                    idle "Menu/cla_button.png"
                    hover "Menu/cla_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if sol_location == "lab":
                imagebutton:
                    action Jump(sol_event)
                    idle "Menu/sol_button.png"
                    hover "Menu/sol_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if kry_location == "lab":
                imagebutton:
                    action Jump(kry_event)
                    idle "Menu/kry_button.png"
                    hover "Menu/kry_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if pro_location == "lab":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if res_location == "lab":
                imagebutton:
                    action Jump(res_event)
                    idle "Menu/res_button.png"
                    hover "Menu/res_button_hover.png"
                    activate_sound "Sound/click.mp3"

screen deck2:

    tag ship_map

    imagemap:
        ground "Menu/deck2_inactive.jpg"
        hover "Menu/deck2_hover.jpg"
        idle "Menu/deck2.jpg"

        hotspot (1610, 758, 310, 70):
            action Show("deck0", dissolve)
        hotspot (1610, 858, 310, 70):
            action Show("deck1", dissolve)

    frame:##################################### LAB
        xmaximum 300
        xpos 1170
        ypos 440
        background None

        vbox:
            if ava_location == "hangar":
                imagebutton:
                    #xpos 1250 ypos 520
                    action Jump(ava_event)
                    idle "Menu/ava_button.png"
                    hover "Menu/ava_button_hover.png"
                    activate_sound "Sound/click.mp3"

            if asa_location == "hangar":
                imagebutton:
                    #xpos 1250 ypos 520
                    action Jump(asa_event)
                    idle "Menu/asa_button.png"
                    hover "Menu/asa_button_hover.png"
                    activate_sound "Sound/click.mp3"

            if chi_location == "hangar":
                imagebutton:
                    #xpos 1250 ypos 520
                    action Jump(chi_event)
                    idle "Menu/chi_button.png"
                    hover "Menu/chi_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if ica_location == "hangar":
                imagebutton:
                    #xpos 1250 ypos 520
                    action Jump(ica_event)
                    idle "Menu/ica_button.png"
                    hover "Menu/ica_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if cla_location == "hangar":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(cla_event)
                    idle "Menu/cla_button.png"
                    hover "Menu/cla_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if sol_location == "hangar":
                imagebutton:
                    action Jump(sol_event)
                    idle "Menu/sol_button.png"
                    hover "Menu/sol_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if kry_location == "hangar":
                imagebutton:
                    action Jump(kry_event)
                    idle "Menu/kry_button.png"
                    hover "Menu/kry_button_hover.png"
                    activate_sound "Sound/click.mp3"
            if pro_location == "hangar":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
                    activate_sound "Sound/click.mp3"
