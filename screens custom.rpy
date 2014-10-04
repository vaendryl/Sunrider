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

    transform warpout:
        alpha 0
        easein 1 alpha 1

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
        zoom zoomlevel/5.0
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

    transform delayed_image(wait,img):
        alpha 0
        pause wait
        alpha 0.8

    transform delay_float_text(yy,wait):
        ypos yy
        alpha 0
        time wait
        alpha 1
        easein 1.0 ypos int(yy-80*zoomlevel)

screen battle_screen:
    tag tactical
    modal False
    zorder -5
    key "mousedown_4" action ZoomAction(["zoom", "in"])    #scroll in and out
    key "mousedown_5" action ZoomAction(["zoom", "out"])
    key "K_PAGEUP" action Return(["zoom", "in"])
    key "K_PAGEDOWN" action Return(["zoom", "out"])
    if 'mouseup_2' not in config.keymap['hide_windows']:
        key "mousedown_2" action Return(["next ship"])
    if 'mouseup_3' not in config.keymap['game_menu']:
        key "mousedown_3" action Return(["deselect"])
    key "]" action Return(["next ship"])
    key "[" action Return(["previous ship"])

    ##messing with the player for fun and profit
    if BM.battlemode:
        timer 900 repeat False action Show('game_over_gimmick')
    
    add MouseTracker() #relates drags and clicks to the viewport and the BM

    if config.developer: #a release version should have set this to False
        key "Q" action Jump(['quit'])  ##DEBUG FAST QUIT##
        key "A" action Return(['anime'])
        if BM.phase != 'formation':
            key "P" action Return(['I WIN'])

    $childx = round(3840*zoomlevel) #this makes it so you can't scroll past the edge of the battlefield when zoomed out
    $childy = round(3006*zoomlevel+300) #extra 300 is so that the status window doesn't occlude ships in the far right bottom corner

    add BM.battle_bg xalign 0.5 yalign 0.5 #zoom 0.5 ##background for the battlefield##

    viewport id "grid":
        xmaximum 1920
        ymaximum 1080
        xadjustment BM.xadj
        yadjustment BM.yadj
        child_size (childx,childy)
        draggable False #BM.draggable
        mousewheel False
        edgescroll BM.edgescroll #(0,0) #(70,400*zoomlevel)

                ##CREATE HEX GRID##

##laggy as fuck!!
        if BM.show_grid:
            for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                    $xposition = dispx(a, b, zoomlevel)
                    $yposition = dispy(a, b, zoomlevel)
                    $xsize = int((HEXW + 4) * zoomlevel)
                    $ysize = int((HEXH + 4) * zoomlevel)
                    add "Battle UI/hex.png":
                        xpos xposition
                        ypos yposition
                        size (xsize,ysize)
                        alpha 0.4
        else:
##much faster!
            $xsize = int((HEXW+5.5) * zoomlevel * 18)
            $ysize = int((HEXD+4) * zoomlevel * 16)
            add 'Battle UI/hexgrid.png':
                alpha 0.4
                # zoom zoomlevel * 0.685
                size (xsize,ysize)
                xpos int(HEXW * zoomlevel)
                ypos int((HEXD-2) * zoomlevel)

        ##legion warning indicator
        ##the idea that uses this has been scrapped, but I'll keep the code around in case it proves useful in the future
#        if hasattr(store,'legion'):
#            if legion.active:
#                if legion.row != 0:
#                    text '  - - - - warning - - - - - warning - - - - - warning- - - - - warning - - - -  ':
#                        color 'f00' ypos int(120*(legion.row-0.25) *zoomlevel)
#                        size int(120*zoomlevel)
##                        layout nowrap

          ##display shield and flak ranges
          ##I'm sure this could be made to be much much faster

        if not BM.hovered == None: #when you hover over a ship
            if BM.hovered.shield_generation > 0:
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                    for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                        if get_distance(BM.hovered.location,(a,b)) <= BM.hovered.shield_range:
                            $ ship = BM.hovered
                            $ effective_shielding = ship.shield_generation + ship.modifiers['shield_generation'][0]
                            if effective_shielding > 0:
                                $xposition = dispx(a,b,zoomlevel)
                                $yposition = dispy(a,b,zoomlevel)
                                $xsize = int((HEXW + 4) * zoomlevel)
                                $ysize = int((HEXH + 4) * zoomlevel)
                                add "Battle UI/blue hex.png":
                                    xpos xposition
                                    ypos yposition
                                    size (xsize,ysize)
                                    alpha 0.7
            if BM.hovered.flak > 0:
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                    for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                        if get_distance(BM.hovered.location,(a,b)) <= BM.hovered.flak_range:
                            $ ship = BM.hovered
                            $effective_flak = ship.flak + ship.modifiers['flak'][0]
                            if effective_flak > 0:
                                $xposition = dispx(a,b,zoomlevel)
                                $yposition = dispy(a,b,zoomlevel)
                                $xsize = int((HEXW + 4) * zoomlevel)
                                $ysize = int((HEXH + 4) * zoomlevel)
                                add "Battle UI/red hex.png":
                                    xpos xposition
                                    ypos yposition
                                    size (xsize,ysize)
                                    alpha 0.9

        if not BM.weaponhover == None: #when you hover over a weapon button
            if BM.weaponhover.wtype == 'Missile' or BM.weaponhover.wtype == 'Rocket' or BM.weaponhover.name == 'Flak Off':
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                        for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                            for ship in enemy_ships:
                                if get_distance(ship.location,(a,b)) <= ship.flak_range:
                                    $effective_flak = ship.flak + ship.modifiers['flak'][0]
                                    if effective_flak > 0:
                                        $xposition = dispx(a,b,zoomlevel)
                                        $yposition = dispy(a,b,zoomlevel)
                                        $xsize = int((HEXW + 4) * zoomlevel)
                                        $ysize = int((HEXH + 4) * zoomlevel)
                                        add "Battle UI/red hex.png":
                                            xpos xposition
                                            ypos yposition
                                            size (xsize,ysize)
                                            alpha 0.9
            if BM.weaponhover.wtype == 'Laser' or BM.weaponhover.wtype == 'Pulse' or BM.weaponhover.name == 'Shield Down' or BM.weaponhover.name == 'Shield Jam':
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                        for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                            for ship in enemy_ships:
                                if get_distance(ship.location,(a,b)) <= ship.shield_range:
                                    $effective_shielding = ship.shield_generation + ship.modifiers['shield_generation'][0]
                                    if effective_shielding > 0:
                                        $xposition = dispx(a,b,zoomlevel)
                                        $yposition = dispy(a,b,zoomlevel)
                                        $xsize = int((HEXW + 4) * zoomlevel)
                                        $ysize = int((HEXH + 4) * zoomlevel)
                                        add "Battle UI/blue hex.png":
                                            xpos xposition
                                            ypos yposition
                                            size (xsize,ysize)
                                            alpha 0.7

                ## DISPLAY COVER ##
        for cover in BM.covers:
            $xposition = dispx(cover.location[0],cover.location[1],zoomlevel, 0.5)
            $yposition = dispy(cover.location[0],cover.location[1],zoomlevel, 0.5)
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

        for ship in BM.ships: #cycle through every ship in the battle
                  ##first we show the circle base below every unit
            if ship.location != None:
                $xposition = dispx(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJY) + int(zoomlevel * MOVY)
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
                $cell_height = 1503 / ((GRID_SIZE[1]+2)/2)
                #$cell_offset = cell_width / 2

                #calculate the position of the ships on the field
                $xposition = dispx(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(ship.location[0],ship.location[1],zoomlevel, 0.25 * ADJY) + int(zoomlevel * MOVY)

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

                
            ## as of the new UI interact code (with MouseTracker) most of the following is defunct.
            ## only the parts that affect lbl do anything anymore.
            
                #default values
                $mode = '' #default
                # $act = Return(['selection',ship])
                $lbl = ship.lbl
                $hvr = hoverglow(ship.lbl)
                # $hvrd = SetField(BM,'hovered',ship)
                # $unhvrd = SetField(BM,'hovered',None)

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

                        if BM.active_weapon.wtype == 'Support':
                            $ mode = 'offline'

                if BM.active_weapon != None:
                    if BM.active_weapon.name == 'Gravity Gun':
                        #the gravity gun is a bit unique
                        if ship.stype != 'Ryder':
                            $ mode = 'offline'
                        else:
                            $ mode = 'target'

                if mode == 'target':
                    $ lbl = hoverglow(ship.lbl)
                    # $ hvr = im.MatrixColor(ship.lbl,im.matrix.brightness(0.2))
                elif mode == 'offline':
                    # $ act = NullAction()
                    # $ hvr = im.MatrixColor(ship.lbl,im.matrix.brightness(-0.3))
                    $ lbl = im.MatrixColor(ship.lbl,im.matrix.brightness(-0.3))

                if BM.hovered != None:
                    if BM.hovered == ship:
                        if mode != 'offline':
                            $ lbl = hoverglow(ship.lbl)
                
                add lbl:
                    xanchor 0.5
                    yanchor 0.5
                    xpos xposition
                    ypos yposition
                    zoom (zoomlevel/2.5)
                
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
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.08 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.66 * ADJY) + int(zoomlevel * MOVY)
                    $hp_size = int(405*(float(ship.hp)/ship.max_hp))
                    add 'Battle UI/label hp bar.png':
                        xpos xposition
                        ypos yposition
                        zoom (zoomlevel/2.5)
                        crop (0,0,hp_size,79)

                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.08 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.72 * ADJY) + int(zoomlevel * MOVY)
                    $energy_size = int(405*(float(ship.en)/ship.max_en))
                    add 'Battle UI/label energy bar.png':
                        xpos xposition
                        ypos yposition
                        zoom (zoomlevel/2.5)
                        crop (0,0,energy_size,79)
                        
                    text str(ship.hp):
                        xanchor 0.5
                        yanchor 0.5
                        xpos int(xposition+80*zoomlevel)
                        ypos int(yposition+27*zoomlevel)
                        size int(16*zoomlevel)
                        font "Font/sui generis rg.ttf"
                        outlines [(2,'000',0,0)]                        

                else:    #enemies

                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.09 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.70 * ADJY) + int(zoomlevel * MOVY)
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

