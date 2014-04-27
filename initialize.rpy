##this module does boring init work so that the script module is more
##accessible and readable

#1) initialize sound channels
#2) init images and backgrounds
#3) init classes and functions (not needed?)

init -10 python:
    ## a few constants
    TURN_SPEED = 0.5  #in seconds
    MOVE_IN_SPEED = 0.5 #for buttons and status displays
    MOVE_OUT_SPEED = 0.5
    MESSAGE_PAUSE = 0.75
    ZOOM_SPEED = 0.1
    GRID_SIZE = (18,16)
    BM = renpy.store.object()
    BM.phase = None

init -1 python:   #create sound channels for simultanious sfx playback
    renpy.music.register_channel("sound1", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound5", "sfx", False)
    renpy.music.register_channel("sound6", "sfx", False)
    renpy.music.register_channel("sound7", "sfx", False)
    renpy.music.register_channel("sound8", "sfx", False)
    renpy.music.register_channel("sound9", "sfx", False)

    renpy.music.register_channel("avavoice", "voice", False)
    renpy.music.register_channel("asavoice", "voice", False)
    renpy.music.register_channel("chivoice", "voice", False)
    renpy.music.register_channel("cosvoice", "voice", False)
    renpy.music.register_channel("kryvoice", "voice", False)
    renpy.music.register_channel("icavoice", "voice", False)
    renpy.music.register_channel("clavoice", "voice", False)
    renpy.music.register_channel("solvoice", "voice", False)
    renpy.music.register_channel("kayvoice", "voice", False)
    renpy.music.register_channel("othvoice", "voice", False)

    #set music volume to 75%. This is seperate from the setting in preferences screen!
    renpy.music.set_volume(0.75)

    Difficulty = 2

init -5:
    image sunrider_phase:
        'gameplay/sunrider_phase.png'
        xalign 0.5
        yalign 0.5
        zoom 5
        easeout TURN_SPEED zoom 1
    image PACT_phase:
        'gameplay/pact_phase.png'
        xalign 0.5
        yalign 0.5
        zoom 5
        easeout TURN_SPEED zoom 1
    image Pirate_phase:
        'gameplay/pirate_phase.png'
        xalign 0.5
        yalign 0.5
        zoom 5
        easeout TURN_SPEED zoom 1

label initialize:
    python:
        BM = Battle() #create an instance of the battle manager which keeps track of lots of things
        player_ships = []
        sunrider = None
        blackjack = None
        liberty = None

    return

label mission1_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        #create the sunrider. you only have to create a player ship once:
        sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault()]
        sunrider = create_ship(Sunrider(),(5,6),sunrider_weapons)

        create_ship(MissileFrigate(),(13,5),[PactFrigateMissile()])
        create_ship(MissileFrigate(),(13,7),[PactFrigateMissile()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Dusty_Universe.ogg"

    return

label mission2_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        #sunrider was already created before mission 1, no need to do so again.
        #we just need to reset it's location:
        sunrider.set_location(5,6)

        create_ship(PirateGrunt(),(13,5),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(13,7),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(Havoc(),(14,6),[HavocAssault(),HavocMissile(),HavocRocket()])
        create_ship(PirateDestroyer(),(16,5),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        create_ship(PirateDestroyer(),(16,7),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = None
    $ EnemyTurnMusic = "music/Sui_Generis.ogg"

    return

label mission3_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        #sunrider gets a new location and a new weapon
        sunrider.set_location(4,6) #reset the location of the sunrider.

        if blackjack == None: # it's possible the player killed havoc in the first turn on low difficulty
            blackjack_weapons = [BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
            blackjack = create_ship(BlackJack(),(6,3),blackjack_weapons)
        blackjack.set_location(5,5)
        liberty.set_location(5,7)

        create_ship(PirateGrunt(),(14,4),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(13,5),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(12,6),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(13,7),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(14,8),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])

        create_ship(PirateBomber(),(14,5),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])
        #create_ship(PirateBomber(),(13,6),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])
        create_ship(PirateBomber(),(14,7),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])

        create_ship(PirateDestroyer(),(15,5),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        create_ship(PirateDestroyer(),(15,6),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        create_ship(PirateDestroyer(),(15,7),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Sui_Generis.ogg"

    return

label mission4_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        if blackjack == None: # it shouldn't be possible to kill Havoc on the first turn, but if the player did...
            blackjack_weapons = [BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
            blackjack = create_ship(BlackJack(),(6,3),blackjack_weapons)

        #we only have to set new locations for the player ships
        sunrider.set_location(4,6)
        blackjack.set_location(5,5)
        liberty.set_location(5,7)

        create_ship(PactMook(),(12,6),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(11,4),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(12,8),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(MissileFrigate(),(16,4),[PactFrigateMissile()])
        create_ship(MissileFrigate(),(16,8),[PactFrigateMissile()])

        create_ship(PactCruiser(),(14,6),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])

        create_ship(PactOutpost(),(13,6),[PACTOutpostLaser(),PACTOutpostKinetic()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Dusty_Universe.ogg"

    return

label mission5_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        if blackjack == None: # it shouldn't be possible to kill Havoc on the first turn, but if the player did...
            blackjack_weapons = [BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
            blackjack = create_ship(BlackJack(),(6,3),blackjack_weapons)

        #all should already exist (and maybe improved!)
        sunrider.set_location(4,6)
        blackjack.set_location(5,5)
        liberty.set_location(5,7)

        create_ship(PirateGrunt(),(10,5),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(11,4),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        #create_ship(PirateGrunt(),(12,3),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])

        create_ship(PirateGrunt(),(10,7),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(11,8),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        #create_ship(PirateGrunt(),(12,9),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])

        create_ship(PirateBomber(),(11,5),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])
        #create_ship(PirateBomber(),(12,4),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])

        create_ship(PirateBomber(),(11,7),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])
        #create_ship(PirateBomber(),(12,8),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])

        create_ship(PirateDestroyer(),(13,9),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        create_ship(PirateDestroyer(),(13,3),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        create_ship(PirateBase(),(14,6),[PirateBaseKinetic(),PirateBaseAssault(),PirateBaseMissile()])


        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Sui_Generis.ogg"

    return