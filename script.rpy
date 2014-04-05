## this is the main script file; everything starts here
## the goal is to offload as much declaring to the init module and jump
## back here for main control

## Declare characters used by this game.
#TO DO

    ##disable the main menu for easy iteration
label splashscreen:

    scene black

    play music "Music/The_Meteor.ogg"

    pause 0.5
    show logo 1 with dissolve
    $ renpy.pause(2)
    show logo 2 with dissolve
    $ renpy.pause(2)
    hide logo with dissolve
    $ renpy.pause(0.5)

    stop music fadeout 1.0
    window show

    asa "Ah.  Ah.  Uh, is this thing working?  Can everyone see me okay?"

    play music "Music/SAMFREE.ogg"

    scene bg renpytomback with dissolve
    show asaga uniform neutral funnysmile with dissolve
    show backgroundcredit:
        xpos 2.0
        linear 30 xpos -1.0

    asa "O-oh! There we go!"
    asa "A-ahem.  Hello and welcome to Doki Doki Space Whale Dating Sim 3.  I'm your ol' childhood friend Asaga Oakrun."
    asa "Eh, what?  You're here for the Sunrider Beta instead?"
    asa "U-uck... Well, about that..."
    asa "Samu-kun came down ill yesterday after he was bit by an emu and couldn't finish coding the game in time."

    show asaga uniform armscrossed confident with dissolve

    asa "Ufufu... But I bet I got something which you want even more than the beta..."
    asa "In my pocket is an exclusive preview of the very first HCG in our new Love in Space exclusive spin off game, Doki Doki Space Whale."
    asa "You better prepare yourself! Because there's three thousand tons of pure love in this image! Now STAND BACK, and BRACE YOURSELF!"

    show chigara uniform handsup surprise:
        xpos 1.1
        ease 0.5 xpos 0.8
    with dissolve

    chi "A-ah! W-wait!"
    chi "Samu-kun made a miraculous recovery and managed to finish the beta in time!"

    show asaga uniform thinking surprise with dissolve

    asa "Eeehh!? I thought that emu bite did him in for good!"

    show chigara uniform twiddlefingers forcedsmile with dissolve

    chi "A-Asaga... Please don't say scary things like that..."

    show asaga uniform excited smile with dissolve

    asa "W-well, in that case, looks like I'll just have to save the HCG for another day!"
    asa "Sit up straight and make sure to keep your arms and legs inside the ride at all times folks!  The Sunrider beta is about to begin!"
    asa "A-ahem, now Chigara, check out these HCGs..."

    show chigara uniform handsup surprise with dissolve

    chi "E-eh... EEEHHHHHHHH!?"

    scene bg black

    show episode1commences:
        zoom 5 xalign 0.5 yalign 0.5
        ease 0.5 zoom 1

    pause 0.5

    play sound "sound/drum.ogg"

    pause

    return

#label start:

    #create the battlemanager and a few lists

 #   jump story

#    menu:
#        "To Battle!":
#            jump battletest

#        "Tell me a story":
#            jump story

#label battletest:

#    ## this starts the battle! see classes.rpy for details
#    call battle_start

  #  'welcome back to visual novel mode!'
 #   'nothing to see here, though. resetting...'

 #   return

#label gameover:
  #  show screen game_over_gimmick
  #  'GAME OVER!'
 #   'better luck next time. resetting...'
 #   hide screen game_over_gimmick
 #   jump start

label quit:
    $ renpy.quit(relaunch=False)
    return


# The game starts here.


label start:

#####################################VARIABLE SET UP

    call initialize

    $ captain_moralist = 0
    $ captain_prince = 0
    $ affection_ava = 0
    $ affection_asaga = 0
    $ affection_chigara = 0
    $ affection_icari = 0
    $ affection_claude = 0
    $ affection_tera = 0
    $ affection_sola = 0
    $ affection_cosette = 0

    $ MetAsaga = False
    $ ChigaraRefugee = False
    $ mission_pirateattack = False

    $ battlemusic = True

    $ galaxymission1 = False
    $ galaxymission2 = False
    $ galaxymission3 = False
    $ mission1 = None
    $ mission2 = None
    $ mission3 = None
    $ mission1_name = None
    $ mission2_name = None
    $ mission3_name = None

    $ mission3_complete = False
    $ mission4_complete = False

    $ asa_location = None
    $ chi_location = None
    $ pro_location = None
    $ gal_location = None
    $ cal_location = None

#####################################VARIABLE SET UP


    stop music fadeout 3.0
    play sound "Sound/buttonclick.wav"
    scene bg cera:
        pause 5.0
    with Dissolve(2)

    window hide

    play music "Music/Tides.ogg" loop
    $ renpy.pause (0.5)
    show introtext0:
        yalign 0.12
        xalign 0.5
    pause
    hide introtext0 with Dissolve(1)
    show intro1:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro1 with Dissolve(1)
    show intro2:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro2 with Dissolve(1)
    show intro3:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro3 with Dissolve(1)
    show intro4:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro4 with Dissolve(1)
    show intro5:
        yalign 0.12
        xalign 0.5
        alpha 0.0
        linear 1.0 alpha 1.0
    pause
    hide intro5 with Dissolve(1)

    show introtext1:
        parallel:
            xalign 0.35 yalign 0.4
            easein 6.0 xalign 0.5
        parallel:
            alpha 0.0
            linear 2.5 alpha 1.0
    $ renpy.pause (2.0)
    show introtext2:
        parallel:
            xalign 0.65 yalign 0.5
            easein 6.0 xalign 0.5
        parallel:
            alpha 0.0
            linear 2.5 alpha 1.0
    $ renpy.pause (2.0)
    show introtext3:
        parallel:
            xalign 0.35 yalign 0.6
            easein 6.0 xalign 0.5
        parallel:
            alpha 0.0
            linear 2.5 alpha 1.0
    $ renpy.pause (8.0)
    hide introtext1 with dissolve
    hide introtext2 with dissolve
    hide introtext3 with dissolve

    $VNmode() #enables rollback

    window show dissolve

    "Shields leaned forward on his seat and spoke to his pilot. The pilot was obscured by his seat and Shields could only hear his burly voice humming to the tinny radio."
    kay "How much further until we get there?"
    pi "Just a moment now. Can't wait until you meet your girl, can you sir?"
    kay "I haven't seen Ava since we were in high school. I doubt she even remembers me."
    pi "The commander? Psh, not her! I mean the Sunrider. The newest ship in the fleet!"
    pi "Here, let me turn the ship around and give you a view."

    scene cg sunrider_drydock:
        xalign 0.0
        linear 20.0 xalign 0.8
    with dissolve

    "Shields leaned against his window and laid his eyes on the Sunrider."
    "Colossal in size, but still sleek looking, Shields found her to his liking. The behemoth vessel stuck a deadly image, like a poised arrowhead at the ready."
    pi "Aye, there, have a look at her. So advanced that the brass needed to train a new line of officers to fly her."
    kay "She looks like a fine vessel."
    pi "Just hang tight, captain. Won't be long now."
    "The shuttle continued its docking approach. Shields sat tight as the shuttle neared the Sunrider and docked."

    scene bg hangar
    with dissolve

    "After exiting the shuttle, Shields walked through the airlock and entered the Sunrider's hangar."

    show ava uniform salute talk with dissolve

    ava "Captain on deck!"

    show ava uniform neutral neutral with dissolve

    ava "Welcome aboard, captain. First Officer Ava Crescentia reporting for duty."

    menu:
        "At ease, commander.":
            jump at_ease

        "It's been awhile, Ava.":
            jump its_been_awhile

label at_ease:
    jump give_report

label its_been_awhile:

    $ affection_ava += 1

    show ava uniform neutral lookleft with dissolve

    ava "Same to you, uh, captain."
    kay "The last time we saw each other was your graduation in high school. I didn't ever dream that I'd ever become your commanding officer."

    show ava uniform neutral neutral with dissolve

    ava "Neither did I."

    menu:
        "I guess things have changed since then.":
            jump things_have_changed

        "It'll be just like old times again.":
            jump old_times

label things_have_changed:
    ava "I agree."
    jump give_report

label old_times:

    $ affection_ava += 1

    kay "Anyways, don't be too awkward around me, alright? I'll be counting on you from now."

    show ava uniform salute neutral with dissolve

    ava "Understood captain."
    kay "I'm not sure you understand..."

    show ava uniform neutral neutral with dissolve

    ava "Understand what?"
    kay "The whole captain thing... It's just bizarre hearing you call me that."
    ava "I do believe that is the correct protocol for a first officer, is it not?"
    kay "Ah, never mind..."
    jump give_report

label give_report:
    kay "Give me a report of Sunrider's status."

    show ava uniform alt neutral neutral with dissolve

    ava "We've been working for the past two weeks testing her systems. She's prepped to go on your word, sir."
    kay "Good. It sounds like High Command wants us out of here asap."

label give_report_menu:
    menu:
        "Tell me more about the Sunrider":
            jump tell_more_Sunrider

        "Tell me more about this orange alert.":
            jump tell_more_orange_alert

        "Let's move on. What's next on our agenda?":
            jump give_report_move_on

label tell_more_Sunrider:

    show ava uniform alt neutral neutral with dissolve
    ava "She's the newest ship in the fleet. She's armed like a warship, but built like a carrier. We can field up to twelve ryders and also provide capital ship support for them."
    ava "Her biggest asset is the Vanguard cannon. They took a gun from a battleship-class warship, modified it extensively, and put it on top of our ship. Still, it works like a charm and can rip holes through ships over twice as big as ours."
    ava "Not only that, but the Sunrider can be flown with a crew of just 50 and has one of the most efficient warp drives in the fleet. We'll be able to jump across the galaxy in just days."
    kay "Sounds like a fine vessel."
    jump give_report_menu

label tell_more_orange_alert:

    show ava uniform armscrossed neutral with dissolve
    ava "Don't tell me you don't know. Rynar's surrendered to PACT just this morning."
    kay "Already? That's another neutral world that's been taken by PACT."
    ava "Not only that, but PACT's taken Minerva, Barona, and Gerald in the past three months. One neutral planet after another. What do you think that means?"
    kay "Encirclement. We're next."
    ava "Exactly. So that's why High Command's not taking any risks. If any hostiles enter our gravity well, we're to open fire first and ask questions later."
    jump give_report_menu

label give_report_move_on:

    show ava uniform alt neutral neutral with dissolve
    ava "First, a tour of the ship."
    kay "Oh good."
    ava "As you've noticed, this is the Sunrider's hangar. We can store up to twelve ryders here."
    kay "I don't see any ryders here. Where are they now?"
    ava "We won't be receiving them until Wednesday. Once they're here though, you'll be able to access them and order equipment changes here."
    ava "This is an interactive map of the Sunrider. You can use it to navigate around the ship."
    ava "We're going to head up to the bridge, up above us on deck 1."
    ava "Try using the map to navigate there. Make sure you click on the deck 1 tab first."

    $ captaindeck = 2
    $ ava_location = "bridge"
    $ ava_event = "bridge_tour"
    jump dispatch

label bridge_tour:

    hide screen deck1
    window show
    scene bg bridge
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    ava "This is the Sunrider's main bridge. This is where you'll be commanding the ship."
    kay "That's a pretty fancy star map in the middle."
    ava "You can use that star map to plot our course and to warp to other systems."
    ava "I'll also usually be here if you ever need me."

    $ captaindeck = 1
    $ ava_location = "engineering"
    $ ava_event = "engineering_tour"
    jump dispatch

label engineering_tour:

    hide screen deck1
    window show
    scene bg engineering
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    ava "This is engineering. The ship's main reactor is located here and we can also use the lab to research and construct new equipment. Unfortunately, the research lab's not yet open."
    kay "That's also going to be available on Wednesday?"
    ava "Correct."

    $ captaindeck = 1
    $ ava_location = "messhall"
    $ ava_event = "messhall_tour"
    jump dispatch

label messhall_tour:

    hide screen deck0
    window show
    scene bg messhall
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    ava "This is the ship's mess hall. We can come down here to eat and relax after work."
    kay "Sounds good to me."

    $ captaindeck = 0
    $ ava_location = "captainsloft"
    $ ava_event = "captainsloft_tour"
    jump dispatch