##show flak icon and intercept text
        if BM.missile_moving:
            for ship in BM.ships:
                if ship.flaksim != None and ship.flak > 0:
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                    $ wait = ship.flaksim[0]
                    $ intercept_count = ship.flaksim[1]
                    if intercept_count:
                        $ BM.battle_log_insert(['attack', 'missile'], "{0} intercepted {1} missiles! Effectiveness: {2}%".format(ship.name, intercept_count, int(ship.flak_effectiveness)))

                    add 'Battle UI/warning icon.png':
                        xanchor 0.5
                        yanchor 0.5
                        xpos xposition
                        ypos yposition
                        zoom (zoomlevel/2.5)
                        alpha 0.8
                        at delayed_image(wait,'Battle UI/warning icon.png')

                    $ textcolor = 'f00'
                    if ship.faction == 'Player':
                        $ textcolor = '0f0'

                    text '{} intercepted! \neffectiveness: {}%'.format( intercept_count , int(ship.flak_effectiveness) ):
                        xanchor 0.5
                        yanchor 0.5
#                        xmaximum 200
                        xpos xposition
                        ypos yposition
                        size 28
                        color textcolor
                        outlines [(2,'000',0,0)]
                        at delay_float_text(yposition,wait)


##show missiles on the map that are currently flying in space##

        if BM.missile_moving:
            for missile in BM.missiles:
                if missile.parent.location != None and missile.target.location != None: #failsafes
                    $xposition = dispx(missile.parent.location[0], missile.parent.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(missile.parent.location[0], missile.parent.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                    $next_xposition = dispx(missile.target.location[0],missile.target.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                    $next_yposition = dispy(missile.target.location[0],missile.target.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)

                    $ travel_time = get_ship_distance(missile.parent,missile.target)*MISSILE_SPEED*1.5
                    add missile.lbl:
                        at move_ship(xposition,yposition,next_xposition,next_yposition,travel_time)
                        xanchor 0.5
                        yanchor 0.5
                        zoom (zoomlevel/4.0)

    #                text str(missile.shot_count):
    #                    at move_ship(xposition,yposition,next_xposition,next_yposition,0.1)
    #                    xanchor 0.5
    #                    yanchor 0.5
    #                    size (20/zoomlevel)
    #                    outlines [(1,'000',0,0)]



##targeting window##

          ##if targeting mode is active show a targeting window over all enemy_ships that gives you chance to hit and other data
        if BM.weaponhover != None or BM.targetingmode and BM.selected != None:
            $ selected = BM.selected  #the screen sometimes loses track of BM.selected and crashes so a local is required

            for ship in BM.ships:
                if ship.location != None:

                    if BM.weaponhover == None:
                        $BM.weaponhover = BM.active_weapon
                    if BM.weaponhover.wtype == 'Support' and (ship.faction != 'Player' or BM.weaponhover.self_buff == True):
                        pass
                    elif BM.weaponhover.wtype != 'Support' and ship.faction == 'Player' and BM.weaponhover.wtype != 'Special':
                        # wtype:'Special' is a support type that's neither a curse nor a buff but can be used on enemies and player units both
                        pass
                    elif BM.weaponhover.wtype == 'Melee' and (ship.stype != 'Ryder' or get_ship_distance(ship,selected) > 1):
                        pass
                    
                    #the gravity gun is a little... special
                    if BM.weaponhover.name == 'Gravity Gun' and ship.stype != 'Ryder':
                        pass

                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.75 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.15 * ADJY) + int(zoomlevel * MOVY)
                    add 'Battle UI/targeting_window.png':
                        xpos xposition
                        ypos yposition
                        xanchor 0.5
                        yanchor 0.5
                        zoom (zoomlevel/1.3)
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,.92 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,.20 * ADJY) + int(zoomlevel * MOVY)
                    text (str(ship.cth) + '%'):
                        xpos xposition
                        ypos yposition
                        xanchor 0.5
                        yanchor 0.5
                        size (20 * zoomlevel)
                        color '000'
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.75 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.40 * ADJY) + int(zoomlevel * MOVY)
                    if selected == None:  #workarounds
                        $ effective_flak = 0
                    else:
                        if BM.weaponhover.wtype == 'Rocket':
                            #this looks double but missile_eccm is from a ship through upgrades whereas weaponhover.eccm is rom the rocket itself. (default 10)
                            $effective_flak = ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm - BM.weaponhover.eccm
                        else:
                            $effective_flak = ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm

                    if effective_flak < 0:
                        $ effective_flak = 0
                    elif effective_flak > 100:
                        $ effective_flak = 100

                    text str(effective_flak):
                        xpos xposition
                        ypos yposition
                        xanchor 1.0
                        yanchor 0.5
                        size (14 * zoomlevel)
                        color 'fff'
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,.92 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,.40 * ADJY) + int(zoomlevel * MOVY)
                    text str(ship.shields):
                        xpos xposition
                        ypos yposition
                        xanchor 1.0
                        yanchor 0.5
                        size (14 * zoomlevel)
                        color 'fff'
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,1.0 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.4 * ADJY) + int(zoomlevel * MOVY)
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

          #when you hover over an enemy ship the HP bar and HP text will overlay again on top of other ships.
          #actually, with the hex grid overlap issues are mostly gone
        # if BM.hovered != None: #when you hover over a ship
            # $ hovered_ship = BM.hovered
            # if hovered_ship.location == None:
                # $ pass
            # # elif hovered_ship.faction != 'Player':
            # $xposition = dispx(hovered_ship.location[0],hovered_ship.location[1],zoomlevel,0.09 * ADJX) + int(zoomlevel * MOVX)
            # $yposition = dispy(hovered_ship.location[0],hovered_ship.location[1],zoomlevel,0.70 * ADJY) + int(zoomlevel * MOVY)
            # $hp_size = int(405*(float(BM.hovered.hp)/BM.hovered.max_hp))
            # add 'Battle UI/label hp bar.png':
                # xpos xposition
                # ypos yposition
                # zoom (zoomlevel/2.5)
                # crop (0,0,hp_size,90)

            # text str(BM.hovered.hp):
                # xanchor 0.5
                # yanchor 0.5
                # xpos int(xposition+80*zoomlevel)
                # ypos int(yposition+27*zoomlevel)
                # size int(16*zoomlevel)
                # font "Font/sui generis rg.ttf"
                # outlines [(2,'000',0,0)]


                ##DISPLAY MOVEMENT OPTIONS##
        if BM.selectedmode and BM.selected.faction == 'Player' and not BM.targetingmode and not BM.phase == 'formation':
            for tile in BM.selected.movement_tiles:
                    
                $ lbl = 'Battle UI/move_tile.png'
                $ tile_location = (tile[3],tile[4])
                
                if get_counter_attack(tile_location) and BM.selected.modifiers['stealth'][0] == 0:
                    $ lbl = im.MatrixColor(lbl,im.matrix.tint(1.0, 0.5, 0.5))
                
                if tile_location == BM.mouse_location:
                    $ lbl = hoverglow(lbl)  
                add lbl:
                    zoom (0.2 * zoomlevel)
                    alpha 0.5
                    xanchor 0.5
                    yanchor 0.5
                    xpos tile[0]
                    ypos tile[1]

                text (str(BM.selected.move_cost*tile[2]) + ' EN'):
                    xpos tile[0]
                    ypos tile[1]
                    xanchor 0.5
                    yanchor 0.5
                    size (20 * zoomlevel)
                    outlines [(2,'000',0,0)]


          #firing the vanguard cannon  [[doesn't seem to be used any more]]
        if BM.vanguard:
            $xposition = dispx(sunrider.locatio[0],sunrider.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
            $yposition = dispy(sunrider.locatio[0],sunrider.location[1],zoomlevel) + int(zoomlevel * MOVY)
            add 'Battle UI/vanguard beam wave.png':
                xanchor 0.0
                yanchor 0.27
                xpos int(xposition+100/zoomlevel)
                ypos yposition
                size (int(1344/zoomlevel),int(120/zoomlevel))
                at vanguard_cannon
                alpha 1.0

         #selecting target for vanguard cannon
        if BM.vanguardtarget:   #creates buttons over enemy ships
            $ loc1 = sunrider.location
            $ loc2 = BM.mouse_location
            if get_distance(loc1, loc2) <= BM.vanguard_range:
                $tiles = interpolate_hex(loc1, loc2)
                for i in tiles:
                    $xposition = dispx(i[0],i[1],zoomlevel)
                    $yposition = dispy(i[0],i[1],zoomlevel)
                    $xsize = int((HEXW + 4) * zoomlevel)
                    $ysize = int((HEXH + 4) * zoomlevel)
                    add "Battle UI/vanguard hex.png":
                        xpos xposition
                        ypos yposition
                        size (xsize,ysize)
                        alpha 0.7

        if BM.enemy_vanguard_path is not None:
            for hex in BM.enemy_vanguard_path:
                $xposition = dispx(hex[0],hex[1],zoomlevel)
                $yposition = dispy(hex[0],hex[1],zoomlevel)
                $xsize = int((HEXW + 4) * zoomlevel)
                $ysize = int((HEXH + 4) * zoomlevel)
                add "Battle UI/vanguard hex.png":
                    xpos xposition
                    ypos yposition
                    size (xsize,ysize)
                    alpha 0.7
                                
          #the Sunrider warps from one cell to another
        if BM.warping:
            for location in store.flash_locations:
                $xposition = dispx(location[0],location[1],zoomlevel) + int(zoomlevel * MOVX)
                $yposition = dispy(location[0],location[1],zoomlevel,-0.5 * ADJY) + int(zoomlevel * MOVY)
                add 'Battle UI/label_warpflash.png':
#                    anchor 0.5  #I get a float object not iterable crash. very annoying
                    xpos xposition
                    ypos yposition
                    at warpout
                    zoom 0.25 * zoomlevel

            ##MOVE SHIP FROM GRID TO GRID##
        if BM.moving and BM.selected != None:
            if BM.selected.location != None:
                $xposition = dispx(BM.selected.current_location[0],BM.selected.current_location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(BM.selected.current_location[0],BM.selected.current_location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                $next_xposition = dispx(BM.selected.next_location[0],BM.selected.next_location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $next_yposition = dispy(BM.selected.next_location[0],BM.selected.next_location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)

                $travel_time = BM.selected.travel_time

                add BM.selected.lbl:
                    at move_ship(xposition,yposition,next_xposition,next_yposition,travel_time)
                    xanchor 0.5
                    yanchor 0.5
                    zoom (zoomlevel/2.5)

        if BM.debugoverlay:  #may use this later for AI debug things too
            for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                    $xposition = dispx(a,b,zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(a,b,zoomlevel,0.5 * ADJY) + int(zoomlevel * MOVY)

                    text '{}/{}'.format(a,b):
                        xanchor 0.5
                        yanchor 0.5
                        xpos xposition
                        ypos yposition


##not part of the viewport##
    if BM.phase != 'formation':
        vbox:
            xalign 1.0
            vbox:
                xalign 1.0
                # textbutton "Battle Log" xalign 1.0 action Show('battle_log')
                # if BM.edgescroll == (0,0):
                    # textbutton "enable edgescroll" action SetField(BM,'edgescroll',(100,800*zoomlevel))
                # else:
                    # textbutton "disable edgescroll" action SetField(BM,'edgescroll',(0,0))
                # if BM.show_tooltips:
                    # textbutton "disable tooltips" xalign 1.0 action SetField(BM,'show_tooltips',False)
                # else:
                    # textbutton "enable tooltips"  xalign 1.0 action SetField(BM,'show_tooltips',True)
                
                if store.Difficulty < 3:
                    textbutton "restart turn" xalign 1.0 action Jump('restartturn')
    
            if config.developer:
                vbox:
                    # ypos 100
                    xalign 1.0
                    textbutton "Debug Cheats" xalign 1.0 action Return(['cheat'])
                    textbutton "Fast Quit" xalign 1.0 action Jump('quit')

                    if BM.debugoverlay:
                        textbutton "coord overlay" xalign 1.0 action SetField(BM,'debugoverlay',False)
                    else:
                        textbutton "coord overlay" xalign 1.0 action SetField(BM,'debugoverlay',True)
                    if BM.show_grid:
                        textbutton "new grid" xalign 1.0 action SetField(BM,'show_grid',False)
                    else:
                        textbutton "old grid" xalign 1.0 action SetField(BM,'show_grid',True)
                    textbutton "debug log" xalign 1.0 action Show('debug_window')

    if BM.just_moved:
        textbutton 'cancel movement':
            ypos 70
            text_size 50
            text_color 'fff'
            action Return(['cancel movement'])

    if not BM.showing_orders and not BM.order_used and not BM.missile_moving and not BM.moving and BM.phase == "Player" and sunrider.location != None:
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


    if BM.phase == 'Player':
        $endturnbutton_idle = im.MatrixColor('Battle UI/button_endturn.png',im.matrix.tint(0.6, 1.0, 0.5))
        for ship in player_ships:
            if ship.en >= ship.max_en:
                $endturnbutton_idle = im.MatrixColor('Battle UI/button_endturn.png',im.matrix.tint(1.0, 0.6, 0.5))
    
        imagebutton:
            xpos 90
            yalign 1.0
            idle endturnbutton_idle
            hover hoverglow(endturnbutton_idle)
            action Return(['endturn'])
            
            
    if BM.phase == 'formation':
        imagebutton:
            xpos 170
            yalign 1.0
            idle 'Skirmish/start.png'
            hover hoverglow('Skirmish/start.png')
            action [ If( BM.selected==None , Return(['start']) ) ]
            
        if BM.mission == 'skirmish':
            imagebutton:
                xpos 88
                ypos 690
                idle 'Skirmish/return.png'
                hover hoverglow('Skirmish/return.png')
                action Return(['quit'])
        
            $ idl = 'Skirmish/remove.png'
            if BM.remove_mode:
                $ idl = hoverglow(im.MatrixColor('Skirmish/remove.png',im.matrix.tint(1.0, 1.0, 0)))
            
            imagebutton:
                xpos 208
                ypos 759
                idle idl
                hover hoverglow('Skirmish/remove.png')
                action Return(['remove'])
                
            imagebutton:
                xpos 328
                ypos 828
                idle 'Skirmish/enemymusic.png'
                hover hoverglow('Skirmish/enemymusic.png')
                action Show('enemy_music')

            imagebutton:
                xpos 448
                ypos 897
                idle 'Skirmish/playermusic.png'
                hover hoverglow('Skirmish/playermusic.png')
                action Show('player_music')                 
    
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
    
    key "mousedown_3" action [Hide('orders'),SetField(BM,'showing_orders',False)]

    frame:
        background 'Battle UI/commandbar_window.png'
        at move_down(-590,0)
        vbox:
            spacing 20
            for order in BM.orders:
                button:
                    xpos 20
                    idle_background 'Battle UI/commandbar_button.png'
                    hover_background hoverglow('Battle UI/commandbar_button.png')
                    action [Return([order]),Hide('orders'),SetField(BM,'showing_orders',False)]

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
#                       first_indent 150
                        size 18
                        outlines [(1,'222',0,0)]

                    hbox:
                        #I should rework orders to include this info :/
                    
                        if order == 'REPAIR DRONES':
                            if sunrider.repair_drones != None:
                                if sunrider.repair_drones == 0:
                                    $colour = '900'
                                else:
                                    $colour = '050'
                                text '[[' + str(sunrider.repair_drones) + ']':
                                    ypos 5
                                    first_indent -170
                                    size 22
                                    color colour
                                    outlines [(1,colour,0,0)]

                        if order == 'FULL FORWARD' and BM.show_tooltips == True:
                            frame:
                                background Solid((0,0,0,200))
                                xpos 150
                                ycenter 20

                                text str('Provides +15 Aim and +20% damage to all allied units. Will cancel All Guard if active.'):
                                    xpos 0
                                    ypos 0
                                    size 18
                                    font "Font/sui generis rg.ttf"
                                    outlines [(1,'000',0,0)]
                        
                        if order == 'ALL GUARD' and BM.show_tooltips == True:
                            frame:
                                background Solid((0,0,0,200))
                                xpos 150
                                ycenter 20

                                text str('Provides +20 Flak, +10 Evasion and +10 shield generation to all ships. Will cancel Full Forward if active.'):
                                    xpos 0
                                    ypos 0
                                    size 18
                                    font "Font/sui generis rg.ttf"
                                    outlines [(1,'000',0,0)]                                    

                        if order == 'REPAIR DRONES' and BM.show_tooltips == True:
                            frame:
                                background Solid((0,0,0,200))
                                xpos 150
                                ycenter 20

                                text str('Restores 50% of the Sunrider\'s health.'):
                                    xpos 0
                                    ypos 0
                                    size 18
                                    font "Font/sui generis rg.ttf"
                                    outlines [(1,'000',0,0)]

                        if order == 'VANGUARD CANNON' and BM.show_tooltips == True:
                            frame:
                                background Solid((0,0,0,200))
                                xpos 150
                                ycenter 20
                                
                                $ damage = get_modified_damage(BM.vanguard_damage,'notplayer')
                                text str('Deals {} unavoidable damage to all units in a straight line extending outwards from the Sunrider with a maximum range of {} hexes.'.format(damage,BM.vanguard_range)):                                
                                    xpos 0
                                    ypos 0
                                    size 18
                                    font "Font/sui generis rg.ttf"
                                    outlines [(1,'000',0,0)]

                        if order == 'SHORT RANGE WARP' and BM.show_tooltips == True:
                            frame:
                                background Solid((0,0,0,200))
                                xpos 150
                                ycenter 20

                                text str('Moves the Sunrider to any point on the map. Can be used with another Order.'):
                                    xpos 0
                                    ypos 0
                                    size 18
                                    font "Font/sui generis rg.ttf"
                                    outlines [(1,'000',0,0)]

                        if order == 'RESURRECTION' and BM.show_tooltips == True:
                            frame:
                                background Solid((0,0,0,200))
                                xpos 150
                                ycenter 20

                                text str('Select a downed unit to launch into the battle once more at full health.'):
                                    xpos 0
                                    ypos 0
                                    size 18
                                    font "Font/sui generis rg.ttf"
                                    outlines [(1,'000',0,0)]
                                    
                        if order == 'RETREAT' and BM.show_tooltips == True:
                            frame:
                                background Solid((0,0,0,200))
                                xpos 150
                                ycenter 20

                                text str('Retreats your units from the battle with no penalties applied.'):
                                    xpos 0
                                    ypos 0
                                    size 18
                                    font "Font/sui generis rg.ttf"
                                    outlines [(1,'000',0,0)]                                    


                                    #I couldn't get the mouse detection working properly with the buttons. Sorry! :S

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

        ##show status window and its data
    if not BM.selected == None:
        $ ship = BM.selected
        add 'Battle UI/statuswindow.png' xalign 1.0 yalign 1.0
        if not BM.selected.portrait == None:
            add BM.selected.portrait xalign 1.0 yalign 1.0
        else:
            $ index = ''
            if config.developer and BM.selected.faction != 'Player':
                if BM.selected in enemy_ships:
                    $ index = ' ' + str(enemy_ships.index(BM.selected))
                # text str(index) xanchor 1.0 xpos 1880 ypos 800 size 20 outlines [(1,'000',0,0)]
            text (BM.selected.name + index) xanchor 1.0 xpos 1880 ypos 726 outlines [(1,'000',0,0)]

        $hp_size = int(374*(float(BM.selected.hp)/BM.selected.max_hp))
        $en_size = int(298*(float(BM.selected.en)/BM.selected.max_en))
        add 'Battle UI/status window_HP.png' xpos 1080 ypos 779 crop (0,0,hp_size,49)
        add 'Battle UI/status window_EN.png' xpos 1133 ypos 805 crop (0,0,en_size,19)
        text (str(BM.selected.hp) + '/' + str(BM.selected.max_hp)) xanchor 0.5 xpos 1510 ypos 779 size 19 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]
        text (str(BM.selected.en) + '/' + str(BM.selected.max_en)) xanchor 0.5 xpos 1490 ypos 805 size 19 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]

        $effective_flak = ship.flak + ship.modifiers['flak'][0]
        if effective_flak < 0:
            $ effective_flak = 0
        elif effective_flak > 100:
            $ effective_flak = 100
        text (str(effective_flak)) xanchor 1.0 xpos 1149 ypos 847 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]

        text (str(BM.selected.shields)) xanchor 1.0 xpos 1149 ypos 897 size 24 font "Font/sui generis rg.ttf" outlines [(1,BM.selected.shield_color,0,0)]
        text (str(BM.selected.armor)) xanchor 1.0 xpos 1149 ypos 947 size 24 font "Font/sui generis rg.ttf" outlines [(1,BM.selected.armor_color,0,0)]
        text (str(BM.selected.evasion)) xanchor 1.0 xpos 1149 ypos 997 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]

        ##show weapon stats in status window on hover

        if not BM.weaponhover == None or not BM.active_weapon == None:
            if BM.weaponhover == None:
                $weapon = BM.active_weapon
            else:
                $weapon = BM.weaponhover
            text (str(real_damage(weapon,ship))) xanchor 1.0 xpos 1380 ypos 840 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]
            text (str(real_damage(weapon,ship)*weapon.shot_count)) xanchor 1.0 xpos 1380 ypos 870 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]
            text (str(weapon.shot_count)) xanchor 1.0 xpos 1515 ypos 840 size 24 font "Font/sui generis rg.ttf" outlines [(1,'000',0,0)]



        ##show buffs
        $count = 0
        for modifier in BM.selected.modifiers:
            if BM.selected.modifiers[modifier][0] != 0:
                text modifier xpos 1217 ypos (922+count*24) size 20 outlines [(1,'000',0,0)]
                if BM.selected.modifiers[modifier][0] > 0:
                    if BM.selected.modifiers[modifier][1] > 0:
                        $ status_effect = '+{}% for {} turns'.format(BM.selected.modifiers[modifier][0],BM.selected.modifiers[modifier][1])
                    else:
                        $ status_effect = '+{}%'.format(BM.selected.modifiers[modifier][0])
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
                $ act = If(can_fire,FireWeapon(weapon))
                $ hvrd = HoverWeapon(weapon)
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
                python:
                    if not hasattr(weapon,'hp_cost'): weapon.hp_cost = 0
                if weapon.hp_cost > 0:
                    text str(-weapon.hp_cost) + 'HP':
                        xanchor 0.5
                        yanchor 0.5
                        xpos (x_offset+80+120*count)
                        ypos (y_offset+115+69*count)
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
                

                
transform move_vertical(xstart,xend,xx=0):
    #used by skirmish windows
    xpos xstart
    linear 0.5 xpos xend
    on hide:
        linear 0.5 xpos xstart
          #not sure why this is needed. I'm calling bug in renpy
        time 2
        alpha 0                

