## this module creates custom screens. I prefer not to clutter the ren'py
## default screens.rpy module as it's pretty full already

## 0) transforms
## 1) status screens
## 2) battle map
## 3) command menu

init -2:  ##0) transforms
#    $import random

    transform hoverglow(img1):  #makes units glow when you mouseover
        im.MatrixColor(img1,im.matrix.brightness(.05))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.15))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.05))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.0))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.05))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.15))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.05))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(0.0))
        pause 0.1
        repeat

    transform vanguard_cannon:
        crop (0,0,0,int(200 / zoomlevel))
        easeout 1 crop (0,0,1344 / zoomlevel,200 / zoomlevel)

    transform buffup(xx):
        ypos xx
        alpha 1

        parallel:
            linear 1 ypos int(xx-190*zoomlevel)
        parallel:
            time 0.5
            linear 0.5 alpha 0

    transform cursedown(xx):
        ypos xx
        alpha 1

        parallel:
            linear 1 ypos int(xx+190*zoomlevel)
        parallel:
            time 0.5
            linear 0.5 alpha 0

    transform movebutton: #used to make it look cool when you click Move
        zoom zoomlevel
        alpha 0.5
        on start:
            alpha 0.5
        on hover:
            linear 0.3 alpha 1.0
        on idle:
            linear 0.5 alpha 0.5

    transform zoom_button(xx,yy=1):
        zoom xx
        alpha yy

    transform move_ship(x1,y1,x2,y2,speed=0.45):
        on start:
            xpos x1 ypos y1
            linear speed xpos x2 ypos y2

