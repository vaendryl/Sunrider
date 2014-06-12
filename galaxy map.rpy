screen galaxymap_buttons: ###################################GALAXY MAP BUTTONS

    modal True

    for planet in planets:
        if planet.shouldShowOnMap():
            imagebutton:
                action Jump(planet.jumpLocation)
                idle "Map/map_icon_base.png"
                hover "Map/map_icon_hover.png"
                xpos planet.xPos ypos planet.yPos
            text planet.name xpos planet.xPos + 55 ypos planet.yPos size 15

    imagebutton:
        xpos 1600 ypos 950
        action Jump("galaxymapend")
        idle "Map/back_button_base.png"
        hover "Map/back_button_hover.png"

screen map_travelto:

    frame:
        xmaximum 900
        xpos 1098
        ypos 620
        background None

        vbox:
            if galaxymission1 == True:
                imagebutton:
                    action Jump(mission1)
                    idle "Map/whitebutton.png"
                    hover "Map/whitebutton_hover.png"
            if galaxymission2 == True:
                imagebutton:
                    action Jump(mission2)
                    idle "Map/whitebutton.png"
                    hover "Map/whitebutton_hover.png"
            if galaxymission3 == True:
                imagebutton:
                    action Jump(mission3)
                    idle "Map/whitebutton.png"
                    hover "Map/whitebutton_hover.png"
            imagebutton:
                action Jump(map_back)
                idle "Map/back_button_base.png"
                hover "Map/back_button_hover.png"

        vbox:
            if galaxymission1 == True:
                text "[mission1_name]" font "Font/sui generis rg.ttf" size 25 first_indent 30 line_leading 40 line_spacing 10 outlines [ (2, "#000", 0, 0) ]
            if galaxymission2 == True:
                text "[mission2_name]" font "Font/sui generis rg.ttf" size 25 first_indent 30 line_spacing 10 outlines [ (2, "#000", 0, 0) ]
            if galaxymission3 == True:
                text "[mission3_name]" font "Font/sui generis rg.ttf" size 25 first_indent 30 line_spacing 10 outlines [ (2, "#000", 0, 0) ]

label galaxymap:

    window hide
    show galaxymap with dissolve
    play music "Music/Star_of_Bethlehem.ogg" fadeout 1.5

    call screen galaxymap_buttons

label warpto_OccupiedCera:

    $ map_back = "Cera_back"
    $ galaxymission1 = False
    $ galaxymission2 = False
    $ galaxymission3 = False
    $ mission1 = None
    $ mission2 = None
    $ mission3 = None
    $ mission1_name = None
    $ mission2_name = None
    $ mission3_name = None

    scene bg black
    show galaxymap:
        alpha 1 zoom 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 xpos -12970 ypos -4800 zoom 10
    show map_cera:
        zoom 0.0268041237113402
        xpos 1297 ypos 480 alpha 0
        parallel:
            ease 1 alpha 1
        parallel:
            ease 0.75 zoom 1 xpos 0 ypos -430
    pause 1
    show map_occupiedcerainfo:
        xpos 1098 ypos 200
    call screen map_travelto
    with dissolve


label warpto_Tydaria:

    $ map_back = "Tydaria_back"

    if MetAsaga == False:
        $ galaxymission1 = True
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = "Tydaria_jump1"
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = "Main: Repair and Resupply"
        $ mission2_name = None
        $ mission3_name = None

    if mission_pirateattack == True:
        $ galaxymission1 = True
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = "piratebaseattack"
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = "Main: Attack Pirate Nest"
        $ mission2_name = None
        $ mission3_name = None

    if warpto_versta == True:
        $ galaxymission1 = False
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = None
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = None
        $ mission2_name = None
        $ mission3_name = None


    scene bg black
    show galaxymap:
        zoom 1 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 xpos -13710 ypos -5190  zoom 10
    show map_tydaria:
        zoom 0.0268041237113402
        xpos 1371 ypos 519 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 zoom 1 xpos 0 ypos -430
    pause 1
    show map_tydariainfo:
        xpos 1098 ypos 200
    call screen map_travelto
    with dissolve

label warpto_astralexpanse:

    $ map_back = "astralexpanse_back"

    if mission_pirateattack == True:
        if mission3_complete == False and mission4_complete == False:
            $ galaxymission1 = True
        else:
            $ galaxymission1 = False
        $ galaxymission2 = False
        $ galaxymission3 = False

        if mission3_complete == False and mission4_complete == False:
            $ mission1 = "humantraffickers"
        else:
            $ mission1 = None
        $ mission2 = None
        $ mission3 = None
        if mission3_complete == False and mission4_complete == False:
            $ mission1_name = "Side: Stop slavers"
        else:
            $ mission1 = None
        $ mission2_name = None
        $ mission3_name = None
    if mission_pirateattack == False:
        $ galaxymission1 = False
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = None
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = None
        $ mission2_name = None
        $ mission3_name = None

    scene bg black
    show galaxymap:
        zoom 1 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 xpos -13710 ypos -5190  zoom 10
    show map_astralexpanse:
        zoom 0.0268041237113402
        xpos 1371 ypos 519 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 zoom 1 xpos 0 ypos -430
    pause 1
    show map_astralexpanse_info:
        xpos 1098 ypos 200
    call screen map_travelto
    with dissolve