screen player_unit_pool_collapsed:
    #this just shows the 'add player units' text and puts a button over it
    zorder 2
    
    add 'Skirmish/addplayer.png':
        xpos -152
    
    button:
        background None
        xpos 0
        ypos 410
        yminimum 250
        ymaximum 250
        xminimum 40
        xmaximum 40
        action Show('player_unit_pool')
    
screen player_unit_pool:
    zorder 3
    
    if BM.mission == 'skirmish':
        $ frame_background = 'Skirmish/addplayer.png'
    else:
        $ frame_background = 'Skirmish/addplayer_nocmd.png'
    
    frame:
        background frame_background
        xmaximum 182
        at move_vertical(-152,0)
        
        vbox:
            for ship in player_ships:
                if ship.location == None and ship != BM.selected:
                    imagebutton:
                        at zoom_button(0.2)
                        idle ship.lbl
                        hover hoverglow(ship.lbl)
                        action Return(['selection',ship]) 
        
    button:
        background None  # Solid((0,0,0,255)) #for testing
        xpos 152
        ypos 410
        yminimum 250
        ymaximum 250
        xminimum 40
        xmaximum 40
        action Hide('player_unit_pool')
        
    if BM.mission == 'skirmish':
        
        text str(BM.cmd):
            xalign 0.5
            xpos 75
            ypos 998
            size 28
            color '000'

        imagebutton:
            xpos 18
            ypos 1038
            idle 'skirmish/increase_cmd.png'
            hover hoverglow('skirmish/increase_cmd.png')
            action SetField( BM , 'cmd' , (BM.cmd + 100) ) 
            alternate SetField( BM , 'cmd' , (BM.cmd + 1000) )
            
        imagebutton:
            xpos 80
            ypos 1038
            idle 'skirmish/decrease_cmd.png'
            hover hoverglow('skirmish/decrease_cmd.png')
            action If( BM.cmd <= 100 , SetField(BM,'cmd',0) , SetField(BM,'cmd',(BM.cmd - 100)) )
            alternate If( BM.cmd <= 1000 , SetField(BM,'cmd',0) , SetField(BM,'cmd',(BM.cmd - 1000)) )
        