screen battle_screen:
    tag tactical
    modal False
    zorder -5
    if BM.moving == False:
        key "mousedown_4" action Return(["zoom", "in"])    #scroll in and out
        key "mousedown_5" action Return(["zoom", "out"])
        key "K_PAGEUP" action Return(["zoom", "in"])
        key "K_PAGEDOWN" action Return(["zoom", "out"])
        if 'mouseup_2' not in config.keymap['hide_windows']:
            key "mousedown_2" action Return("next ship")
        if 'mouseup_3' not in config.keymap['game_menu']:
            key "mousedown_3" action Return("deselect")
        key "]" action Return("next ship")
        key "[" action Return("previous ship")
    else:
        timer 0.5 repeat True action Return(['timer',0])   #this is used when a ship is moving from grid to grid

    if config.developer: #a release version should have set this to False
        key "Q" action Jump('quit')  ##DEBUG FAST QUIT##
        key "A" action Return('anime')
        key "P" action Return('I WIN')

    $childx = round(3840*zoomlevel) #this makes it so you can't scroll past the edge of the battlefield when zoomed out
    $childy = round(2160*zoomlevel)


    add BM.battle_bg xalign 0.5 yalign 0.5 #zoom 0.5 ##background for the battlefield##

    viewport id "grid":
        xmaximum 1920
        ymaximum 1080
        xadjustment BM.xadj
        yadjustment BM.yadj
        child_size (childx,childy)
        draggable BM.draggable
        mousewheel False
        edgescroll BM.edgescroll #(0,0) #(70,400*zoomlevel)

                ##CREATE GRID##
        for a in range(1,GRID_SIZE[1]+2):
            $ yposition = a * int((120 * zoomlevel))
            $ xposition = int((192 * zoomlevel))
            $ xmax = 18 * int((192 * zoomlevel))
            add "Battle UI/grid horizontal.jpg":
                ypos yposition
                xpos xposition
                size (xmax,4)
                alpha 0.4
        for a in range(1,GRID_SIZE[0]+2):
            $ xposition = a * int((192 * zoomlevel))
            $ yposition = int((120 * zoomlevel))
            $ ymax = 16 * int((120 * zoomlevel))
            add "Battle UI/grid vertical.jpg":
                xpos xposition
                ypos yposition
                size (4,ymax)
                alpha 0.4


          ##display shield and flak ranges

        if not BM.hovered == None: #when you hover over a ship
            if BM.hovered.shield_generation > 0:
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                    for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                        if get_distance(BM.hovered.location,(a,b)) <= BM.hovered.shield_range:
                            $xposition = a * int(192 * zoomlevel)
                            $yposition = b * int(120 * zoomlevel)
                            $xsize = int(196 * zoomlevel)
                            $ysize = int(124 * zoomlevel)
                            add "Battle UI/blue square.png":
                                xpos xposition
                                ypos yposition
                                size (xsize,ysize)
                                alpha 0.7
            if BM.hovered.flak > 0:
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                    for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                        if get_distance(BM.hovered.location,(a,b)) <= BM.hovered.flak_range:
                            $xposition = (a * int(192 * zoomlevel)) + int(4*zoomlevel)
                            $yposition = (b * int(120 * zoomlevel)) + int(4*zoomlevel)
                            $xsize = int(188 * zoomlevel)
                            $ysize = int(116 * zoomlevel)
                            add "Battle UI/red square.png":
                                xpos xposition
                                ypos yposition
                                size (xsize,ysize)
                                alpha 0.9

        if not BM.weaponhover == None: #when you hover over a weapon button
            if BM.weaponhover.wtype == 'Missile' or BM.weaponhover.wtype == 'Rocket':
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                        for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                            for ship in enemy_ships:
                                if get_distance(ship.location,(a,b)) <= ship.flak_range:
                                    $xposition = (a * int(192 * zoomlevel)) + int(4*zoomlevel)
                                    $yposition = (b * int(120 * zoomlevel)) + int(4*zoomlevel)
                                    $xsize = int(188 * zoomlevel)
                                    $ysize = int(116 * zoomlevel)
                                    add "Battle UI/red square.png":
                                        xpos xposition
                                        ypos yposition
                                        size (xsize,ysize)
                                        alpha 0.9
            if BM.weaponhover.wtype == 'Laser' or BM.weaponhover.wtype == 'Pulse':
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                        for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                            for ship in enemy_ships:
                                if get_distance(ship.location,(a,b)) <= ship.shield_range:
                                    $xposition = a * int(192 * zoomlevel)
                                    $yposition = b * int(120 * zoomlevel)
                                    $xsize = int(196 * zoomlevel)
                                    $ysize = int(124 * zoomlevel)
                                    add "Battle UI/blue square.png":
                                        xpos xposition
                                        ypos yposition
                                        size (xsize,ysize)
                                        alpha 0.7

                ## DISPLAY COVER ##
        for cover in BM.covers:
            $xposition = int((cover.location[0]+0.5) * 192 * zoomlevel)
            $yposition = int((cover.location[1]+0.5) * 120 * zoomlevel)
            $xsize = int(210 * zoomlevel)
            $ysize = int(120 * zoomlevel)
            add cover.label:
                xanchor 0.5
                yanchor 0.5
                xpos xposition
                ypos yposition
                size (xsize,ysize)
                at Transform(cover.label,rotate = cover.angle)



                ## DISPLAY SHIP AVATARS ##

          ## cycling through every cell in the grid in order is required so that units
          ## do not overlap units below them making things look weird.
        for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
            for b in range(1,GRID_SIZE[1]+1):  #cycle through columns

                  ##first display the coloured bases that go beneath the units
                for ship in BM.ships: #cycle through every ship in the battle
                    if ship.location == (a,b):
                          ##first we show the circle base below every unit
                        $xposition = int((ship.location[0]+0.5) * 192 * zoomlevel)
                        $yposition = int((ship.location[1]+0.5) * 120 * zoomlevel)
                        $xsize = int(210 * zoomlevel)
                        $ysize = int(120 * zoomlevel)
                        if ship.faction == 'Player':
                            add "Battle UI/player base.png":
                                xanchor 0.5
                                yanchor 0.5
                                xpos xposition
                                ypos yposition
                                size (xsize,ysize)
                        if ship.faction == 'PACT':
                            add "Battle UI/pact_base.png":
                                xanchor 0.5
                                yanchor 0.5
                                xpos xposition
                                ypos yposition
                                size (xsize,ysize)
                        if ship.faction == 'Pirate':
                            add "Battle UI/pirate_base.png":
                                xanchor 0.5
                                yanchor 0.5
                                xpos xposition
                                ypos yposition
                                size (xsize,ysize)

                        $cell_width = 1920 / ((GRID_SIZE[0]+2)/2)
                        $cell_height = 1080 / ((GRID_SIZE[1]+2)/2)

                        #calculate the position of the ships on the field
                        $xposition = int((ship.location[0]+0.5) * cell_width * zoomlevel)
                        $yposition = int((ship.location[1]+0.25) * cell_height * zoomlevel)

                        if ship.getting_buff:  #used if you buff someone
                            add 'Battle UI/buff_back.png':
                                xpos int(xposition-(cell_width/2)*zoomlevel)
                                zoom (zoomlevel/2.0)
                                at buffup(yposition)

                        if ship.getting_curse:  #used if you curse someone
                            add 'Battle UI/curse_back.png':
                                xpos int(xposition-(cell_width/2)*zoomlevel)
                                zoom (zoomlevel/2.0)
                                at cursedown(yposition-(190)*zoomlevel)

                        #default values
                        $mode = '' #default
                        $act = Return(['selection',ship])
                        $lbl = ship.lbl
                        $hvr = hoverglow(ship.lbl)
                        $hvrd = SetField(BM,'hovered',ship)
                        $unhvrd = SetField(BM,'hovered',None)

                        #some properties of the imagebutton representing a ship change depending on circumstances
                        if ship.faction == 'Player':
                            #by default player ships can be selected, which the above values are already set to.

                            if BM.targetingmode:
                                #you cannot target yourself with an active weapon
                                $ mode = 'offline'

                                if BM.active_weapon.wtype == 'Support':
                                    #except when the active weapon is a support skill. in that case, player ships become targets
                                    $ mode = 'target'

                        else: #ship is an enemy faction
                            #by default enemy ships can be selected (to view stat details), which the above values are already set to.

                            if BM.targetingmode:
                                #with an active weapon selected enemies become targets
                                $ mode = 'target'

                                if BM.active_weapon.wtype == 'Melee' and (ship.stype != 'Ryder' or get_ship_distance(BM.selected,ship) != 1):
                                    #except when the active weapon is melee and this enemy is neither a ryder nor next to the attacking ship
                                    $ mode = 'offline'

                                if BM.active_weapon.name == 'Gravity Gun':
                                    #the gravity gun is a special type weapon
                                    if ship.stype != 'Ryder':
                                        $ mode = 'offline'

                        if mode == 'target':
                            $ lbl = hoverglow(ship.lbl)
                            $ hvr = im.MatrixColor(ship.lbl,im.matrix.brightness(0.2))
                        elif mode == 'offline':
                            $ act = NullAction()
                            $ hvr = im.MatrixColor(ship.lbl,im.matrix.brightness(-0.3))
                            $ lbl = hvr

                        imagebutton:
                            xanchor 0.5
                            yanchor 0.5
                            xpos xposition
                            ypos yposition
                            action act
                            idle lbl
                            hover hvr
                            hovered hvrd
                            unhovered unhvrd
                            focus_mask True
                            at zoom_button(zoomlevel/2.5)

                        if ship.fireing_flak:
                            add 'Battle UI/warning icon.png':
                                xanchor 0.5
                                yanchor 0.5
                                xpos xposition
                                ypos yposition
                                zoom (zoomlevel/2.5)
                                alpha 0.8

                        if ship.getting_buff:
                            add 'Battle UI/buff_front.png':
                                xpos int(xposition-96*zoomlevel)
                                zoom (zoomlevel/2.0)
                                at buffup(int(yposition+50*zoomlevel))

                        if ship.getting_curse:
                            add 'Battle UI/curse_front.png':
                                xpos int(xposition-96*zoomlevel)
                                zoom (zoomlevel/2.0)
                                at cursedown(yposition-(190-50)*zoomlevel)

                          ##add the HP bar and the EN bar
                        if ship.faction == 'Player':
                            $xposition = int((ship.location[0]+0.08) * 192 * zoomlevel)
                            $yposition = int((ship.location[1]+0.66) * 120 * zoomlevel)
                            $hp_size = int(405*(float(ship.hp)/ship.max_hp))
                            add 'Battle UI/label hp bar.png':
                                xpos xposition
                                ypos yposition
                                zoom (zoomlevel/2.5)
                                crop (0,0,hp_size,79)