label warpto_pactstation:

    $ map_back = "pactstation_back"

    if mission_pirateattack == True:
        if mission3_complete == False and mission4_complete == False:
            $ galaxymission1 = True
        else:
            $ galaxymission1 = False
        $ galaxymission2 = False
        $ galaxymission3 = False

        if mission3_complete == False and mission4_complete == False:
            $ mission1 = "pactstationattack"
        else:
            $ mission1 = None
        $ mission2 = None
        $ mission3 = None
        if mission3_complete == False and mission4_complete == False:
            $ mission1_name = "Side: Destroy PACT outpost"
        else:
            $ mission1_name = None
        $ mission2_name = None
        $ mission3_name = None

    if mission_pirateattack == False:
        $ galaxymission1 = False
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = None
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = None
        $ mission2_name = None
        $ mission3_name = None

    scene bg black
    show galaxymap:
        zoom 1 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 xpos -13710 ypos -5190  zoom 10
    show map_pactstation:
        zoom 0.0268041237113402
        xpos 1371 ypos 519 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 zoom 1 xpos 0 ypos -430
    pause 1
    show map_pactstationinfo:
        xpos 1098 ypos 200
    call screen map_travelto
    with dissolve

label warpto_versta:

    $ map_back = "versta_back"

    if amissionforalliance == True:
        $ galaxymission1 = True
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = "jumphotversta"
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = "Main: Rescue Diplomats"
        $ mission2_name = None
        $ mission3_name = None

    else:

        $ galaxymission1 = False
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = None
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = None
        $ mission2_name = None
        $ mission3_name = None

    scene bg black
    show galaxymap:
        alpha 1 zoom 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 xpos -14900 ypos -7250 zoom 10
    show map_versta:
        zoom 0.0268041237113402
        xpos 1490 ypos 725 alpha 0
        parallel:
            ease 1 alpha 1
        parallel:
            ease 0.75 zoom 1 xpos 0 ypos -430
    pause 1
    show map_versta_info:
        xpos 1098 ypos 200
    call screen map_travelto
    with dissolve

label warpto_nomodorn:

    $ map_back = "nomodorn_back"

    if missionforryuvia == True:
        $ galaxymission1 = True
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = "jumptonomodorn"
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = "Main: Find Crown Jewel"
        $ mission2_name = None
        $ mission3_name = None

    else:

        $ galaxymission1 = False
        $ galaxymission2 = False
        $ galaxymission3 = False
        $ mission1 = None
        $ mission2 = None
        $ mission3 = None
        $ mission1_name = None
        $ mission2_name = None
        $ mission3_name = None

    scene bg black
    show galaxymap:
        alpha 1 zoom 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 xpos -16900 ypos -5900 zoom 10
    show map_nomodorn:
        zoom 0.0268041237113402
        xpos 1630 ypos 590 alpha 0
        parallel:
            ease 1 alpha 1
        parallel:
            ease 0.75 zoom 1 xpos 0 ypos -430
    pause 1
    show map_nomodorn_info:
        xpos 1098 ypos 200
    call screen map_travelto
    with dissolve

label Tydaria_back:
    hide map_tydariainfo
    scene bg black
    show map_tydaria:
        zoom 1
        xpos 0 ypos -430 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 zoom 0.0268041237113402 xpos 1371 ypos 519
    show galaxymap:
        xpos -13710 ypos -5190 zoom 10 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 xpos 0 ypos 0 zoom 1
    pause 1
    call screen galaxymap_buttons

label Cera_back:
    hide map_occupiedcerainfo
    scene bg black
    show map_cera:
        zoom 1
        xpos 0 ypos -430 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 zoom 0.0268041237113402 xpos 1297 ypos 480
    show galaxymap:
        xpos -12970 ypos -4800 zoom 10 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 xpos 0 ypos 0 zoom 1
    pause 1
    call screen galaxymap_buttons

label astralexpanse_back:
    hide map_astralexpanse_info
    scene bg black
    show map_astralexpanse:
        zoom 1
        xpos 0 ypos -430 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 zoom 0.0268041237113402 xpos 1371 ypos 519
    show galaxymap:
        xpos -13710 ypos -5190 zoom 10 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 xpos 0 ypos 0 zoom 1
    pause 1
    call screen galaxymap_buttons

label pactstation_back:
    hide map_pactstationinfo
    scene bg black
    show map_pactstation:
        zoom 1
        xpos 0 ypos -430 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 zoom 0.0268041237113402 xpos 1297 ypos 480
    show galaxymap:
        xpos -12970 ypos -4800 zoom 10 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 xpos 0 ypos 0 zoom 1
    pause 1
    call screen galaxymap_buttons

label versta_back:
    hide map_versta_info
    scene bg black
    show map_versta:
        zoom 1
        xpos 0 ypos -430 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 zoom 0.0268041237113402 xpos 1490 ypos 725
    show galaxymap:
        xpos -14900 ypos -7250 zoom 10 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 xpos 0 ypos 0 zoom 1
    pause 1
    call screen galaxymap_buttons

label nomodorn_back:
    hide map_nomodorn_info
    scene bg black
    show map_nomodorn:
        zoom 1
        xpos 0 ypos -430 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 zoom 0.0268041237113402 xpos 1630 ypos 590
    show galaxymap:
        xpos -16300 ypos -5900 zoom 10 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 xpos 0 ypos 0 zoom 1
    pause 1
    call screen galaxymap_buttons

label galaxymapend:

    jump dispatch