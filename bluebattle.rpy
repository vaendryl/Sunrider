label Blue_Side_Battle1:

    #"Before going into battle, I reviewed the state of our research and development."
    python:
        #My code to visit the upgrade shop doesn't work :( 



        BM.battle_bg = "Background/asteroids3.jpg"
        BM.mission = 1 #other missions might have logic that we don't want to invoke
        

        
        #This section is copied from initialize.rpy - look for the battle init labels
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
        
        #create_ship(PirateDestroyer(),(8,6),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        #create_ship(PactBattleship(),(11,9))
        #create_ship(PactBattleship(),(11,3))
        create_ship(PactCruiser(),(11,9),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        create_ship(PactCruiser(),(11,3),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        #create_ship(PactCarrier(),(12,6),[PACTCarrierAssault()])


        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

        PlayerTurnMusic = "music/Titan.ogg"
        EnemyTurnMusic = "music/Sui_Generis.ogg"
        check2 = False
        check3 = False
        battle_check1 = False
        
        #this next line is absolutely essential, and requires a change to classes.rpy so that it will work
        BM.sidemission = "BO_Side_Battle1_Loop"        
    jump battle_start

    
label BO_Side_Battle1_Loop:

    if check2 == False:

        $BM.draggable = False
        show ava uniform handonhip neutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "We've located two PACT cruisers that have been separated from the main force.  Let's take them out before anyone knows we're here."

        hide ava onlayer screens with dissolve

        $BM.draggable = True

        $ check2 = True

    if battle_check1 == False and BM.turn_count == 5:
        
        $BM.draggable = False
        show ava uniform handonhip neutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "Reinforcement warp signatures detected!  I suggest we get out of here."
        menu:
            "We've hit them, let's run":
                ava "Aye aye sir.  If nothing else, we've provoked them into defending this area.  That's a kind of victory."
                $retreating = True
            "Let them come.  The more PACT we take out, the safer this sector becomes.":
                ava "I hope you know what you're doing"
                $ retreating = False


        hide ava onlayer screens with dissolve
        $ BM.draggable = True
        $ battle_check1 = True
        
        if retreating == True:
            $BM.battle_end()

    if check3 == False and BM.turn_count == 6:
        $BM.draggable = False
        show ava uniform handonhip neutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "Their reinforcements are here."
        ava "They've activated some sort of field that's scrambling our warp drive!"
        
        $ create_ship(PirateDestroyer(),(10,10),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        $ create_ship(PirateDestroyer(),(10,10),[PirateDestroyerLaser(),PirateDestroyerKinetic()])     

        $ create_ship(PirateDestroyer(),(10,4),[PirateDestroyerLaser(),PirateDestroyerKinetic()])        
        $ create_ship(PirateDestroyer(),(10,4),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        hide ava onlayer screens with dissolve
        $ BM.draggable = True
        $ check3 = True
        
    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump BO_Side_Battle1_Loop #loop back
    else:
        $ BM.sidemission = ''  #REALLY IMPORTANT
        hide screen battle_screen
        hide screen commands
        return #go back to the main script
        
        
        
#Temporary holding space for code that hopefully never gets called


        
        
        
        
        
        show cosette plugsuit armscrossed angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        cos "What are you doing, you fools!  Kill them!"
        kay "Not this time, Cosette.  We're here to end your activities in this sector."

        show cosette plugsuit front evilsmile onlayer screens with dissolve

        cos "Heh-heh... You're a bold one..."

        show cosette plugsuit point yanderegrin onlayer screens with dissolve

        cos "But naive!"

        hide cosette onlayer screens with dissolve

        python:


            create_ship(PirateDestroyer(),(12,10),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        play sound "sound/Voice/Ava/Ava Others 4.ogg"
        $ PlayerTurnMusic = "music/Sora_no_Senritsu.ogg"
        
        