#                            text str(ship.hp):
#                                xpos (xposition+60*zoomlevel)
#                                ypos (yposition+30*zoomlevel)
#                                size int(30 * zoomlevel)

                            $xposition = int((ship.location[0]+0.08) * 192 * zoomlevel)
                            $yposition = int((ship.location[1]+0.72) * 120 * zoomlevel)
                            $energy_size = int(405*(float(ship.en)/ship.max_en))
                            add 'Battle UI/label energy bar.png':
                                xpos xposition
                                ypos yposition
                                zoom (zoomlevel/2.5)
                                crop (0,0,energy_size,79)

                        else:    #enemies

                            $xposition = int((ship.location[0]+0.09) * 192 * zoomlevel)
                            $yposition = int((ship.location[1]+0.70) * 120 * zoomlevel)
                            $hp_size = int(405*(float(ship.hp)/ship.max_hp))
                            add 'Battle UI/label hp bar.png':
                                xpos xposition
                                ypos yposition
                                zoom (zoomlevel/2.5)
                                crop (0,0,hp_size,90)

                            text str(ship.hp):
                                xanchor 0.5
                                yanchor 0.5
                                xpos int(xposition+80*zoomlevel)
                                ypos int(yposition+27*zoomlevel)
                                size int(16*zoomlevel)
                                font "Font/sui generis rg.ttf"
                                outlines [(2,'000',0,0)]




          ##show missiles on the map that are currently flying in space##
        if len(BM.missiles) > 0:
            for missile in BM.missiles:
                $xposition = int((missile.location[0]+0.5) * 192 * zoomlevel)
                $yposition = int((missile.location[1]+0.25) * 120 * zoomlevel)
                $next_xposition = int((missile.next_location[0]+0.5) * 192 * zoomlevel)
                $next_yposition = int((missile.next_location[1]+0.25) * 120 * zoomlevel)
                add missile.lbl:
                    at move_ship(xposition,yposition,next_xposition,next_yposition,0.1)
                    xanchor 0.5
                    yanchor 0.5
                    zoom (zoomlevel/4.0)
                text str(missile.shot_count):
                    at move_ship(xposition,yposition,next_xposition,next_yposition,0.1)
                    xanchor 0.5
                    yanchor 0.5
                    size (20/zoomlevel)
                    outlines [(1,'000',0,0)]

