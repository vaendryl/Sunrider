screen upgrade:

    default active_ship = sunrider
    $cost_increase = 1.5
    add "Menu/upgrade_back.jpg"

    if active_ship == sunrider:
        add "Menu/upgrade_sunrider.png"
    if active_ship == blackjack:
        add "Menu/upgrade_blackjack.png"
    if active_ship == liberty:
        add "Menu/upgrade_liberty.png"

    text '{!s}$'.format(BM.money):
        size 50
        xpos 0.15
        ypos 0.7
        color '090'
        outlines [(1,'000',0,0)]

    textbutton 'next unit':
        xpos 0.8
        ypos 0.1
        text_size 50
        text_color 'fff'
        text_outlines [(1,'000',0,0)]
        action If(active_ship == sunrider,
            SetScreenVariable('active_ship',blackjack),If(active_ship == blackjack,
                SetScreenVariable('active_ship',liberty),
                SetScreenVariable('active_ship',sunrider)))

    imagebutton:
        xpos 1650 ypos 975
        action Jump("dispatch")
        idle "Menu/return.jpg"
        hover "Menu/return_hover.jpg"

    vbox:
        area (40, 270, 1050, 440)

        viewport id "upgrade_list":
            draggable True
            mousewheel True
            scrollbars "vertical"
            child_size (1050,2000)

            vbox:

                add "Menu/upgrade_blank.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_blank.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_blank.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_blank.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_blank.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"
                add "Menu/upgrade_item.png"

            vbox:
                xpos 970
                add "Menu/upgrade_blank.png"
                $upgrade = active_ship.upgrades['HP']
                imagebutton:
                    action If(BM.money >= upgrade[1],
                        [SetDict(active_ship.upgrades,'HP',[upgrade[0]+1,int(upgrade[1]*cost_increase)]),
                            SetField(active_ship,'max_hp',active_ship.max_hp + 100),
                            SetField(BM,'money',BM.money-upgrade[1])])
                    idle "Menu/upgrade_button.png"
                    hover "Menu/upgrade_button_hover.png"

                $upgrade = active_ship.upgrades['energy']
                imagebutton:
                    action If(BM.money >= upgrade[1],
                        [SetDict(active_ship.upgrades,'energy',[upgrade[0]+1,int(upgrade[1]*cost_increase)]),
                            SetField(active_ship,'max_en',active_ship.max_en + 10),
                            SetField(BM,'money',BM.money-upgrade[1])])
                    idle "Menu/upgrade_button.png"
                    hover "Menu/upgrade_button_hover.png"

                $upgrade = active_ship.upgrades['engine']
                imagebutton:
                    action If(BM.money >= upgrade[1],
                        [SetDict(active_ship.upgrades,'engine',[upgrade[0]+1,int(upgrade[1]*cost_increase)]),
                            SetField(active_ship,'move_cost',active_ship.move_cost -1),
                            SetField(BM,'money',BM.money-upgrade[1])])
                    idle "Menu/upgrade_button.png"
                    hover "Menu/upgrade_button_hover.png"

                $upgrade = active_ship.upgrades['thrusters']
                imagebutton:
                    action If(BM.money >= upgrade[1],
                        [SetDict(active_ship.upgrades,'thrusters',[upgrade[0]+1,int(upgrade[1]*cost_increase)]),
                            SetField(active_ship,'evasion',active_ship.evasion + 1),
                            SetField(BM,'money',BM.money-upgrade[1])])
                    idle "Menu/upgrade_button.png"
                    hover "Menu/upgrade_button_hover.png"


            vbox:

                text "BASIC ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_leading 5 line_spacing 22 color "#0a0a0a"
                text "HULL PLATING" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "ENERGY REACTOR" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "ENGINE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "THRUSTERS" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"

                text "KINETIC ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   ACCURACY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   DAMAGE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   ENERGY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "LASER ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   ACCURACY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   DAMAGE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   ENERGY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "MISSILE ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   ACCURACY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   DAMAGE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   ENERGY" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "DEFENSES  ----------" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   SHIELD POWER" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   SHIELD RANGE" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   FLAK" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   ARMOR" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"
                text "   REPAIR CREW" font "Font/segoeui.ttf" size 25 first_indent 5 line_spacing 22 color "#0a0a0a"

            vbox:
                text "  " font "Font/segoeui.ttf" size 25 first_indent 470 line_leading 5 line_spacing 22 color "#0a0a0a"
                text "{!s} > {!s}".format(active_ship.max_hp,active_ship.max_hp+100) font "Font/segoeui.ttf" size 25 first_indent 470 line_spacing 22 color "#0a0a0a"
                text "{!s} > {!s}".format(active_ship.max_en,active_ship.max_en+10) font "Font/segoeui.ttf" size 25 first_indent 470 line_spacing 22 color "#0a0a0a"
                text "{!s} > {!s}".format(active_ship.move_cost,active_ship.move_cost-1) font "Font/segoeui.ttf" size 25 first_indent 470 line_spacing 22 color "#0a0a0a"
                text "{!s} > {!s}".format(active_ship.evasion,active_ship.evasion+1) font "Font/segoeui.ttf" size 25 first_indent 470 line_spacing 22 color "#0a0a0a"

            vbox:
                text "  " font "Font/segoeui.ttf" size 25 first_indent 710 line_leading 5 line_spacing 22 color "#0a0a0a"
                text "Lvl {}".format(active_ship.upgrades['HP'][0]) font "Font/segoeui.ttf" size 25 first_indent 710 line_spacing 22 color "#0a0a0a"
                text "Lvl {}".format(active_ship.upgrades['energy'][0]) font "Font/segoeui.ttf" size 25 first_indent 710 line_spacing 22 color "#0a0a0a"
                text "Lvl {}".format(active_ship.upgrades['engine'][0]) font "Font/segoeui.ttf" size 25 first_indent 710 line_spacing 22 color "#0a0a0a"
                text "Lvl {}".format(active_ship.upgrades['thrusters'][0]) font "Font/segoeui.ttf" size 25 first_indent 710 line_spacing 22 color "#0a0a0a"

            vbox:
                text "  " font "Font/segoeui.ttf" size 25 first_indent 790 line_leading 5 line_spacing 22 color "#0a0a0a"
                text "{}$".format(active_ship.upgrades['HP'][1]) font "Font/segoeui.ttf" size 25 first_indent 790 line_spacing 22 color "#0a0a0a"
                text "{}$".format(active_ship.upgrades['energy'][1]) font "Font/segoeui.ttf" size 25 first_indent 790 line_spacing 22 color "#0a0a0a"
                text "{}$".format(active_ship.upgrades['engine'][1]) font "Font/segoeui.ttf" size 25 first_indent 790 line_spacing 22 color "#0a0a0a"
                text "{}$".format(active_ship.upgrades['thrusters'][1]) font "Font/segoeui.ttf" size 25 first_indent 790 line_spacing 22 color "#0a0a0a"

screen store_missile:
    add "Menu/unionstore_missiles.png" xpos 1170 ypos 200

screen store_rocket:
    add "Menu/unionstore_rocket.png" xpos 1170 ypos 200