screen enemy_unit_pool_collapsed:
    zorder 2
    
    add 'Skirmish/addenemy.png':
        xpos 1890
    
    button:
        background None
        xpos 1890
        ypos 410
        yminimum 250
        ymaximum 250
        xminimum 40
        xmaximum 40
        action Show('enemy_unit_pool')

screen enemy_unit_pool:
    zorder 3
    
    #I will want to put this in a BM field and add new stuff when they get encountered.
    #I think I'll modify the create_ship function to add it automatically if it's not there yet
    $ all_enemies = store.all_enemies
    
    frame:
        background 'Skirmish/addenemy.png'
        # xalign 1.0
        xmaximum 176
        at move_vertical(1890,1744)
        
        viewport:
            xpos 20
            ypos 20
            mousewheel True #luckily this viewport eats scrolls above it, so the main one doesn't return it.
            scrollbars "vertical"
            
            vbox:
                spacing 20
                
                for ship in all_enemies:
                    imagebutton:
                        at zoom_button(0.15)
                        idle ship.lbl
                        hover hoverglow(ship.lbl)
                        action Return(['selection',ship])
                        
    button:
        background None
        xpos 1738
        ypos 410
        yminimum 250
        ymaximum 250
        xminimum 40
        xmaximum 40
        action Hide('enemy_unit_pool')                        