##targeting window##

          ##if targeting mode is active show a targeting window over all enemy_ships that gives you chance to hit and other data
          ##loop again to show the targeting window. this way other ships don't overlap with it.
        if not BM.weaponhover == None or BM.targetingmode:

              #the looping is NEEDED to counter overlap problems. it sucks, I know. I wish I could set zorder to individual images
            for a in range(1,GRID_SIZE[0]+1):
                for b in range(1,GRID_SIZE[1]+1):
                    for ship in BM.ships:

                        if BM.weaponhover == None:
                            $BM.weaponhover = BM.active_weapon
                        if BM.weaponhover.wtype == 'Support' and ship.faction != 'Player':
                            $continue
                        if BM.weaponhover.wtype != 'Support' and ship.faction == 'Player':
                            $continue
                        if BM.weaponhover.wtype == 'Melee' and (ship.stype != 'Ryder' or get_ship_distance(ship,BM.selected) > 1):
                            $continue
                        if BM.weaponhover.name == 'Gravity Gun' and ship.stype != 'Ryder':
                            $continue


                        if ship.location == (a,b):
                            $xposition = int((ship.location[0]+0.75) * 192 * zoomlevel)
                            $yposition = int((ship.location[1]+0.15) * 120 * zoomlevel)
                            add 'Battle UI/targeting_window.png':
                                xpos xposition
                                ypos yposition
                                xanchor 0.5
                                yanchor 0.5
                                zoom (zoomlevel/1.3)
                            $xposition = int((ship.location[0]+0.92) * 192 * zoomlevel)
                            $yposition = int((ship.location[1]+0.2) * 120 * zoomlevel)
                            text (str(ship.cth) + '%'):
                                xpos xposition
                                ypos yposition
                                xanchor 0.5
                                yanchor 0.5
                                size (20 * zoomlevel)
                                color '000'
                            $xposition = int((ship.location[0]+0.75) * 192 * zoomlevel)
                            $yposition = int((ship.location[1]+0.4) * 120 * zoomlevel)
                            text str(ship.flak):
                                xpos xposition
                                ypos yposition
                                xanchor 1.0
                                yanchor 0.5
                                size (14 * zoomlevel)
                                color 'fff'
                            $xposition = int((ship.location[0]+0.92) * 192 * zoomlevel)
                            $yposition = int((ship.location[1]+0.4) * 120 * zoomlevel)
                            text str(ship.shields):
                                xpos xposition
                                ypos yposition
                                xanchor 1.0
                                yanchor 0.5
                                size (14 * zoomlevel)
                                color 'fff'
                            $xposition = int((ship.location[0]+1.0) * 192 * zoomlevel)
                            $yposition = int((ship.location[1]+0.4) * 120 * zoomlevel)
                              ##when you hover over a weapon that does kinetic or assault type damage it shows you armor is double as effective
                            if BM.weaponhover == None:
                                $weapon = BM.active_weapon
                            else:
                                $weapon = BM.weaponhover
                            if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
                                text (str(ship.armor) + 'x2'):
                                    xpos xposition
                                    ypos yposition
                                    xanchor 0.0
                                    yanchor 0.5
                                    size (12 * zoomlevel)
                                    color 'fff'
                            else:
                                text str(ship.armor):
                                    xpos xposition
                                    ypos yposition
                                    xanchor 0.0
                                    yanchor 0.5
                                    size (14 * zoomlevel)
                                    color 'fff'




                ##DISPLAY MOVEMENT OPTIONS##
        if BM.selectedmode and BM.selected.faction == 'Player' and not BM.targetingmode:
            for tile in BM.selected.movement_tiles:

                imagebutton:
                    at movebutton
                    idle 'Battle UI/move_tile.png'
                    hover 'Battle UI/move_tile.png'
                    xanchor 0.5
                    yanchor 0.5
                    xpos tile[0]
                    ypos tile[1]
                    action Return(['move',(tile[3],tile[4])])
                    alternate Return("deselect")

                text (str(BM.selected.move_cost*tile[2]) + ' EN'):
                    xpos tile[0]
                    ypos tile[1]
                    xanchor 0.5
                    yanchor 0.5
                    size (20 * zoomlevel)


          #firing the vanguard cannon
        if BM.vanguard:
            $xposition = int((sunrider.location[0]+0.5) * 192 * zoomlevel)
            $yposition = int((sunrider.location[1]) * 120 * zoomlevel)
            add 'Battle UI/vanguard beam wave.png':
                xanchor 0.0
                yanchor 0.27
                xpos int(xposition+100/zoomlevel)
                ypos yposition
                size (int(1344/zoomlevel),int(120/zoomlevel))
                at vanguard_cannon
                alpha 1.0

            ##MOVE SHIP FROM GRID TO GRID##
        if BM.moving:
            $xposition = int((BM.selected.current_location[0]+0.5) * 192 * zoomlevel)
            $yposition = int((BM.selected.current_location[1]+0.25) * 120 * zoomlevel)
            $next_xposition = int((BM.selected.next_location[0]+0.5) * 192 * zoomlevel)
            $next_yposition = int((BM.selected.next_location[1]+0.25) * 120 * zoomlevel)

            add BM.selected.lbl:
                at move_ship(xposition,yposition,next_xposition,next_yposition)
                xanchor 0.5
                yanchor 0.5
                zoom (zoomlevel/2.5)

    if config.developer:
        vbox:
            ypos 50
            xalign 1.0
            textbutton "Debug Cheats" action Return('cheat')
            textbutton "Fast Quit" xalign 1.0 action Jump('quit')

    if BM.edgescroll == (0,0):
        vbox:
            xalign 1.0
            textbutton "enable edgescroll" action SetField(BM,'edgescroll',(100,800*zoomlevel))
    else:
        vbox:
            xalign 1.0
            textbutton "disable edgescroll" action SetField(BM,'edgescroll',(0,0))

    if not BM.showing_orders and not BM.order_used:
        imagebutton:
            xpos 0
            ypos 0
            idle 'Battle UI/commandbar.png'
            hover hoverglow('Battle UI/commandbar.png')
            action [SetField(BM,'showing_orders',True),Show('orders')]
        text '{!s}'.format(BM.cmd):
            xanchor 1.0
            xpos 165
            ypos 10
            size 30
            color 'fff'
            outlines [(1,'000',0,0)]

    $endturnbutton_idle = im.MatrixColor('Battle UI/button_endturn.png',im.matrix.tint(0.6, 1.0, 0.5))
    for ship in player_ships:
        if ship.en >= ship.max_en:
            $endturnbutton_idle = im.MatrixColor('Battle UI/button_endturn.png',im.matrix.tint(1.0, 0.6, 0.5))

    imagebutton:
        xpos 90
        yalign 1.0
        idle endturnbutton_idle
        hover hoverglow(endturnbutton_idle)
        action Return('endturn')