label captainsloft_tour:

    hide screen ship_map
    window show
    scene bg captainsloft
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    ava "Finally, these are your personal quarters."
    kay "Looks like I've moved up in life. Wow, it's almost like a loft in Cera City."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Please don't mess up your room too much, captain."
    kay "I've already got some ideas on how to redecorate it."

    show ava uniform handonhip neutral with dissolve

    ava "You can come here to access your personal logs and other material. Furthermore, if a member of the crew needs your help with something, they'll be waiting outside of your door."
    ava "You can use your map to walk around the ship. You're encouraged to interact with your crew mates whenever possible."
    kay "Alright. A happy ship makes for a strong ship."
    ava "And that concludes our tour. Like I said, I'll be in the bridge most of the time, so you can come to me if you need help."
    kay "What's next?"
    ava "I'm afraid we'll have to cut the formalities short, captain. Like I said, Command wants us out of dry dock as soon as possible."
    ava "We are scheduled for our first live engine test. We'll be sailing port shortly and making one loop around the moon."
    kay "Fine with me. Let's return to the bridge and see what the Sunrider's capable of."

    scene bg bridge
    show ava uniform handonhip neutral:
        xalign 0.5
    with screenwipe
    play music "Music/WorldBuilder.ogg" fadein 1.5 fadeout 1.5

    kay "All hands, this is your captain speaking."
    kay "Man your stations. Activate the main reactor and light the engines.  Momentarily, we'll begin a live test of our engines by sailing port and making one round to the moon."
    kay "We are to enter orange alert as soon as we clear port. Raise shields and scan for any possible hostiles."
    kay "I know this is just a test, but keep your guard up. I want everyone to be on their feet in case we run into any problems."
    ava "Main reactor is coming awake, captain. Power is increasing."
    kay "Wake our lady up, Ava. We're getting out of here."

    show ava uniform order talk with dissolve

    ava "Aye sir. Helmsman, light the engines."

    show ava uniform handonhip neutral with dissolve

    ava "Engineering reports the reactor is working within parameters."
    ava "Power is increasing to the engines."
    ava "Blast off in three."
    ava "Two."

    stop music fadeout 0.5
    play sound "Sound/explosion1.wav"
    scene bg bridge:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show ava uniform handonhip neutral:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8

    hide ava uniform order talk with dissolve

    ava "Ugh..."
    kay "What the hell was that!?"

    show ava uniform alt neutral angry with dissolve

    ava "Checking status."
    ava "Engineering reports the reactor core is still stable. No explosions reported in either deck 0 or 2."
    ava "Captain, the only place that blast could have come from is outside."
    kay "Outside!? As in-"
    ava "Contact!  PACT warp signatures detected!"
    kay "What?"
    ava "Missile boats! They jumped in right under our noses!"
    kay "Red alert! Cancel the engine test!"

    play sound "Sound/redalert.ogg"
    play music "Music/Intruders.ogg"
    scene bg bridgered
    show ava uniform alt order angry
    with dissolve

    ava "Aye captain. All hands, battle stations! This is not a drill!"
    kay "This is turning out to be one hell of a maiden flight. Ava, what's our weapon status?"

    show ava uniform alt neutral mad with dissolve

    ava "Limited. The vanguard cannon is still off line. We have flak turrets, saviors, and a few shots of hell darts."
    kay "... ... ..."
    ava "Captain... You're not seriously thinking of taking the Sunrider into battle, are you? We haven't even completed any of our engine tests, much less any munitions checks."
    kay "No time like the present, Ava."

    play sound "Sound/explosion1.wav"
    scene bg bridgered:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show ava uniform alt neutral mad:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    with dissolve

    show ava uniform alt neutral mad:
        xalign 0.5
    with dissolve

    kay "And from the sound of things, I don't think PACT's going to wait for us to finish our tests."
    kay "Get this ship operational, double time."

    show ava uniform alt order angry with dissolve

    ava "Aye sir. Helmsman, all power to engines!"
    ava "Warning, we have inbound one enemy!"

    scene bg space1
    show missileboatdrydock:
        xpos 0.55 ypos 0.5
    show parallax_ship1 behind missileboatdrydock
    show parallax_ship2 behind missileboatdrydock
    show parallax_ship3 behind missileboatdrydock
    with screenwipe

    "An enemy missile frigate took aim at the Sunrider. Captain Shields gritted his teeth as the Sunrider's engines sparked back to life - painfully slowly."

    play sound "Sound/missile.ogg"
    show missileboatmissile1:
        xpos 0.6 ypos 0.4 additive 1.0
        ease .5 xpos -0.1 ypos 1.0
        repeat 3
    pause 0.2
    play sound1 "Sound/missile.ogg"
    show missileboatmissile2:
        xpos 0.62 ypos 0.43 additive 1.0
        ease .5 xpos -0.1 ypos 1.0
        repeat 3
    pause 0.2
    play sound2 "Sound/missile.ogg"
    show missileboatmissile3 behind missileboatdrydock:
        xpos 0.45 ypos 0.4 additive 1.0
        ease .5 xpos -0.1 ypos 0.9
        repeat 3
    pause 0.2
    play sound3 "Sound/missile.ogg"
    show missileboatmissile4 behind missileboatdrydock:
        xpos 0.46 ypos 0.4 additive 1.0
        ease .5 xpos -0.1 ypos 0.9
        repeat 3
    pause 0.2
    play sound4 "Sound/missile.ogg"
    show missileboatmissile1:
        xpos 0.6 ypos 0.6 additive 1.0
        ease .5 xpos 0.1 ypos 1.1
        repeat 3
    pause 0.2
    play sound5 "Sound/missile.ogg"
    show missileboatmissile2 behind missileboatdrydock:
        xpos 0.4 ypos 0.6 additive 1.0
        ease .5 xpos 0.0 ypos 1.1
        repeat 3
    pause 0.2
    play sound5 "Sound/missile.ogg"

    kay "Ava...!"

    scene bg black
    show parallax_missile1
    show parallax_missile2
    show parallax_missile3
    with screenwipe
    play sound "Sound/missilefly.ogg"
    show missileboatmissilelarge5:
        xpos 1.2 ypos 0.43 zoom 0.04
        ease 4 xpos 0.3 ypos 0.5 zoom 0.1
    show missileboatmissilelarge6:
        xpos 1.2 ypos 0.65 zoom 0.08
        ease 4 xpos 0.5 ypos 0.63 zoom 0.1
    show missileboatmissilelarge4:
        xpos 1.2 ypos 0.23 zoom 0.3
        ease 4 xpos 0.4 ypos 0.32 zoom 0.2
    show missileboatmissilelarge8:
        xpos 1.2 ypos 0.65 zoom 0.2
        ease 4 xpos 0.21 ypos 0.90 zoom 0.3
    show missileboatmissilelarge3:
        xpos 1.2 ypos 0.76 zoom 0.4
        ease 4 xpos 0.34 ypos 0.65 zoom 0.3
    show missileboatmissilelarge7:
        xpos 1.2 ypos 0.12 zoom 0.6
        ease 4 xpos 0.21 ypos 0.23 zoom 0.4
    show missileboatmissilelarge2:
        xpos 1.2 ypos 0.56 zoom 0.6
        ease 4 xpos 0.43 ypos 0.34 zoom 0.5
    show missileboatmissilelarge1:
        xpos 1.2 ypos 0 zoom 0.7
        ease 4 xpos 0.23 ypos 0.45 zoom 0.6
    pause 3

    scene cg drydockdestroyed 0 with screenwipe
    show missileboatmissile1:
        xpos 1 ypos 0.3 additive 1.0 zoom 0.3
        linear .3 xpos 0.65 ypos 0.4
        repeat
    $ renpy.pause (0.3)
    play sound1 "Sound/explosion1.ogg"
    show cg drydockdestroyed 1:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show missileboatmissile2:
        xpos 1 ypos 0.4 additive 1.0 zoom 0.3
        linear .3 xpos 0.7 ypos 0.45
        repeat 3
    $ renpy.pause (0.3)
    play sound2 "Sound/explosion1.ogg"
    show cg drydockdestroyed 2:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show missileboatmissile3:
        xpos 0.8 ypos 0 additive 1.0 zoom 0.3
        linear .3 xpos 0.5 ypos 0.2
    $ renpy.pause (0.3)
    play sound3 "Sound/explosion1.ogg"
    show cg drydockdestroyed 3:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    show missileboatmissile4:
        xpos 0.9 ypos 0 additive 1.0 zoom 0.3
        linear .3 xpos 0.4 ypos 0.24
    $ renpy.pause (0.3)
    play sound4 "Sound/explosion2.ogg"
    show cg drydockdestroyed 4:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 8
    hide missileboatmissile1
    $ renpy.pause (0.5)
    hide missileboatmissile2
    $ renpy.pause (0.5)
    hide missileboatmissile3
    $ renpy.pause (0.5)
    hide missileboatmissile4

    "Simultaneously as the frigate launched a swarm of missiles at the Sunrider, her engines roared to life, lurching the ship forward."
    "The missiles struck the dry dock's supports exactly as the Sunrider flew out of the resulting fireball. Behind her, the dry dock collapsed in a chaos of steel and fire."

    scene bg bridgered
    show ava uniform alt neutral mad
    with screenwipe

    "Captain Shields breathed a sigh of relief while Ava looked utterly unaffected by the peril they were just in."
    ava "We're in the clear. Sunrider is joining the fight."
    kay "Fire weapons! Take these bastards out!"

label firstbatle:

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    scene bg bridgered:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show ava uniform alt neutral mad:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide battlewarning

    call mission1_inits
    $ BM.mission = 1  #this sets the label to loop on. in this case it will be mission1
    $ battle1_check1 = False  #without this you would see the dialogue over and over again all the time
    jump battle_start #jumps to mission1 automatically thanks to setting BM.mission to 1

label mission1:

        #an example of scripted dialogue inside the battle
    if not battle1_check1:  #if you don't check for a flag like this you'll see this dialogue every loop.
        $BM.draggable = False  #this makes clicking to advance text work but you can't drag the battlefield around anymore

        show ava uniform alt neutral neutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve  #the onlayer part is required to make ava visible on top of the battle_screen

        ava "Welcome to the tactical screen, captain.  From here, you can issue orders to the crew during battle."
        ava "In front, you see the battle grid.  This grid shows where friendlies and enemies are positioned on the battlefield."
        ava "You may click and drag the left mouse button move the camera around the battle grid.  Further, you can use the mouse wheel to zoom in and out."
        ava "To issue an order to a unit, simply select an unit under your command, indicated by the blue ring.  Then you may either order the unit to move to another grid, or to use an attack."
        ava "Moving and attacking expends energy.  Each unit has a finite number of energy points.  Once all of the units under your command no longer have enough energy to act, you must end your turn."
        ava "PACT units are indicated by the red ring.  Your current objective is to eliminate all PACT units from the map."
        ava "The Sunrider is armed with a comprehensive suite of weapons to fulfill this task."
        ava "Laser based weapons have the longest range, but deal little damage.  Kinetic based weapons have short range, but pack a punch.  Missile based weapons have both long range and firepower, but are limited in supply, and so must be used wisely."
        ava "Use the Sunrider's weapons to eliminate the PACT missile frigates.  Good luck, captain."

        hide ava onlayer screens with dissolve #onlayer is also required here because otherwise the hide statement can't find the right image

        $ battle1_check1 = True #this ensures you see this dialogue only once

        $ BM.draggable = True  #this enables dragging the viewport again.

    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission1 #loop back
    else:
        pass #continue down to the next label

