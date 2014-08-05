screen upgrade:
    modal True

    add "Menu/upgrade_back.jpg"

    text '{!s}$'.format(BM.money):
        size 50
        xpos 0.15
        ypos 0.7
        color '090'
        outlines [(1,'000',0,0)]

    # imagebutton:
        # xpos 0.05 ypos 925
        # action Return("submit")
        # idle "Menu/submit.jpg"
        # hover "Menu/submit_hover.jpg"

    imagebutton:
        xpos 0.05 ypos 975
        action Return("quit")
        idle "Menu/return.jpg"
        hover "Menu/return_hover.jpg"

    if BM.selected == None:
        $ BM.selected = sunrider
    $ ship = BM.selected

    $ can_use_melee = False
    for weapon in ship.weapons:
        if weapon.wtype == 'Melee':
            $ can_use_melee = True
    $ uses_kinetics = False
    for weapon in ship.weapons:
        if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
            $ uses_kinetics = True
    $ uses_lasers = False
    for weapon in ship.weapons:
        if weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
            $ uses_lasers = True

    #dictionaries are inherently unsorted, so this is needed ;_;
    $ upgrade_list = []
    $ upgrade_list.append(["BASIC -----------",None,None,None,None])
    $ upgrade_list.append(ship.upgrades['max_hp'])
    $ upgrade_list.append(ship.upgrades['max_en'])
    $ upgrade_list.append(ship.upgrades['evasion'])
#    $ upgrade_list.append(ship.upgrades['move_cost'])  #probably should be set individually in design

    if uses_kinetics:
        $ upgrade_list.append(["KINETIC -----------",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['kinetic_dmg'])
        $ upgrade_list.append(ship.upgrades['kinetic_acc'])
        $ upgrade_list.append(ship.upgrades['kinetic_cost'])

    if uses_lasers:
        $ upgrade_list.append(["LASER -----------",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['energy_dmg'])
        $ upgrade_list.append(ship.upgrades['energy_acc'])
        $ upgrade_list.append(ship.upgrades['energy_cost'])

    if ship.max_missiles > 0:
        $ upgrade_list.append(["MISSILE -----------",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['missile_dmg'])
        $ upgrade_list.append(ship.upgrades['missile_eccm'])
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
    if ship == phoenix:
        add "Menu/upgrade_phoenix.png"
    if ship == bianca:
        add "Menu/upgrade_bianca.png"
    if ship == seraphim:
        add "Menu/upgrade_seraphim.png"
    if ship == paladin:
        add "Menu/upgrade_paladin.png"

    if config.developer:
        textbutton 'DEBUG: reset upgrades (refunds money)':
            xalign 1.0
            ypos 0.0
            text_size 30
            text_color 'fff'
            text_outlines [(1,'000',0,0)]
            action Return('reset')

    ## show icons of all the player ships in player_ships
    $ count = 0
    for iconship in player_ships:
        if not iconship.mercenary:
            $ icon = None
            $ hovericon = None
            $ xposition = 1640
            if count % 2 != 0:
                $ xposition = 1758
            $ yposition = 441 + count * 70

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
                action SetField(BM,'selected',iconship)
                idle icon
                hover hovericon
                focus_mask True

            $ count += 1

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
                            text name:
                                color '000'
                                min_width 460

                            if increase < 1:
                                text str(current*100)+'% -> '+ str((current+increase)*100)+'%':
                                    color '000'
                                    min_width 260
                            else:
                                text str(current)+' -> '+ str(current+increase):
                                    color '000'
                                    min_width 260

                            text str(level):
                                color '000'
                                min_width 110
                            text str(cost):
                                color '000'
                                min_width 120

                            if BM.money >= cost:
                                textbutton '+':
                                    text_color 'fff'
                                    action Return(['+', attribute])
                                    hovered SetField(BM,'active_upgrade',upgrade)
                                    unhovered SetField(BM,'active_upgrade',None)
                            else:
                                textbutton 'X':
                                    text_color 'c00'
                                    action NullAction()
                                    hovered SetField(BM,'active_upgrade',upgrade)
                                    unhovered SetField(BM,'active_upgrade',None)

                            if level > 1:
                                textbutton '-':
                                    text_color 'fff'
                                    action Return(['-', attribute])
                                    hovered SetField(BM,'active_upgrade',upgrade)
                                    unhovered SetField(BM,'active_upgrade',None)
                                    

      ##show weapon icons and their stats##
    if BM.active_upgrade != None:
        $ name,level,increase,cost,multiplier = BM.active_upgrade
        $ quantifier = ''
        if increase < 1 or name == 'Missile Flak Resistance':
            $ type = None
            if name.find('Damage') != -1:
                $ type = 'damage'
                $ quantifier = 'DMG'
            if name.find('Accuracy') != -1:
                $ type = 'accuracy'
                $ quantifier = '%'
            if name.find('Energy Cost') != -1:
                $ type = 'energy_use'
                $ quantifier = 'EN'
            if name.find('Flak Resistance') != -1:
                $ type = 'eccm'
                $ quantifier = ' Flak Resistance'

            $ count = 0
            for weapon in ship.weapons:
                if name.find( weapon_type(weapon) ) == 0:
                    add weapon.lbl:
                        ypos (750 + count*140)
                        xpos 480
                    frame:
                        background Solid((255,255,255,255))
                        xpos 640
                        ypos (820 + count*140)
                        yanchor 0.5

                        has vbox

                        $ stat = getattr(weapon,type)
                        if increase < 1:
                            $ current = int(stat * (1.0+increase*(level-1)) )
                            $ next = int(stat * (1.0+increase * level ))
                        else:
                            $ current = stat + increase * (level-1)
                            $ next = stat + increase * level

                        if weapon.wtype == 'Rocket':
                            $ stat += 10

#                        text weapon.name:
#                            color '000'
                        text str(current)+quantifier+' -> '+ str(next) + quantifier:
                            color '000'

                    $ count += 1