screen player_music:
    modal True
    
    #maybe this list should be defined in the inits
    python:
        music_list = {
            "Driving The Top Down": 'Music/Driving_the_Top_Down.ogg',
            "La Busqueda de Lanna": 'Music/La_Busqueda_de_Lanna.ogg',
            "Powerful": 'Music/Powerful.ogg',
            "Riding With The Wind": 'Music/Riding_With_the_Wind.ogg',
            "Titan": 'Music/Titan.ogg'
            }
            
    add "Skirmish/playermusic_back.png"
    
    vbox:
        xalign 0.4
        yalign 0.4
        spacing 20
        
        for song in music_list: 

            button:
                xpos 0
                idle_background "Skirmish/song_button.png"
                hover_background hoverglow("Skirmish/song_button.png")
                action [ Hide('player_music'), Return( ["playermusic",music_list[song]] ) ]
                
                text song:
                    min_width 544   #length of the background. needed for hover
                    xalign 0.5
                    color '000'
                    size 28

screen enemy_music:
    modal True
    
    python:
        music_list = {
            "Battle Against Time": 'Music/Battle_Against_Time.ogg',
            "Dusty Universe": 'Music/Dusty_Universe.ogg',
            "Intruders": 'Music/Intruders.ogg',
            "Poltergeist Attack": 'Music/Poltergeist_Attack.ogg',
            "Posthumus Regium": 'Music/Posthumus_Regium.ogg',
            "Sui Generis": 'Music/Sui_Generis.ogg'
            }
             
    add "Skirmish/enemymusic_back.png"
    
    vbox:
        xalign 0.4
        yalign 0.4
        spacing 20
        
        for song in music_list: 

            button:
                xpos 0
                idle_background "Skirmish/song_button.png"
                hover_background hoverglow("Skirmish/song_button.png")
                action [ Hide('enemy_music'), Return( ["enemymusic",music_list[song]] ) ]
                
                text song:
                    min_width 544   #length of the background. needed for hover
                    xalign 0.5
                    color '000'
                    size 28                    
                    
            
        
        
        
        
        
        