label firstbattle_end:

    hide screen battle_screen
    hide screen commands

    window show

    play music "Music/WorldBuilder.ogg"

    scene bg bridgered with dissolve

    show ava uniform handonhip neutral with dissolve

    ava "Our forces are pushing the remaining PACT units back. The PACT frigates are no longer a threat."
    kay "Join the rest of our fleet. Let's pitch in with the mop up operation."
    ava "Aye captain."
    kay "Two missile frigates down with hardly a scratch. Not bad for my first command, huh Ava?"

    show ava uniform armscrossed smile with dissolve

    ava "Hmph."
    kay "Charge up trinities again. Let's give the rest of those missile frigates a parting gift before they warp out of Cera."

    show ava uniform alt neutral neutral with dissolve

    ava "Aye captain. Charging trinities."
    kay "They must have been trying to warp in missile frigates and take out our ships before we could respond."
    kay "Given how small the attacking force was though, I'd say the entire operation was-"

    show ava uniform alt neutral angry with dissolve
    stop music fadeout 1.5

    ava "Alert! New contacts on scanner!"
    kay "More missile frigates?"
    ava "No... It's unlike anything I've ever seen before."

    scene cg_legionwarpin_background with dissolve
    $ renpy.predict("CG/legionwarpin_full.jpg")
    $ renpy.predict("CG/legionwarpin_legion_warp.png")

    play music "Music/Posthumus_Regium.ogg"

    play sound1 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate2 warp:
        xpos 1940 ypos 200
        ease 0.05 xpos 300 ypos 200
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash:
        xpos 300 ypos 200
    show cg_legionwarpin_missilefrigate2 out
    pause 0.15
    play sound2 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate1 warp:
        xpos 1940 ypos 800
        ease 0.05 xpos 700 ypos 900
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash:
        xpos 700 ypos 900
    show cg_legionwarpin_missilefrigate1 out behind cg_legionwarpin_missilefrigate_warpflash
    pause 0.15
    play sound3 "Sound/small_warpout.ogg"
    show cg_legionwarpin_missilefrigate3 warp behind cg_legionwarpin_missilefrigate2:
        xpos 1950 ypos 100
        ease 0.05 xpos 975 ypos 100
    pause 0.05
    show cg_legionwarpin_missilefrigate_warpflash behind cg_legionwarpin_missilefrigate2:
        xpos 975 ypos 100
    show cg_legionwarpin_missilefrigate3 out behind cg_legionwarpin_missilefrigate2
    pause 0.2
    play sound4 "Sound/large_warpout.ogg"
    show cg_legionwarpin_legion warp behind cg_legionwarpin_missilefrigate1:
        xpos 3000 ypos 600
        ease 0.2 xpos 970 ypos 600
    pause 0.2
    scene cg_legionwarpin_legion_full:
        xpos 0.505 ypos 0.56
        pause 1.0
        ease 0.5 zoom 0.4
        ease 0.5 zoom 0.42
    with flash
    $ renpy.pause(4)

    scene bg bridgered with dissolve
    show ava uniform neutral surprise with dissolve

    ava "Sweet mother of god..."
    kay "What is that thing, Ava!? I don't remember PACT having anything that colossal!"

    show ava uniform alt neutral mad with dissolve

    ava "I'm just getting intel from HQ... It's the PACT Super-Dreadnought class warship Legion."

    show ava uniform alt neutral angry with dissolve

    ava "Over three kilometers in length... Armed with enough guns to take down a fleet three times our size by itself! That thing's Veniczar S. Arcadius' personal flagship!"
    ava "HQ has issued a general retreat! All units are to fall back! The Prime Minister's Office has been advised to issue an immediate unconditional surrender!"
    kay "Retreat? It's over already?"

    show ava uniform alt order angry with dissolve

    ava "Warning! I'm detecting a massive power surge coming from it... Wait! Brace for impact!"

    scene legion_cera_fleetfire1 with dissolve
    pause 0.5
    play sound "Sound/legion_laser.ogg"
    show legion_cera_fleetfire2 with screenwipereverse
    hide legion_cera_fleetfire2 with screenwipereverse

    scene cerafleet1 with dissolve
    pause 0.5

    play sound "Sound/explosion1.wav"
    pause 0.1
    play sound1 "Sound/explosion1.wav"
    pause 0.1
    play sound2 "Sound/explosion1.wav"
    scene cerafleet2:
        xalign 0.5
        ease 0.025 xalign 0.40
        ease 0.05 xalign 0.6
        ease 0.025 xalign 0.5
        repeat 8
    $ renpy.pause(5)

    scene bg bridgered with dissolve
    show ava uniform neutral surpriseangry with dissolve

    ava "What disgusting firepower..."

    show ava uniform alt neutral angry with dissolve

    ava "Battleships Gallant and the Behomian Maiden have been sunk! The Fearless has sustained severe damage!"
    ava "Hull breaches reported on section 34-A! Our port trinities are no longer operative!"
    kay "Break away! Our ship doesn't stand a chance against that!"
    ava "The enemy warship is powering its weapons again!"

    scene legion_cerafire1 with dissolve
    play sound "Sound/legion_maincannon.ogg"
    scene legion_cerafire2 with dissolvelong
    pause 1.0
    scene legion_cerafire3 with dissolvemedium
    $ renpy.pause(1)
    scene legion_cerafire4 with dissolve
    show legion_cerafire5 with horizontalwipereversefast
    hide legion_cerafire5 with horizontalwipereversefast
    play sound1 "Sound/explosion1.wav"
    play sound1 "Sound/explosion5.ogg"
    scene legion_cerafire6:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 4
    with dissolve
    scene legion_cerafire7:
        xalign 0.5
        ease 0.025 xalign 0.3
        ease 0.05 xalign 0.7
        ease 0.025 xalign 0.5
        repeat 15
    with dissolve
    $ renpy.pause(2.0)

    scene bg bridgered
    show ava uniform altneutral surpriseshout
    with dissolve

    kay "R-report!"
    ava "The warship's nuked Cera City with that last shot. I'm still trying to figure out the scope of the damage, but..."
    kay "U-unbelievable... To use a weapon of that magnitude on a civilian target..."
    ava "More than a million civilians have been lost! All contact has been lost with our civilian and military leadership!"
    ava "The rest of the Cera Space Force is scattering! We're going to get overwhelmed if we don't get out of here!"
    ava "What are your orders, captain!?"
    kay "... ... ..."
    ava "CAPTAIN!!"
    "The Sunrider began to pound as more enemies arrived. Shields wiped sweat off from his brows and saw that his hand was soaked."
    "The pounding wasn't coming from the enemy. It was his own heart."
    kay "Fall back..."
    kay "... ... ..."
    kay "Fall back! Warp to the nearest safe harbor!"

    play music "Music/Coming_Soon_Part1.ogg" fadeout 1.5
    show ava uniform alt neutral mad with dissolve

    ava "Understood."

    show ava uniform alt order angry with dissolve

    ava "Navigator, punch in the fall back coordinates into the computer! Spool up the warp drive and prepare to jump!"
    kay "... ... ..."
    "Shields took a final look at his burning home world."
    "This wasn't the end."
    "He was going to be back. No matter the cost."

    play music "Music/Coming_Soon_Part2.ogg" noloop fadeout 0.5
    scene bg space_red
    show sunrider_warpout 1:
        xpos 0.5 ypos 0.5
    show parallax_ship1 behind sunrider_warpout
    show parallax_ship2 behind sunrider_warpout
    show parallax_ship3 behind sunrider_warpout
    with dissolve
    pause 2.0

    show sunrider_warpout_engine:
        xpos 0.5 ypos 0.48
        alpha 0
        linear 5.0 alpha 1
    show ava uniform alt neutral mad:
        xpos 0.2 xzoom -1
    with dissolve

    ava "Warp out in 3...!"
    $ renpy.pause(1.0)
    ava "2..."

    hide ava with dissolve
    show captain order 1:
        xpos 0.4
    with dissolve
    kay "... ... ..."

    $ renpy.pause(1.0)

    show captain order 2 with dissolve
    kay "WARP!!!"

    hide captain with dissolve

    pause 1.5
    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_flash:
        xpos 0.5 ypos 0.5
        alpha 1.0
        linear 0.5 alpha 0
    hide sunrider_warpout_engine with dissolvequick
    show sunrider_warpout 3:
        ease 0.3 xpos -1.0 ypos 2.0
    pause 0.5

    window hide

    play sound1 "Music/Posthumus_Regium_Finale.ogg" fadeout 0.5 fadein 0.5 noloop
    scene bg black2 with dissolvelong
    pause 0.1
    show mainlogo:
        subpixel True
        xpos 0.5 ypos 0.5 zoom 1.0
        ease 7.0 zoom 1.1
    with dissolvelong
    $ renpy.pause(9.0)
    hide mainlogo with dissolvelong
    pause 1.0

    window show

    scene bg captainsoffice with dissolve
    play music "Music/The_Meteor.ogg"

    "Shields sat at his office, writing his daily log."
    kay "{i}It's been a week since the fall of Cera. Despite our best efforts, we have been unable to regroup with the rest of the Cera Space Force. The crew is starting to fear that we may be the only ones who got out of that massacre in one piece. To tell the truth, I'm beginning to believe that too.{/i}"
    kay "{i}I don't know what we're going to do or what next step to take. All I know is that we're going to be alone from now.{/i}"
    "The doorbell interrupted Shields' thoughts."
    kay "Come in."

    show ava uniform armscrossed neutral with dissolve

    ava "Captain."
    kay "Any news of the fleet?"
    ava "None."
    kay "... ... ..."
    ava "The crew's beginning to get worried. We've been doing nothing but scanning for the past week. If a PACT force finds us, we're sitting ducks here."

    menu:
        "You're suggesting that we give up the search?":
            jump giveupsearch
        "That's agreed. I think we've wasted enough of our time here.":
            jump wastedenoughtime

label giveupsearch:

    show ava uniform alt neutral neutral with dissolve

    ava "Long range scanners do not show any Cera signatures. What's left of our government surrendered and was dissolved six days ago. Most likely, what's left of the Cera Space Force has either gone rogue or been impressed into the PACT fleet."
    jump shipwithoutflag

label wastedenoughtime:

    show ava uniform alt neutral neutral with dissolve

    ava "What's left of our government surrendered and was dissolved six days ago. I don't think there's any hope in looking for our military any more."
    jump shipwithoutflag

label shipwithoutflag:
    kay "Ava, tell me something. What's a ship without a flag?"

    show ava uniform neutral looklefttalk with dissolve

    ava "Sir? Well, a pirate ship."

    menu:
        "Pirate ship Sunrider. I like the sound of that.":
            jump pirateshipsunrider

        "I don't intend on becoming a pirate captain.":
            jump notapiratecaptain


label pirateshipsunrider:

    $ captain_moralist += 1

    show ava uniform handonhip neutral with dissolve

    ava "Are you suggesting we go rogue?"
    kay "I don't think we have much of a choice. Our government's no more. We're going to have to go it alone from now on."
    jump whatareyousuggesting

label notapiratecaptain:

    $ captain_prince += 1

    show ava uniform handonhip neutral with dissolve

    ava "I wasn't suggesting we turn to piracy."
    kay "Remember, Ava. The Sunrider will always be carrying the flag of Cera."
    jump whatareyousuggesting

label whatareyousuggesting:

    ava "So what are you suggesting?"
    kay "PACT won't get away with what they did to our home. We're going to take the fight to them."

    show ava uniform armscrossed neutral with dissolve

    ava "With just our one ship?"
    kay "We'll find allies. We're not the only neutral world to have been conquered by them."
    kay "We find others like us. Build a fleet together. And then retake all of our planets, one by one."
    ava "Hm. I suppose you've already got a plan."

    menu:
        "Just like old times, Ava.":
            jump justlikeoldtimes

        "Are you questioning my orders, commander?":
            jump questioningorders

        "I'm not the kid you remember anymore, Ava.":
            jump notthekidyouremember

label justlikeoldtimes:

    $ affection_ava += 1

    show ava uniform alt neutral neutral with dissolve

    ava "It's a good thing they put me as your first officer. I don't even want to imagine how much trouble you'd cause if I weren't here to clean up after you."
    kay "Hahaha. Come on now, is that all you can remember of me from high school?"
    ava "Well, I do recall that you were certainly one of the most frustrating youths for a student council president to have to deal with..."
    ava "I remember the time you installed an anti-gravity device in the student council room. It was impossible getting everything cleaned up afterwards."
    kay "Ah, that little thing. Come on, you had a good laugh afterwards, didn't you?"

    show ava uniform armscrossed frown with dissolve

    ava "No."

    jump newordersjumptotydaria

label notthekidyouremember:

    kay "I'm not the kid you remember anymore, Ava."
    kay "We can't let ourselves be defeated so easily. If PACT pushes us, I say we push back. The Sunrider's still got a lot of fight left in her yet."

    show ava uniform alt neutral neutral with dissolve

    ava "All right. We fight."
    ava "I must say, captain..."
    kay "What's that?"
    ava "You still haven't changed a bit."

    jump newordersjumptotydaria

label questioningorders:

    $ affection_ava -= 2

    kay "Are you questioning my orders, commander?"

    show ava uniform alt neutral neutral with dissolve

    ava "My apologies, captain. I, uh, had a momentary slip of the tongue."

    jump newordersjumptotydaria

label newordersjumptotydaria:

    show ava uniform alt neutral neutral with dissolve

    ava "In the meantime, what are your orders?"
    kay "We'll warp to the nearest neutral planet of Tydaria. Chances are, after the fall of Cera, they'll be more than likely to be jittery about PACT. "
    ava "Understood. The ship will be prepared to warp at your command."

    menu:
        "What's the status of the Sunrider?":
            jump statusofthesunrideraftercera

        "How are you holding up after what happened?":
            jump howareyouholdingup

        "Report to the bridge. I'll see you there once I'm ready.":
            jump seeyouthereonceready

