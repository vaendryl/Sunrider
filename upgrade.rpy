screen upgrade:
    add "Menu/upgrade_back.jpg"

    text '{!s}$'.format(BM.money):
        size 50
        xpos 0.15
        ypos 0.7
        color '090'
        outlines [(1,'000',0,0)]

    imagebutton:
        xpos 1650 ypos 975
        action Return("quit")
        idle "Menu/return.jpg"
        hover "Menu/return_hover.jpg"

    if BM.selected == None:
        $ BM.selected = sunrider
    $ ship = BM.selected

    $can_use_melee = False
    for weapon in ship.weapons:
        if weapon.wtype == 'Melee':
            $ can_use_melee = True

    #dictionaries are inherently unsorted, so this is needed ;_;
    $ upgrade_list = []
    $ upgrade_list.append(["BASIC -----------",None,None,None,None])
    $ upgrade_list.append(ship.upgrades['max_hp'])
    $ upgrade_list.append(ship.upgrades['max_en'])
    $ upgrade_list.append(ship.upgrades['evasion'])
#    $ upgrade_list.append(ship.upgrades['move_cost'])  #probably should be set individually in design
    $ upgrade_list.append(["KINETIC -----------",None,None,None,None])
    $ upgrade_list.append(ship.upgrades['kinetic_dmg'])
    $ upgrade_list.append(ship.upgrades['kinetic_acc'])
    $ upgrade_list.append(ship.upgrades['kinetic_cost'])
    $ upgrade_list.append(["LASER -----------",None,None,None,None])
    $ upgrade_list.append(ship.upgrades['energy_dmg'])
    $ upgrade_list.append(ship.upgrades['energy_acc'])
    $ upgrade_list.append(ship.upgrades['energy_cost'])

    if ship.max_missiles > 0:
        $ upgrade_list.append(["MISSILE -----------",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['missile_dmg'])
        $ upgrade_list.append(ship.upgrades['missile_acc'])
        $ upgrade_list.append(ship.upgrades['missile_cost'])
        $ upgrade_list.append(ship.upgrades['max_missiles'])

    if can_use_melee:
        $ upgrade_list.append(["MELEE -----------",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['melee_dmg'])
        $ upgrade_list.append(ship.upgrades['melee_acc'])
        $ upgrade_list.append(ship.upgrades['melee_cost'])

    $ upgrade_list.append(["DEFENSES -----------",None,None,None,None])

    if ship.shield_generation > 0:
        $ upgrade_list.append(ship.upgrades['shield_generation'])
        $ upgrade_list.append(ship.upgrades['shield_range'])

    if ship.flak > 0:
        $ upgrade_list.append(ship.upgrades['flak'])

    $ upgrade_list.append(ship.upgrades['base_armor'])

    if ship.repair > 0:
        $ upgrade_list.append(ship.upgrades['repair'])

    if ship == sunrider:
        add "Menu/upgrade_sunrider.png"
    if ship == blackjack:
        add "Menu/upgrade_blackjack.png"
    if ship == liberty:
        add "Menu/upgrade_liberty.png"

    textbutton 'next ship':
        xpos 0.8
        ypos 0.1
        text_size 50
        text_color 'fff'
        text_outlines [(1,'000',0,0)]
        action Return('next')

    vbox:
        area (40, 270, 1050, 440)

        viewport id "upgrade_list":
            draggable True
            mousewheel True
            scrollbars "vertical"
            child_size (1050,2000)

            vbox:

                for upgrade in upgrade_list:
                    if upgrade[1] == None:
                        add "Menu/upgrade_blank.png"
                    else:
                        add "Menu/upgrade_item.png"

            vbox:
                ypos 10
                xpos 20
                spacing 23

                for upgrade in upgrade_list:
                    if upgrade[1] == None:
                        text upgrade[0]:
                            color '000'
                    else:
                        $ name,level,increase,cost,multiplier = upgrade
                        $ attribute = ""
                        for key in ship.upgrades:
                            if ship.upgrades[key][0] == name:
                                $ attribute = key
                        $ current = getattr(ship,attribute)
                        hbox:
                            spacing 60
                            text name:
                                color '000'
                                min_width 400

                            if increase < 1:
                                text str(current*100)+'% -> '+ str((current+increase)*100)+'%':
                                    color '000'
                                    min_width 200
                            else:
                                text str(current)+' -> '+ str(current+increase):
                                    color '000'
                                    min_width 200

                            text str(level):
                                color '000'
                                min_width 50
                            text str(cost):
                                color '000'
                                min_width 60
                            if BM.money >= cost:
                                textbutton '+':
                                    text_color 'fff'
                                    action Return(attribute)
                            else:
                                textbutton 'X':
                                    text_color 'c00'
                                    action NullAction()

#    textbutton 'next unit':
#        xpos 0.8
#        ypos 0.1
#        text_size 50
#        text_color 'fff'
#        text_outlines [(1,'000',0,0)]
#        action If(active_ship == sunrider,
#            SetScreenVariable('active_ship',blackjack),If(active_ship == blackjack,
#                SetScreenVariable('active_ship',liberty),
#                SetScreenVariable('active_ship',sunrider)))



#    vbox:
#        area (40, 270, 1050, 440)

#        viewport id "upgrade_list":
#            draggable True
#            mousewheel True
#            scrollbars "vertical"
#            child_size (1050,2000)

#            vbox:

#                add "Menu/upgrade_blank.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_blank.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_blank.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_blank.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_blank.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"
#                add "Menu/upgrade_item.png"

#            vbox:
#                xpos 970
#                add "Menu/upgrade_blank.png"
#                $upgrade = active_ship.upgrades['HP']
#                imagebutton:
#                    action If(BM.money >= upgrade[1],
#                        [SetDict(active_ship.upgrades,'HP',[upgrade[0]+1,int(upgrade[1]*cost_increase)]),
#                            SetField(active_ship,'max_hp',active_ship.max_hp + 100),
#                            SetField(BM,'money',BM.money-upgrade[1])])
#                    idle "Menu/upgrade_button.png"
#                    hover "Menu/upgrade_button_hover.png"

#                $upgrade = active_ship.upgrades['energy']
#                imagebutton:
#                    action If(BM.money >= upgrade[1],
#                        [SetDict(active_ship.upgrades,'energy',[upgrade[0]+1,int(upgrade[1]*cost_increase)]),
#                            SetField(active_ship,'max_en',active_ship.max_en + 10),
#                            SetField(BM,'money',BM.money-upgrade[1])])
#                    idle "Menu/upgrade_button.png"
#                    hover "Menu/upgrade_button_hover.png"

#                $upgrade = active_ship.upgrades['engine']
#                imagebutton:
#                    action If(BM.money >= upgrade[1],
#                        [SetDict(active_ship.upgrades,'engine',[upgrade[0]+1,int(upgrade[1]*cost_increase)]),
#                            SetField(active_ship,'move_cost',active_ship.move_cost -1),
#                            SetField(BM,'money',BM.money-upgrade[1])])
#                    idle "Menu/upgrade_button.png"
#                    hover "Menu/upgrade_button_hover.png"

#                $upgrade = active_ship.upgrades['thrusters']
#                imagebutton:
#                    action If(BM.money >= upgrade[1],
#                        [SetDict(active_ship.upgrades,'thrusters',[upgrade[0]+1,int(upgrade[1]*cost_increase)]),
#                            SetField(active_ship,'evasion',active_ship.evasion + 1),
#                            SetField(BM,'money',BM.money-upgrade[1])])
#                    idle "Menu/upgrade_button.png"
#                    hover "Menu/upgrade_button_hover.png"


#            vbox:

#                text "BASIC ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_leading 5 line_spacing 22 color "#0a0a0a"
#                text "HULL PLATING" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "ENERGY REACTOR" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "ENGINE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "THRUSTERS" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"

#                text "KINETIC ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   ACCURACY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   DAMAGE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   ENERGY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "LASER ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   ACCURACY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   DAMAGE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   ENERGY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "MISSILE ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   ACCURACY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   DAMAGE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   ENERGY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "DEFENSES  ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   SHIELD POWER" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   SHIELD RANGE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   FLAK" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   ARMOR" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
#                text "   REPAIR CREW" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"

#            vbox:
#                text "  " font "Font/segoeui.ttf" size 25 first_indent 470 line_leading 5 line_spacing 22 color "#0a0a0a"
#                text "{!s} > {!s}".format(active_ship.max_hp,active_ship.max_hp+100) font "Font/segoeui.ttf" size 25 first_indent 470 line_spacing 22 color "#0a0a0a"
#                text "{!s} > {!s}".format(active_ship.max_en,active_ship.max_en+10) font "Font/segoeui.ttf" size 25 first_indent 470 line_spacing 22 color "#0a0a0a"
#                text "{!s} > {!s}".format(active_ship.move_cost,active_ship.move_cost-1) font "Font/segoeui.ttf" size 25 first_indent 470 line_spacing 22 color "#0a0a0a"
#                text "{!s} > {!s}".format(active_ship.evasion,active_ship.evasion+1) font "Font/segoeui.ttf" size 25 first_indent 470 line_spacing 22 color "#0a0a0a"

#            vbox:
#                text "  " font "Font/segoeui.ttf" size 25 first_indent 710 line_leading 5 line_spacing 22 color "#0a0a0a"
#                text "Lvl {}".format(active_ship.upgrades['HP'][0]) font "Font/segoeui.ttf" size 25 first_indent 710 line_spacing 22 color "#0a0a0a"
#                text "Lvl {}".format(active_ship.upgrades['energy'][0]) font "Font/segoeui.ttf" size 25 first_indent 710 line_spacing 22 color "#0a0a0a"
#                text "Lvl {}".format(active_ship.upgrades['engine'][0]) font "Font/segoeui.ttf" size 25 first_indent 710 line_spacing 22 color "#0a0a0a"
#                text "Lvl {}".format(active_ship.upgrades['thrusters'][0]) font "Font/segoeui.ttf" size 25 first_indent 710 line_spacing 22 color "#0a0a0a"

#            vbox:
#                text "  " font "Font/segoeui.ttf" size 25 first_indent 790 line_leading 5 line_spacing 22 color "#0a0a0a"
#                text "{}$".format(active_ship.upgrades['HP'][1]) font "Font/segoeui.ttf" size 25 first_indent 790 line_spacing 22 color "#0a0a0a"
#                text "{}$".format(active_ship.upgrades['energy'][1]) font "Font/segoeui.ttf" size 25 first_indent 790 line_spacing 22 color "#0a0a0a"
#                text "{}$".format(active_ship.upgrades['engine'][1]) font "Font/segoeui.ttf" size 25 first_indent 790 line_spacing 22 color "#0a0a0a"
#                text "{}$".format(active_ship.upgrades['thrusters'][1]) font "Font/segoeui.ttf" size 25 first_indent 790 line_spacing 22 color "#0a0a0a"

screen store_missile:
    add "Menu/unionstore_missiles.png" xpos 1170 ypos 200

screen store_rocket:
    add "Menu/unionstore_rocket.png" xpos 1170 ypos 200