screen tooltips:
    zorder 9

    #I fear I'll be needing a custom displayable for this eventually

    #grab mouse location
    $ mouse_x,mouse_y = renpy.get_mouse_pos()

    #check if you're hovering over a weapon, tooltips are enabled and you're not currently selecting a target
    if BM.weaponhover != None and BM.show_tooltips and BM.active_weapon == None:
        $ weapon = BM.weaponhover

        if weapon.tooltip != None:
            frame:
                background Solid((0,0,0,200))
                xpos mouse_x + 100
                ycenter mouse_y

                text str(weapon.tooltip):
                    xpos -70 #NO IDEA why I can only get things to align right this way.
                    ypos -10
                    size 18
                    font "Font/sui generis rg.ttf"
                    outlines [(1,'000',0,0)]


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

    if store.damage == 'miss':
        $current_hp = BM.target.hp
    else:
        $current_hp = BM.target.hp+ store.damage

    $hp_size1 = int(409*(float(current_hp)/BM.target.max_hp))
    add 'Battle UI/dmgstatus_bar.png':
        xpos 1340
        ypos 3
        crop (0,0,hp_size1,42)
    text 'HP: {!s}/{!s}'.format(current_hp,BM.target.max_hp):
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
        $current_hp = BM.target.hp
    else:
        $damage = store.damage
        $current_hp = BM.target.hp+ store.damage
    $hp_size1 = int(409*(float(current_hp)/BM.target.max_hp))
    $hp_size2 = int(409*(float(current_hp-damage)/BM.target.max_hp))

    add 'Battle UI/dmgstatus_bar.png':
        xpos 1340
        ypos 3
        at hp_falls(hp_size1,hp_size2)

    text 'HP: {!s}/{!s}'.format((current_hp-damage),BM.target.max_hp):
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

    $ textsize = 50
    if len(destroyed_ships) > 12:
        $ textsize = 40
    elif len(destroyed_ships) > 20:
        $ textsize = 30

    $ total_ships = len(destroyed_ships)
    if store.boss_killed:
        $ total_ships += len(enemy_ships)

    $ wait_time = 0.3
    if len(destroyed_ships)> 20:
        $ wait_taime = 0.1
    
    
    for ship in destroyed_ships:
        if not ship.faction == 'Player':
            add ship.blbl:
                xanchor 0.5
                at victory_ships(xx,wait,0.5)
            text '{}$'.format(int(ship.money_reward)):
                xanchor 0.5
                yanchor 1.0
                size textsize
                outlines [(2,'000',0,0)]
                at victory_ships(xx,wait,1)

            $wait += wait_time
            $xx += 1520/total_ships

    if store.boss_killed:
        for ship in enemy_ships:
            add ship.blbl:
                xanchor 0.5
                at victory_ships(xx,wait,0.5)
            text 'Surrendered':
                xanchor 0.5
                yanchor 1.0
                color '090'
                size textsize - 15
                outlines [(2,'000',0,0)]
                at victory_ships(xx,wait,1)

            $wait += 0.3
            $xx += 1520/total_ships

    $wait += 0.5
    text 'enemy destruction reward: {}$'.format(int(store.total_money)):
        xpos 0.2
        ypos 0.6
        size 40
        outlines [(2,'000',0,0)]
        at delay_text(wait)

    $ yposition = 0.65
    if store.surrender_bonus > 0:
        $wait += 0.1
        text 'surrender bonus: {}$'.format(int(store.surrender_bonus)):
            xpos 0.2
            ypos yposition
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)
        $ yposition += 0.05


    $wait += 0.1
    text 'repair costs: {}$'.format(int(store.repair_cost)):
        xpos 0.2
        ypos yposition
        size 40
        outlines [(2,'000',0,0)]
        at delay_text(wait)
    $ yposition += 0.05

    if store.Difficulty == 5:
        $wait += 0.1
        text 'space whale tax: {}$'.format(int(store.net_gain * 0.25)):
            xpos 0.2
            ypos yposition
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)
        $ yposition += 0.05
    
    $wait += 0.1
    text 'net gain: {}$'.format(int(store.net_gain)):
        xpos 0.2
        ypos yposition
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
    
    $ difficulty_penalty = store.Difficulty - 1
    if difficulty_penalty < 0: 
        $ difficulty_penalty = 0
                
    text 'command points received: {}'.format( int( (store.net_gain*10)/(BM.turn_count+difficulty_penalty) ) ):
        xanchor 1.0
        xpos 0.8
        ypos 0.70
        size 40
        outlines [(2,'000',0,0)]
        at delay_text(wait)
        
    $ diff_text = "Current difficulty: {}".format( DIFFICULTY_NAMES[store.Difficulty] )
    $ low_diff_text = "lowest difficulty: {}".format( DIFFICULTY_NAMES[BM.lowest_difficulty] )
    
    vbox:
        xalign 1.0
        yalign 1.0
        
        text diff_text:
            size 12
            xalign 1.0
        text low_diff_text:
            size 12
            xalign 1.0
        

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
        color 'fff'
        outlines [(2,'000',0,0)]

    timer 3.25 action Hide('message')