label statusofthesunrideraftercera:

    ava "She's had better days. We had to sail port before we could finish any of our tests. Our missiles are empty and our Vanguard Cannons are still offline."
    ava "And that's not even the worst. We had to leave Cera before we could pick up any of our ryders. Not only that, but we're missing our chief engineer and our doctor. Both Research and Development and the Sickbay are still dark."
    kay "Whew. Try to make do with what we have. We'll have to resupply and finish our tests at Tydaria."
    ava "On that note, I have one more issue."
    ava "Running a ship is going to take money. I've looked into some ways to raise some immediate cash."
    ava "The various galactic powers all post bounties on rival factions. I've been putting together a folder containing letters of marque from all governments currently aligned against PACT."
    kay "In other words, our only way of making money right now is privateering for other planets which have a grudge against PACT. Which is pretty much everyone, I'm guessing."
    ava "Correct. We'll be paid a sum of money for each PACT target we sink. The bigger the target, the bigger the reward."
    kay "Alright, keep me posted on the money situation."

    menu:
        "How are you holding up after what happened?":
            jump howareyouholdingup

        "Report to the bridge. I'll see you there once I'm ready.":
            jump seeyouthereonceready


label howareyouholdingup:

    show ava uniform armscrossed lookleftmouthopen with dissolve

    ava "I'm... fine, captain. There's no reason to worry about me."
    kay "Are you sure?"

    show ava uniform alt neutral neutral with dissolve

    ava "Yes. We've got more immediate problems than that."
    kay "I suppose you're right."
    ava "Indeed."
    kay "Still, if you need to talk about anything, my door's always open."

    menu:
        "What's the status of the Sunrider?":
            jump statusofthesunrideraftercera

        "Report to the bridge. I'll see you there once I'm ready.":
            jump seeyouthereonceready

label seeyouthereonceready:

    ava "Understood."

    $ captaindeck = 0
    $ ava_location = "bridge"
    $ ava_event = "warptotydaria"
    jump dispatch

label warptotydaria:

    $ warpto_occupiedcera = True
    $ warpto_tydaria = True

    hide screen deck1
    window show
    scene bg bridge with dissolve
    show ava uniform alt neutral neutral with dissolve

    ava "You can use the starmap at the center of the bridge to plot our course."

    hide ava with dissolve

    menu:
        "Access galaxy map.":
            jump galaxymap

        "Return to map.":
            jump dispatch

label Tydaria_jump1:

    window show

    play music "Music/WorldBuilder.ogg" fadeout 1.5

    scene bg bridge with fade
    show ava uniform alt neutral neutral with dissolve

    ava "Aye captain. Course laid in."

    show ava uniform order talk with dissolve

    ava "All hands, this is the Commander speaking. We will momentarily enter jump space to the neutral world of Tydaria."
    ava "Assume jump stations and await further orders on dropout."
    ava "The jump drive is functioning as expected, captain. Core status is green. On your word."
    kay "Warp!"

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene tydaria_orbit:
        ypos 0
        ease 1.5 ypos -120
    with dissolve
    pause 1

    show sunrider_warpout_standard out:
        xpos 2300 ypos 1200 zoom 2
        ease 0.2 xpos 1000 ypos 500 zoom 0.5
    pause 0.2
    play sound "Sound/large_warpout.ogg"
    show cg_legionwarpin_missilefrigate_warpflash:
        zoom 1.5 xpos 1550 ypos 750
    show sunrider_warpout_standard

    pause 2.0

    scene bg bridge with fade
    show ava uniform alt neutral neutral with dissolve

    ava "Warp complete, captain. We're arriving at the mining world of Tydaria."
    ava "What kind of help do you think we'll be able to get here?"
    kay "Resources and supplies, at least. There's a big space mining operation going on around the rings of the planet."
    ava "You might want to hold that thought. I'm detecting unknown vessels on an intercept course for us."
    kay "Flag?"
    ava "I'm not finding any of them on any of the flag registries..."

    play music "Music/Sui_Generis.ogg" fadeout 1.5
    show ava uniform alt neutral angry with dissolve

    ava "Damn. Pirates!"

    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform alt neutral angry
    with dissolve

    kay "Red alert! Raise shields and power weapons!"
    ava "We are being hailed!"

    show ava uniform alt neutral angry:
        zoom 1
        ease 0.5 xpos 0.7
    pause 0.5
    show cosette plugsuit handsonhip evilsmile:
        xpos 0.3
    with wipeup

    cos "Haahaaahaaa! This is the pirate ryder Havoc! Lower your shields and surrender your cargo!"
    kay "Stand down. This is an armed warship of the Cera Space Force. We will not hesitate to open fire if you approach."
    cos "Cera Space Force, huh? Your ship will make a lovely addition to my pirate fleet. After we've dealt with you, of course!"

    show cosette plugsuit point evilsmile with dissolve

    cos "Boys, rough them up!"

    hide cosette plugsuit point evilsmile with wipedown
    show ava uniform alt neutral angry:
        zoom 1
        ease 0.5 xpos 0.5

    kay "Ava, what's the situation?"
    ava "Two pirate ryders, inbound fast.  Both infantry class. There's one more bomber-class ryder leading them, designation Havoc."
    ava "Also, two pirate destroyers are approaching. Estimated time until arrival: Ten minutes."
    kay "Let's try to end this before the destroyers get here. Concentrate all firepower on the lead pirate ryder!"
    kay "Besides, she just looks like a little girl. Maybe a little show of force will help put her in her place."

    show ava uniform armscrossed frown with dissolve

    ava "Captain... Please don't underestimate the enemy..."

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    scene bg bridgered:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show ava uniform armscrossed frown:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide cosette
    hide battlewarning

    call mission2_inits
    $ BM.mission = 2
    $ battle2_check1 = False
    $ battle2_check2 = False
    jump battle_start

