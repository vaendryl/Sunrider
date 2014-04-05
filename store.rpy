screen store_union:

    tag storyscreen

    imagebutton:
        xpos 1650 ypos 975
        action Jump("dispatch")
        idle "Menu/return.jpg"
        hover "Menu/return_hover.jpg"

    frame:
        xmaximum 1200
        xpos 50
        ypos 270
        background None

        vbox:

            imagebutton:
                action If(BM.money >= 500 and sunrider.rockets < 2,[SetField(BM,'money',(BM.money - 500)),SetField(sunrider,'rockets',sunrider.rockets + 1)])
                idle "Menu/store_item.png"
                hover "Menu/store_item_hover.png"
                hovered Show("store_rocket", transition=None)
                unhovered Hide("store_rocket", transition=None)

        vbox:
            text "Tactical nuclear warhead    [[owned:{!s}]".format(sunrider.rockets) font "Font/segoeui.ttf" size 25 first_indent 100 line_spacing 38 color "#0a0a0a"

        vbox:
            text "500" font "Font/segoeui.ttf" size 25 first_indent 900 line_spacing 38 color "#0a0a0a"

    text '{!s}$'.format(BM.money):
        size 50
        xpos 0.15
        ypos 0.7
        color '090'
        outlines [(1,'000',0,0)]

screen store_missile:
    add "Menu/unionstore_missiles.png" xpos 1170 ypos 200

screen store_rocket:
    add "Menu/unionstore_rocket.png" xpos 1170 ypos 200