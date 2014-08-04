label initStore:
    python:
        store_items = []
        #syntax: StoreItem(item id, visibility condition, display name, cost, actions, tool-tip, (optional)itemcount variable, (optional)maximum amount)

        actions = [SetField(sunrider,'rockets',eval('sunrider.rockets') + 1)]
        tooltip = 'Purchase warheads to allow the Sunrider to fire powerful rockets at the enemy. A rocket deals {} damage, but can be shot down by enemy flak. The Sunrider can carry a maximum of 2 at a time.'.format(sunrider.weapons[3].damage)
        StoreItem('Rockets', 'True', "Warhead Ammo", 300, actions, tooltip, 'sunrider.rockets', 2)

        actions = [SetField(store.sunrider_rocket,'damage',1200)]
        tooltip = 'While the proliferation of nuclear warheads throughout the galaxy has made them readily available, more powerful weapons are regulated closely by the Alliance. With the payment of appropriate fees, the Union can replace your current stock of nuclear warheads with quantum warheads, permanently increasing the Sunrider\'s rocket damage to 1200.'
        StoreItem('Rocketupgrade1', 'sunrider_rocket.damage < 1200', "Quantum Torpedo License", 2000, actions, tooltip)

        ## this has got to be the stupidest workaround I've ever needed -_-
        ## wasted way too much time dealing with the constant crashing when sunrider.repair_drones == None
        no_repairbots = False
        if sunrider.repair_drones == None:
            no_repairbots = True
            sunrider.repair_drones = 0
            
        actions = [SetField( sunrider,'repair_drones',eval('sunrider.repair_drones+1') )]   #bah
        tooltip = 'These autonomous robots can rapidly restore destroyed hull sections as well as complex electronic systems. They are a must have for all hostile operations.  Restores 50% of the Sunrider\'s HP on use. The Sunrider can carry a maximum of 8 at a time.'
        StoreItem('repair drones', 'sunrider.repair_drones != None', "Repair Drones", 400, actions, tooltip, 'sunrider.repair_drones', 8)
        if no_repairbots:
            sunrider.repair_drones = None

        # I had to put this here or it would crash
        alliancecruiser_weapons = [AllianceCruiserLaser(),AllianceCruiserMissile(),AllianceCruiserKinetic(),AllianceCruiserAssault()]

        actions = [CreateShipAction(AllianceCruiser(),alliancecruiser_weapons)]
        tooltip = ''
        StoreItem('alliance cruiser', 'store.mission12_complete or paladin != None', "Alliance Cruiser", 2000, actions, tooltip)

        # TODO
        unionfrigate_weapons = []

        actions = [CreateShipAction(UnionFrigate(),unionfrigate_weapons)]
        tooltip = ''
        StoreItem('union frigate', 'True', "Union Frigate", 750, actions, tooltip)

    return

screen store_union:
    modal True
    tag storyscreen

    #$ renpy.call_in_new_context('initStore')

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
            for item in store_items:
                if item.isVisible():
                    imagebutton:
                        action If(BM.money >= item.cost and (item.variable_name is None or eval(item.variable_name) < item.max_amt),item.actions,NullAction())
                        idle "Menu/store_item.png"
                        hover "Menu/store_item_hover.png"
                        hovered SetField(BM,'hovered',item.id)
                        unhovered SetField(BM,'hovered',None)
        vbox:
            for item in store_items:
                if item.isVisible():
                    text item.display_name + ("    [[owned:{!s}]".format(eval(item.variable_name)) if item.max_amt != -1 else "") font "Font/sui generis rg.ttf" size 30 first_indent 50 line_spacing 38 color "#0a0a0a"
        vbox:
            for item in store_items:
                if item.isVisible():
                    text str(item.cost) font "Font/sui generis rg.ttf" size 30 first_indent 710 line_spacing 38 color "#0a0a0a"

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
        
        for item in store_items:
            if BM.hovered == item.id:
                text item.display_name xpos 50 ypos 50 size 35 font "Font/sui generis rg.ttf" color '000'
                text item.tooltip xpos 50 ypos 150 size 20 font "Font/GOTHIC.TTF" color '000'



# screen store_missile:
    # add "Menu/unionstore_missiles.png" xpos 1170 ypos 200

# screen store_rocket:
    # add "Menu/unionstore_rocket.png" xpos 1170 ypos 200