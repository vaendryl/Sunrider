screen store_union:
    modal True
    tag storyscreen


    $current_damage = store.sunrider_rocket.damage

    use store_info

    imagebutton: #return button
        xpos 0.05 ypos 0.8
        action [ SetField(BM,'hovered',None) , Jump("dispatch") ]
        idle "Menu/return.jpg"
        hover "Menu/return_hover.jpg"

    frame:
        xmaximum 800
        xpos 10
        ypos 270
        background None
        vbox:
            spacing 20
            imagebutton:
                action If(BM.money >= 300 and sunrider.rockets < 2,[SetField(BM,'money',(BM.money - 300)),SetField(sunrider,'rockets',sunrider.rockets + 1)])
                idle "Menu/store_item.png"
                hover "Menu/store_item_hover.png"
                hovered SetField(BM,'hovered','Rockets')
                unhovered SetField(BM,'hovered',None)
            if current_damage < 1200:
                imagebutton:
                    action If(BM.money >= 2000,[ SetField(BM,'money',(BM.money - 2000)),SetField(store.sunrider_rocket,'damage',1200) ])
                    idle "Menu/store_item.png"
                    hover "Menu/store_item_hover.png"
                    hovered SetField(BM,'hovered','Rocketupgrade1')
                    unhovered SetField(BM,'hovered',None)
            if sunrider.repair_drones != None:
                imagebutton:
                    action If(BM.money >= 400 and sunrider.repair_drones < 8,[ SetField(BM,'money',(BM.money - 400)),SetField(sunrider,'repair_drones',sunrider.repair_drones + 1) ])
                    idle "Menu/store_item.png"
                    hover "Menu/store_item_hover.png"
                    hovered SetField(BM,'hovered','repair drones')
                    unhovered SetField(BM,'hovered',None)
        vbox:
            text "Warhead Ammo    [[owned:{!s}]".format(sunrider.rockets) font "Font/sui generis rg.ttf" size 30 first_indent 50 line_spacing 38 color "#0a0a0a"
            if current_damage < 1200:
                text "Quantum Torpedo License" font "Font/sui generis rg.ttf" size 30 first_indent 50 line_spacing 38 color "#0a0a0a"
            if sunrider.repair_drones != None:
                text "Repair Drones [[owned:{!s}]".format(sunrider.repair_drones) font "Font/sui generis rg.ttf" size 30 first_indent 50 line_spacing 38 color "#0a0a0a"
        vbox:
            text "300" font "Font/sui generis rg.ttf" size 30 first_indent 710 line_spacing 38 color "#0a0a0a"
            if current_damage < 1200:
                text "2000" font "Font/sui generis rg.ttf" size 30 first_indent 710 line_spacing 38 color "#0a0a0a"
            if sunrider.repair_drones != None:
                text "400" font "Font/sui generis rg.ttf" size 30 first_indent 710 line_spacing 38 color "#0a0a0a"

    text '{!s}$'.format(BM.money):
        size 50
        xpos 0.15
        ypos 0.7
        color '090'
        outlines [(1,'000',0,0)]

screen store_info:
    zorder 10

    frame:
        xmaximum 600
        background None
        xpos 0.5
        ypos 0.2
        if BM.hovered == 'Rockets':
#            $ damage = sunrider.weapons[3].damage
            text 'Warhead Ammo' xpos 50 ypos 50 size 35 font "Font/sui generis rg.ttf" color '000' 
            text 'Purchase warheads to allow the Sunrider to fire powerful rockets at the enemy. A rocket deals {} damage, but can be shot down by enemy flak. The Sunrider can carry a maximum of 2 at a time.'.format(sunrider.weapons[3].damage) xpos 50 ypos 150 size 20 font "Font/GOTHIC.TTF" color '000'
        elif BM.hovered == 'Rocketupgrade1':
            text 'Quantum Torpedo License' xpos 50 ypos 50 size 35 font "Font/sui generis rg.ttf" color '000'
            text 'While the proliferation of nuclear warheads throughout the galaxy has made them readily available, more powerful weapons are regulated closely by the Alliance. With the payment of appropriate fees, the Union can replace your current stock of nuclear warheads with quantum warheads, permanently increasing the Sunrider\'s rocket damage to 1200.' xpos 50 ypos 150 size 20 font "Font/GOTHIC.TTF" color '000'
        elif BM.hovered == 'repair drones':
            text 'Repair Drones' xpos 50 ypos 50 size 35 font "Font/sui generis rg.ttf" color '000'
            text 'These autonomous robots can rapidly restore destroyed hull sections as well as complex electronic systems. They are a must have for all hostile operations.  Restores 50% of the Sunrider\'s HP on use. The Sunrider can carry a maximum of 8 at a time.' xpos 50 ypos 150 size 20 font "Font/GOTHIC.TTF" color '000'



screen store_missile:
    add "Menu/unionstore_missiles.png" xpos 1170 ypos 200

screen store_rocket:
    add "Menu/unionstore_rocket.png" xpos 1170 ypos 200