transform move_down(ystart,yend,xx=0):
    xpos xx
    ypos ystart
    linear 0.5 ypos yend
    on hide:
        linear 0.5 ypos ystart
          #not sure why this is needed. I'm calling bug in renpy
        time 2
        alpha 0



screen orders:
    zorder 1
    modal True

    frame:
        background 'Battle UI/commandbar_window.png'
        at move_down(-590,0)
        vbox:
            spacing 20
            for order in BM.orders:
                button:
                    xpos 20
#                    insensitive_background im.MatrixColor('Battle UI/commandbar_button.png',im.matrix.brightness(-0.50))
                    idle_background 'Battle UI/commandbar_button.png'
                    hover_background hoverglow('Battle UI/commandbar_button.png')
                    action [Return(order),Hide('orders'),SetField(BM,'showing_orders',False),SetField(BM,'order_used',True)]
#                    action If(BM.cmd >= BM.orders[order][1],[Return(order),Hide('orders'),SetField(BM,'showing_orders',False)])

                    has hbox

                    text order:
                        ypos 5
                        min_width 300
                        size 22
                        outlines [(1,'222',0,0)]
                    text str(BM.orders[order][0]):
                        ypos 5
                        xpos 50
                        min_width 50
                        text_align 1.0
                        size 18
                        outlines [(1,'222',0,0)]

    imagebutton:
            at move_down(0,590)
            idle 'Battle UI/commandbar.png'
            hover hoverglow('Battle UI/commandbar.png')
            action [Hide('orders'),SetField(BM,'showing_orders',False)]
    text '{!s}'.format(BM.cmd):
        xanchor 1.0
        xpos 165
        ypos 10
        at move_down(10,600,165)
        size 30
        color 'fff'
        outlines [(1,'000',0,0)]


