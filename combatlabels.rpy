## this file is a horrible mishmash of experimental code that often end up used in the game
## many of this stuff should be organized in other files...

init:
    image black = Solid((0, 0, 0, 255))

label testpause:
    python:
        renpy.pause(1)
        
    return

transform shake(time=0.5,repeats=20): #defunct?
    xalign 0.5 yalign 0.5
    pause time
    block:
        ease 0.01 xpos 0.51
        ease 0.02 xpos 0.49
        ease 0.01 xpos 0.5
        repeat repeats

label test_battle:
    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []
        BM.mission = 'test'
        
        BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']

        #create the sunrider. you only have to create a player ship once:
        sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault()]
        sunrider = create_ship(Sunrider(),(8,6),sunrider_weapons)

        blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
        blackjack = create_ship(BlackJack(),(10,5),blackjack_weapons)

        liberty_weapons = [LibertyLaser(),Repair(),AccUp(),DamageUp(),AccDown()]
        liberty = create_ship(Liberty(),(8,7),liberty_weapons)

        phoenix_weapons = [PhoenixMelee(),Stealth(),GravityGun()]
        phoenix = create_ship(Phoenix(),(10,7),phoenix_weapons)

        create_ship(Havoc(),(13,5),[Melee(),HavocAssault(),HavocMissile(),HavocRocket()])
        enemy_ships[-1].hp = 1
        create_ship(PactSupport(),(14,5))
        # create_ship(PirateGrunt(),(13,7),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        # create_ship(PirateGrunt(),(13,6),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        # create_ship(PirateGrunt(),(13,8),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        # create_ship(PactCruiser(),(14,8),[])

        # create_ship(PirateDestroyer(),(16,5),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        # create_ship(PirateDestroyer(),(16,7),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Dusty_Universe.ogg"

#    $ buy_upgrades() ##testing

    jump battle_start
    return

label missiontest:

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump missiontest #loop back
    else:
        pass #continue down

    # jump dispatch
    return
    
  
  
  
label endofturn:
    show screen battle_screen
    $update_stats()

    if not BM.phase == 'Player':
        play sound1 'sound/battle.wav'
        show sunrider_phase onlayer screens zorder 50
        pause TURN_SPEED
        play sound2 'sound/drum.ogg'
        hide sunrider_phase onlayer screens zorder 50 with dissolve
        $ BM.phase = 'Player'
    elif BM.phase == 'Player' and enemy_ships[0].faction == 'PACT':
        play sound1 'sound/battle.wav'
        show PACT_phase onlayer screens zorder 50
        pause TURN_SPEED
        play sound2 'sound/drum.ogg'
        hide PACT_phase onlayer screens zorder 50 with dissolve
        $ BM.phase = 'PACT'
    elif BM.phase == 'Player' and enemy_ships[0].faction == 'Pirate':
        play sound1 'sound/battle.wav'
        show Pirate_phase onlayer screens zorder 50
        pause TURN_SPEED
        play sound2 'sound/drum.ogg'
        hide Pirate_phase onlayer screens zorder 50 with dissolve
        $ BM.phase = 'Pirate'

    $update_modifiers() #update buffs and curses

    if BM.phase == 'Player':
        $ renpy.take_screenshot()
        $ renpy.save('beginturn')

    return

    
label battle_start:
    play music PlayerTurnMusic
    python:
        BM.stopAI = False
        BM.order_used = False
        renpy.take_screenshot()
        renpy.save('battlestart')
        renpy.take_screenshot()
        renpy.save('beginturn')
        if BM.show_tooltips:
            renpy.show_screen('tooltips')
        # BM.xadj.value = 872
        # BM.yadj.value = 370
        for ship in player_ships:
            ship.hp = ship.max_hp
            ship.en = ship.max_en
        # renpy.show_screen('mousefollow')
        store.zoomlevel = 0.65
        BM.show_grid = False
        sort_ship_list()
        BM.start()


    return

label sunrider_destroyed:
    hide screen commands
    hide screen battle_screen
    scene badend

    $ BM.phase = 'Player' #this makes it so you can save and load again, as it's normally blocked during the enemy's turn

    menu:
        "Try Again":
            jump tryagain

        "Load Saved Game":
            jump loadsavedgame

    return

label loadsavedgame:   #used when the player chooses to load a saved game after game over
    show screen load
    pause
    jump sunrider_destroyed
    return

label tryagain:
    $renpy.load('battlestart')
    pause
    $show_message('this should never show up')
    pause
    return

label restartturn:
    $renpy.load('beginturn')
    pause
    $show_message('this should never show up')
    pause
    return

label after_load:

    python:
        reset = False
        if not hasattr(store,'BM'):
            BM = Battle()
            MasterBM = BM
        if hasattr(BM,'save_version'):
            if BM.save_version != config.version:
                reset = True
            else:
                pass #everything is fine, do not reset
        else:
            reset = True

        if reset:
            
            #replace old union frigates with new ones
            for ship in player_ships[:]:
                if ship.name == 'Mining Union Frigate':
                    if len(ship.weapons) == 1:
                        create_ship(UnionFrigate(),ship.location)
                        player_ships.remove(ship)
        
            #temporary fix
            rocketdamage = 800
            chi_repair = 300
            
            if hasattr(store,'sunrider_rocket'):
                rocketdamage = store.sunrider_rocket.damage
            if hasattr(store,'chigara_repair'):
                chi_repair = store.liberty.weapons[1].damage
                
            reset_classes()
            
            if sunrider != None:
                store.sunrider.weapons[3].damage = rocketdamage
            if liberty != None:
                store.liberty.weapons[1].damage = chi_repair                
            
            BM.save_version = config.version
            
            if store.mission2_complete:
                res_location = "lab"
                res_event = "allocatefunds"             

        #cleanup
        if hasattr(BM,'ships') and hasattr(store,'player_ships') and hasattr(store,'enemy_ships'):
            if BM.ships != []:
                BM.ships = []
                for ship in player_ships:
                    BM.ships.append(ship)
                for ship in enemy_ships:
                    BM.ships.append(ship)
    return