screen mousefollow:
    zorder 10
    if BM.selected == None:
        $ follow_image = sunrider.lbl
    else:
        $ follow_image = BM.selected.lbl

    $ follow_image = im.Rotozoom(follow_image,0,0.25)
#    $ follow_image = im.matrix(follow_image).opacity(0.4)
    add MouseFollow(follow_image):
        alpha 0.7

screen ryderlist:
    zorder 3
    modal True
    
    key "mousedown_3" action Return(["deselect"])
    
    text 'Choose which Ryder to repair':
            xalign 0.5
            yalign 0.1
            size 40
            outlines [(2,'000',0,0)]
            
    
    frame:
        xalign 0.5
        ypos 0.2
        xminimum 400
        xmaximum 400
        yminimum 300
        ymaximum 800
        background Solid((0,0,0,200))
        
        $ count = 0
        for iconship in destroyed_ships:
            if iconship.faction == 'Player' and not iconship.mercenary and iconship.stype == 'Ryder':
                $ icon = None
                $ hovericon = None
                $ xposition = 50
                if count % 2 != 0:
                    $ xposition = 168
                $ yposition = 20 + count * 70

                #this is the sort of mess you get if you don't put this stuff in the library
                if iconship.name == 'Sunrider':
                    $ icon = 'Menu/upgrade_sunrider_button.png'
                    $ hovericon = 'Menu/upgrade_sunrider_button_hover.png'
                elif iconship.name == 'Liberty':
                    $ icon = 'Menu/upgrade_liberty_button.png'
                    $ hovericon = 'Menu/upgrade_liberty_button_hover.png'
                elif iconship.name == 'Black Jack':
                    $ icon = 'Menu/upgrade_blackjack_button.png'
                    $ hovericon = 'Menu/upgrade_blackjack_button_hover.png'
                elif iconship.name == 'Havoc':
                    $ icon = 'Menu/upgrade_havoc_button.png'
                    $ hovericon = 'Menu/upgrade_havoc_hover.png'
                elif iconship.name == 'Phoenix':
                    $ icon = 'Menu/upgrade_phoenix_button.png'
                    $ hovericon = 'Menu/upgrade_phoenix_button_hover.png'
                elif iconship.name == 'Seraphim':
                    $ icon = 'Menu/upgrade_seraphim_button.png'
                    $ hovericon = 'Menu/upgrade_seraphim_hover.png'
                elif iconship.name == 'Bianca':
                    $ icon = 'Menu/upgrade_bianca_button.png'
                    $ hovericon = 'Menu/upgrade_bianca_hover.png'
                elif iconship.name == 'Paladin':
                    $ icon = 'Menu/upgrade_paladin_button.png'
                    $ hovericon = 'Menu/upgrade_paladin_button_hover.png'

                imagebutton:
                    xpos xposition
                    ypos yposition
                    action Return( ['selection',iconship] )
                    idle icon
                    hover hovericon
                    focus_mask True

                $ count += 1
        
screen skirmishhelp:
    
    frame:
        xalign 0.5
        ypos 0.2
        xminimum 600
        # xmaximum 600
        yminimum 300
        ymaximum 800
        background Solid((0,0,0,200))
        
        vbox:
            text "Welcome to skirmish mode! Here, you will be able to refine your strategies by fighting custom battles."
            text "Click on ADD PLAYER SHIPS and click and drop your units to the map. Do the same to add enemy units."
            text "Pressing SHIFT allows you to add the selected unit multiple times to the map."
            text "Pressing the MIDDLE MOUSE BUTTON allows you to instantly grab the next player unit from the player pool."
            text "To remove placed units, simply press the REMOVE button, then click on the unit you wish to remove."
            text "You may set the amount of usable command points during the battle using the buttons on the player pool bar."
            text "However, you will not earn any money or command points in Skirmish Mode."
            
            textbutton "PROCEED":
                xalign 0.5
                action Hide('skirmishhelp')