screen commands: ##show the weapon buttons etc##
    zorder 1 #always show on top of the battle screen

        ##show status window and it's data
    if not BM.selected == None:
        add 'Battle UI/statuswindow.png' xalign 1.0 yalign 1.0
        if not BM.selected.portrait == None:
            add BM.selected.portrait xalign 1.0 yalign 1.0
        else:
            text BM.selected.name xanchor 1.0 xpos 1880 ypos 726 outlines [(1,'000',0,0)]
        $hp_size = int(374*(float(BM.selected.hp)/BM.selected.max_hp))
        $en_size = int(298*(float(BM.selected.en)/BM.selected.max_en))
        add 'Battle UI/status window_HP.png' xpos 1080 ypos 779 crop (0,0,hp_size,49)
        add 'Battle UI/status window_EN.png' xpos 1133 ypos 805 crop (0,0,en_size,19)
        text (str(BM.selected.hp) + '/' + str(BM.selected.max_hp)) xanchor 0.5 xpos 1510 ypos 779 size 19 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]
        text (str(BM.selected.en) + '/' + str(BM.selected.max_en)) xanchor 0.5 xpos 1490 ypos 805 size 19 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]
        text (str(BM.selected.flak)) xanchor 1.0 xpos 1149 ypos 847 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]
        text (str(BM.selected.shields)) xanchor 1.0 xpos 1149 ypos 897 size 24 font "Font/sui generis rg.ttf" outlines [(1,BM.selected.shield_color,0,0)]
        text (str(BM.selected.armor)) xanchor 1.0 xpos 1149 ypos 947 size 24 font "Font/sui generis rg.ttf" outlines [(1,BM.selected.armor_color,0,0)]
        text (str(BM.selected.evasion)) xanchor 1.0 xpos 1149 ypos 997 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]

        ##show weapon stats in status window on hover
        if not BM.weaponhover == None or not BM.active_weapon == None:
            if BM.weaponhover == None:
                $weapon = BM.active_weapon
            else:
                $weapon = BM.weaponhover
            text (str(weapon.damage)) xanchor 1.0 xpos 1380 ypos 840 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]
            text (str(weapon.damage*weapon.shot_count)) xanchor 1.0 xpos 1380 ypos 870 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]
            text (str(weapon.shot_count)) xanchor 1.0 xpos 1515 ypos 840 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]

        ##show buffs
        $count = 0
        for modifier in BM.selected.modifiers:
            if BM.selected.modifiers[modifier][0] != 0:
                text modifier xpos 1217 ypos (922+count*24) size 20 outlines [(1,'000',0,0)]
                if BM.selected.modifiers[modifier][0] > 0:
                    $ status_effect = '+{}% for {} turns'.format(BM.selected.modifiers[modifier][0],BM.selected.modifiers[modifier][1])
                else:
                    $ status_effect = '{}% for {} turns'.format(BM.selected.modifiers[modifier][0],BM.selected.modifiers[modifier][1])
                text status_effect xanchor 1.0 xpos 1554 ypos (922+count*24) size 19 outlines [(1,'000',0,0)]
                $count += 1

        ##show weapon buttons
        if BM.selected.faction == 'Player':
            add 'Battle UI/button_arc.png' xalign 0.0 yalign 1.0
            $count = 0
            for weapon in BM.selected.weapons:
                if count < 4:
                    $x_offset = 8
                    $y_offset = 690
                else:
                    $x_offset = -353
                    $y_offset = 345

                #calculate the cost of this weapon based off of upgrades
                $ energy_cost = -weapon.energy_use
                if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
                    $ energy_cost = int(-weapon.energy_use * BM.selected.kinetic_cost)
                if weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
                    $ energy_cost = int(-weapon.energy_use * BM.selected.energy_cost)
                if weapon.wtype == 'Missile' or weapon.wtype == 'Rocket':
                    $ energy_cost = int(-weapon.energy_use * BM.selected.missile_cost)
                if weapon.wtype == 'Melee':
                    $ energy_cost = int(-weapon.energy_use * BM.selected.melee_cost)

                #check if this weapon can be fired right now
                $can_fire = BM.selected.en >= -energy_cost
                if weapon.uses_missiles:
                    $ can_fire = can_fire and weapon.ammo_use <= BM.selected.missiles
                if weapon.uses_rockets:
                    $ can_fire = can_fire and weapon.ammo_use <= BM.selected.rockets

                #default behaviour
                $ lbl = weapon.lbl
                $ hvr = hoverglow(weapon.lbl)
                $ act = If(can_fire,Return(['weapon_fire',weapon]))
                $ hvrd = Return(['hover',weapon])
                $ unhvrd = SetField(BM,'weaponhover',None)
                $ insens = im.MatrixColor(weapon.lbl,im.matrix.brightness(-0.50))

                #the behavior of the imagebutton (representing a weapon) changes depending on various circumstances
                if BM.targetingmode: #you are selecting a target to attack or use a support skill on.
                    if BM.active_weapon == weapon:
                        $ lbl = hoverglow(weapon.lbl)
                        $ hvr = im.MatrixColor(weapon.lbl,im.matrix.brightness(0.2))
                        $ act = [SetField(BM,'targetingmode',False),SetField(BM,'active_weapon',None)]
                    else:
                        $ lbl = im.MatrixColor(weapon.lbl,im.matrix.brightness(-0.50))
                        $ hvr = lbl
                        $ hvrd = None
                        $ act = NullAction()

                imagebutton:
                        insensitive insens
                        xpos (x_offset+120*count)
                        ypos (y_offset+69*count)
                        idle lbl
                        hover hvr
                        action act
                        hovered hvrd
                        unhovered unhvrd

                  ##show energy cost of weapon on weaponbutton
                text str(energy_cost) + 'EN':
                    xanchor 0.5
                    yanchor 0.5
                    xpos (x_offset+80+120*count)
                    ypos (y_offset+95+69*count)
                    size 20
                    font "Font/sui generis rg.ttf"
                    outlines [(1,'000',0,0)]
                  ##show ammo available and max_ammo
                if weapon.uses_missiles:
                    text '[[{!s}/{!s}]'.format(BM.selected.missiles,BM.selected.max_missiles):
                        xanchor 0.5
                        yanchor 0.5
                        xpos (x_offset+80+120*count)
                        ypos (y_offset+40+69*count)
                        size 20
                        font "Font/sui generis rg.ttf"
                        outlines [(1,'000',0,0)]
                if weapon.uses_rockets:
                    text '[[{!s}/{!s}]'.format(BM.selected.rockets,BM.selected.max_rockets):
                        xanchor 0.5
                        yanchor 0.5
                        xpos (x_offset+80+120*count)
                        ypos (y_offset+40+69*count)
                        size 20
                        font "Font/sui generis rg.ttf"
                        outlines [(1,'000',0,0)]

                $count += 1


