## this file is a horrible mishmash of experimental code that often end up used in the game
## many of this stuff should be organized in other files...

init:
    image black = Solid((0, 0, 0, 255))

label testpause:
    python:
        renpy.pause(1)

    return
    
label RnD_skirmish:

    window hide

    python:
        store.xadj = ui.adjustment()
        store.yadj = ui.adjustment()
        BM.active_upgrade = None
        buy_upgrades()
    
jump mission_skirmish

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

        blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse(),AwakenAsaga()]
        blackjack = create_ship(BlackJack(),(10,5),blackjack_weapons)

        liberty_weapons = [LibertyLaser(),Repair(),AccUp(),DamageUp(),AccDown()]
        liberty = create_ship(Liberty(),(8,7),liberty_weapons)

        phoenix_weapons = [PhoenixMelee(),Stealth(),GravityGun()]
        phoenix = create_ship(Phoenix(),(10,7),phoenix_weapons)

        create_ship(Havoc(),(13,5),[Melee(),HavocAssault(),HavocMissile(),HavocRocket()])
        enemy_ships[-1].name = 'Legion' #testing out the new cannon
        havoc = enemy_ships[-1]

        # enemy_ships[-1].hp = 1
        # create_ship(PactSupport(),(14,5))
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
        $ renpy.pause(TURN_SPEED, hard=True)
        play sound2 'sound/drum.ogg'
        hide sunrider_phase onlayer screens zorder 50 with dissolve
        $ BM.phase = 'Player'
    else:
        if len(enemy_ships) > 0:
            if enemy_ships[0].faction == 'PACT':
                play sound1 'sound/battle.wav'
                show PACT_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide PACT_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'PACT'
            elif enemy_ships[0].faction == 'Pirate':
                play sound1 'sound/battle.wav'
                show Pirate_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide Pirate_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'Pirate'
        else:
            if destroyed_ships[-1].faction == 'PACT':
                play sound1 'sound/battle.wav'
                show PACT_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide PACT_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'PACT'
            elif destroyed_ships[-1].faction == 'Pirate':
                play sound1 'sound/battle.wav'
                show Pirate_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
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
        BM.battlestart.player_ships = store.player_ships[:]
        for ship in BM.battlestart.player_ships:
            ship.battlestart_location = ship.location
        BM.battlestart.enemy_ships = deepcopy(store.enemy_ships)
        BM.battlestart.covers = deepcopy(BM.covers)
        BM.battlestart.sunrider_rockets = sunrider.rockets
        BM.battlestart.sunrider_repair_drones = sunrider.repair_drones
        BM.battlestart.cmd = BM.cmd
        BM.stopAI = False
        BM.order_used = False
        BM.enemy_vanguard_path = []
        BM.player_vanguard_path = []
        BM.active_strategy = [None,0]
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
    hide badend
    $ clean_battle_exit(True)
    python:
        store.battle1_check1 = False
        store.battle2_check1 = False
        store.battle2_check2 = False
        store.battle_check1 = False
        i = 1
        while True:
            if hasattr(store, 'check{}'.format(i)):
                setattr(store, 'check{}'.format(i), False)
                i += 1
            else:
                break
        
        try:
            store.destroyed_ships = []
            store.player_ships = BM.battlestart.player_ships
            for ship in store.player_ships:
                ship.missiles = ship.max_missiles
                ship.location = ship.battlestart_location
            sunrider.rockets = BM.battlestart.sunrider_rockets
            sunrider.repair_drones = BM.battlestart.sunrider_repair_drones
            BM.cmd = BM.battlestart.cmd
            BM.turn_count = 1
            
            store.enemy_ships = BM.battlestart.enemy_ships
            for ship in store.enemy_ships:
                if isinstance(ship, Havoc):
                    store.havoc = ship
            
            BM.covers = BM.battlestart.covers
            for cover in BM.covers:
                cover.hp = cover.max_hp
        except:
            renpy.jump('tryagain_old')
        BM.ships = []
        for ship in store.player_ships:
            BM.ships.append(ship)
        for ship in store.enemy_ships:
            BM.ships.append(ship)
        
        BM.grid = []
        for a in range(GRID_SIZE[0]):
            BM.grid.append([False]*GRID_SIZE[1])
        for ship in BM.ships:
            if ship.location == None:
                continue
            x, y = ship.location
            BM.grid[x - 1][y - 1] = True
    jump battle_start
    return