screen battle_log():
    default filter_all      = True
    default filter_system   = True
    default filter_order    = True
    default filter_attack   = True
    default filter_kinetic  = True
    default filter_laser    = True
    default filter_missile  = True
    default filter_melee    = True
    default filter_details  = False
    default filter_support  = True
    default filter_heal     = True
    default filer_buff      = True
    default filter_debuff   = True
    default log_tags        = set(['all', 'system', 'player', 'enemy', 'order', 'attack', 'detailed', 'laser', 'kinetic', 'missile', 'melee', 'support', 'heal', 'buff', 'debuff'])
    drag:
        xalign 0.5
        ypos 0.2
        frame:
            xpadding 10
            ypadding 10
            xalign 0.5
            ypos 0.2
            xminimum 800
            xmaximum 900
            yminimum 100
            ymaximum 400
            background Solid((0,0,0,200))
            vbox:
                hbox:
                    xfill True
                    hbox:
                        # re-evaluation should update filter_all in case if all other are enabled
                        if filter_system and filter_attack and filter_details and filter_support and filter_order:
                            $filter_all = True
                        else:
                            $filter_all = False
                        label "Filters:":
                            right_padding 10
                        textbutton "all":
                            action If(filter_all, true=[ToggleScreenVariable("filter_all"),
                                                        SetScreenVariable("filter_system", False),
                                                        SetScreenVariable("filter_attack", False),
                                                        SetScreenVariable("filter_laser", False),
                                                        SetScreenVariable("filter_kinetic", False),
                                                        SetScreenVariable("filter_missile", False),
                                                        SetScreenVariable("filter_melee", False),
                                                        SetScreenVariable("filter_details", False),
                                                        SetScreenVariable("filter_support", False),
                                                        SetScreenVariable("filter_heal", False),
                                                        SetScreenVariable("filter_buff", False),
                                                        SetScreenVariable("filter_debuff", False),
                                                        SetScreenVariable("filter_order", False),
                                                        SelectedIf(filter_all)],
                                                 false=[ToggleScreenVariable("filter_all"),
                                                        SetScreenVariable("filter_system", True),
                                                        SetScreenVariable("filter_attack", True),
                                                        SetScreenVariable("filter_laser", True),
                                                        SetScreenVariable("filter_kinetic", True),
                                                        SetScreenVariable("filter_missile", True),
                                                        SetScreenVariable("filter_melee", True),
                                                        SetScreenVariable("filter_details", True),
                                                        SetScreenVariable("filter_support", True),
                                                        SetScreenVariable("filter_heal", True),
                                                        SetScreenVariable("filter_buff", True),
                                                        SetScreenVariable("filter_debuff", True),
                                                        SetScreenVariable("filter_order", True),
                                                        SelectedIf(filter_all)])
                        textbutton "system":
                            action [ToggleScreenVariable("filter_system")]
                        textbutton "order":
                            action [ToggleScreenVariable("filter_order")]
                        if filter_attack:
                            textbutton "attack":
                                action [ToggleScreenVariable("filter_attack"),
                                        SetScreenVariable("filter_laser", True),
                                        SetScreenVariable("filter_kinetic", False),
                                        SetScreenVariable("filter_missile", False),
                                        SetScreenVariable("filter_melee", False),
                                        SelectedIf(filter_attack)]
                        elif filter_laser:
                            textbutton "laser":
                                action [ToggleScreenVariable("filter_laser"), ToggleScreenVariable("filter_kinetic"), SelectedIf(filter_laser)]
                        elif filter_kinetic:
                            textbutton "kinetic":
                                action [ToggleScreenVariable("filter_kinetic"), ToggleScreenVariable("filter_missile"), SelectedIf(filter_kinetic)]
                        elif filter_missile:
                            textbutton "missile":
                                action [ToggleScreenVariable("filter_missile"), ToggleScreenVariable("filter_melee"), SelectedIf(filter_missile)]
                        elif filter_melee:
                            textbutton "melee":
                                    action [ToggleScreenVariable("filter_melee")]
                        else: #means attack is not selected
                            textbutton "attack":
                                action [ToggleScreenVariable("filter_attack"),
                                        SetScreenVariable("filter_laser", True),
                                        SetScreenVariable("filter_kinetic", True),
                                        SetScreenVariable("filter_missile", True),
                                        SetScreenVariable("filter_melee", True),
                                        SelectedIf(filter_attack)]
                        if filter_support:
                            textbutton "support":
                                action [ToggleScreenVariable("filter_support"),
                                        SetScreenVariable("filter_heal", True),
                                        SetScreenVariable("filter_buff", False),
                                        SetScreenVariable("filter_debuff", False),
                                        SelectedIf(filter_support)]
                        elif filter_heal:
                            textbutton "heal":
                                action [ToggleScreenVariable("filter_heal"), ToggleScreenVariable("filter_buff"), SelectedIf(filter_heal)]
                        elif filter_buff:
                            textbutton "buff":
                                action [ToggleScreenVariable("filter_buff"), ToggleScreenVariable("filter_debuff"), SelectedIf(filter_buff)]
                        elif filter_debuff:
                            textbutton "debuff":
                                    action [ToggleScreenVariable("filter_debuff")]
                        else: #means that support is not selected
                            textbutton "support":
                                action [ToggleScreenVariable("filter_support"),
                                        SetScreenVariable("filter_heal", True),
                                        SetScreenVariable("filter_buff", True),
                                        SetScreenVariable("filter_debuff", True),
                                        SelectedIf(filter_support)]
                        textbutton "details":
                            action [ToggleScreenVariable("filter_details")]
                            
                    textbutton "X":
                        xalign 1.0
                        action Hide('battle_log')

                side "c r":
                    viewport:
                        id 'battle log'
                        xmaximum 900
                        yinitial 1.0
                        yadjustment BM.battle_log_yadj
                        mousewheel True

                        vbox:
                            #if flag all is true then all tags are enabled
                            if filter_all:
                                $log_tags = set(['all', 'system', 'player', 'enemy', 'order', 'attack', 'detailed', 'laser', 'kinetic', 'missile', 'melee', 'support', 'heal', 'buff', 'debuff'])
                            else:
                                #otherwise we check which tags should be enabled
                                $log_tags = set([])
                                if filter_system:
                                    $log_tags.add('system')
                                if filter_order:
                                    $log_tags.add('order')
                                if filter_attack:
                                    $log_tags.update(set(['attack', 'laser', 'kinetic', 'missile', 'melee']))
                                else:
                                    if filter_laser:
                                        $log_tags.add('attack')
                                        $log_tags.add('laser')
                                    if filter_kinetic:
                                        $log_tags.add('attack')
                                        $log_tags.add('kinetic')
                                    if filter_missile:
                                        $log_tags.add('attack')
                                        $log_tags.add('missile')
                                    if filter_melee:
                                        $log_tags.add('attack')
                                        $log_tags.add('melee')
                                if filter_details:
                                    $log_tags.add('detailed')
                                if filter_support:
                                    $log_tags.update(set(['support', 'heal', 'buff', 'debuff']))
                                else:
                                    if filter_heal:
                                        $log_tags.add('support')
                                        $log_tags.add('heal')
                                    if filter_buff:
                                        $log_tags.add('support')
                                        $log_tags.add('buff')
                                    if filter_debuff:
                                        $log_tags.add('support')
                                        $log_tags.add('debuff')
                            for type, entry in BM.battle_log:
                                #To be printed log's tags should contain tags which are stored in filter
                                if log_tags.issuperset(set(type)):
                                    text entry
                                    
                    vbar:
                        value YScrollValue('battle log')
                        hovered SetField(BM, 'draggable', False)
                        unhovered SetField(BM, 'draggable', True)

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

    if BM.battlemode:
        for a in range(80):
            $randint = renpy.random.randint(50,150)
            $randx = renpy.random.random()
            $randy = renpy.random.random()
            $randt = renpy.random.randint(100,600) / 100.0
    #        text 'Game Over!' xpos randx ypos randy size randint at gameovergimmick(randx,randy, randt)
            add 'Battle UI/label_pactbattleship.png' xpos randx ypos randy zoom (randint / 300.0) at gameovergimmick(randx,randy, randt)
            
screen debug_window:
    zorder 100
    # modal True

    drag:
        xalign 0.5
        ypos 0.2
        frame:
            xpadding 10
            ypadding 10
            xalign 0.5
            ypos 0.2
            xminimum 800
            xmaximum 900
            yminimum 100
            ymaximum 400
            background Solid((0,0,0,200))
            
            vbox:
                hbox:
                    xfill True
                    label 'debug log'
                    textbutton 'clear':
                        xalign 1.0
                        action SetField(BM,'debug_log',[])
                    textbutton "X":
                        xalign 1.0
                        action Hide('debug_window')            
            
                side "c r":
                    viewport:
                        id 'debug log'
                        yinitial 1.0
                        vbox:
                            for entry in BM.debug_log:
                                text str(entry)
                    vbar:
                        value YScrollValue('debug log')
                        hovered SetField(BM, 'draggable', False)
                        unhovered SetField(BM, 'draggable', True)        
            
        