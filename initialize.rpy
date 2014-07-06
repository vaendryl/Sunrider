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
    MISSILE_SPEED = 0.3
    SHIP_SPEED = 0.3
    ZOOM_SPEED = 0.1
    GRID_SIZE = (18,16) #(X,Y) aka (width,height)
    BM = renpy.store.object()
    BM.phase = None

    planets = []

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

init python:

    Planet("CERA", "warpto_OccupiedCera", 1297, 480, "warpto_occupiedcera")
    Planet("TYDARIA", "warpto_Tydaria", 1390, 540, "warpto_tydaria")
    Planet("ASTRAL EXPANSE", "warpto_astralexpanse", 1250, 540, "warpto_astralexpanse")
    Planet("PACT Outpost", "warpto_pactstation", 1420, 480, "warpto_pactstation1")
    Planet("VERSTA", "warpto_versta", 1490, 725, "warpto_versta")
    Planet("NOMODORN", "warpto_nomodorn", 1630, 590, "warpto_nomodorn")

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
        enemy_ships = []
        sunrider = None
        blackjack = None
        liberty = None
        phoenix = None
        bianca = None
        seraphim = None
        paladin = None
        havoc = None
        paradigm = None

        check1 = False
        check2 = False
        check3 = False
        check4 = False
        check5 = False
        check6 = False
        check7 = False
        check8 = False
        check9 = False
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
        create_ship(Havoc(),(14,6),[HavocMelee(),HavocAssault(),HavocMissile(),HavocRocket()])
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
            blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
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
            blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
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
            blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
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

