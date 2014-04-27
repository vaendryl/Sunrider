#################################################MAP MOVEMENT
        
label dispatch:
    
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
            if chi_location == "sickbay":
                imagebutton:
                    #xpos 1140 ypos 595
                    action Jump(chi_event)
                    idle "Menu/chi_button.png"
                    hover "Menu/chi_button_hover.png"
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
            if pro_location == "lab":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
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
                    
            if pro_location == "hangar":
                imagebutton:
                    #xpos 560 ypos 435
                    action Jump(pro_event)
                    idle "Menu/pro_button.png"
                    hover "Menu/pro_button_hover.png"
                    activate_sound "Sound/click.mp3"