transform hp_falls(hp_size1,hp_size2):
    crop (0,0,hp_size1,42)
    linear 1 crop (0,0,hp_size2,42)

transform float_up:
    xpos 0.5
    ypos 0.5
    linear 3 ypos 0.2 alpha 0


screen animation_hp:
    zorder 2
    default damage_delay = 1.0
    timer damage_delay action [Hide('animation_hp'),Show('animation_hp2')]

    add 'Battle UI/dmgstatus.png':
        xalign 1.0

    $hp_size1 = int(409*(float(BM.target.hp)/BM.target.max_hp))
    add 'Battle UI/dmgstatus_bar.png':
        xpos 1340
        ypos 3
        crop (0,0,hp_size1,42)
    text 'HP: {!s}/{!s}'.format(BM.target.hp,BM.target.max_hp):
        xpos 1750
        ypos 8
        size 19
        color 'fff'

screen animation_hp2:
    zorder 3

    add 'Battle UI/dmgstatus.png':
        xalign 1.0

    if store.damage == 'miss':
        $damage = 0
    else:
        $damage = store.damage
    $hp_size1 = int(409*(float(BM.target.hp)/BM.target.max_hp))
    $hp_size2 = int(409*(float(BM.target.hp-damage)/BM.target.max_hp))

    add 'Battle UI/dmgstatus_bar.png':
        xpos 1340
        ypos 3
        at hp_falls(hp_size1,hp_size2)

    text 'HP: {!s}/{!s}'.format((BM.target.hp-damage),BM.target.max_hp):
        xpos 1750
        ypos 8
        size 19
        color 'fff'
    text '{!s}'.format(damage):
        xanchor 1.0
        xpos 1670
        ypos 45
        size 40
        color '800'
        outlines [(1,'fff',0,0)]
    text '{!s}'.format(store.hit_count):
        xanchor 1.0
        xpos 1780
        ypos 45
        size 40
        color '800'
        outlines [(1,'fff',0,0)]
    text '{!s}'.format(-damage):
        xanchor 0.5
        at float_up
        size 30
        color '800'
        outlines [(1,'fff',0,0)]

    vbox:
        xalign 1.0
        ypos 0.2

        if store.total_armor_negation > 0:
            text 'armor negated {} damage'.format(int(store.total_armor_negation)):
                xalign 1.0
                size 22
                color 'fff'
                outlines [(1,'000',0,0)]
        if store.total_shield_negation > 0:
            text 'shields negated {} damage'.format(int(store.total_shield_negation)):
                xalign 1.0
                size 22
                color 'fff'
                outlines [(1,'000',0,0)]