label mission6_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        sunrider.set_location(4,6)
        blackjack.set_location(5,5)
        liberty.set_location(5,7)

        create_ship(PactMook(),(12,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(12,4),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactMook(),(12,8),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(12,9),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactCruiser(),(13,4),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        create_ship(PactCruiser(),(13,8),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Driving_the_Top_Down.ogg"
    $ EnemyTurnMusic = "music/Battle_Against_Time.ogg"

    return

label mission7_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        sunrider.set_location(4,6)
        blackjack.set_location(5,6)
        liberty.set_location(5,7)

        phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
        phoenix = create_ship(Phoenix(),(5,5),phoenix_weapons)

        create_ship(PactMook(),(14,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(13,4),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(12,5),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactMook(),(12,8),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(13,9),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(14,10),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactBomber(),(13,5),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
        #create_ship(PactBomber(),(14,4),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

        create_ship(PactBomber(),(13,8),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
        #create_ship(PactBomber(),(14,9),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

        create_ship(MissileFrigate(),(15,3),[PactFrigateMissile()])
        create_ship(MissileFrigate(),(15,10),[PactFrigateMissile()])

        create_ship(PactCruiser(),(15,5),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        create_ship(PactCruiser(),(15,6),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        create_ship(PactCruiser(),(15,7),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Driving_the_Top_Down.ogg"
    $ EnemyTurnMusic = "music/Battle_Against_Time.ogg"

    return

label mission8_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        sunrider.set_location(4,6)
        blackjack.set_location(5,6)
        liberty.set_location(5,7)
        agamemnon_weapons = []
        agamemnon = create_ship(Agamemnon(),(2,6),agamemnon_weapons)

        create_ship(PactMook(),(12,5),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(12,6),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(12,7),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(12,8),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactCruiser(),(18,5),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        create_ship(PactCruiser(),(18,8),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])


        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Driving_the_Top_Down.ogg"
    $ EnemyTurnMusic = "music/Battle_Against_Time.ogg"

    return

label mission9_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        #check if phoenix exists. create it if it doesn't.
        if not hasattr(store,'phoenix'):
            phoenix = None
        if phoenix == None:
            phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
            phoenix = create_ship(Phoenix(),None,phoenix_weapons)


        if protectmochi == True:

            sunrider.set_location(4,6)
            blackjack.set_location(10,6)
            liberty.set_location(10,7)
            phoenix.set_location(10,5)

        if protectmochi == False:

            sunrider.set_location(4,6)
            blackjack.set_location(6,6)
            liberty.set_location(6,7)
            phoenix.set_location(6,5)

        mochi_weapons = []
        mochi = create_ship(Mochi(),(14,7),mochi_weapons)

        create_ship(PirateGrunt(),(13,5),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(13,9),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(16,5),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        create_ship(PirateGrunt(),(16,9),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])

        create_ship(PirateBomber(),(17,5),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])
        create_ship(PirateBomber(),(17,9),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])

        create_ship(PirateDestroyer(),(12,4),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        create_ship(PirateDestroyer(),(12,10),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        create_ship(Havoc(),(18,7),[HavocMelee(),HavocAssault(),HavocMissile(),HavocRocket()])
        enemy_ships[-1].boss=False

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Battle_Against_Time.ogg"

    return

label mission10_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        sunrider.set_location(4,6)
        blackjack.set_location(0,0)
        player_ships.remove(blackjack)
        BM.selected = sunrider  #just in case blackjack is still selected.
        liberty.set_location(6,7)
        phoenix.set_location(6,6)
        bianca.set_location(6,5)

        create_cover((8,4))
        create_cover((12,6))
        create_cover((10,2))
        create_cover((14,10))
        create_cover((11,10))
        create_cover((7,5))
        create_cover((10,12))

        create_ship(RyuvianCruiser(),(10,5),[RyuvianCruiserKinetic(),RyuvianCruiserMissile()])
        create_ship(RyuvianCruiser(),(10,10),[RyuvianCruiserKinetic(),RyuvianCruiserMissile()])
        create_ship(RyuvianCruiser(),(14,6),[RyuvianCruiserKinetic(),RyuvianCruiserMissile()])
        create_ship(RyuvianCruiser(),(14,8),[RyuvianCruiserKinetic(),RyuvianCruiserMissile()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Poltergeist_Attack.ogg"

    return

label mission11_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        sunrider.set_location(4,6)
        blackjack.set_location(6,4)
        liberty.set_location(6,7)
        phoenix.set_location(6,6)
        bianca.set_location(6,5)
        seraphim.set_location(6,8)

        create_ship(PactBattleship(),(15,5),[PACTBattleshipLaser(),PACTBattleshipKinetic(),PACTBattleshipAssault(),PACTBattleshipMissile(),PACTBattleshipRocket()])
        create_ship(PactBattleship(),(15,7),[PACTBattleshipLaser(),PACTBattleshipKinetic(),PACTBattleshipAssault(),PACTBattleshipMissile(),PACTBattleshipRocket()])
        create_ship(PactCruiser(),(13,5),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        create_ship(MissileFrigate(),(14,4),[PactFrigateMissile()])
        create_ship(MissileFrigate(),(14,8),[PactFrigateMissile()])

        create_ship(PactMook(),(12,4),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(13,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(14,2),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactMook(),(12,7),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(13,8),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(14,9),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactBomber(),(15,4),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
        create_ship(PactBomber(),(15,8),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/La_Busqueda_de_Lanna.ogg"
    $ EnemyTurnMusic = "music/The_Flight_of_the_Crow.ogg"

    return

label mission12_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        sunrider.set_location(4,8)
        blackjack.set_location(6,6)
        bianca.set_location(6,7)
        phoenix.set_location(6,8)
        liberty.set_location(6,9)
        seraphim.set_location(6,10)
        paladin.set_location(6,11)
        alliancecruiser1.set_location(5,7)
        alliancecruiser2.set_location(5,9)

        create_ship(PactBattleship(),(13,6),[PACTBattleshipLaser(),PACTBattleshipKinetic(),PACTBattleshipAssault(),PACTBattleshipMissile(),PACTBattleshipRocket()])
        create_ship(PactBattleship(),(12,7),[PACTBattleshipLaser(),PACTBattleshipKinetic(),PACTBattleshipAssault(),PACTBattleshipMissile(),PACTBattleshipRocket()])
        create_ship(PactBattleship(),(12,8),[PACTBattleshipLaser(),PACTBattleshipKinetic(),PACTBattleshipAssault(),PACTBattleshipMissile(),PACTBattleshipRocket()])
        create_ship(PactBattleship(),(13,9),[PACTBattleshipLaser(),PACTBattleshipKinetic(),PACTBattleshipAssault(),PACTBattleshipMissile(),PACTBattleshipRocket()])

        create_ship(PactCarrier(),(16,6),[PACTCarrierAssault()])
        create_ship(PactCarrier(),(16,9),[PACTCarrierAssault()])

        create_ship(PactMook(),(10,7),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(11,6),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactMook(),(10,10),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(11,11),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactBomber(),(11,7),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
        create_ship(PactBomber(),(12,6),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
        create_ship(PactBomber(),(11,9),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Riding_With_the_Wind.ogg"
    $ EnemyTurnMusic = "music/Posthumus_Regium.ogg"

    return


label preview_mission:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        #create the sunrider. you only have to create a player ship once:

        sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault()]
        sunrider = create_ship(Sunrider(),(5,6),sunrider_weapons)
        blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
        blackjack = create_ship(BlackJack(),(6,5),blackjack_weapons)
        liberty_weapons = [LibertyLaser(),Repair(),AccUp(),DamageUp()]
        liberty = create_ship(Liberty(),(6,6),liberty_weapons)
        phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
        phoenix = create_ship(Phoenix(),(6,7),phoenix_weapons)
        seraphim_weapons = [SeraphimKinetic()]
        seraphim = create_ship(Seraphim(),(6,8),seraphim_weapons)

        create_ship(PactMook(),(14,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(13,4),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(12,5),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactMook(),(12,8),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(13,9),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
        create_ship(PactMook(),(14,10),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])

        create_ship(PactBomber(),(13,5),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
        #create_ship(PactBomber(),(14,4),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

        create_ship(PactBomber(),(13,8),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
        #create_ship(PactBomber(),(14,9),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

        create_ship(MissileFrigate(),(15,3),[PactFrigateMissile()])
        create_ship(MissileFrigate(),(15,10),[PactFrigateMissile()])

        create_ship(PactCruiser(),(15,5),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        create_ship(PactCruiser(),(15,6),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])

        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Driving_the_Top_Down.ogg"
    $ EnemyTurnMusic = "music/Battle_Against_Time.ogg"

    return