label mission2:

    if not battle2_check1:
        $BM.draggable = False

        show ava uniform armscrossed frown onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve  #the onlayer part is required to make ava visible on top of the battle_screen

        ava "We're heavily outnumbered, captain. What are your orders?"
        kay "Concentrate on the lead bomber. These pirates think about nothing but themselves. Once Cosette realizes we mean business, she'll probably back off."
        show ava uniform handonhip mad onlayer screens zorder 50 with dissolve

        ava "Understood, captain. Let's hope this goes as planned..."

        show ava uniform handonhip mad onlayer screens zorder 50:
            ease 0.25 xpos -0.15

        play sound "Sound/objectives.ogg"
        "Objective: Destroy the Havoc"

        hide ava onlayer screens with dissolve #onlayer is also required here because otherwise the hide statement can't find the right image

        $ battle2_check1 = True #this ensures you see this dialogue only once

        $ BM.draggable = True  #this enables dragging the viewport again.

    if battle2_check2 == False and sunrider.hp < sunrider.max_hp:
        $BM.draggable = False

        kay "Damage report!"

        show ava uniform alt neutral angry onlayer screens zorder 50:
            xzoom -1 xpos 0.2
        with dissolve

        ava "We're venting air in four sections. Our systems are stretched to capacity!"
        kay "How did so many missiles get through!? Are the gunners blind, Ava?"
        ava "We're still recovering from Cera, captain. The Sunrider's giving it her all."

        hide ava onlayer screens with dissolve
        scene havoc_tydaria_miss1 onlayer screens

        show cosette plugsuit point evilsmile onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        cos "Now's our chance! Take their engines out, but leave the ship intact!"
        cos "We'll board and cut down the crew hand to hand."

        kay "You're awfully persistent for a little girl, aren't you?"

        play sound "Sound/hit.wav"
        show cosette plugsuit neutralalt yandereshock onlayer screens:
            xpos 0.2
            ease 0.02 xpos 0.19
            ease 0.04 xpos 0.21
            ease 0.02 xpos 0.2
            repeat 4
        with dissolve

        cos "Hurk..."
        cos "Did... you... just... call... me..."

        show cosette plugsuit neutral yanderegrin onlayer screens:
            zoom 1.0
        with dissolve

        cos "LITTLE!?"
        kay "Uh... yes?"

        show cosette plugsuit neutral yanderegrin onlayer screens:

        cos "Y-YOOUUUU!!!"
        cos "KILL THEM ALL! BUT LEAVE THE CAPTAIN FOR ME!"
        cos "HE'S... MINE!"

        hide cosette plugsuit neutral yanderegrin onlayer screens with dissolve
        show ava uniform armscrossed looklefttalk onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "Captain... Please do not provoke the enemy..."

        hide ava uniform armscrossed looklefttalk onlayer screens with dissolve

        kay "Damn... Just one problem after another..."

        play sound "Sound/laser.wav"
        show havoc_tydaria_miss2 onlayer screens with dissolvequick
        pause 0.2
        play sound "Sound/laser.wav"
        show havoc_tydaria_miss3 onlayer screens  with dissolvequick
        pause 0.2
        hide havoc_tydaria_miss2 onlayer screens  with dissolvequick
        play sound "Sound/laser.wav"
        show havoc_tydaria_miss4 onlayer screens  with dissolvequick
        pause 0.2
        hide havoc_tydaria_miss3 onlayer screens  with dissolvequick
        pause 0.2
        hide havoc_tydaria_miss4 onlayer screens  with dissolvequick

        show cosette plugsuit point yandereneutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        cos "Eh?"

        scene blackjack_tydaria_enter onlayer screens  with dissolve
        play music "Music/Driving_the_Top_Down.ogg"

        $ PlayerTurnMusic = "Music/Driving_the_Top_Down.ogg"

        show asaga plugsuit neutralalt alert onlayer screens:
            xpos 0.8
        with dissolve

        asa "The cavalry has arrived!"
        kay "What the... Who are you?"

        show asaga plugsuit vpose onlayer screens with dissolve

        asa "A HERO OF JUSTICE!"
        asa "Looks like you could use a hand there! Don't worry, my Black Jack will take care of these guys in a flash!"

        show ava uniform armscrossed neutral onlayer screens:
            xpos 0.2
        with dissolve

        ava "She's flying a mercenary ryder licensed by the United Mining Guild, captain. Probably hired security for the mining operation on Tydaria. Do you think we can trust her?"
        kay "Doesn't look like we have much of a choice."
        kay "Alright, pilot of the Black Jack. Let's see what you've got."
        asa "No problem!"

        hide blackjack_tydaria_enter onlayer screens
        hide ava onlayer screens
        hide asaga onlayer screens
        hide cosette onlayer screens

        $ battle2_check2 = True
        $ BM.draggable = True

        show screen battle_screen

        python:
            blackjack_weapons = [BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
            blackjack = create_ship(BlackJack(),(6,3),blackjack_weapons)

    $ BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission2 #loop back
    else:
        pass #continue down to the next label

label secondbattle_end:

    hide screen battle_screen
    hide screen commands
    window show

    scene bg black2 with horizontalwipereverse
    scene bg hangar with horizontalwipereverse

    play music "Music/WorldBuilder.ogg"  fadeout 1.5

    show asaga plugsuit handsonhips happy:
        xpos 0.35
    with dissolve

    asa "Whew, that sure was hairy! I didn't ever think those pirates would pick on a military ship!"

    show ava uniform armscrossed frown:
        xpos 0.65
    with dissolve

    ava "Stop right there, pilot. You're going to have get searched for weapons."

    menu:
        "Hey Ava... Don't be so uptight.":
            jump dontbesouptight

        "Sorry, regular protocol.":
            jump sorryregularprotocol

label dontbesouptight:

    $ affection_asaga += 1
    $ captain_moralist += 1

    show ava uniform handonhip mad with dissolve

    ava "Captain, military protocol section 9-32B clearly states that all-"
    kay "I'm Captain Kayto Shields of the assault carrier Sunrider. Excuse my first officer, Commander Ava Crescentia. She's not as bad as she seems at first. Who are you?"

    jump asagaoakrunpilot

label sorryregularprotocol:

    $ affection_ava += 1
    $ captain_prince += 1

    show asaga plugsuit armscrossed sad with dissolve

    asa "Uuu... Does this mean that I'm gonna have get groped by the mean lady beside you?"

    show ava uniform armscrossed surprisemad with dissolve

    ava "L-lady...?"
    kay "Hahaha. I'm Captain Kayto Shields of the assault carrier Sunrider. The mean lady beside me is Commander Ava Crescentia. And who are you?"

    jump asagaoakrunpilot

label asagaoakrunpilot:

    show asaga plugsuit neutralalt smile with dissolve

    asa "Asaga Oakrun, pilot of the Black Jack."
    kay "Thanks for the help out there."
    asa "Eh-heh... Don't worry, those guys were nothin'!"
    kay "So, what exactly were you doing out there? I can't imagine a lone ryder operating out here for no reason."
    asa "Oh nothing, just keeping the space ways safe!"

    show ava uniform alt neutral mad with dissolve

    ava "Safe...?"

    show asaga plugsuit vpose with dissolve

    asa "Dunnnndadada!! Coming to the rescue wherever the weak are oppressed! It's the hero of justice, the vanguard of the innocent! For love, freedom, and just a little bit of money on the side, it's Asaga of the Black Jack!"

    show ava uniform armscrossed frown with dissolve

    ava "... ... ..."
    kay "Let me guess. You're a freelancer?"

    show asaga plugsuit armscrossed smile:
        xzoom -1
    with dissolve

    asa "Eh-heh... I guess you could call me that."

    show asaga plugsuit neutral content with dissolve

    asa "The space around here's pretty dangerous, so the Mining Union's been paying me to bust up any pirates around here. Easier said then done though! Those guys are harder to kill than cockroaches!"

    menu:
        "Tell me more about your freelancing.":
            jump tellmorefreelancing
        "Tell me more about the pirates.":
            jump tellmorepirates
        "Tell me more about the Mining Union.":
            jump tellmoreUnitedMiningFederation
        "Let's move on to our next course of action.":
            jump moveonnextaction

label tellmorefreelancing:

    show asaga plugsuit armscrossed content with dissolve

    asa " Ah, I've been wandering around the neutral rim, looking around for any odd jobs here and there. I'd like to call myself an adventurer."
    kay " And you do this alone, in just a single ryder?"
    asa " Ah, not really. I have Chigara to help me out. She's the one who built me my Black Jack here."
    kay " Chigara...? Is she an engineer?"
    asa " Yeah, you can call her that. She's a genius when it comes to technology, and she can fix just about anything mechanical!"
    kay "(I'm betting we'll get to meet this Chigara very soon...)"

    menu:
        "Tell me more about the pirates.":
            jump tellmorepirates
        "Tell me more about the United Mining Federation.":
            jump tellmoreUnitedMiningFederation
        "Let's move on to our next course of action.":
            jump moveonnextaction

label tellmoreUnitedMiningFederation:

    show asaga plugsuit armscrossed content with dissolve

    kay "The Mining Union?"
    asa "I'm working for them right now. I don't really know much about 'em, aside from the fact that they mine the ore on Tydaria and pay me money to take out the pirates."
    asa "A lady by the name of Sophita is my contact with the Union.  If you're looking for some work, she'd be the person to talk to around here."
    kay "What do they think of PACT?"
    asa "Nothing much, really.  They don't really pick sides, as long as they can keep mining."
    kay "(I wonder how long that'll last...)"

    menu:
        "Tell me more about your freelancing.":
            jump tellmorefreelancing
        "Tell me more about the pirates.":
            jump tellmorepirates
        "Let's move on to our next course of action.":
            jump moveonnextaction

label tellmorepirates:

    show asaga plugsuit armscrossed mad with dissolve

    asa "The pirates in this sector are led by a nasty girl named Cosette Cosmos. You've already met her."
    kay "What's a little girl like that doing committing piracy?"
    asa "Cosette may look like a brat, but don't underestimate her. She's feared in this whole sector as a ruthless pirate. I even heard a rumor the other day that she slit her own pa's throat for not buying her candy on her 14th birthday."
    kay "I'm not sure if I really believe-"
    asa "And there's this other one about her ship, the Havoc, being filled with rats, that she keeps as pets."
    kay "Really."
    asa "Anyways, I've had a couple run ins with her, and I can say, she's not to be trifled with."
    asa "Be careful of the Havoc's anti-matter missiles. Those will definitely put more than a dent on any capital ship's hull."
    asa "The Havoc's only weakness is that it's pretty slow and sluggish, so it can be picked off by other ryders."
    kay "Thanks, I'll keep that in mind."

    menu:
        "Tell me more about your freelancing.":
            jump tellmorefreelancing
        "Tell me more about the United Mining Federation.":
            jump tellmoreUnitedMiningFederation
        "Let's move on to our next course of action.":
            jump moveonnextaction

label moveonnextaction:

    show asaga plugsuit neutral content with dissolve

    asa "Hey, you guys are a part of the former Cera Space Force, huh?"
    kay "That's right."
    asa "Why don't we join forces for awhile? From the look of things here, you seem to be an assault carrier without any ryders. Help me take care of these pirates, and I'll join you guys as the Sunrider's first ryder."

    show ava uniform armscrossed frown with dissolve

    ava "Captain, we don't know if we can trust this girl. We've only just met her!"

    menu:
        "She's already saved our necks. And she's right. A carrier without any ryders is useless. I say we work together for now.":
            jump savednecksworktogether
        "Sorry, Asaga. I don't think I can let you join the team without making Ava lose sleep for the next week.":
            jump sorryasagaavalosesleep

label savednecksworktogether:

    $ affection_asaga += 1

    show ava uniform facepalm with dissolve

    ava "Sigh..... I knew you were going to say that."

    show asaga plugsuit neutralalt closedeyessmile with dissolve

    asa "Eh-heh... I'm glad we agree, capt'n!"

    jump fornowsunriderrepairs

label sorryasagaavalosesleep:

    $ affection_ava += 1

    show asaga plugsuit neutral sad with dissolve

    asa "Aww..."
    kay "But you can stay onboard for a bit, I guess. I don't want to be caught without a ryder if the pirates decide to come back with reinforcements."

    show asaga plugsuit excited closedeyessmile with dissolve

    asa "Yayyy--"

    show ava uniform facepalm with dissolve

    ava "Unbelievable..."

    jump fornowsunriderrepairs

label fornowsunriderrepairs:

    kay "For now, the Sunrider needs repairs and supplies."
    kay "We'll make our way to Tydaria and dock there. Then we'll decide our next course of action."

    show asaga plugsuit handsonhips happy with dissolve

    asa "Oh! I know someone who can help us with that! Chigara has her workshop in Tydaria. She'll be able to fix your ship in no time!"
    ava "Chigara? Friend of yours?"
    asa "Uh-huh! She's a genius when it comes to technology!"
    kay "Alright, if your friend can help us, we can head to her workshop."
    kay "Ava and I are going to head up to the bridge now. You should stay here with your ship. We'll call you on the comm if anything comes up."
    asa "Understood, capt'n!"

    scene bg black2 with horizontalwipereverse
    scene bg bridge with horizontalwipereverse

    show ava uniform armscrossed neutral with dissolve

    ava "Sigh... I can't believe you're seriously going to let her stay onboard."
    kay "What's the matter, Ava?"
    ava "Nothing! It's just... ugh..."
    ava "Anyways, what are you waiting for? The quicker we get to Tydaria, the less I need to worry about a fleet of pirate ships warping in around us. Just use the star map and order the Sunrider to the workshop. I've already put in its coordinates on the computer, so you should be able to find it without any problems."

    scene bg black2 with horizontalwipereverse
    scene bg bridge with horizontalwipereverse
    show ava uniform armscrossed neutral with dissolve

    kay "This is the Sunrider, requesting permission to dock."
    chi "Ah... Welcome to the Stardust Bakery."
    kay "B-bakery...? Didn't Asaga say this was a workshop?"
    ava "I knew we shouldn't have trusted her..."
    chi "Ummm... We offer a cupcakes, cream puffs, strawberry cakes, and various muffins... Oh."
    chi "And we might just do starship repairs as well."
    kay "This is getting weirder and weirder by the minute."
    chi "If I can just come on board, I'll be able to survey the extent of the repairs and give you a quote. How's that?"
    kay "Uh, alright, sure. I think we have a friend of yours waiting in the hangar too."

    scene bg hangar with dissolve
    play music "Music/Colors_Of_An_Orchestra.ogg"  fadeout 1.5

    show asaga plugsuit excited happy with dissolve

    asa "Hey Chigaraaa! I'm back home!"

    show asaga plugsuit excited happy:
        zoom 1
        ease 0.5 xpos 0.35
    show chigara plugsuitlabcoat altneutral smile:
        xpos 0.65
    with dissolve

    chi "Ah... And you've brought friends..."

    show asaga plugsuit altneutral happy with dissolve

    asa "Uh huh, this is Capt'n Kayto Shields of the starship Sunrider! And that lady's First Officer Ava Crescentia."

    show ava uniform facepalm:
        xpos 0.9
    with dissolve

    ava "Ugh..."

    hide ava with dissolve
    kay "It's nice to meet you. You must be Chigara."

    chi "Umm... Chigara Lynn's my full name, but Asaga calls me that."

    menu:

        "So what's this about this place being a bakery?":
            jump beingabakery
        "This is a strange place for a girl to have a workshop...":
            jump girltohaveaworkship
        "Let's get down to business. The Sunrider's in need of repairs. Not only that, but we still need to complete our tests and resupply.":
            jump completeourtestsandresupply

label beingabakery:

    show chigara plugsuitlabcoat altneutral forcedsmile with dissolve

    chi "Ah, the Stardust Bakery is the best place to get pastries in Tydaria."

    show asaga plugsuit handsonhips happy with dissolve

    asa "The only place!"
    chi "Cup cakes, cream puffs, sandwiches, we have it all."
    kay "Errr... Do you get a lot of business here?"

    show chigara plugsuitlabcoat altneutral sad with dissolve

    chi "Uuuu... No. Everyone seems much more interested in getting their ship fixed..."
    kay "So why don't you just open a dry dock instead of a bakery?"

    show asaga plugsuit handsonhips mad with dissolve

    asa "Oy, oy! It's always been Chigara's dream to run a bakery! You can't just shut a girl's dreams down like that!"
    chi "Uuu... M-maybe I really should consider giving up. It feels so awkward selling cupcakes next to the starship fuel..."

    menu:
        "This is a strange place for a girl to have a workshop...":
            jump girltohaveaworkship
        "Let's get down to business. The Sunrider's in need of repairs. Not only that, but we still need to complete our tests and resupply.":
            jump completeourtestsandresupply


label girltohaveaworkship:

    show chigara plugsuitlabcoat altneutral smile with dissolve

    chi "Not at all.  Tydaria is one of the Mining Union's primary worlds.  I've been renting this dock from the Union and patching up ships with Asaga for a while now."
    chi "As long as I service the Union's ships, they've been very supportive of my efforts here."

    show chigara plugsuitlabcoat altneutral sad with dissolve

    chi "Well… aside from the bakery."
    kay "I was referring more to yourself..."

    show chigara plugsuitlabcoat altneutral forcedsmile with dissolve

    chi "Me? Mmm... Well, I guess you can call me one of those people like Asaga..."
    kay "A freelancer?"
    chi "Oh yes, that."
    kay "(Something tells me there's more to this pair than they're letting on… These girls don't exactly fit my image of freelancers…)"

    menu:
        "So what's this about this place being a bakery?":
            jump beingabakery
        "Let's get down to business. The Sunrider's in need of repairs. Not only that, but we still need to complete our tests and resupply.":
            jump completeourtestsandresupply


label completeourtestsandresupply:

    show chigara plugsuitlabcoat neutral neutral with dissolve

    chi "Mmm... Most of the damage seems to be to the outer hull. It shouldn't be too hard to repair."
    kay "Now, I think you're understating things. The Sunrider's a top of the line military vessel. It's not going to be like scraping a meteoroid impact from a mining ship."

    show asaga plugsuit armscrossed confident with dissolve

    asa "Ufufufu... Don't worry, capt'n. Chigara's a crazy genius when it comes to technology. I've never seen a single machine that she couldn't fix."
    kay "Look over there. See that? That's a busted power convertor that took a lab of twelve  scientists a month to make. There's no way you could fix that!"

    show chigara plugsuitlabcoat altneutral forcedsmile with dissolve

    chi "Ummm... I actually made this little contraption in my sleep yesterday night... I was really confused when I woke up and saw a power converter on my bed, but I think it should work perfectly for your ship."
    kay "Wha..."
    asa "C'mon, try it, capt'n! I swear it'll work!"
    chi "Excuse me... Here we go..."
    kay "Well, I'll be damned. Not only does it work, but the efficiency's been increased by 20 percent."
    asa "I told ya she was a genius!"
    chi "Ehehehehe..."
    kay "Uh, well okay then. You can start repairs as soon as possible."

    hide asaga with dissolve
    show ava uniform handonhip neutral:
        xpos 0.35
    with dissolve

    ava "Do you want to oversee the repair work?"
    kay "Uhh, I think I'll leave you in charge of that. I'll be in my quarters, trying to find a way to write about this in my logs."
    ava "Understood captain. I'll contact you once repairs are complete."

    scene bg black2 with horizontalwipereverse
    scene bg captainsoffice with horizontalwipereverse

    kay "Begin captain's log. The Sunrider's been in dry dock for the past two days. Repairs have gone ahead of schedule and we're back to full combat status already. That Chigara girl really is something. I wouldn't mind having her in my engineering staff."
    kay "We're about to set sail again. I'm still not sure what to do about our two guests. Even though Ava still doesn't trust them, they've been an invaluable help. I think they'd do well on board the Sunrider."
    kay "... ... ..."
    kay "End captain's log."
    kay "(Well, I guess it's time to explore the ship.)"

    $ captaindeck = 0
    $ ava_location = "bridge"
    $ ava_event = "firstpriority"
    $ asa_location = "hangar"
    $ asa_event = "defeatingthepirates"
    $ chi_location = "engineering"
    $ chi_event = "chigarafirstconvo"

    jump dispatch

label firstpriority:

    $ captaindeck = 1

    hide screen deck1
    window show
    scene bg bridge
    show ava uniform handonhip neutral with dissolve

    ava "The ship is at your command, captain."

    menu:
        "What do you think our next move should be?":
            jump firstprioritytofindryders
        "What's the ship's status?":
            jump readytosetsailcommand
        "Carry on, Ava.":
            jump dispatch

label firstprioritytofindryders:

    ava "First things first. Like you said, the Sunrider's an assault carrier without any ryders. Our first priority should be to find pilots and ryders to fill up our empty hangar."
    kay "We already have one interested pilot."

    show ava uniform armscrossed frown with dissolve

    ava "You should be careful with that one. Asaga's the type of person that seeks out danger."
    kay "How do you even know that?"
    ava "Woman's intuition."
    kay "Huh, alright then."

    menu:
        "What's the ship's status?":
            jump readytosetsailcommand
        "Carry on, Ava.":
            jump dispatch

label readytosetsailcommand:

    show ava uniform handonhip neutral with dissolve

    ava "The repairs are already complete. We're ready to set sail as soon as you give the command."
    menu:
        "What do you think our next move should be?":
            jump firstprioritytofindryders
        "Carry on, Ava.":
            jump dispatch

label defeatingthepirates:

    $ captaindeck = 2

    hide screen deck2
    window show
    scene bg hangar
    show asaga plugsuit neutralalt smile with dissolve

    asa "Oh! Did you need me for something, capt'n?"

    menu:
        "How did you meet Chigara?":
            jump howdidyoumeetChigara
        "How's the Black Jack doing?":
            jump howstheBlackJackdoing
        "About joining the Sunrider...":
            jump aboutjoiningtheSunrider
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble

label howdidyoumeetChigara:

    $ ChigaraRefugee = True

    show asaga plugsuit armscrossed smile with dissolve

    asa "Me and Chigara go back pretty far. I think we met about five years ago, back when she was just a girl. Mmm... Well, I think she was a refugee from a planet that was destroyed in a natural disaster. Anyways, I saw a bunch of these dirty guys scaring her in the middle of the street, so I stepped in and tried to scare them away."
    kay "How'd that turn out?"
    asa "Eh-heh... Let's say that I kind of bit off more than I could chew. But I swear, I was gonna win in the end! Lucky for those guys though, Chigara pulled out a gadget that zapped them with electricity, so I didn't have to space them for good."

    menu:
        "You're lucky she was there to save you!":
            jump luckyshewastheretosave
        "So you rescued Chigara?":
            jump soyourescuedChigara

label luckyshewastheretosave:

    show asaga plugsuit armscrossed annoyed with dissolve

    asa "H-hey, like I said, I was gonna beat them in the end!"
    jump eversincethencomrades

label soyourescuedChigara:

    show asaga plugsuit armscrossed smile with dissolve

    asa "Yup, totally!"
    jump eversincethencomrades

label eversincethencomrades:

    show asaga plugsuit handsonhips happy with dissolve

    asa "And ever since then, we've been comrades in arms!"
    kay "(It feels like she skipped a few chapters of that story...)"
    kay "(Still, a refugee from a doomed world?  Maybe I should ask Chigara more about this.)"

    menu:
        "How's the Black Jack doing?":
            jump howstheBlackJackdoing
        "About joining the Sunrider...":
            jump aboutjoiningtheSunrider
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble

label howstheBlackJackdoing:

    show asaga plugsuit armscrossed confident with dissolve

    asa "Uwah-hah! Thanks for askin', but nothing ever troubles mah Black Jack! It's always in tiptop form!"
    asa "By the way, if you happen to get your hands on any ryder upgrades, feel free to arm it on the Black Jack, or on any other ryder the Sunrider's carrying. Although preferably on the Black Jack."
    kay "How do we get ryder upgrades?"

    show asaga plugsuit thinking lookleft with dissolve

    asa "Well, most of the time I just ask Chigara to research some upgrades for me. It takes some money, but it's a pretty reliable way of getting upgrades!"

    menu:
        "How did you meet Chigara?":
            jump howdidyoumeetChigara
        "About joining the Sunrider...":
            jump aboutjoiningtheSunrider
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble

label aboutjoiningtheSunrider:

    show asaga plugsuit excited happy with dissolve

    asa "So, are you willing to help, capt'n? If you help me take out the pirates, I'll join you guys on board the Sunrider!"

    menu:
        "Why do you want to join the Sunrider?":
            jump whyjoinSunrider
        "Tell me more about the pirates you're after.":
            jump tellmoreaboutpirates
        "I think I'll have to think about it more...":
            jump illhavetothinkmore
        "All right, you've got a deal.":
            jump youvegotadeal

label whyjoinSunrider:

    show asaga plugsuit vpose with dissolve

    asa "For the adventure, of course! And the excitement!"
    kay "Really, is that all?"

    show asaga plugsuit armscrossed smile with dissolve

    asa "Well, you're headed after PACT, right?"
    kay "PACT's conquered our home. Of course we're after them."
    asa "Well, maybe I want to help out. If we don't do anything, PACT's going to take over the galaxy. And that's not just bad for us. That's going to be bad for anyone who cares about freedom and justice."

    menu:
        "I couldn't agree more.":
            jump couldntagreemore

        "What's your grudge against PACT?":
            jump whatsgrudgeagainstPACT

label couldntagreemore:

    show asaga plugsuit armscrossed confident with dissolve

    asa "Eh-heh... I knew we'd think alike from the moment I met you, capt'n."

    menu:
        "Tell me more about the pirates you're after.":
            jump tellmoreaboutpirates
        "I think I'll have to think about it more...":
            jump illhavetothinkmore
        "All right, you've got a deal.":
            jump youvegotadeal

label whatsgrudgeagainstPACT:

    show asaga plugsuit thinking content with dissolve

    asa "Mmm... Well, nothing as big as having my planet conquered by them. It's... Uhh... Something more personal."

    show asaga plugsuit excited happy with dissolve

    asa "Anyways, let's just say I'm doing it for the heroics!"

    menu:
        "Tell me more about the pirates you're after.":
            jump tellmoreaboutpirates
        "I think I'll have to think about it more...":
            jump illhavetothinkmore
        "All right, you've got a deal.":
            jump youvegotadeal

label tellmoreaboutpirates:

    show asaga plugsuit armscrossed mad with dissolve

    asa "They've been terrorizing this sector for the past year. Merchants, military, even unarmed civilians. Nobody's safe from them."
    asa "Now that kind of thing just makes my blood boil! I say we go and take the fight to them!"
    asa "There's a pirate's nest hidden in the Tydarian asteroid field where they operate from. We can take the Sunrider and mess that nest up! That'll show them not to pick on civilians!"
    kay "And also get you your payment from the Mining Union?"

    show asaga plugsuit armscrossed content with dissolve

    asa "Eh-heh, that too. Hey, everyone's got to make a living!"

    menu:
        "Why do you want to join the Sunrider?":
            jump whyjoinSunrider
        "I think I'll have to think about it more...":
            jump illhavetothinkmore
        "All right, you've got a deal.":
            jump youvegotadeal

label illhavetothinkmore:

    show asaga plugsuit neutralalt smile with dissolve

    asa "Well, don't wait too long, capt'n! Each moment that passes is more time for PACT to get stronger!"

    menu:
        "How did you meet Chigara?":
            jump howdidyoumeetChigara
        "How's the Black Jack doing?":
            jump howstheBlackJackdoing
        "About joining the Sunrider...":
            jump aboutjoiningtheSunrider
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble


label youvegotadeal:

    $ pro_location = "bridge"
    $ pro_event = "attackonpiratesnest"

    show asaga plugsuit armscrossed confident with dissolve

    asa "Eh-heh... I knew you'd agree, capt'n."

    show asaga plugsuit excited happy with dissolve

    asa "Don't worry, don't worry! We'll whack those pirates in no time at all, and then attend to your PACT problem together."
    kay "Welcome to the team, Asaga."

    show asaga plugsuit handsonhips happy with dissolve

    asa "I won't let you down, capt'n! Ah-hahahaha!"

    menu:
        "That'll be all for now, Asaga. Try to stay out of trouble.":
            jump thatllbeallasagastayouttrouble

label thatllbeallasagastayouttrouble:

    jump dispatch

label chigarafirstconvo:


    $ captaindeck = 1
    hide screen deck1
    window show

    scene bg engineering with dissolve
    show chigara plugsuitlabcoat holdingipad surprise with dissolve

    chi "E-eah! Oh, sorry, Captain Shields, I didn't see you coming."
    kay "Sorry for surprising you."

    show chigara plugsuitlabcoat holdingipad curious with dissolve

    chi "Was there something you needed?"

    if ChigaraRefugee:
        menu:
            "So you made the Black Jack yourself?":
                jump youmadeblackjackyourself

            "Do you also pilot a ryder, Chigara?":
                jump youalsopilotryder

            "I heard from Asaga you were a refugee.":
                jump asagayouwerearefugee

            "Where did you learn to work with machines like that?":
                jump wherelearnmachinelikethat

            "Thanks Chigara. That'll be all for now.":
                jump thanksallfornow

    menu:
        "So you made the Black Jack yourself?":
            jump youmadeblackjackyourself

        "Do you also pilot a ryder, Chigara?":
            jump youalsopilotryder

        "Where did you learn to work with machines like that?":
            jump wherelearnmachinelikethat

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label youmadeblackjackyourself:

    show chigara plugsuitlabcoat holdingipad smile with dissolve

    chi "That's correct. Asaga used to pilot around a military surplus fighter that she put together from a junk heap. I used to be worried sick that it'd fall apart, so I decided that I'd build a new ryder for her."
    kay "The Black Jack's unlike anything I've seen in my life. You know, if you worked for a engineering company, you could change the galaxy."

    show chigara plugsuitlabcoat holdingipad sad with dissolve

    chi "Ah... But then I wouldn't be able to open my bakery..."

    if ChigaraRefugee:
        menu:

            "Do you also pilot a ryder, Chigara?":
                jump youalsopilotryder

            "I heard from Asaga you were a refugee.":
                jump asagayouwerearefugee

            "Where did you learn to work with machines like that?":
                jump wherelearnmachinelikethat

            "Thanks Chigara. That'll be all for now.":
                jump thanksallfornow

    menu:
        "Do you also pilot a ryder, Chigara?":
            jump youalsopilotryder

        "Where did you learn to work with machines like that?":
            jump wherelearnmachinelikethat

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label youalsopilotryder:

    show chigara plugsuitlabcoat holdingipad smile with dissolve

    chi "I do. The Liberty's a support ryder though, so I usually fly as Asaga's wing mate and provide her with support. That's only for really tough missions though. Usually, the Black Jack's strong enough to fly by itself."
    kay "The Liberty, huh... Did you also make that yourself?"
    chi "Uh-huh. They're both my creations."
    kay "We could sure use more ryders... I don't suppose we could also bring the Liberty on board?"

    show chigara plugsuitlabcoat holdingipad forcedsmile with dissolve

    chi "Eh-heh... About that..."
    chi "Asaga's been pumped up about attacking the pirates, so she's already arranged to bring the Liberty here."
    kay "Really? Shesh, nobody's told me about that, and I'm supposed to be the captain."

    if ChigaraRefugee:
        menu:
            "So you made the Black Jack yourself?":
                jump youmadeblackjackyourself

            "I heard from Asaga you were a refugee.":
                jump asagayouwerearefugee

            "Where did you learn to work with machines like that?":
                jump wherelearnmachinelikethat

            "Thanks Chigara. That'll be all for now.":
                jump thanksallfornow

    menu:
        "So you made the Black Jack yourself?":
            jump youmadeblackjackyourself

        "Where did you learn to work with machines like that?":
            jump wherelearnmachinelikethat

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label asagayouwerearefugee:

    show chigara plugsuitlabcoat holdingipad neutral with dissolve

    chi "Ah, that's right. I used to be a refugee from the planet Diode."
    kay "Diode... I remember hearing about the Diode catastrophe about six years ago. Didn't a science experiment go terribly wrong and open a micro black hole on the planet?"

    show chigara plugsuitlabcoat holdingipad sad with dissolve

    chi "It was a terrible event..."
    chi "Ever since that happened, I've been on my own. Well, at least until Asaga found me."
    chi "I'm sorry. I don't really like talking about what happened that day."
    kay "Sorry, I didn't mean to pry."

    menu:
        "So you made the Black Jack yourself?":
            jump youmadeblackjackyourself

        "Do you also pilot a ryder, Chigara?":
            jump youalsopilotryder

        "Where did you learn to work with machines like that?":
            jump wherelearnmachinelikethat

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label wherelearnmachinelikethat:

    show chigara plugsuitlabcoat holdingipad neutral with dissolve

    chi "My people were always experts with technology. I guess it's because I've been trained since I was really little."
    chi "Unfortunately, there's not many of us left now, so it must seem really amazing to you. But back home, I wasn't even that amazing with science."

    show chigara plugsuitlabcoat holdingipad reminsice with dissolve

    chi "Eh-heh... You should have seen my parents. They were really amazing."
    kay "What did your parents do?"
    chi "They were researching some incredible things. Technology to bring people back from the dead. To synthesize complicated machinery from thin air. To tell the truth, compared to what they were making, what I'm doing here is really only child's play."

    if ChigaraRefugee:
        menu:
            "So you made the Black Jack yourself?":
                jump youmadeblackjackyourself

            "Do you also pilot a ryder, Chigara?":
                jump youalsopilotryder

            "I heard from Asaga you were a refugee.":
                jump asagayouwerearefugee

            "Thanks Chigara. That'll be all for now.":
                jump thanksallfornow

    menu:
        "So you made the Black Jack yourself?":
            jump youmadeblackjackyourself

        "Do you also pilot a ryder, Chigara?":
            jump youalsopilotryder

        "Thanks Chigara. That'll be all for now.":
            jump thanksallfornow

label thanksallfornow:

    jump dispatch


label attackonpiratesnest:

    hide screen deck1
    window show
    play music "Music/Mission_Briefing.ogg" fadeout 1.5

    scene bg bridge with dissolve
    show asaga plugsuit altneutral neutral:
        xzoom -1 xpos 0.2
    with dissolve
    show ava uniform alt neutral neutral with dissolve
    show chigara plugsuitlabcoat altneutral neutral:
        xpos 0.8
    with dissolve

    kay "Bring me up to date on our situation."

    show ava uniform handonhip neutral with dissolve

    ava "Cosette's pirates are operating from an asteroid base near Tydaria's moon."
    ava "Even with the help of our new pilots, the attack will not be easy."
    ava "The base itself has been built into an asteroid which the pirates dug out, then reinforced with armor and decked out with weapons.  The asteroid base is impervious to most conventional weaponry as a result.  Not only that, but the asteroids surrounding the base will make a natural environment for ambush."
    kay "Just one problem after another…"

    show asaga plugsuit handsonhips happy with dissolve

    asa "Don't worry, captain! These pirates are cowards. They're only used to fighting unarmed civilians and ragtag freelancers.  They'll be shakin' in their boots once they see the Sunrider barreling towards them!"

    show ava uniform armscrossed neutral with dissolve

    ava "Regardless, we should prepare the Sunrider's systems to the utmost before attempting any operation against the pirate's nest.  This is where our new guest comes in."

    show chigara plugsuitlabcoat altneutral forcedsmile with dissolve

    chi "O-oh… H-hello everyone."

    show chigara plugsuitlabcoat holdingipad smile with dissolve

    chi "I've been working on getting the Sunrider's Research and Development Lab operational.  I'd say that we're just about ready to open our doors."
    chi "From now, you'll be able to allocate funding to research new technologies, captain.  Just speak with me in the Lab and I can get started."
    kay "Sounds good. But where are we going to get the money for that?"

    show ava uniform handonhip neutral with dissolve

    ava "Missions. There're a lot of people out there in the galaxy who need a helping hand. If we sort their problems out, usually through judicious application of our main cannon, then we can be paid in return."
    kay "So we'll essentially be freelancing ourselves, huh? All right."

    ava "I've already prepared a potential mission for you, captain."
    ava "There's a PACT communications spire near us, which has been coordinating nearly 35 percent of their military efforts in the Neutral Rim.  Normally, it'd be guarded by an entire fleet, but we've hit a stroke of good luck."
    ava "An ion storm delayed the arrival of the spire's guardian fleet during a switchover, and now the communication spire is undefended.  If we were to warp in and destroy it, we could throw a wrench into all of PACT's war efforts in the Neutral Rim.  And not only that, the leaders of at least three neutral worlds would pay us handsomely."

    show asaga plugsuit altneutral neutral with dissolve

    asa "Hang on, capt'n. I have something else for you too."
    asa "There's been a band of particularly nasty thugs who've been kidnapping girls from Tydaria and selling them into the slave trade."
    kay "More of Cosette's goons?"

    show asaga plugsuit armscrossed mad with dissolve

    asa "Nah, these guys are something else. At least Cosette sticks to just killing and smuggling weapons."

    show ava uniform armscrossed lookleftmouthopen with dissolve

    ava "Human traffickers, captain. Out here, the laws protecting human dignity don't amount to much."
    asa "I just got a tip from a friend in the Tydarian government that their raiding party's been spotted in the Astral Expanse.  If we get there in time, we might still be able to catch them and put an end to their operation for good!"
    ava "Captain, as much as the trafficking of innocent girls aches our collective conscience, we have a war to win against PACT.  That communication spire's clearly more important than getting rid of some low life perverts."

    show asaga plugsuit excited angry with dissolve

    asa "But they're kidnapping innocents and selling them into the slave trade! Come on, captain, we can't just forget about them!"
    ava "Hmph. Whichever you choose captain, remember that time is of the essence for some missions.  We only have a limited window of time to perform side missions, so be sure to choose wisely which mission to undertake."
    ava "It is also in your discretion to ignore side missions and focus on our main objectives as well."
    kay "All right. I'll think on it and see what I can do."

    $ captaindeck = 1
    $ asa_location = None
    $ chi_location = "lab"
    $ chi_event = "researchanddevelopment"
    $ ava_location = "captainsloft"
    $ ava_event = "meetsophita"
    $ pro_location = None
    $ gal_location = "bridge"
    $ gal_event = "jumptogalaxy"

    $ warpto_astralexpanse = True
    $ warpto_pactstation1 = True

    $ mission_pirateattack = True

    $ liberty_weapons = [LibertyLaser(),Repair(),AccUp(),DamageUp()]
    $ liberty = create_ship(Liberty(),(5,7),liberty_weapons)
    $ sunrider.register_weapon(SunriderPulse()) #add a new weapon

    jump dispatch

label jumptogalaxy:

    hide screen deck1
    window show
    jump galaxymap

label meetsophita:

    $ captaindeck = 0

    hide screen deck0
    window show
    scene bg captainsoffice with dissolve

    show ava uniform handonhip neutral with dissolve

    ava "Captain, I have news for you."
    kay "What is it?"
    ava "I've received a message from the Mining Union. It seems that they're interested in speaking to you."
    kay "Any thoughts on what they want from us?"

    show ava uniform alt neutral neutral with dissolve

    ava "The Mining Union is one of the biggest private corporations in the galaxy. They control nearly every stage of the mining process, from the extraction of ores from the rock bed, to the refinement of those ores into starship grade steel. Last time I checked, the Mining Union provides the steel for nearly half the galaxy's navies."
    kay "So they stand to profit the most from a war, huh. How do I contact them?"
    ava "Your office is equipped with a FTL transponder.  You'll be able to make real time holographic calls from your office to anywhere else in the galaxy with it."
    ava "I'll update your address book with the Mining Union's representative.  It's a woman named Sophita Brooks.  You can also make FTL calls to anyone else on your address book from your office."
    kay "All right, thanks."

    $ ava_location = None

    menu:
        "(Use FTL Transponder)":
            jump FTLTransponderintro

        "(Return to ship map)":
            jump dispatch

label FTLTransponderintro:

    menu:
        "(Call Sopita Brooks)":
            jump introsophita
        "(Return)":
            jump dispatch

label introsophita:

    scene bg captainsoffice with dissolve

    $ cal_location = "captainsloft"
    $ cal_event = "ftltransponder"

    show sophita with dissolve

    sop "Captain. I'm pleased to make your acquaintance.  I am Sophita Brooks, vice secretary of operations."
    kay "Captain Kayto Shields of the starship Sunrider. And to what do I owe the pleasure?"
    sop "I come to you with a business opportunity. We at the Union are always eager to seek new partners. And certainly, the opportunity to work with the captain of a prototype warship does not come often."
    kay "I'm listening."
    sop "We've forwarded you a list of contracts.  If you wish, you may seek to undertake them. And of course, we will provide you with fair compensation for your efforts if you choose to undertake them."
    kay "Contracts? Of what sort?"
    sop "Of the sort requiring a big stick, captain. I'll leave it to you to figure out what I mean."
    sop "Further, if you wish to trade with us, I am available as your contact as well."
    kay "What do you have for sale?"
    sop "Proton torpedoes, tactical nuclear warheads, and all the other necessities of modern life."
    sop "Also, during our excavations, sometimes we find... shall we say, interesting artifacts.  While they're quite old, I am told they still possess impressive powers."
    kay "(Ancient artifacts... Could she be referring to lost technology?)"
    sop "I see I have your attention now, captain."
    sop "If you have the money, we will deliver these artifacts for your personal use. I'm sure that you will find them to be most helpful."
    kay "I'll keep that in mind."
    sop "Just remember, the Union will always be available to help - provided you have the money and the will."
    kay "The only two forces in the galaxy greater than any warship."
    sop "I see we are on the same page than."

    menu:
        "Show me what you have for sale.":
            jump unionstore
        "Good bye.":
            jump dispatch

label ftltransponder:

    $ captaindeck = 0

    hide screen deck0
    show window
    scene bg captainsoffice with dissolve

    menu:
        "(Call Sopita Brooks)":
            jump unionstore
        "(Return)":
            jump dispatch

label unionstore:

    scene store_back with dissolve
    window hide

    call screen store_union
    hide screen store_rocket

label researchanddevelopment:

    $ captaindeck = 1

    hide screen deck1

    scene bg lab

    show chigara plugsuitlabcoat holdingipad neutral with dissolve

    chi "Welcome to research and development, captain.  Is there anything I can help you with?"

    menu:
        "Let me allocate our funds.":
            jump allocatefunds

        "Nothing right now.":
            jump dispatch

label allocatefunds:

    python:
        if blackjack == None: # it shouldn't be possible to kill Havoc on the first turn, but if the player did...
            blackjack_weapons = [BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
            blackjack = create_ship(BlackJack(),(6,3),blackjack_weapons)

    call screen upgrade

label humantraffickers:

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene bg bridge

    show ava uniform handsonhips neutral with dissolve

    ava "Warp complete, captain. We're arriving at the Astral Expanse."
    kay "Scan for unregistered starships. They couldn't have gotten very far away."

    show ava uniform alt neutral mad with dissolve

    ava "Pirate signatures detected up ahead! It's the traffickers!"

    play sound "sound/redalert.ogg"
    scene bg bridgered
    show ava uniform alt neutral mad
    with dissolve

    kay "All hands, red alert! Set in an intercept course! Let's take these bastards out!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    scene bg bridgered:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show ava uniform alt neutral mad:
        xalign 0.5
        ease 0.025 xalign 0.45
        ease 0.05 xalign 0.55
        ease 0.025 xalign 0.5
        repeat 2
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide battlewarning

    call mission3_inits
    $ BM.mission = 3
    $ battle3_check1 = False
    jump battle_start

label mission3:

#    if not battle3_check1:
#        $BM.draggable = False

#        "test"

#        $ battle3_check1 = True #this ensures you see this dialogue only once

#        $ BM.draggable = True  #this enables dragging the viewport again.

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission3 #loop back
    else:
        pass #continue down to the next label

label aftermission3cutscene:

    $ captain_moralist += 5
    $ affection_asaga += 3

    stop music fadeout 1.5
    hide screen commands
    hide screen battle_screen

    scene bg bridgered with dissolve
    play music "Music/WorldBuilder.ogg"  fadeout 1.5    #this was missing, so I added it. not sure if it's the right song

    window show

    show ava uniform handonhip neutral with dissolve

    ava "Captain, some of the traffickers have managed to survive on escape pods.  They have dropped a distress beacon and are requesting relief.  What are your orders?"

    show asaga plugsuit armscrossed evil:
        xpos 0.2
    with wipedown

    asa "Eh-heh, serves 'em right!  Let's make an example of them and space them for good!"

    show chigara plugsuit handonchest sad:
        xpos 0.8
    with wipedown

    chi "A-ah... But shouldn't we turn them over to the authorities on Tydaria instead?"

    show ava uniform armscrossed frown with dissolve

    ava "The Tydarian justice system is underfunded as it is.  It'll be years until these traffickers face trial.  I say we speed the process up by leaving them here to their fates."

    menu:
        "We still have an obligation to the law.  Pick them up and lock them in the brig.":
            jump leavethemtydarianauthorities

        "Let them get a taste of their own medicine.  Jam the distress beacon and get us out of here.":
            jump jamdistressbeaconleave

label leavethemtydarianauthorities:

    $ affection_chigara += 1

    show ava uniform alt neutral neutral with dissolve

    ava "Aye captain.  I'll inform security to prepare to take in some prisoners."

    show asaga plugsuit excited angry with dissolve

    asa "But captain, these guys could just bribe themselves out of jail!  They're too dangerous to let live!"
    kay "Killing these people in cold blood won't put us in the right, Asaga. The justice system will deal with these crooks.  Not our guns."

    show asaga plugsuit armscrossed frustrated with dissolve

    asa "Arrgghh, all right, all right, you're right."

    show chigara plugsuit handstogether forcedsmile with dissolve

    chi "Asaga can get a little too excited at times, especially when people are being hurt.  I'm glad you're here to keep her on the right path, captain."

    jump mission3complete

label jamdistressbeaconleave:

    $ affection_ava += 1
    $ affection_asaga += 1

    show ava uniform alt neutral neutral with dissolve

    ava "Aye captain.  All ryders, return home.  Let's get out of here."

    show asaga plugsuit armscrossed evilgrin with dissolve

    asa "Heh heh, I jammed their beacon.  I hope these guys get what's coming!"

    show chigara plugsuit twidlefingers scared with dissolve

    chi "Oh dear, oh dear..."

    jump mission3complete

label mission3complete:

    $ mission3_complete = True

    jump dispatch

label pactstationattack:

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene bg bridge with dissolve

    window show

    show ava uniform handonhip mad with dissolve

    ava "Warp complete, captain.  The spire is right up ahead."
    ava "Warning, PACT signatures. The spire is being protected by squad of ships led by a PACT cruiser."
    kay "A cruiser? I thought you said this thing was undefended!"

    show ava uniform armscrossed neutral with dissolve

    ava "A single cruiser is undefended, captain.  Normally, there'd be an entire fleet surrounding the spire."
    ava "Be careful - that spire's decked out with rail guns. Our scans indicate that it's out of missiles though. Let's try taking it out from a distance."
    kay "All right. Asaga, Chigara, are you ready down there?"

    show asaga plugsuit neutralalt alert:
        xzoom -1 xpos 0.2
    with wipedown

    asa "On your word, capt'n! Let's take these guys out!"

    show chigara plugsuit excited scared:
        xpos 0.8
    with wipedown

    chi "I-I'll try my best, captain!"

    play sound "sound/redalert.ogg"
    scene bg bridgered
    show ava uniform armscrossed neutral
    show asaga plugsuit neutralalt alert:
        xzoom -1 xpos 0.2
    show chigara plugsuit neutral scared:
        xpos 0.8
    with dissolve

    kay "All hands, battle stations!"

    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide chigara
    hide battlewarning

    call mission4_inits
    $ BM.mission = 4
    $ battle_check1 = False
    jump battle_start

label mission4:

    if battle_check1 == False:

        $BM.draggable = False

        show ava uniform handonhip mad onlayer screens zorder 50 with dissolve

        ava "This is a hit and run operation, captain.  Our primary objective is the destruction of the PACT spire.  All other enemy units are secondary targets."
        kay "All right.  All units, focus on the spire!  Try to minimize combat with the escort fleet!"

        play sound "Sound/objectives.ogg"
        "Objective: Destroy the PACT Spire"

        hide ava onlayer screens with dissolve
        $ battle_check1 = True

        $ BM.draggable = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission4 #loop back
    else:
        pass #continue down to the next label

label mission4_end:

    $ mission4_complete = True

    hide screen battle_screen
    hide screen commands
    window show

    play music "Music/WorldBuilder.ogg" fadeout 1.5

    scene bg bridgered with dissolve
    show ava uniform fistup yes with dissolve

    ava "The spire has been destroyed! The mission is accomplished!"
    kay "All units, return to the Sunrider! Let's get out of here before PACT realizes what's going on and sends reinforcements."

    hide ava with dissolve
    show asaga plugsuit handsonhips grin with wipedown

    asa "Understood, captain! All wings are returning home. We did it!"

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    $ captaindeck = 1
    jump dispatch

label piratebaseattack:

    $ Random = renpy.random.randint(1,9)

    if Random == 1:
        scene space back1
    if Random == 2:
        scene space back2
    if Random == 3:
        scene space back3
    if Random == 4:
        scene space back4
    if Random == 5:
        scene space back5
    if Random == 6:
        scene space back6
    if Random == 7:
        scene space back7
    if Random == 8:
        scene space back8
    if Random == 9:
        scene space back9

    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 1.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0

    pause 1.0

    scene asteroid back1:
        yanchor 0 ypos 0
        ease 1.5 ypos -200
    with dissolve
    pause 1

    show sunrider_warpout_standard out:
        xpos 2300 ypos 1200 zoom 2
        ease 0.2 xpos 1000 ypos 500 zoom 0.5
    pause 0.2
    play sound "Sound/large_warpout.ogg"
    show cg_legionwarpin_missilefrigate_warpflash:
        zoom 1.5 xpos 1550 ypos 750
    show sunrider_warpout_standard

    pause 2.0

    scene bg bridge with fade
    window show

    show ava uniform alt neutral mad with dissolve

    ava "Warp successful. We've arrived at the Tydarian Asteroid Field."
    kay "All right everyone. Keep your eyes peeled for any pirate vessels. The rocks here are interfering with our scanners, so I'm 120 percent sure the pirates are waiting to ambush us."

    show asaga plugsuit excited happy:
        xpos 0.2
    with wipedown

    asa "Roger that! We're all ready down here in the hanger! Just give the word, capt'n!"

    show ava uniform alt neutral angry with dissolve

    ava "Alert. Enemies detected. Incoming pirate fleet!"

    show cosette plugsuit front evilsmile:
        xpos 0.8
    with wipedown

    cos "Huufufu... I didn't think anyone would be so bold as to attack our base. Show these whelps what happens when you cross Cosette Cosmos!"

    play sound "sound/redalert.ogg"
    scene bg bridgered
    show cosette plugsuit front evilsmile:
        xpos 0.8
    show asaga plugsuit excited happy:
        xpos 0.2
    show ava uniform alt neutral angry
    with dissolve

    kay "All hands! Battle stations!"

    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    show battlewarning:
        xpos 0.5 ypos 0.5
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide cosette
    hide battlewarning

    call mission5_inits
    $ BM.mission = 5
    $ battle_check1 = False
    jump battle_start

label mission5:

    $BM.battle_bg = "Background/asteroids3.jpg"

    if battle_check1 == False and BM.turn_count == 5:

        $BM.draggable = False
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
            create_ship(PirateGrunt(),(17,6),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
            create_ship(PirateGrunt(),(17,5),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
            create_ship(PirateGrunt(),(17,7),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
            create_ship(PirateGrunt(),(17,4),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])

            create_ship(PirateBomber(),(18,6),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])
            create_ship(PirateBomber(),(18,5),[PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()])

            create_ship(PirateDestroyer(),(12,1),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
            create_ship(PirateDestroyer(),(12,10),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        play sound "sound/Voice/Ava/Ava Others 4.ogg"
        $ PlayerTurnMusic = "music/Sora_no_Senritsu.ogg"

        $ BM.draggable = True
        $ battle_check1 = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission5 #loop back
    else:
        pass #continue down to the next label

label mission5_end:

    $ mission5_complete = True

    hide screen battle_screen
    hide screen commands
    window show

    scene bg bridge with dissolve

    play music "Music/The_Beginning_Of_The_Adventure.ogg" fadeout 1.5

    show ava uniform armscrossed smile with dissolve

    ava "I must say captain, I'm impressed. Perhaps we do stand a chance against PACT after all."

    menu:
        "Of course we do, Ava. This is only the beginning of our story.":
            jump onlythebeginningofstory

        "Don't let your guard down. We still have a lot of work ahead of us.":
            jump stillworkahead

label onlythebeginningofstory:

    ava "And I look forward to seeing how it'll continue."
    jump celebratehangar

label stillworkahead:

    show ava uniform salute talk with dissolve

    ava "Understood sir!"
    jump celebratehangar

label celebratehangar:

    show ava uniform neutral talk with dissolve

    ava "The girls should be in the hanger. You should go and celebrate with them."

    $ captaindeck = 1
    $ asa_location = "hangar"
    $ asa_event = "celebratepiratebase_asa"
    $ chi_location = None
    $ chi_event = None
    $ gal_location = None

    jump dispatch

label celebratepiratebase_asa:

    hide screen deck2

    scene bg hangar with dissolve

    $ asa_location = None
    $ asa_event = None

    show asaga plugsuit excited happy with dissolve

    asa "Uwah-hahahaha! We did it, capt'n, we did it! That pirate's nest is history!"

    show asaga plugsuit neutralalt smile with dissolve

    asa "Eh-hehh... As promised, I'll be glad to join you aboard the Sunrider. If you've got a war against PACT, then sign me up!"
    kay "Good to hear that. PACT's empire is still getting stronger with each day. We'll need all the help we can get if we're going to stop them."

    show asaga plugsuit vpose with dissolve

    asa "Understood, capt'n! Asaga Oakrun at your service!"

    menu:
        "What do you think will happen to the pirates?":
            jump thinkwillhappenpirates
        "What's going to happen with Chigara?":
            jump goingtohappenwithChigara
        "Let's move on. We need to assign you a room on the Sunrider.":
            jump assignasagaroom

label assignasagaroom:

    show asaga plugsuit altneutral happy with dissolve

    asa "I'm lookin' forward to a bed! It gets so uncomfortable sleeping on the Black Jack sometimes..."
    kay "Ava can help you get moved in."
    asa "Oh, by the way, I think Chigara's wanted to talk to you. You should go speak to her!"

    $ chi_location = "hangar"
    $ chi_event = "celebratepiratebase_chi"
    $ captaindeck = 2

    jump dispatch

label thinkwillhappenpirates:

    show asaga plugsuit thinking content with dissolve

    asa "Without their pirate's nest, their activities in this sector are practically finished. But I don't think we've seen the last of them yet."
    asa "They've probably retreated deeper into uncolonized space to recoup and rebuild their fleet. Then they'll probably come back for revenge."
    kay "Sounds like we've made some enemies today."

    show asaga plugsuit excited happy with dissolve

    asa "Don't worry 'bout a thing! I'm sure we'll be able to take care of them if they ever decide to come back!"

    menu:
        "What's going to happen with Chigara?":
            jump goingtohappenwithChigara
        "Let's move on. We need to assign you a room on the Sunrider.":
            jump assignasagaroom

label goingtohappenwithChigara:

    show asaga plugsuit excited happy with dissolve

    asa "Oh! You should talk to her about that. I think she wanted to speak to you anyways."

    menu:
        "What do you think will happen to the pirates?":
            jump thinkwillhappenpirates
        "Let's move on. We need to assign you a room on the Sunrider.":
            jump assignasagaroom

label celebratepiratebase_chi:

    hide screen deck2
    scene bg hangar

    show chigara plugsuit handonchest smile with dissolve

    chi "Ah, captain. I'm back."
    kay "Welcome back, Chigara. You did good out there."

    show chigara plugsuit twiddlefingers embarrassed with dissolve

    chi "Eh-heh... Really? I wonder..."
    kay "What are your plans now?"

    show chigara plugsuit handstogether sad with dissolve

    chi "Umm... Well, I guess with Asaga gone, it's going to get more lonely."
    chi "And business hasn't been so good at the bakery either..."
    kay "You should join us on the Sunrider too. We could use an extra pilot like you."

    show chigara plugsuit palmsup surprise with dissolve

    chi "E-eh!? Really!? Is that allowed?"
    kay "Of course it is. I'm the captain."

    show chigara plugsuit handstogether smile with dissolve

    chi "Eh-heh... Well, I guess I don't really have a choice, do I? In that case, I'll be in your care from now on, captain."
    kay "Welcome to the Sunrider, Chigara."
    kay "I've got to go now. You can speak to Ava if you have any problems with moving in."
    chi "Understood, captain. I look forward to working with you."

label credits:

     ###############################################################PLACE HOLDER

    scene bg black2 with dissolvelong
    play music "Music/Firn_ED.ogg" fadeout 1.5

    show credits1:
        xalign 0.5
        yalign 0.5
    with dissolve
    $ renpy.pause(2.0)

    hide credits1 with dissolve

    show credits2:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits3:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits4:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits5:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits6:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits7:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits8:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits9:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits10:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits11:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits12:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits13:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits14:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits15:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits16:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits17:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits18:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits19:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits20:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits21:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits22:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits23:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits24:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits25:
        xalign 0.5
        ypos 1.1
        linear 6.666666666666667 ypos 0.5
    $ renpy.pause(15.0)

    return

label devconsoleshow:
    show screen devconsole