transform victory_tf(xx,wait):
    alpha 0
    ypos 0
    xpos (xx+500)
    zoom 20
    time wait
    linear 0.5 alpha 1 xpos xx ypos 242 zoom 1
    time (1+wait)
    linear 0.5 ypos -100 alpha 0

screen victory:
#    modal True
    $word = 'Victory!'
    $wait = 0.2
    $xx = 750

    add Solid((0,0,0,200))

    for letter in word:
        text letter:
            xanchor 0.5
            size 150
            color 'fff'
            outlines [(4,'000',0,0)]
            at victory_tf(xx,wait)

        $wait += 0.2
        $xx += 75

transform victory_ships(xx,wait,zz):
    alpha 0
    ypos 0
    xpos (xx+500)
    zoom 20
    time wait
    linear 0.5 alpha 1 xpos xx ypos 350 zoom zz

transform delay_text(wait):
    alpha 0
    time wait
    linear 1 alpha 1

screen victory2:
    modal True
    $wait = 0.2
    $xx = 200
    $store.total_money = 0
    $store.repair_cost = 0

    add Solid((0,0,0,200))

    textbutton 'Continue':
        xalign 0.5
        ypos 0.8
        text_size 30
        action Hide('victory2')
        text_color 'fff'

    text 'Destroyed enemy ships:':
        xpos 0.2
        ypos 0.2
        size 50
        outlines [(2,'000',0,0)]

    for ship in destroyed_ships:
        if not ship.faction == 'Player':
            add ship.blbl:
                xanchor 0.5
                at victory_ships(xx,wait,0.5)
            text '{}$'.format(ship.money_reward):
                xanchor 0.5
                yanchor 1.0
                size 50
                outlines [(2,'000',0,0)]
                at victory_ships(xx,wait,1)

            $wait += 0.3
            $xx += 1520/len(destroyed_ships)
            $store.total_money += ship.money_reward
        else:
            $store.repair_cost += int(ship.max_hp * 0.2)

    for ship in player_ships:
        $store.repair_cost += int((ship.max_hp - ship.hp)*0.1)

    $wait += 0.5
    text 'total money gained: {}$'.format(store.total_money):
        xpos 0.2
        ypos 0.6
        size 40
        outlines [(2,'000',0,0)]
        at delay_text(wait)

    $wait += 0.1
    text 'repair costs: {}$'.format(int(store.repair_cost)):
        xpos 0.2
        ypos 0.65
        size 40
        outlines [(2,'000',0,0)]
        at delay_text(wait)

    $wait += 0.1
    $store.net_gain = int(store.total_money - store.repair_cost)
    text 'net gain: {}$'.format(net_gain):
        xpos 0.2
        ypos 0.7
        size 40
        outlines [(2,'000',0,0)]
        at delay_text(wait)

    $wait += 0.5
    text 'Command Points':
        xanchor 1.0
        xpos 0.8
        ypos 0.6
        size 50
        outlines [(2,'000',0,0)]
        at delay_text(wait)

    $wait += 0.1
    text 'number of turns: {}'.format(BM.turn_count):
        xanchor 1.0
        xpos 0.8
        ypos 0.65
        size 40
        outlines [(2,'000',0,0)]
        at delay_text(wait)

    $wait += 0.1
    text 'command points received: {}'.format(int((store.net_gain*10)/BM.turn_count)):
        xanchor 1.0
        xpos 0.8
        ypos 0.70
        size 40
        outlines [(2,'000',0,0)]
        at delay_text(wait)

transform message_transform(x,y):
    # These control the position.
    xalign x yalign y
    # These control the actions on show and hide.
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

screen message:
    zorder 50
    text message:
        at message_transform(xpos,ypos)
        size 24
        outlines [(1,'fff',0,0)]

    timer 3.25 action Hide('message')


transform gameovergimmick(x,y,t):
    # These control the position.
    xpos x ypos y
    easeout t xpos -0.1
    block:
        xpos 1.0
        easeout t xpos -0.1
        repeat

screen game_over_gimmick:
    zorder 50

    for a in range(60):
        $randint = random.randint(12,40)
        $randx = random.random()
        $randy = random.random()
        $randt = random.randint(100,600) / 100.0
        text 'Game Over!' xpos randx ypos randy size randint at gameovergimmick(randx,randy, randt)