# this is just kept for compatability
label tryagain_old:
    $ renpy.load('battlestart')
    pause
    $ show_message('this should never show up')
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

        #used by skirmish
        if not hasattr(store,'all_enemies'):
            add_enemy_list()

        ##debugging stuff##
        # renpy.hide_screen('battle_screen')
        # if not hasattr(BM,'show_tooltips'): BM.show_tooltips = True
        # if not hasattr(BM,'debugoverlay'): BM.debugoverlay = False
        # if not hasattr(BM,'warping'): BM.warping = False
        # if not hasattr(BM,'enemy_vanguard_path'): BM.enemy_vanguard_path = []
        # if not hasattr(BM,'vanguardtarget'): BM.vanguardtarget = None
        # if not hasattr(BM,'show_grid'): BM.show_grid = True

        if not hasattr(store,'BM'): BM = Battle()
        if not hasattr(BM,'debug_log'): BM.debug_log = []

        # return_stack = renpy.get_return_stack()
        # for item in return_stack:
            # BM.debug_log.append(str(item) )
        # renpy.show_screen('debug_window')
        # renpy.pause()

        #check if the classes should be reset
        reset = False
        if not hasattr(store,'BM'):
            store.BM = Battle()
            store.MasterBM = BM
        if hasattr(store.BM,'save_version'):
            if store.BM.save_version != config.version:
                reset = True
            else:
                pass #everything is fine, do not reset
        else:
            reset = True

        if reset:

            # #update the multipersistent object with the most critical flags.
            # update_mp()

            #add the restore skill to Bianca if she doesn't have it (due to very old save)
            if hasattr(store,'bianca'):
                if bianca is not None:
                    if len(bianca.weapons) == 4:
                        ship.register_weapon(Restore())
                else:
                    bianca = Bianca()
                    bianca.weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
                
            #this was reduced in 7.2
            store.BM.formation_range = 6
                
            #some backwards compatibility with previously bought store items.
            if hasattr(store,'sunrider_rocket'):
                if store.sunrider_rocket.damage == 1200:
                    if not hasattr(store.sunrider_rocket,'keep_after_reset'):
                        store.sunrider_rocket.keep_after_reset = {}
                    store.sunrider_rocket.keep_after_reset['damage'] = 1200
            if hasattr(store,'chigara_repair'):
                if store.chigara_repair.damage == 500:
                    if not hasattr(store.chigara_repair,'keep_after_reset'):
                        store.chigara_repair.keep_after_reset = {}
                    store.chigara_repair.keep_after_reset['damage'] = 500
                    store.chigara_repair.keep_after_reset['energy_use'] = 70

            #updates the BM, ships and weapons used so that new default values are added.
            reset_classes()

            #set the new save version
            store.BM.save_version = config.version

            #make sure the player can access the lab
            if store.mission2_complete:
                res_location = "lab"
                res_event = "allocatefunds"

        #attempt to supply a fail-safe label if the return label does not exist.
        #this requires a very recent (unreleased) version of renpy to work!
        # try:
            # return_stack = renpy.get_return_stack()
            # new_stack = []
            # for item in return_stack:
                # if renpy.has_label(item):
                    # new_stack.append(item)
                # else:
                    # BM.debug_log.append('return label {} missing'.format(str(item)))
                    # fail_safe_label = 'dispatch'
                    # if BM.battlemode:
                        # fail_safe_label = 'mission{}'.format(BM.mission)
                    # new_stack.append(fail_safe_label)
            # renpy.set_return_stack(new_stack)
        # except:
            # pass
            # show_message('there was an error in the return stack code')
            # BM.debug_log.append('there was an error in the return stack code')

    return




