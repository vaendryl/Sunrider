## this is the main script file; everything starts here
## the goal is to offload as much declaring to the init module and jump
## back here for main control

## Declare characters used by this game.
#TO DO

    ##disable the main menu for easy iteration
label splashscreen:
    $BM = Battle()

    scene black
    pause 0.5
    show logo 1 with dissolve
    $ renpy.pause(2)
    show logo 2 with dissolve
    $ renpy.pause(2)
    hide logo with dissolve
    $ renpy.pause(0.5)

    stop music fadeout 1.0
    return

label quit:
    $ renpy.quit(relaunch=False)
    return


# The game starts here.
label start:

#####################################VARIABLE SET UP

    call initialize

    call firstvariables

#####################################VARIABLE SET UP

    #temporary
    jump test_battle


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

    scene bg bridge
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    window show

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

    scene bg engineering
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    window show

    ava "This is engineering. The ship's main reactor is located here and we can also use the lab to research and construct new equipment. Unfortunately, the research lab's not yet open."
    kay "That's also going to be available on Wednesday?"
    ava "Correct."

    $ captaindeck = 1
    $ ava_location = "messhall"
    $ ava_event = "messhall_tour"
    jump dispatch

label messhall_tour:

    hide screen deck0
    scene bg messhall
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    window show

    ava "This is the ship's mess hall. We can come down here to eat and relax after work."
    kay "Sounds good to me."

    $ captaindeck = 0
    $ ava_location = "captainsloft"
    $ ava_event = "captainsloft_tour"
    jump dispatch

label captainsloft_tour:

    hide screen ship_map
    scene bg captainsloft
    show ava uniform alt neutral neutral:
        xanchor 0.5 xpos 0.8
    with dissolve

    window show

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

    play music "Music/WorldBuilder.ogg"

    scene bg bridgered
    show ava uniform handonhip neutral
    with dissolve

    window show

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

    scene bg bridge
    show ava uniform alt neutral neutral
    with dissolve

    window show

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

        scene blackjack_tydaria_enter onlayer screens with dissolve
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

        show screen battle_screen

        python:
            blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
            blackjack = create_ship(BlackJack(),(6,3),blackjack_weapons)

        show asaga plugsuit neutralalt smile onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        asa "By the way, did you know about repeating attacks?"
        asa "Some weapons like assault rifles don't deal much damage, but shoot multiple times in a single attack.  It's a good way to deal reliable damage against units with high evasion like ryders."
        asa "Watch out though! They're totally useless against units with armor, like capital ships."
        asa "If you select a weapon, the third number listed on the enemy unit is that unit's armor rating.  Be careful when you're using your kinetic-type weapons especially, because armor's twice as effective against kinetics!"

        hide asaga onlayer screens with dissolve

        $ battle2_check2 = True
        $ BM.draggable = True


    $ BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission2 #loop back
    else:
        pass #continue down to the next label

label secondbattle_end:

    hide screen battle_screen
    hide screen commands

    scene bg black2 with horizontalwipereverse
    scene bg hangar with horizontalwipereverse
    window show

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

    scene bg bridge
    show ava uniform handonhip neutral
    with dissolve

    window show

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

    scene bg hangar
    show asaga plugsuit neutralalt smile
    with dissolve

    window show

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

    scene bg engineering
    show chigara plugsuitlabcoat holdingipad surprise
    with dissolve

    window show

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

    play music "Music/Mission_Briefing.ogg" fadeout 1.5

    scene bg bridge
    show asaga plugsuit altneutral neutral:
        xzoom -1 xpos 0.2
    show ava uniform alt neutral neutral
    show chigara plugsuitlabcoat altneutral neutral:
        xpos 0.8
    with dissolve

    window show

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

    $ liberty_weapons = [LibertyLaser(),Repair(),AccUp(),Disable(),FlakOff(),ShutOff()]
    $ liberty = create_ship(Liberty(),(5,7),liberty_weapons)
    $ sunrider.register_weapon(SunriderPulse()) #add a new weapon

    jump dispatch

label jumptogalaxy:

    hide screen deck1
    with dissolve
    jump galaxymap

label meetsophita:

    $ captaindeck = 0

    hide screen deck0

    scene bg captainsoffice
    show ava uniform handonhip neutral
    with dissolve

    window show

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
    $ cal_location = "captainsloft"
    $ cal_event = "introsophita"

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

    window hide

    python:
        BM.active_upgrade = None
        config.rollback_enabled = False
        buy_upgrades()
        renpy.block_rollback()
        config.rollback_enabled = True
        captaindeck = 1

    jump dispatch

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
    $ check1 = False
    jump battle_start

label mission3:

    if check1 == False:
        $BM.draggable = False

        show chigara plugsuit altneutral neutral onlayer screens:
            xpos 0.2 xzoom -1
        with dissolve

        chi "Ah captain.  The Liberty is capable of generating a small energy field."
        chi "Energy fields provide protection against laser based weapons for all units within the blue field indicated on the map."
        chi "Using allied defenses while exploiting weaknesses in the enemy's defenses is essential to winning."
        chi "No defense is perfect though, so make sure you exploit the holes in the enemy's defenses by using the best weapon type for the situation."

        hide chigara onlayer screens with dissolve

        $ check1 = True

        $ BM.draggable = True

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

        show chigara plugsuit altneutral neutral onlayer screens:
            xpos 0.2 xzoom -1
        with dissolve

        chi "Ah captain.  The Liberty is capable of generating a small energy field."
        chi "Energy fields provide protection against laser based weapons for all units within the blue field indicated on the map."
        chi "Using allied defenses while exploiting weaknesses in the enemy's defenses is essential to winning."
        chi "No defense is perfect though, so make sure you exploit the holes in the enemy's defenses by using the best weapon type for the situation."

        hide chigara onlayer screens with dissolve

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

    play music "Music/WorldBuilder.ogg" fadeout 1.5

    scene bg bridgered
    show ava uniform fistup yes
    with dissolve

    window show

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
    $ warpto_pactstation1 = False

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
    $ check2 = False
    jump battle_start

label mission5:

    $BM.battle_bg = "Background/asteroids3.jpg"

    if check2 == False:

        $BM.draggable = False
        show ava uniform handonhip neutral onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "The time has come for you to issue executive orders, captain."
        ava "As you win battles, you gain command points based on your battlefield performance."
        ava "Those command points may be spent to issue powerful executive orders which can quickly change the tide of combat."
        ava "Simply select the orders tab at the top left side of the battle screen and then select the order you wish to issue."

        hide ava onlayer screens with dissolve

        $BM.draggable = True

        $ check2 = True

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
    $ mission_pirateattack = False

    hide screen battle_screen
    hide screen commands

    play music "Music/The_Beginning_Of_The_Adventure.ogg" fadeout 1.5

    scene bg bridge
    show ava uniform armscrossed smile
    with dissolve

    window show

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

    $ asa_location = None
    $ asa_event = None

    scene bg hangar
    show asaga plugsuit excited happy
    with dissolve

    window show

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
    show chigara plugsuit handonchest smile
    with dissolve

    window show

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

    window hide

    stop music fadeout 1.5

    show eyecatch_top with eyecatch_wipe
    show eyecatch_bottom with eyecatch_wiperev
    show eyecatch_logo with dissolve
    $ renpy.pause (2.0)
    scene bg black2 with dissolvelong
    scene bg captainsoffice with dissolvelong

    window show

    play music "Music/The_Meteor.ogg"

    kay "Begin captain's log."
    kay "It's been a two weeks since we took down Cosette's base in the asteroids.  Since then, we've been chasing down minor criminals and undertaking hit and run attacks on PACT supply lines."
    kay "Despite our efforts, PACT's invasion of the Neutral Rim has continued unabated."
    kay "Six more governments have voluntarily joined PACT and two more have been conquered.  PACT's war machine has been indiscriminate, slaughtering both civilians and combatants alike."
    kay "In the mere month since Cera, millions more innocents have been murdered."
    kay "Unless something is done, the day when PACT rules the entire Neutral Rim appears to be fast approaching."

    play sound "sound/doorbell.ogg"

    "-Door bell-"
    kay "Come in."

    show ava uniform handonhip neutral with dissolve

    ava "Captain, we've just received an encrypted transmission."
    kay "Transmission? Where from?"
    ava "It's from the Solar Alliance.  Admiral Harold Grey is interested in speaking to you."
    kay "An audience with the admiral, huh?  I didn't realize we were so important already."
    ava "I've added the Admiral's line to your FTL transponder.  You can patch him through now."
    kay "All right, let's hear what the Admiral wants with us."

    $ badpolitics = False

    show ava uniform handonhip neutral:
        zoom 1.0
        ease 0.5 xpos 0.7
    pause 0.0001
    show grey:
        xpos 0.3
    with dissolve

    gre " Greetings, Captain of the Sunrider. I am Admiral Grey of the Alliance Space Force."
    kay "This is Captain Kayto Shields of the Cera Space Force.  This is my First Officer, Ava Crescentia.  What would the admiral of the Solar Alliance want with us?"
    gre " You must have my condolences for the loss of your great planet. It pains me to hear that another neutral world has fallen to PACT's war machine."
    kay "PACT must be stopped at all costs, admiral.  I am certain of this."
    gre " I understand you've been operating as a freelancer since your government's fall.  I've got a certain proposal that you might be interested in."
    kay "You've got my attention."
    kay "(Another interested client...  Being a mercenary armed with an assault carrier sure helps get business.)"
    gre "Our diplomats have been sent on a mission to the neutral world of Versta to convince its people to join the Alliance for quite some time."
    gre "Unfortunately, it does not seem like the mission was successful, and a PACT invasion fleet is rapidly approaching the world. I need you to go in there and get our men out before the PACT fleet finds them and kills them."
    gre "Of course, I will see to it that you and your crew are rewarded for your efforts."

    menu:
        "Why do you need us? Surely, the Alliance must have other ships up to the task.":
            jump othershipstask

        "Are the diplomats high ranking government officials? Why do you need them protected so much?":
            jump protectedsomuch

        "Is there really no hope of getting Versta to join the Alliance?":
            jump nohopejoin

        "You have a deal, admiral. Any mission against PACT is good in my book.":
            jump goodinbook

label othershipstask:

    gre " Unfortunately, because of the break down in talks, our military vessels are forbidden to enter Versta space. It is too dangerous getting the diplomats out without an armed escort, so we've had no choice but to resort to an unaligned vessel like the Sunrider."

    menu:
        "Are the diplomats high ranking government officials? Why do you need them protected so much?":
            jump protectedsomuch

        "Is there really no hope of getting Versta to join the Alliance?":
            jump nohopejoin

        "You have a deal, admiral. Any mission against PACT is good in my book.":
            jump goodinbook


label protectedsomuch:

    gre " Not per se. But an execution of our diplomats by PACT will be viewed by my government as an act of war, and the Alliance will have no choice but to declare war on PACT."
    gre "I've been ordered by President Alythe himself that an intergalactic war with PACT over a minor neutral rim world would be an unacceptable outcome."

    menu:
        "A devastating war between PACT and the Alliance now would cost the lives of billions. The Alliance should wait for a better moment to fight PACT.":
            jump matterforpoliticians

        "But PACT's going to take over the galaxy one way or another, admiral. The Alliance must stop them.":
            jump matterforpoliticians

label nohopejoin:

    gre " I'm afraid the latest reports from our negotiators have been grim. Now, Versta's in a state of total panic regarding the approaching invasion fleet, and they somehow think we're responsible for it."
    gre " My government views it as a lost cause and just want the diplomats pulled out before PACT gets their hands on them."

    menu:
        "Why do you need us? Surely, the Alliance must have other ships up to the task.":
            jump othershipstask

        "Are the diplomats high ranking government officials? Why do you need them protected so much?":
            jump protectedsomuch

        "You have a deal, admiral. Any mission against PACT is good in my book.":
            jump goodinbook

label matterforpoliticians:

    $ badpolitics = True

    gre " A matter for politicians to decide, unfortunately.  Hmph.  The President has ordered that we prevent an intergalactic war, so those are your directives."

    menu:
        "Why do you need us? Surely, the Alliance must have other ships up to the task.":
            jump othershipstask

        "Are the diplomats high ranking government officials? Why do you need them protected so much?":
            jump protectedsomuch

        "You have a deal, admiral. Any mission against PACT is good in my book.":
            jump goodinbook

label goodinbook:

    $ amissionforalliance = True

    gre " Good.  My staff have already mailed your First Officer with the details.  You have your orders, Sunrider. I expect results. Admiral Grey out."

    hide grey with dissolve
    show ava uniform handonhip neutral:
        zoom 1.0
        ease 0.5 xpos 0.5

    kay "A mission from the Alliance. Can't say I was expecting that."

    show ava uniform alt neutral neutral with dissolve

    ava "Times like this, almost everyone wants a hired gun.  Especially if you happen to have a very big gun.  At this rate, we might see a new golden age of privateering."
    kay "We might want to swap out your uniform with something more eye catching then.  Do you have the Pirate Commander design yet?"

    show ava uniform armscrossed frown with dissolve

    ava "No."

    if badpolitics == True:
        menu:

            "Tell me about the situation between the Alliance and PACT.":
                jump situationbetweenalliance

            "It doesn't sound like the admiral is a fan of his own government.":
                jump notfanofgov

            "Well, now we know our next step. Let's get underway to Versta.":
                jump getunderwayvesta

    menu:

        "Tell me about the situation between the Alliance and PACT.":
            jump situationbetweenalliance

        "Well, now we know our next step. Let's get underway to Versta.":
            jump getunderwayvesta

label notfanofgov:

    show ava uniform armscrossed neutral with dissolve

    ava "Hmm... I get the same feeling as well."
    ava "So far, the President of the Alliance has been avoiding war with PACT at all costs. But my sense is that the military establishment inside the Alliance is already gearing up for a war."
    kay "That makes sense. PACT intends to take over the galaxy one way or another. It's only matter of time until the Alliance will be forced into the fight."

    menu:

        "Tell me about the situation between the Alliance and PACT.":
            jump situationbetweenalliance

        "Well, now we know our next step. Let's get underway to Versta.":
            jump getunderwayvesta

label situationbetweenalliance:

    show ava uniform alt neutral neutral with dissolve

    ava "What do you want to know?"

    menu:
        "Tell me more about the Alliance.":
            jump tellmorealliance

        "Tell me more about PACT.":
            jump tellmorepact

        "The Alliance and PACT aren't at war yet?":
            jump alliancepactnowar

label tellmorealliance:

    ava "The Solar Alliance is the current power house of the galaxy. It's actually a military, economic, and research alliance between the planet of Solaris and numerous other worlds."
    kay "It doesn't sound like everyone wants to join the Alliance though."
    ava "Some planets simply wish to be left alone. The planets that make up the neutral rim are too far from Solaris and have so far avoided joining the Alliance. Cera was one of those planets."
    kay "Still, isn't the Alliance a democracy? What's so bad about it?"
    ava "A space democracy is a difficult thing to maintain. A single politician might need to represent over a billion citizens."
    ava "Recently, political deadlock has characterized the Alliance."
    ava "The United Universalist Party in the Solar Congress wishes to take the war path against PACT. Meanwhile, the Progress Party wishes a negotiated settlement."
    ava "Neither party has managed to get anything done because of their irreconcilable differences."
    ava "President Alythe has avoided war with PACT at all costs. Even though PACT continues to swallow up most of the neutral rim, the Alliance has done nothing about it."

    menu:
        "Tell me more about PACT.":
            jump tellmorepact

        "The Alliance and PACT aren't at war yet?":
            jump alliancepactnowar

        "Thanks for the history lesson. That's all I needed to know.":
            jump thankshistorylesson

label tellmorepact:

    ava "PACT, short for the People's Alliance for Common Treatment, was originally an independence movement which started at New Eden against the New Empire."
    ava "New Eden was a paradise planet which was rich in valuable resources. However, the rulers of the New Empire hoarded the planet's riches for themselves, while the masses lived in poverty."
    ava "Eventually, the division in wealth reached a critical point and the people of New Eden declared a revolution against their own rulers."
    kay "If they're an independence movement, then why are they trying to take over the galaxy now?"
    ava "The independence movement went horribly wrong shortly after PACT overthrew the New Empire. Extreme nationalism and paranoia set in."
    kay "So then what happened?"
    ava "A mysterious figure known as Veniczar Arcadius took power. Much about him is shrouded in mystery. He appears behind a mask at all times and speaks only through a computer."
    ava "During the war of independence, he was a heroic figure who freed his people. But after he took power, he became a different man."
    ava "Arcadius wielded the nationalism and the paranoia of his people and led them on a war path, beginning PACT's rapid expansion. You can see that today, as PACT conquers every planet in the neutral rim, one by one. Nobody really knows when they're going to stop."

    menu:
        "Tell me more about the Alliance.":
            jump tellmorealliance

        "The Alliance and PACT aren't at war yet?":
            jump alliancepactnowar

        "Thanks for the history lesson. That's all I needed to know.":
            jump thankshistorylesson

label alliancepactnowar:

    show ava uniform handonhip neutral with dissolve

    ava "No, but I wouldn't bet on that lasting. War between the two powers is all but inevitable, I would say."
    kay "What makes you say that?"
    ava "So far, PACT has only been hitting neutral rim planets that are far away from Solaris. Eventually though, the entire neutral rim is going to belong to PACT. And then who's PACT going to attack next?"
    kay "Right, I see your point."

    menu:
        "Tell me more about the Alliance.":
            jump tellmorealliance

        "Tell me more about PACT.":
            jump tellmorepact

        "Thanks for the history lesson. That's all I needed to know.":
            jump thankshistorylesson

label thankshistorylesson:

    if badpolitics == True:
        menu:

            "Tell me about the situation between the Alliance and PACT.":
                jump situationbetweenalliance

            "It doesn't sound like the admiral is a fan of his own government.":
                jump notfanofgov

            "Well, now we know our next step. Let's get underway to Versta.":
                jump getunderwayvesta

    menu:

        "Tell me about the situation between the Alliance and PACT.":
            jump situationbetweenalliance

        "Well, now we know our next step. Let's get underway to Versta.":
            jump getunderwayvesta

label getunderwayvesta:

    show ava uniform neutral neutral with dissolve

    ava "Understood captain."

    $ captaindeck = 0
    $ asa_location = None
    $ chi_location = None
    $ gal_location = "bridge"
    $ res_location = "lab"
    $ res_event = "allocatefunds"
    $ warpto_versta = True
    $ warpto_occupiedcera = True
    $ warpto_tydaria = True
    $ warpto_astralexpanse = True

    jump dispatch

label jumphotversta:

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

    scene versta_approach:
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


    ava "We've arrived at the planet of Vesta."

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5
    show ava uniform alt neutral angry

    ava "Wait a minute... Alert! Drop point is hot! I'm detecting PACT signatures all around us!"

    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform alt neutral angry
    with dissolve

    kay "Red alert! Scramble our ryders!"

    show asaga plugsuit excited happy:
        xpos 0.2
    with wipeup

    asa "We're ready at your command, capt'n! Just give the word!"
    kay "One hell of an entrance... All right everyone, let's take the enemy out!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    show layer master at shake1
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide battlewarning

    call mission6_inits
    $ BM.mission = 6
    $ check1 = False
    jump battle_start

label mission6:

    $BM.battle_bg = "Background/space7.jpg"

    if check1 == False and BM.turn_count == 2:

        $BM.draggable = False

        show ava uniform alt neutral angry onlayer screens zorder 50:
            xpos 0.8
        with dissolve

        ava "I'm detecting a new warp signature..."

        scene space back7 onlayer screens zorder 50 with dissolve
        pause 0.5

        play sound "sound/small_warpout.ogg"

        show phoenixwarpin onlayer screens zorder 50:
            xpos 1500 ypos 150 zoom 0.0
            ease 0.1 xpos 960 ypos 540 zoom 1.0
        pause 0.1
        hide phoenixwarpin onlayer screens zorder 50
        show white onlayer screens zorder 100:
            alpha 0
            ease 0.1 alpha 0.4
            ease 0.1 alpha 0
        show phoenixwarpout onlayer screens zorder 50

        pause 0.0001

        show ava uniform alt neutral angry onlayer screens zorder 50:
            xpos 0.8
        with dissolve

        ava "An unidentified ryder has just entered the battle!"
        kay "A ryder capable of warping...?"
        ava "It seems to be using some sort of booster pack..."
        kay "Flag?"
        ava "Unidentified... It doesn't match any of our pirate designs ..."

        play sound "sound/Laser 1.ogg"
        show phoenixwarpout laser onlayer screens zorder 50 with dissolve
        show phoenixwarpout onlayer screens zorder 50 with dissolve

        hide ava onlayer screens zorder 50
        show asaga plugsuit handsonhips surpriseangry onlayer screens zorder 50:
            xpos 0.8
        with dissolve

        asa "W-woah! W-whatever that is, it isn't friendly!"
        kay "Tsch... For now, treat it as a PACT special unit! Take it down along with the rest of the enemy!"

        hide asaga onlayer screens
        hide phoenixwarpout onlayer screens
        hide space back7 onlayer screens

        $ BM.draggable = True
        $ check1 = True

        show screen battle_screen

        python:
            create_ship(PhoenixBoaster(),(15,6),[PhoenixBoasterLaser(),PhoenixBoasterAssault()])

    $ BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission6 #loop back
    else:
        pass #continue down to the next label

label mission6victory:

    $ mission6_complete = True

    hide screen battle_screen
    hide screen commands

    scene bg bridgered
    show ava uniform neutral neutral
    with dissolve

    window show

    show asaga plugsuit excited happy:
        xpos 0.2 xzoom -1
    with wipeup

    asa "We did it! The PACT fleet's history!"

    show chigara plugsuit handonchest smile:
        xpos 0.8
    with wipeup

    chi "Ah... It looks like we won."

    show ava uniform armscrossed frown with dissolve

    ava "Don't celebrate just yet. That was too weak to have been the main invasion force. It was just an recon squad."
    kay "And now the enemy knows we're here."
    kay "Asaga, Chigara, return to the Sunrider for now."

    hide asaga with dissolve
    hide chigara with dissolve

    show ava uniform handonhip neutral with dissolve

    ava "Captain, I'm still reading the PACT special unit on scanners."
    kay "Left behind, huh... I guess it can't go anywhere without its warp booster."
    ava "Your orders?"
    kay "Disable it, and then get the Liberty to haul it to our hangar. I think we have ourselves our first PACT prisoner."

    show ava uniform salute neutral with dissolve

    ava "Understood captain."

    scene bg hangar with dissolve
    play music "Music/Mission_Briefing.ogg"
    show asaga plugsuit neutralalt alert with dissolve

    asa "Oh! Chigara tells me that we have a prisoner!"
    kay "Yeah."

    show asaga plugsuit armscrossed confident with dissolve

    asa "Uu-fufufu... So... You gonna interrogate the pilot? Throw 'em out the airlock if they don't spill all their secrets?"
    kay "Uhhh no, I was actually just planning on asking some questions and then turning him over to the Alliance after this is all done."

    show asaga plugsuit altneutral sad with dissolve

    asa "Aw, so much for how they do it on the holovision..."

    show ava uniform armscrossed frown:
        xpos 0.2
    with dissolve

    ava "Hmph. Stand back, everyone. This guy might be dangerous."

    show chigara plugsuit twiddlefingers scared:
        xpos 0.8
    with dissolve

    chi "Huu... I think I'll just watch from back here..."
    kay "Alright, open the ryder's hatch and get our prisoner out."

    show ava uniform armscrossed frown:
        zoom 1
        ease 0.5 xpos 0.4
    show asaga plugsuit altneutral sad:
        zoom 1
        ease 0.5 xpos 0.6
    show chigara plugsuit twiddlefingers scared:
        zoom 1
        ease 0.5 xpos 0.8
    pause 0.001
    show icari plugsuit neutral closedeyes:
        xpos 0.12
    with dissolve

    ica "... ... ..."

    show asaga plugsuit excited surprise with dissolve

    asa "O-oh! She's just a girl like us, Chigara!"

    show icari plugsuit neutral neutral with dissolve

    ica "Is this... a PACT vessel?"
    kay "No. I'm Captain Kayto Shields of the Cera Space Force. Welcome aboard the Sunrider."

    show icari plugsuit armscrossed neutral with dissolve

    ica "Cera? I thought you were conquered by PACT."
    kay "Not all of us. Who are you?"
    ica "Icari Isidolde. Private mercenary."
    kay "Were you hired by PACT?"

    show icari plugsuit armscrossed confident with dissolve

    ica "Heh... Nothing of the sort. Was on a mission. I can't tell you more than that."

    show ava uniform armscrossed frowntalk with dissolve

    ava "You're now our prisoner.  Put your hands up and turn over all your weapons."
    kay "Have security escort our guest to the brig.  We'll continue with our discussion there."

    scene bg brig
    show brigoverlay
    with dissolve
    show icari plugsuit armscrossed wait behind brigoverlay:
        xpos 0.3
    with dissolve
    show ava uniform alt neutral neutral:
        zoom 1.5 xpos 0.7 ypos 1.35
    with dissolve

    kay "How's our guest holding up, Ava?"

    show ava uniform armscrossed neutral with dissolve

    ava "Per protocol, we've scanned her for contraband.  We found enough assassination tools on her person to topple small governments.  I'd say we caught a professional hitman."
    kay "Anything identifying who she's working for?"
    ava "We scanned through the database on her ryder and all of her electronics and found nothing.  She's no amateur."
    kay "All right. Let's try talking to her."

    show icari plugsuit armscrossed frown with dissolve

    ica "Tsch. I sure hope you haven't dirtied up my ryder."
    kay "You don't need to worry about that. Why don't you avoid all this trouble by giving us some info?"

    show icari plugsuit handonhip lookawaysnide with dissolve

    ica "Heh, what do you want?"
    kay "Why'd you attack us? Are you working for PACT?"

    show icari plugsuit handonhip annoyedtalk with dissolve

    ica "I already told you, I don't work for those fanatics. Haven't you been listening?"
    ica "I attacked you because I thought you were PACT freelancers.  Last I heard, the entire Cera Space Force was impressed into the PACT Fleet and the few survivors became pirates or freelancers."
    ica "If you haven't noticed, this area of the galaxy's like the Wild Wild West. Plenty of guns for sale have thrown their lots with PACT nowadays, thinking that's the way the galaxy's gonna spin."

    show icari plugsuit handonhip lookawaysnide with dissolve

    ica "Heh, not if I have anything to say about it anyways."
    kay "You're no friend of PACT?"

    show icari plugsuit handonhip annoyedtalk with dissolve

    ica "No! Hate 'em. I would have busted up their whole fleet back there."

    show icari plugsuit armscrossed tsun with dissolve

    ica "If it weren't for you smashing up my booster anyways. Ugh..."
    kay "Well, at least we're on the same side then."

    show icari plugsuit handonhip annoyedtalk with dissolve

    ica "So are you going to tell me what a Cera captain's doing here?"

    show ava uniform alt neutral angry with dissolve

    ava "We're asking the questions here, not you."

    show icari plugsuit handonhip snide with dissolve

    ica "Heh, what, we're not here to become friends?"
    ica "C'mon captain, throw me something here. Aren't we going to work this out together?"
    kay "All right."
    kay "We're here on Alliance business.  We're doing a bit of freelancing ourselves."

    show icari plugsuit handonhip lookawaysnide with dissolve

    ica "Heh, interesting."
    kay "There, you have our secret. How about you tell me yours?"
    ica "... ... ..."

    show icari plugsuit armscrossed frown with dissolve

    ica "All right, captain. You've made your point. If I tell you mine, you're going to have to promise not to lay a finger on my Phoenix. Oh, and also to get your damned housewife's scowl out of my face."

    show ava uniform armscrossed frown with dissolve

    ava "Hmph."
    kay "All right.  I suppose we could lay off your ryder."

    show icari plugsuit armscrossed tsun with dissolve

    ica "I hope so."

    show icari plugsuit handonhip annoyedtalk with dissolve

    ica "You wouldn't have happened to have been hired by an Alliance admiral who looked like a grey old statue, would you?"
    kay "Well, he certainly was grey.  In more ways than one."

    show icari plugsuit handonhip snide with dissolve

    ica "Hahahaha.  That bastard hasn't changed a bit."
    kay "You know him?"
    ica "Know him? I've worked for him for ages."
    kay "Doing what?"
    ica "What do you think? If you want anything in this galaxy, you need some undesirables erased.  Oh, nothing terrible, mind you, the admiral's a pretty principled guy."
    ica "But you have a crazed criminal on the loose? Then you need my services."
    ica "Have a sleazy dictator whose been getting too out of hand? I can set that straight too.  Ongessite prices too high? I provide the stick - and the Admiral provides the carrots. If you catch my drift."
    kay "You're a contract assassin."
    ica "Let me guess, you're here about the diplomats on Versta right?"
    kay "Looks like the big secret's out."

    show icari plugsuit armscrossed confident with dissolve

    ica "Heh."
    kay "What's a contract assassin like you doing here then?  Versta's a rescue mission.  Nobody needs to be shot."

    show icari plugsuit neutral snide with dissolve

    ica "Rescue mission? Is that what the Admiral told you?"

    show ava uniform armscrossed frowntalk with dissolve

    ava "If you know something, you better spill it."
    ica "Not so fast.  That little information's gonna cost you.  Nothing big, mind you."
    ava "If I recall correctly, you're the one stuck sitting in a jail cell, not us."

    show icari plugsuit armscrossed tsun with dissolve

    ica "I'm not going to go around revealing client information unless there's security for me."
    ica "And I'd say you need my help more than ever if you still think you're here on a rescue mission.  If I tell you what's going on, you let me outta this cell and give me back my ryder."
    kay "(It seems like she's interested in talking.  Let's play along for now and see what she says.)"
    kay "All right.  If we're both against PACT, I'm interested in seeing what you have to say."
    ica "I may be an assassin, but I'm no scoundrel.  You can depend on my words, captain."

    show icari plugsuit neutral neutral with dissolve

    ica "War between the Solar Alliance and PACT is inevitable.  Everyone knows that and they're just too scared to admit it.  The galaxy's on the brink of an interstellar war on a scale it hasn't seen in one hundred years."
    ica "There's a certain faction within the Alliance which understands this and wants to intervene before the entire Neutral Rim's PACT's back yard."
    ica "And honestly, I'd rather not be bowing to the Veniczar, so I say good on them.  The only issue is that President Alythe's a damned pussy who couldn't fight an angry duck to save his own life."
    ica "The Alliance needs a push.  And this crisis is the opportunity everyone's been waiting for to bring the Alliance into this fight."

    show ava uniform handonhip neutral with dissolve

    ava "So you've been hired by this faction to hover around Vesta, and make sure that those diplomats are captured by PACT to spark a war.  Is that what you're saying?"
    ica "Now you're catching on.  You let me ensure that those diplomats are captured by PACT, and you can bet you'll have the Alliance's full support behind you in your war."
    kay "And if they find out I had anything to do with their capture?"

    show icari plugsuit armscrossed neutral with dissolve

    ica "Who gives a damn? The Alliance military wants PACT to get those diplomats to get this war started anyways.  You'll probably get a shiny medal for saving the Neutral Rim or something."
    kay "(This is a little hard to believe, but her hatred of PACT seems sincere.  What should I do?)"

    menu:
        "All right, you've made your point.  I'll let you out of your cell, but you'll be confined to quarters for now while we perform our own investigation.":
            jump outcellinvestigation
        "I don't believe you.  You can stay here in your cell while we perform our own investigation.":
            jump dontbelieveicari

label outcellinvestigation:

    $ affection_icari += 1

    show icari plugsuit armscrossed annoyed with dissolve

    ica "Tsch, that's the best you can do?"
    kay "It's not like you're going anywhere on your ryder without a booster pack.  So enjoy the warm bed."
    ica "Fine, just get me outta this cell and bring me something to eat."

    $ asa_location = "messhall"
    $ asa_event = "whattodoicari_asa"

    $ chi_location = "engineering"
    $ chi_event = "whattodoicari_chi"

    $ ava_location = "bridge"
    $ ava_event = "whattodoicari_ava"

    $ cal_location = "captainsloft"
    $ cal_event = "ftltransponder"

    $ gal_location = None
    $ captaindeck = 1
    jump dispatch

label dontbelieveicari:

    show icari plugsuit neutral angry with dissolve

    ica "Are you kidding me, captain!?  We had a deal!"
    kay "I didn't promise anything.  Ava, get our guest something to eat.  She'll be staying here for a while."
    ava "Understood."

    show icari plugsuit armscrossed bitter with dissolve

    ica "Tsch... Whatever.  Once you find out that I'm telling the truth, you'll be back here begging for help.  Just you wait!"

    $ asa_location = "messhall"
    $ asa_event = "whattodoicari_asa"

    $ chi_location = "engineering"
    $ chi_event = "whattodoicari_chi"

    $ ava_location = "bridge"
    $ ava_event = "whattodoicari_ava"

    $ cal_location = "captainsloft"
    $ cal_event = "ftltransponder"

    $ gal_location = None
    $ captaindeck = 1
    jump dispatch

label whattodoicari_ava:

    hide screen deck1

    scene bg bridge
    show ava uniform alt neutral neutral:
        zoom 1 xpos 0.5
    with dissolve

    window show

    kay "Did you get our guest set up?"
    ava "She's getting comfortable. About what she said..."

    menu:
        "She's got a point. Sparking an Alliance-PACT war is the only way we can stop PACT.":
            jump pointwaronlyway

        "She's obviously crazy. We're going to complete our mission and save those diplomats.":
            jump obviouslycrazysave

label pointwaronlyway:

    $ captain_prince += 1

    show ava uniform armscrossed neutral with dissolve

    ava "I admit, the only power in the galaxy capable of stopping PACT is the Alliance.  But can we trust the mercenary's words?"
    kay "PACT's destroyed our home. We're going to get payback for what they've done, no matter what."
    ava "I hope that you're not being blinded by what happened at Cera."
    kay "It's not like you disagree."
    ava "... ... ..."

    show ava uniform neutral lookleft with dissolve

    ava "True, Alliance intervention is the only hope we have at liberating Cera.  Liberating our home world will take a fleet.  And the Alliance has a mighty one at that."
    kay "PACT's going to take over the whole galaxy unless the Alliance steps in. If a few diplomats have to be sacrificed for the safety of the galaxy, so be it."

    show ava uniform handonhip neutral with dissolve

    ava "Very well, captain. I may not trust the mercenary, but I don't disagree with what you're saying."

    jump consideringoptionsfornow

label obviouslycrazysave:

    $ captain_moralist += 1

    ava "I agree we should be careful about her. But given our situation, we should consider what she has told us."
    kay "I won't have the blood of civilians on my hands, Ava."

    show ava uniform armscrossed neutral with dissolve

    ava "Noble of you. But know this captain: War between the Alliance and PACT will happen one way or another."
    ava "All we would be doing would be hastening the process. Every second we wait, PACT will have conquered one more neutral world and grown that much stronger."
    ava "The quicker the war between the Alliance and PACT begins, the more lives we can save in the end."

    jump consideringoptionsfornow

label consideringoptionsfornow:

    kay "Anyways, I'm still considering our options for now. What's our next step?"

    show ava uniform neutral talk with dissolve

    ava "I've made contact with the Alliance diplomats.  They're going to attempt to make an escape soon."
    kay "All right.  Will we be bringing them aboard?"
    ava "Actually, they've arranged to escape on the civilian liner Agamemnon.  We'll be providing escort in case things gets hairy."
    kay "Civilian liner?  I'm not so sure..."
    ava "They tell me international law prohibits them from coming aboard a foreign military vessel."
    kay "(That's the first time I've ever heard of a rule like that.  Something's amiss...)"
    kay "One challenge after another.  Keep me posted, Ava."

    $ ava_location = None
    $ pro_location = "captainsloft"
    $ pro_event = "proceed_rescuediplomats"
    $ captaindeck = 1

    jump dispatch

label whattodoicari_asa:

    hide screen deck0

    scene bg messhall
    show asaga uniform neutral happy
    with dissolve

    window show

    asa "Oh, did you need me for something, capt'n?"
    kay "I presume you've heard the rumors about the mercenary we've captured."

    show asaga uniform excited grin with dissolve

    asa "Well, we're still gonna rescue those diplomats, aren't we? And beat up the PACT fleet, of course!"
    kay "I don't think we'll be able to destroy the whole invasion fleet by ourselves, Asaga..."

    show asaga uniform neutral happy with dissolve

    asa "Don't worry, don't worry! Just leave it to me and mah Black Jack! We'll take care of the invasion fleet in no time!"

    menu:
        "What do you think about what the mercenary said?":
            jump whatdoyouthink

        "Just be careful out there and don't do anything reckless, okay?":
            jump caredontreckless

label whatdoyouthink:

    show asaga uniform armscrossed nonono with dissolve

    asa "No, no, no, capt'n! You can't do that and let innocents die!"

    show asaga uniform excited angry with dissolve

    asa "You gotta stand for what's right!  We're gonna win this fight the hard way, but the right way!"

    menu:
        "But we'll never beat PACT without the Alliance's help. We're just one ship.":
            jump neverbeatpactalliance
        "You're right.  We're going to win this war with our principles intact.":
            jump betterpactwinprinciples

label neverbeatpactalliance:

    $ captain_prince += 1

    show asaga uniform armscrossed confidenthappy with dissolve

    asa "Ahh, don't be so down, capt'n! You have me and the Black Jack! Together, we can do anything!"

    jump thanksfortalkasaga

label betterpactwinprinciples:

    $ captain_moralist += 1

    show asaga uniform excited grin with dissolve

    asa "Hell yeah, capt'n!"
    jump thanksfortalkasaga

label thanksfortalkasaga:

    kay "Uh, I'll keep that in mind. Thanks."

    show asaga uniform neutral smile with dissolve

    asa "I'll see you later!"

    $ asa_location = None
    $ pro_location = "captainsloft"
    $ pro_event = "proceed_rescuediplomats"
    $ captaindeck = 0

    jump dispatch

label caredontreckless:

    asa "Of course, capt'n!"

    $ pro_location = "captainsloft"
    $ pro_event = "proceed_rescuediplomats"
    $ captaindeck = 0

    jump dispatch

label whattodoicari_chi:

    hide screen deck1

    scene bg engineering
    show chigara uniform handsup surprise
    with dissolve

    window show

    chi "E-eah! O-oh, sorry, captain, I didn't see you coming..."

    menu:
        "What's your take on what's going on with the mercenary?":
            jump yourtakemercenary
        "How's the research station coming?":
            jump howsresearchstation

label yourtakemercenary:

    show chigara uniform twiddlefingers smile with dissolve

    chi "Ummm... I'm not very good with making decisions, so I think you'd be much better suited to thinking about it than I am..."

    show chigara uniform handstogether smile with dissolve

    chi "Eh-heh. Whatever the captain decides, I'm sure it'll be the right decision."

    menu:
        "Thanks for the vote of confidence, Chigara.":
            jump thanksconfidencechigara
        "Are you sure? You're smarter than anyone else I've ever met.":
            jump smarteranyoneelse

label howsresearchstation:

    show chigara uniform neutral neutral with dissolve

    chi "Ah, I've finished setting my equipment up. Even though it's still at the beginning stages, I'll be able to get started on some basic research projects."

    menu:
        "Good to hear. I'll allocate funding later.":
            jump goodallocatefundinglater
        "Great, let's see what projects need funding...":
            jump allocatefunds

label goodallocatefundinglater:

    chi "Understood, captain."

    menu:
        "What's your take on what's going on with the mercenary?":
            jump yourtakemercenary
        "Thanks for your work.  I'll see you later, Chigara.":
            jump thanksbyechigara

label smarteranyoneelse:

    chi "Uh-huh. I may be comfortable with machines, captain, but that's just about it. Where people are concerned, I feel... Well, I just don't feel like I understand them very well."
    kay "Maybe machines really are easier to deal with than people..."

    menu:
        "How's the research station coming?":
            jump howsresearchstation

        "Thanks for your work.  I'll see you later, Chigara.":
            jump thanksbyechigara

label thanksconfidencechigara:

    chi "Eh-heh. Any time, captain. Was there something else you needed?"

    menu:
        "How's the research station coming?":
            jump howsresearchstation

        "Thanks for your work.  I'll see you later, Chigara.":
            jump thanksbyechigara

label thanksbyechigara:

    show chigara uniform neutral neutral with dissolve

    chi "Good bye, captain."

    $ chi_location = None
    $ pro_location = "captainsloft"
    $ pro_event = "proceed_rescuediplomats"
    $ captaindeck = 1

    jump dispatch

label proceed_rescuediplomats:

    hide screen deck0
    stop music fadeout 1.5
    scene black
    window show
    with dissolve

    kay "Well then, I think I'll return to my room to think about what to do..."

    scene bg captainsoffice with dissolve

    kay "Begin captain's log. We've made contact with the diplomats on Versta and are going to attempt an escape."
    kay "I should be focused on getting them out of here safe, but I can't get what the mercenary said out of my mind."
    kay "Some part of my head thinks that she has some ulterior motive and she's tricking us all. Maybe she's a PACT spy and making us wander into a trap."
    kay "Maybe the diplomats know something that PACT doesn't and she's just fooling us into silencing them."
    kay "Or maybe she's really telling the truth."

    play music "Music/A_Dark_Dream.ogg"
    scene bg captainsoffice_nolights
    show captainsoffice_nolights_overlay
    with dissolve

    kay "What the-"

    show icari plugsuit armscrossed confident behind captainsoffice_nolights_overlay with dissolve

    ica "Hello again, captain. Unfortunately, it looks like you'll have to upgrade your security system, since it was all too easy for me to crack."
    kay "Security, get to my quarters now!"
    ica "Of course, I've already disabled all communications out of this room as well."
    kay "What do you want, mercenary?"

    show icari plugsuit handonhip snide behind captainsoffice_nolights_overlay with dissolve

    ica "Relax captain. I'm not here to slit your throat, or anything gory like that. I just want to talk."
    kay "Just talk?"

    show icari plugsuit altneutral neutral behind captainsoffice_nolights_overlay with dissolve

    ica "I never imagined that I'd find myself onboard a Cera vessel. It must be hard, being the only ship left."
    kay "I don't disagree, but we get by."
    ica "Tell me... How many people died at Cera that day?"

    menu:
        "Your attempts at manipulating me won't work, mercenary.":
            jump photoalbumlook
        "Too many.":
            jump photoalbumlook

label photoalbumlook:

    show item album:
        xpos 0.1 ypos 0.2
    with dissolve

    ica "Who's that in the picture album behind you?"
    kay "That's none of your business."

    show icari plugsuit altneutral smallsnide with dissolve

    ica "She looks young.  You don't seem like a father though.  So I'm thinking... your sister?"
    kay "You're walking on thin ice.  I suggest you drop it."

    hide item with dissolve

    ica "What's the matter, captain? Did I hit a soft spot?"

    show icari plugsuit altneutral smallsnide:
        zoom 1
        ease 1.00 zoom 1.5 ypos 1.4

    ica "Are you scared for her?"
    ica "... ... ..."

    show icari plugsuit neutral neutral with dissolve

    ica "I know what it's like to lose family... Listen to me, captain."
    ica "PACT killed my entire family years ago.  I swore I'd get PACT back for what they did, and I'm finally so close."
    ica "We can work together, you and I.  Let's bring the Alliance into this war and end the PACT invasion.  I'll even work under you as a pilot if you're going after PACT."
    kay "What if I said I don't trust you?"
    ica "How about I let you in a little secret, captain..."
    kay "I thought mercenaries didn't share secrets."
    ica "I'm willing to make an exception, just for you."
    ica "Do you know who it was that hired me to take out those diplomats? It was Admiral Grey of the Solar Alliance himself."
    kay "Admiral Grey? Funny you say that, considering he sent us here to protect the diplomats."

    show icari plugsuit armscrossed neutral with dissolve

    ica "Get with the program, captain.  Everyone in the Alliance military knows that war is inevitable."
    ica "You can save those diplomats now... And with each passing day, PACT will conquer one planet after another.  Millions more will lose their lives..."
    ica "Until PACT finally runs out of neutral planets to conquer and turns to Alliance space."
    ica "Then there will be an interstellar war of unimaginable proportions, with PACT bringing to bear the resources of every planet of the Neutral Rim against the Alliance."
    ica "Or those diplomats can die now.  Then the Alliance will intervene while PACT is still mustering its strength."
    ica "While a few may have to be sacrificed, you will save the lives of millions."
    ica "Admiral Grey understands this.  That is why he hired me to ensure those diplomats never make it out of Verstra space."

    menu:
        "You're not making any sense. Why would Admiral Grey send us here to save the diplomats, and then hire you to make sure they get captured by PACT?":
            jump nosensesavediplomats
        "You're saying Alliance military's going to coup the civilian government?":
            jump militarycoupgovernment
        "So in the end, what are you after?":
            jump endafterwhat

label nosensesavediplomats:

    ica "Admiral Grey still has to obey the commands of President Alythe. The President has ordered that war with PACT is to be avoided at all costs."
    ica "That's why he used the official channels to send the Sunrider here to protect the diplomats."
    ica "Then on the unofficial channels, he contacted me to ensure that the diplomats are captured."

    menu:
        "You're saying Alliance military's going to coup the civilian government?":
            jump militarycoupgovernment
        "So in the end, what are you after?":
            jump endafterwhat

label militarycoupgovernment:

    ica "Perhaps. Not today, or tomorrow, but if the Solar Congress continues to be mired in politics while PACT swallows up the entire neutral rim, the Alliance military will act to protect its citizens, with or without the support of the civilian leaders."

    menu:
        "You're not making any sense. Why would Admiral Grey send us here to save the diplomats, and then hire you to make sure they get captured by PACT?":
            jump nosensesavediplomats
        "So in the end, what are you after?":
            jump endafterwhat

label endafterwhat:

    show icari plugsuit altneutral smallsnide with dissolve

    ica "Like I said, captain, I just want to see PACT defeated. I think we share that common goal, don't we?"

    show icari plugsuit neutral neutral:
        ease 0.5 zoom 1.8 ypos 1.6

    ica "So, what will it be captain?"
    ica "Will you stand by while PACT conquers one neutral planet after another, growing more powerful with each day; or will you make a stand and stop PACT once and for all?"

    menu:
        "I hate PACT and everything they stand for. That includes killing innocents to accomplish my goals.  Now get back to the brig where you belong.":
            jump hatepactbackbrig
        "All right.  I believe you.  Let's work together.":
            jump rightyouworktogether

label hatepactbackbrig:

    $ captain_moralist += 10

    show icari plugsuit neutral frown:
        ease 0.5 zoom 1.5 ypos 1.4
    with dissolve

    ica "You don't understand, captain. PACT is evil. They don't care about the lives of innocents. We have to act now to stop them, before it's too late!"
    kay "We still have a duty to humanity on board this ship.  I will not command the killing of innocents."

    play music "Music/Battle_Against_Time.ogg"

    show icari plugsuit pistol angry with dissolve

    ica "Tsch... Looks like you've left me no choice then."
    ica "PACT must be stopped no matter what, and I won't let you interfere with my mission."

    scene bg captainsoffice
    show icari plugsuit pistol angry:
        zoom 1.5 xpos 0.5 ypos 1.4
    show ava uniform alt neutral angry:
        xpos 0.8 zoom 1
    with dissolve

    ava "Captain!"

    show icari plugsuit pistol angry:
        ease 0.5 ypos 1.4 xpos -0.5

    ica "!!!"

    show ava uniform neutral angrytalk:
        ease 0.5 xpos 0.5

    ava "Are you alright?"
    kay "Yeah."
    ava "I ran up here as soon as I realized the mercenary escaped.  Looks like I was almost too late."
    kay "That mercenary's becoming a problem. Find her and stop her!"

    jump findherandstopher

label rightyouworktogether:

    $ captain_prince += 1
    $ affection_icari += 3

    show icari plugsuit neutral smile:
        ease 0.5 zoom 1.5 ypos 1.4
    with dissolve

    ica "I'm glad we agree."
    kay "Now, will you please turn the lights in my office back on?"

    show icari plugsuit armscrossed confidentlaugh with dissolve

    ica "Hahahaha.  Of course, captain."

    scene bg captainsoffice
    show icari plugsuit armscrossed confidentlaugh:
        zoom 1.5 xpos 0.5 ypos 1.4
    with dissolve

    kay "I'll need to inform Ava of the change in plans.  You should go back to where you're supposed to be now, and just play along for now."

    show icari plugsuit armscrossed confident with dissolve

    ica "All right, I'm willing to be your prisoner for a bit."

    show icari plugsuit armscrossed embarassedtsun with dissolve

    ica "Oh... And thank you captain."
    ica "For uh... hearing me out."
    kay "???"
    ica "Seriously, you're going to need my help if you couldn't figure it out on your own..."

    jump agreehelpicari

label findherandstopher:

    $ affection_asaga += 2

    scene bg bridge with dissolve

    kay "What's the status on the Phoenix!?"

    show ava uniform alt neutral angry with dissolve

    ava "Damn! She's already hacked into our security system and escaped on her ryder!"

    show ava uniform alt order angry with dissolve

    ava "All pilots, scramble your ryders and pursue!"

    show ava uniform alt neutral angry with dissolve
    show asaga uniform excited surprise:
        xpos 0.2
    with wipeup

    asa "O-oh! Press quick save, Chigara, it's go time!"

    show chigara uniform handsup surprise:
        xpos 0.8
    with wipeup

    chi "E-eh!?"

    show ava uniform fistup angry with dissolve

    ava "What's going on down there!?"

    show asaga uniform armscrossed embarassedgrin with dissolve

    asa "Oh nuthin', was just in the middle of a game, that's all!"

    hide asaga with dissolve
    hide chigara with dissolve

    kay "It was their break time."

    show ava uniform facepalm with dissolve

    ava "Unbelievable..."

    play sound "sound/warning.ogg"

    "-Warning-"

    kay "What now?"

    show ava uniform neutral angrytalk with dissolve

    ava "Uh... Warning! Massive PACT signatures detected!"

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5
    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform neutral angrytalk
    with dissolve

    kay "Red alert!  All hands, assume battle stations!"
    ava "It's the PACT invasion fleet. They arrived here early!"
    kay "Just one thing after another. Asaga, come in."

    show asaga plugsuit excited focushappy:
        xpos 0.2
    with wipeup

    asa "I'm here, capt'n!"
    kay "Change of plans.  Focus on defending the diplomats against the PACT fleet.  Keep your eyes out for the mercenary unit.  I have the feeling she'll be back to interfere with our mission."
    asa "Aye capt'n!"
    kay "Bring us alongside the Agamemnon.  A civilian transport won't last long against that PACT fleet without the Sunrider's cover fire."
    ava "Aye captain.  We are being hailed by the Agamemnon."
    kay "Put her through."
    "Agamemnon" "It looks like the PACT fleet's going to make our escape complicated.  Good to have you by our side, Sunrider."
    kay "Glad to be here.  Stay close and let us do the fighting.  Warp as soon as we leave Versta's gravity well with or without us."
    "Girl" "Is the big ship going to protect us?"
    kay "Uh, Agamemnon, did we just hear that last transmission correctly?"
    "Agamemnon" "I'm sorry, but with the PACT invasion fleet approaching, we couldn't just leave the children behind!"
    kay "(As if this couldn't get any worse! So that's why they were so against escaping with us!)"
    kay "How many?"
    "Agamemnon" "Six hundred children in all.  It was the only way to get them off planet before PACT arrived!"
    kay "This mission just got even more complicated."
    kay "All ryders.  Your orders are to defend the Agamemnon at all costs.  Don't let a single PACT unit hit it."

    show asaga plugsuit handsonhips determined with dissolve

    asa "Understood, captain!  Don't worry, we'll keep those children safe!"

    show chigara plugsuit excited determined:
        xpos 0.8
    with wipeup

    chi "We'll do this with our lives!"
    kay "All ryders, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    $ ep2_cancelwarp = False

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide chigara
    hide battlewarning

    call mission8_inits
    $ BM.mission = 8
    $ check1 = False
    $ check2 = False
    $ check3 = False
    $ check4 = False
    $ check5 = False

    jump battle_start

label agreehelpicari:

    $ affection_ava += 1

    scene bg bridge with dissolve
    show ava uniform armscrossed neutral with dissolve

    ava "Captain.  We're nearly finished with the preparations for our escort mission.  The diplomats are secure on the civilian transport Agamemnon.  I was just about to call you down here, in fact."
    kay "About that.  There's been a change of plans, Ava."
    ava "Oh?"
    kay "The mercenary is right."
    kay "The lives of a few diplomats cannot compare to the billions of innocents who will be killed if PACT is permitted to invade the Neutral Rim unchallenged."

    show ava uniform armscrossed smile with dissolve

    ava "Understood, captain. As is the norm in war, sacrifices must be made for the greater good.  I will relay your new orders to the crew then."
    kay "Thank you, Ava."

    play sound "sound/warning.ogg"

    "-Warning-"

    kay "What happened!?"

    show ava uniform neutral angrytalk with dissolve

    ava "Contact!  Multiple warp signatures detected!  It's PACT!"

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5
    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform neutral angrytalk
    with dissolve

    kay "Red alert! All hands, assume battle stations!"
    ava "It's the PACT invasion fleet.  They arrived here early!"
    kay "Get us out of the planet's gravity well and spool up our warp drive.  Our role here is finished."
    ava "Understood, captain."

    show ava uniform handonhip mad with dissolve

    ava "The PACT fleet has noticed us.  A squadron of ships has broken off to intercept.  Time until in range: Ten minutes."
    ava "We are receiving a message from the Agamemnon.  Should I open the channel?"

    menu:
        "Put me through to them.":
            jump agaputmethrough
        "No, close the channel.":
            jump agaclosechannel

label agaputmethrough:

    ava "Aye captain."
    "Agamemnon" "What are you doing!?  I thought you were supposed to be our escort!"
    kay "Change of plans.  It seems like your leaders no longer wish to see you alive."
    "Agamemnon" "What do you mean...?"
    kay "Your sacrifice is necessary to stop PACT and save the lives of billions."
    "Agamemnon" "What? What is this nonsense you're spurting!?"
    "Agamemnon" "Wait-- you mean to sacrifice us to spark a war...  Of course...!"
    kay "I hope you understand your position."
    "Agamemnon" "No... You cannot possibly do this to us!  Not when we..."
    "Girl" "What's going on?  Why isn't the big ship protecting us?"
    kay "What the-  Agamemnon, did I just hear what I think I did?"
    "Agamemnon" "There are six hundred children on board this ship, Sunrider!"
    "Agamemnon" "With the PACT invasion fleet approaching, taking the Versta children under Alliance protection was the only thing we could do!"
    kay "What!?"

    show ava uniform neutral angrytalk with dissolve

    ava "Captain, we are getting underway.  What are your orders?"
    "Agamemnon" "Without your protection, our act of charity will instead doom the children!"
    "Agamemnon" "Please, help us!"
    kay "(Six hundred children? There was no way to have foreseen this!)"

label cmd_savethechildren:

    if BM.cmd >= 300:
        menu:
            "...Maintain course.  Prepare to break through that PACT squadron.":
                jump maintainpreparethroughpact
            "COMMAND DECISION: Cancel warp.  We're going to escort the Agamemnon out of here! |300 CMD/[BM.cmd] Available|":
                jump cancelwarpagaout

    if BM.cmd < 300:
        menu:
            "...Maintain course.  Prepare to break through that PACT squadron.":
                jump maintainpreparethroughpact
            "COMMAND DECISION: Cancel warp.  We're going to escort the Agamemnon out of here! |INSUFFICIENT CMD POINTS|":
                jump cmd_savethechildren


label maintainpreparethroughpact:

    $ affection_asaga -= 2
    $ captain_prince += 10

    show ava uniform salute angry with dissolve

    ava "Aye captain."
    kay "Asaga, your orders are to focus on the PACT squadron ahead of us and open up a path for the Sunrider to warp.  Ignore the Agamemnon, understand?"

    show asaga plugsuit altneutral surprise:
        xpos 0.2
    with wipeup

    asa "B-but what about-"
    kay "It's necessary to stop PACT.  Do it."

    show asaga plugsuit armscrossed grumpy with dissolve

    asa "I'm not feeling so good about this....."

    show chigara plugsuit excited scared:
        xpos 0.8
    with wipeup

    chi "Asaga, we have to do this or else Vestra won't be the last planet that PACT invades!"

    show asaga uniform armscrossed madshout with dissolve

    asa "A-all right, all right, let's go!"

    hide chigara with dissolve
    show icari plugsuit armscrossed confident:
        xpos 0.8
    with wipeup

    ica "Heh, I think you'll need my help too."

    show asaga uniform handsonhips mad with dissolve

    asa "Eh? What are you doing here?"
    ica "Just a bit of back up, in case things don't go as planned.  With the captain's approval, of course."
    kay "All right, Icari.  Help us break through the PACT fleet and you will have earned our trust."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Looks like I'll be taking another look at our security protocols after this..."
    kay "Icari's no ordinary prisoner, Ava.  I think we can let it slide this time."
    kay "All ryders, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide icari
    hide asaga
    hide battlewarning

    call mission7_inits
    $ BM.mission = 7
    jump battle_start

label cancelwarpagaout:

    $ ep2_cancelwarp = True

    play sound "sound/swordhit.ogg"
    show captainflash:
        xpos 1.1 ypos 0.2
        ease 0.7 xpos 0.35
        pause 0.5
        ease 0.8 alpha 0

    $ BM.cmd -= 300
    $ captain_moralist += 5
    $ affection_asaga += 2

    show ava uniform salute angry with dissolve

    ava "Aye captain.  Changing course.  We will take the Agamemnon under our wing."

    show asaga plugsuit excited focushappy:
        xpos 0.2
    with dissolve

    asa "All right! Let's go and kick some PACT ass! Haha!"

    show chigara plugsuit excited determined:
        xpos 0.8
    with dissolve

    chi "I'm ready, captain!"
    kay "All ryders, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide chigara
    hide battlewarning

    call mission8_inits
    $ BM.mission = 8
    $ check1 = False
    $ check2 = False
    $ check3 = False
    $ check4 = False
    $ check5 = False

    jump battle_start

label agaclosechannel:

    $ captain_prince += 5

    ava "Understood."

    show ava uniform handonhip mad with dissolve

    ava "The Agamemnon has left port, captain.  They are making a run for it out of Versta's gravity well."
    kay "Let them be.  Prepare to break through that PACT squadron and engage warp."
    ava "Aye captain."
    kay "Asaga, your orders are to focus on the PACT squadron ahead of us and open up a path for the Sunrider to warp.  Ignore the Agamemnon, you understand?"

    show asaga plugsuit altneutral surprise:
        xpos 0.2
    with wipeup

    asa "B-but-"
    kay "It's necessary to stop PACT.  Do it."

    show asaga plugsuit excited forcedsmile with dissolve

    asa "O-okay, captain.  C'mon Chigara, let's go out there and beat PACT up!"

    show chigara plugsuit excited scared:
        xpos 0.8
    with wipeup

    chi "I-I'll try my best, captain!"

    hide chigara with dissolve
    show icari plugsuit armscrossed confident:
        xpos 0.8
    with wipeup

    ica "Heh, I think you'll need my help too."

    show asaga uniform handsonhips mad with dissolve

    asa "Eh? What are you doing here?"

    ica "Just a bit of back up, in case things don't go as planned.  With the captain's approval, of course."
    kay "All right, Icari.  Help us break through the PACT fleet and you will have earned our trust."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Looks like I'll be taking another look at our security protocols after this..."
    kay "Icari's no ordinary prisoner, Ava.  I think we can let it slide this time."
    kay "All ryders, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide icari
    hide asaga
    hide battlewarning

    $ check1 = False

    call mission7_inits
    $ BM.mission = 7
    jump battle_start

label mission7:

    if check1 == False:
        $BM.draggable = False

        play sound "sound/objectives.ogg"
        "Note:  The Phoenix can briefly become immune to blindside attacks by going into stealth mode."

        $ check1 = True

        $ BM.draggable = True  #this enables dragging the viewport again.

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission7 #loop back
    else:
        pass #continue down to the next label

label aftermission7:

    $ Saveddiplomats = False

    hide screen commands
    hide screen battle_screen

    play music "Music/Invasion of Chaos.ogg"

    scene bg bridgered with dissolve
    window show

    show ava uniform neutral angrytalk with dissolve

    ava "The PACT squadron has been neutralized!"
    kay "Get us out of the planet's gravity well, double time!"
    ava "Aye captain."

    scene cg_epi2_cgback
    show cg_epi2_phoenix
    with dissolve

    asa "Wait!  I'm reading the Agamemnon on the scanner!"
    ava "It made it past the PACT fleet?"
    chi "No... look!"

    show cg_epi2_shuttleflame:
        xpos 0.5 ypos -0.1
        ease 1.0 xpos 0.0 ypos 0.0

    "Agamemnon" "...-static- requesting assistance... -static-... critical... -static-... the children..."

    show cg_epi2_cgset:
        ease 0.8 xpos -2900 ypos -528 zoom 3
        ease 0.5 alpha 0
    show cg_epi2_cg2:
        alpha 0
        pause 0.5
        ease 0.8 alpha 1.0

    ica "...!!!"

    pause 0.5
    scene cg_epi2_cg3 with dissolve
    pause 1.0
    scene cg_epi2_cg2 with dissolve
    pause 0.8
    scene white with dissolve

    play sound "sound/explosion4.ogg"

    scene cg_epi2_cgback
    show cg_epi2_shuttleflame
    show cg_epi2_explode1:
        alpha 0
        ease 0.8 alpha 1
        ease 0.8 alpha 0
    show cg_epi2_explode2:
        alpha 0
        pause 0.3
        ease 0.8 alpha 1
        ease 0.8 alpha 0
    show cg_epi2_explode3:
        alpha 0
        pause 0.6
        ease 0.8 alpha 1
        ease 0.8 alpha 0
    pause 1.0
    hide cg_epi2_shuttleflame

    pause 1.5
    scene bg bridgered with dissolve
    show ava uniform neutral angrytalk:
        xpos 0.4
    with dissolve

    ava "Contact lost with Agamemnon!"
    kay "... ... ..."

    show icari plugsuit armscrossed sad:
        xpos 0.6
    with wipeup

    ica "I've been looking forward to this for as long as I can remember..."

    show icari plugsuit armscrossed cry with dissolve

    ica "And yet why..."

    show asaga plugsuit excited shout:
        xpos 0.8
    with wipeup

    asa "Tsch.....  PACT...!!!"

    show chigara plugsuit handonchest sadsurprise:
        xpos 0.2
    with wipeup

    chi "How horrible...."
    ava "The Sunrider has cleared the planet's gravity well.  Warp out at your command, captain."
    kay "All ryders, return home."
    kay "We're getting out of here."

    stop music fadeout 1.5
    scene black with dissolvelong
    scene bg captainsoffice with dissolve
    play music "Music/The Tumbrel.ogg" fadeout 1.5

    show ava uniform alt neutral neutral with dissolve

    ava "The results of our investigation are complete, captain."
    ava "It appears that what the mercenary told us was the truth.  While Admiral Grey's Office officially denies any involvement, several inside sources have informed me that the mercenary had been hired by the Admiral."
    ava "Further, by going through previous obituaries, I've confirmed that the mercenary's mother, father, and brother were killed by PACT thirteen years ago."
    kay "I see..."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Are you feeling all right sir?"
    "Shields stood from his chair."
    kay "Yeah."
    "He turned around and picked up the picture frame of his sister."

    show item album:
        xpos 0.2 ypos 0.3
    with dissolve

    kay "So the girl's lost her whole family to PACT, huh."

    hide item with dissolve

    show ava uniform neutral neutral with dissolve

    ava "It would appear so.  What do you intend to do with her?"
    kay "Invite her to stay.  She's a talented pilot.  And she's got an axe to grind against PACT.  We could use someone like her on our side."
    ava "Understood, captain."
    ava "There is one final matter."
    kay "Hm?"
    ava "The Solar Congress convened for an emergency session earlier today."
    ava "While the official vote has not yet taken place, all indications show it will unanimously adopt a resolution condemning PACT aggression in the Neutral Rim and mobilize the Space Force in defense of Alliance space."
    kay "So the Alliance will finally take action."
    ava "The galaxy's mere seconds away from total intergalactic war now."
    kay "Good."
    ava "... ... ..."

    show ava uniform armscrossed looklefttalk with dissolve

    ava "Kayto. Is this really..."
    kay "What?"

    show ava uniform neutral neutral with dissolve

    ava "Nothing sir.  That concludes my report."
    ava "I must attend to other matters now."
    kay "Carry on, Ava."
    hide ava with dissolve

    scene black with dissolve
    scene bg messhallwindows with dissolve
    show icari uniform armscrossed sad:
        zoom 1.5 ypos 1.4 xpos 0.5
    with dissolve

    ica "... ... ..."
    kay "What's the matter.  You got exactly what you wanted, and now you're giving me the long face?"

    show icari uniform armscrossed lookawayannoyed with dissolve

    ica "Tsch.  Sneaking up on me, captain?"
    kay "Don't give me that.  I know you heard me coming from the moment I entered the door."
    ica "Contract killing's an ugly business, captain.  If you think I'm going to be torn up about those kids, then you're wrong."
    kay "I saw your face after you came back."

    show icari uniform armscrossed tsun with dissolve

    ica "I was just... dazed, that's all.  A-also, I keep onions in my cockpit.  W-what, you don't believe me? It's true!"

    show icari uniform armscrossed sad with dissolve

    ica "... ... ..."
    ica "Tsch."
    ica "I saw a girl on that ship. And it just reminded me..."
    ica "When I was twelve, I was just a kid wandering the stars with my parents."
    ica "Damned PACT ships came out of nowhere one day and they boarded our ship, demanding star charts which we knew nothing about."
    ica "I saw their leader shoot my mom between the eyes right in front of me."
    ica "I barely managed to get to the escape pod before they blasted the whole ship. I drifted through space for five days until I was rescued by an Alliance patrol."

    show icari uniform armscrossed depressedblush with dissolve

    ica "In the end... I was the only survivor."

    show icari uniform neutral madblush with dissolve

    ica "They all deserve to die for what they did that day... I've spent my whole life trying to avenge my family.  And I won't stop now."
    kay "... ... ..."
    "Shields walked to the window and gazed out into the stars."
    "Far away, invisible to the naked eye, Cera glimmered among the countless lights."
    "A wave of sadness came upon Shields, suffocating his throat and squeezing the air out of his lungs."
    "Then came the rage - boiling rage which could barely be suppressed."
    kay "No."
    kay "Neither will I."

    window hide
    scene black with dissolve
    scene cg_album:
        ease 5.0 xpos -0.3
    with dissolvelong

    pause 8.0

    jump ep3_start

label mission8:

    if ep2_cancelwarp == True:

        $BM.draggable = False

        show ava uniform altneutral angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ava "Captain, we just had an unauthorized launch from our hangar! It's the mercenary!"
        kay "Disable her ryder!"
        ava "Too late! She's already out of our range."
        kay "All units. Icari has escaped on the Phoenix. Keep your eyes open for her. No doubt she intends to interfere with our mission."

        hide ava onlayer screens with dissolve
        $ ep2_cancelwarp = False
        $ BM.draggable = True

    if check1 == False:

        $BM.draggable = False

        play sound "Sound/objectives.ogg"
        "Objective: Bring the Agamemnon to the far right edge of the map."

        $ check1 = True
        $ BM.draggable = True

    if check2 == False and BM.turn_count == 3:

        play sound "sound/Voice/Ava/Ava Others 6.ogg"
        python:
            create_ship(PactMook(),(13,3),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(13,4),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(14,3),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

            create_ship(PactMook(),(13,7),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactMook(),(13,8),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(14,8),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])

        $ check2 = True

    if check3 == False and BM.turn_count == 5:

        play sound "sound/Voice/Ava/Ava Others 5.ogg"
        python:
            create_ship(MissileFrigate(),(15,5),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(15,8),[PactFrigateMissile()])
            create_ship(PactCruiser(),(14,6),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(14,7),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
        $ check3 = True

    if check4 == False and BM.turn_count == 6:

        $BM.draggable = False

        show icari plugsuit point angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ica "Get outta my way!"

        hide icari onlayer screens with dissolve
        show asaga plugsuit handsonhips angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        asa "Oy!  Don't you see what's happening here!?  If you go through with this, all those children are gonna die!"

        hide asaga onlayer screens with dissolve
        show icari plugsuit neutral angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ica "And if I don't, a million more will die as PACT conquers planet after planet!"

        hide icari onlayer screens with dissolve
        show asaga plugsuit excited angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        asa "You don't even know if letting everyone die now will prevent that!"
        asa "Screw thinking about what might happen tomorrow!  'Cause you've got innocents to protect today, right in front of you!"

        hide asaga onlayer screens with dissolve
        show icari plugsuit handonhip snide onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        ica "Heheh...  You're naïve."
        ica "War cannot be won without sacrifice.  The righteous like you are just blind to reality!"

        hide icari onlayer screens with dissolve
        show asaga plugsuit point angry onlayer screens:
            xzoom -1 xpos 0.2
        with dissolve

        asa "Y-you're crazy!"

        hide asaga onlayer screens with dissolve

        python:
            create_ship(PhoenixEnemy(),(18,6),[PhoenixEnemyMelee(),PhoenixEnemyAssault()])

        $ BM.draggable = True
        $ check4 = True


    if check5 == False and BM.turn_count == 8:

        play sound "sound/Voice/Ava/Ava Others 6.ogg"
        python:
            create_ship(PactCruiser(),(16,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,1),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(16,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(17,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,16),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])

        $ check5 = True

    $BM.battle()  #continue the battle

    if agamemnon.location[0] == 18:
        $ BM.battle_end()

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission8 #loop back
    else:
        pass #continue down to the next label

label aftermission8:

    python:
        BM.ships.remove(agamemnon)
        player_ships.remove(agamemnon)

        phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
        phoenix = create_ship(Phoenix(),(9,5),phoenix_weapons)

    $ Saveddiplomats = True

    hide screen commands
    hide screen battle_screen

    play music "Music/Battle_Against_Time.ogg" fadeout 1.5

    scene space back8
    show blackjack
    with dissolve

    window show

    show asaga plugsuit point angry:
        xzoom -1 xpos 0.2
    with dissolve

    asa "It's over, Icari!  Surrender!"

    scene space back9
    show phoenix:
        xzoom -1
    with dissolve

    show icari plugsuit neutral creepy:
        xpos 0.3
    with dissolve

    ica "... ... ..."

    show icari plugsuit neutral creepygrin with dissolve

    ica "Ufufufu..."

    show icari plugsuit point crazylaugh with dissolve

    ica "HAH!  You think you've won? "
    ica "The only thing you'll accomplish today is allow PACT to win this war!  And I'll never allow that!"
    ica "With these very hands... I'll rid the galaxy of PACT!  For everyone that they've murdered!"
    kay "Icari, stop!"
    ica "Hehehehe... Hahahahaha!!"

    play sound "sound/mechchange.ogg"
    show phoenix assault with dissolve

    ica "I'm... going to avenge everyone!  And there won't be anyone to stop me!"

    scene cg_epi2_cgback
    show cg_epi2_shuttle
    with dissolve

    show cg_epi2_phoenix:
        xpos -0.75 ypos 1.75
        ease 0.8 xpos 0.0 ypos 0.0

    pause 2.0

    stop music fadeout 1.5

    show cg_epi2_cgset2:
        ease 0.8 xpos -2900 ypos -528 zoom 3
        ease 0.5 alpha 0
    show cg_epi2_cg2:
        alpha 0
        pause 0.5
        ease 0.8 alpha 1.0

    ica "... ... ..."

    scene cg_epi2_cg3 with dissolve
    pause 1.0
    scene cg_epi2_cg2 with dissolve

    ica "... ... ..."

    scene cg_epi2_cgset2 with dissolve

    ica "...Tsch..."

    play music "Music/Limitless.ogg"

    scene bg bridgered
    show icari plugsuit neutral mad
    with dissolve
    pause 0.5
    show icari plugsuit neutral mad2 with dissolve
    pause 0.5
    show icari plugsuit neutral sadblush with dissolve
    pause 0.5
    show icari plugsuit neutral sadcry with dissolve

    ica "Why..."
    kay "Because you're not like PACT, Icari.  Don't ever forget that."

    show icari plugsuit armscrossed cryclosedeyes with dissolve

    ica "...Tsch."
    ica "So uncool..."

    show ava uniform neutral talk:
        xpos 0.2
    with dissolve

    ava "Captain, we've escaped Versta's gravity well.  The Agamemnon is warping out."
    kay "Spool up our warp drive.  Get us out of here too."
    kay "All ryders, return home.  That includes you, Icari."

    show icari plugsuit armscrossed crysmile with dissolve

    ica "... ... ..."
    ica "Understood.  Phoenix, returning."

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

    scene bg hangar with dissolve

    show asaga plugsuit vpose:
        xpos 0.4
    with dissolve

    asa "Ah hah!! That's two for two, captain!"
    kay "Good job, Asaga. I admit, I was starting to sweat pretty heavily there."

    show asaga plugsuit armscrossed smile with dissolve

    asa "Eh-heh... Any time!"

    show chigara plugsuit handonchest smile:
        xpos 0.2
    with dissolve

    chi "Ah, I've come back too, captain."
    kay "Good job to you too, Chigara."
    chi "Eh-heh... Thank-you, captain."

    show ava uniform alt neutral mad:
        xpos 0.8
    show icari plugsuit armscrossed concernedlookaway:
        xpos 0.6
    with dissolve

    ava "I've apprehended the mercenary. What should we do with her?"
    ica "... ... ..."
    kay "Well, I guess it's better being one of the good guys after all, huh Icari?"

    show icari plugsuit armscrossed tsun with dissolve

    ica "What? I-it's not like I wanted to help you out or anything! I just felt bad about those kids..."

    show icari plugsuit armscrossed sad with dissolve

    ica "... ... ..."
    ica "But... I guess I was wrong. For just a moment there, I would actually have done it."
    ica "I would have shot at those kids, just to get even with PACT."
    ica "My whole family was killed by PACT when I was just twelve years old."
    ica "We were... just space explorers. But they still came onboard, demanding charts that we knew nothing about."

    show icari plugsuit armscrossed cry with dissolve

    ica "When we couldn't give them what they wanted, their leader shot my mom between the eyes."
    ica "I... barely managed to get to the escape pod before they blasted the ship... I drifted through space for five days until I was rescued by an Alliance patrol."
    ica "In the end... I was the only survivor."
    ica "They all deserve to die for what they did... I've spent my whole life trying to avenge my family.  And I won't stop now."
    kay "You want to avenge your family by murdering a bunch of children?  You won't be any better than PACT if you did that."
    ica "... ... ..."
    ica "I know..."
    kay "I know a better way.  Our hangar bay's awfully empty, and we're looking for skilled pilots."
    kay "You play by our rules, and there might be a space for you onboard this ship."
    kay "We'll defeat PACT the right way, without harming any innocents."
    kay "It'll be a hard mission and we might all die trying, but I'd rather be dead than forget about what we're fighting to protect."

    show icari plugsuit neutral sadcry with dissolve

    ica "You'd still have me on your team? Even after all I've done?"
    kay "Everyone on this ship knows what it feels like to lose family.  Don't think for a second that you're alone."

    show icari plugsuit neutral smilecry with dissolve

    ica "I... never expected such kindness from you, captain. Perhaps... you're right. We can win this war without using the same methods as PACT."
    kay "There is a way to win. PACT won't get away with what they did to Cera, or your family. I'll make sure we all get payback."
    ica "All right... You have a deal. I'll help you defeat PACT... and in exchange, I'll play by your rules."

    show ava uniform armscrossed frowntalk with dissolve

    ava "Don't think this means I won't have my eyes on you, mercenary. You might have won over the captain's sympathy, but the instant you cause any trouble, I'll be throwing you in the brig."

    show asaga plugsuit armscrossed grumpy with dissolve

    asa "Oy Capt'n, you suppose putting this person on our ship is a good idea? She's already tried to slit our throats one too many times..."
    kay "We're all trying to stop PACT, aren't we? Besides, we'll need all the help we can get."

    show asaga plugsuit armscrossed sigh with dissolve

    asa "All right, I guess an extra wing mate isn't so bad... So long as she's aiming at PACT."

    show icari plugsuit neutral talkconcernblush with dissolve

    ica "I swear, I'll win your trust. We'll fight together from now."
    asa "Yeah... but I think I'll lock the doors when I sleep, just in case..."

    show chigara plugsuit handstogether forcedsmile with dissolve

    chi "Ah... W-welcome to the team, Icari... Eh-heh..."
    chi "Let's try to get along well from now, alright? No more fighting..."

    show asaga plugsuit handsonhips happy with dissolve

    asa "Ah well, now that that's over, let's grab some grub! I'm hungry!"

    show ava uniform facepalm with dissolve

    ava "Unbelievable..."

    show asaga plugsuit handsonhips laugh with dissolve

    asa "Haahhahahaha! C'mon capt'n! Come join me and Chigara! We have so much to talk about!"
    kay "Well Ava, looks like you'll be taking a break. And Icari, you too."

    show icari plugsuit armscrossed tsunblush with dissolve

    ica "S-seriously... I guess I have no choice then..."

    hide chigara with dissolve
    hide asaga with dissolve
    hide icari with dissolve
    hide ava with dissolve

    "With that, the team walked upstairs to the star lounge to celebrate their latest victory."
    "While the clouds of war which loomed in the distance were darker than ever, tonight they had something to celebrate."

    window hide
    scene black with dissolve
    scene cg_album:
        ease 5.0 xpos -0.3
    with dissolvelong

    pause 8.0

    jump ep3_start

label ep3_start:

    #try to remove the agamemnon from the game
    python:

        res_location = "lab"
        res_event = "allocatefunds"
        try:
            a,b = agamemnon.location
            BM.grid[a-1][b-1] = False
            BM.ships.remove(agamemnon)
            player_ships.remove(agamemnon)
            del agamemnon  #deletes the last traces. the variable will henceforth not even be defined, as though it was never used.
        except:
            pass
#            show_message('debug: there was an error removing the agamemnon. maybe it already was.')


    $ renpy.pause (0.1)

    window hide

    stop music fadeout 1.5

    show eyecatch_top with eyecatch_wipe
    show eyecatch_bottom with eyecatch_wiperev
    show eyecatch_logo with dissolve
    $ renpy.pause (2.0)
    scene bg black2 with dissolvelong
    scene bg captainsloft with dissolvelong

    window show

    play music "Music/Moonlit_Night.ogg"

    scene cg_avateatime with dissolve

    "Ava relaxed on the sofa as Shields brought a tray of tea to the table."
    kay "I've been meaning to use this tea set. There you go. Fresh out of the box."
    ava "I didn't know you were into tea."
    kay "Heh, I'm not nearly sophisticated enough. It was a little going away gift from family for my commission."
    "Ava raised her tea cup and took a sip. Steam wafted up as she held the cup in her hand."
    ava "It's been awhile since we could talk like this."
    kay "Reminds me of the old times, when we used to play cards in the student council room."
    ava "I'm surprised you even remember. It's been so many years since then."
    kay "I guess seeing you again made me nostalgic. You know, you haven't really changed much since those days."
    ava "Well, things are different now, captain."
    ava "Back then, you were the one following me."

    menu:
        "I guess I just wanted to see you in action.":
            jump guessseeaction

        "Someone had to keep you out of trouble.":
            jump someonekeepouttrouble

label guessseeaction:

    ava "Hm?"
    kay "You were always in motion. Getting things done. I guess I was a bit in awe."
    kay "Maybe I wanted to watch you and learn from the best."
    ava "It's strange, hearing you say that now."

    menu:
        "That was then. Things are different now.":
            jump thenthingsdifferent

        "Do you ever think about what it'd be like if you sat in the captain's seat instead?":
            jump everthinkcaptainsseat

label someonekeepouttrouble:

    ava "Ah, was that what it was?"
    kay "Of course. You were always trying to solve other people's problems. It was only a matter of time until you hurt yourself."
    ava "Heh. Alright, I won't deny that."
    kay "Remember your campaign slogan? Something about being the duty of the student council president to solve the student body's troubles?"
    ava "I guess... Things were simpler back then."
    ava "You're right. I did try too hard. And in the end, I just left disappointed."
    kay "Disappointed? You never told me that."
    ava "I wanted to do more. It was a chance to turn the entire school around. I thought I could really make a difference."
    ava "Heh. But people don't like change. Those that stand out are just naturally made the target of scorn."
    ava "I guess despite everything I did, I was forgotten. Just like all the class presidents before me."

    jump highschooldayslaugh

label thenthingsdifferent:

    ava "Understood. I'm your first officer before anything else, captain."

    jump highschooldayslaugh

label everthinkcaptainsseat:

    ava "... ... ..."
    ava "No."
    ava "I'm your first officer. There's nothing more to it than that."
    ava "I'll execute your orders, captain. That's all there is to it."

    jump highschooldayslaugh

label highschooldayslaugh:

    ava "... ... ..."
    ava "Hahahaha."
    kay "What? What's so funny?"
    ava "Look at me. We're in the middle of a war, and here I am, reminiscing about high school."
    ava "I thought the problems I had back then were insurmountable. And now, here we are, a one ship army against the entire PACT Empire. Kind of makes our high school problems seem like a joke, doesn't it?"
    kay "Hah. Well, we were just kids. I'm sure back then, our problems were as big as the Veniczar himself."

    if Saveddiplomats == True:
        jump tookindstopstopmism

    if Saveddiplomats == False:
        jump solongagoentangled

label tookindstopstopmism:

    ava "You're too kind. Considering our situation, I wonder if it's time for you to drop your optimism and start making the hard calls."
    kay "What do you mean?"
    ava "We're not in high school any more. It's a war out there."
    ava "Compassion may mean death on the battlefield. As captain, you'll have to put all of us in danger. You can't let your personal feelings interfere with what needs to be done."
    kay "As captain, it's my job to keep all of you safe. I wouldn't be able to do that unless I considered my feelings."
    ava "Alright. It's your ship. It's just something to keep in mind, that's all."

    jump guessjustmoveonthose

label solongagoentangled:

    ava "It seems like so long ago. Now, we're entangled in Alliance conspiracies and too busy counting the dead."
    kay "This war's already a piece of hell."
    kay "It's barely even been a month and it's claimed far too many lives."
    ava "Everything you've did was for the greater good."
    ava "None of us wants to see more lives taken by PACT. The crew's behind you in stopping this conflict as quickly as possible."
    kay "Still doesn't make sleeping any easier."

    jump guessjustmoveonthose

label guessjustmoveonthose:

    ava "I guess we'll just have to move on from those days. It's not like we can ever go back now."
    kay "... ... ..."
    kay "PACT will pay for what they've done to our home."
    ava "To tell the truth, I'd rather not think about it. All the people we've lost. All the memories destroyed."
    kay "... ... ..."
    ava "I'm sorry. Pretty much the whole crew's lost someone close to them."

    menu:
        "We'll kill the Veniczar for this. It's the only way justice can be done.":
            jump killveniczaronlyjustice

        "We have to stop PACT, so that what happened on Cera will never happen again.":
            jump stoppactwhathappenednever

label killveniczaronlyjustice:

    $ captain_prince += 1
    ava "Understood, sir. I'll be right behind you every step of the way."

    menu:

        "Give me your thoughts on the crew.":
            jump givemethoughtscrew
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label stoppactwhathappenednever:

    $ captain_moralist += 1
    ava "Understood, sir. I'll be right behind you every step of the way."

    menu:

        "Give me your thoughts on the crew.":
            jump givemethoughtscrew
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label givemethoughtscrew:

    ava "A motley bunch, I'll give you that."
    ava "Asaga's been stirring up every sort of trouble you could imagine. I caught her gambling with the crew just the other day."

    menu:
        "Oh come on, what's wrong with a little game of cards now and then?":
            jump whatswronggamecard

        "I presume you've dealt with her?":
            jump presumedealther

label whatswronggamecard:

    $ supportedasagacards = True

    ava "Captain, military protocol mandates that gambling be strictly-"
    kay "Try to loosen up a bit, Ava. Our pilots need to blow off some steam now and then."
    ava "Well, if that's your order."
    kay "No, Ava… You know that military protocol doesn't mean much now that Cera's a PACT colony."
    kay "I didn't think the protocols for the situation we're in now even exist."
    ava "That is unfortunate. However, someone must enforce discipline on this ship."
    kay "All right… Just don't push yourself too hard, alright? Relax every now and then."
    ava "Understood, captain."
    kay "(She still totally doesn't get what I mean…)"

    menu:
        "How's Chigara been doing?":
            jump howschigarabeendoing
        "How's our mercenary been adjusting?":
            jump howmercenaryadjust
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label howschigarabeendoing:

    ava "Things have been going much better with her. I must say I'm impressed. She's really turned engineering around. You should go check out her research lab."
    kay "Sounds good."

    menu:
        "How's our mercenary been adjusting?":
            jump howmercenaryadjust
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label howmercenaryadjust:

    ava "Better than I thought she would. She's been helping us fix the bugs in our security systems. Maybe I was wrong about her."
    kay "Good to hear."

    menu:
        "How's Chigara been doing?":
            jump howschigarabeendoing
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label presumedealther:

    ava "Right. I've restricted her to eating rations for the next week."

    menu:
        "How's Chigara been doing?":
            jump howschigarabeendoing
        "How's our mercenary been adjusting?":
            jump howmercenaryadjust
        "Thanks for the chat. I should get back to work.":
            jump thankschatback

label thankschatback:

    ava "As should I."
    kay "We should have these talks more often. I could put my tea set to use."

    play music "Music/Mission_Briefing.ogg" fadeout 1.5

    $ captaindeck = 0
    $ asa_location = "messhall"
    $ asa_event = "ep3_asatalk"

    $ chi_location = "engineering"
    $ chi_event = "ep3_chitalk"

    $ ica_location = "hangar"
    $ ica_event = "ep3_icatalk"

    $ pro_location = "bridge"
    $ pro_event = "missionfromryuvians"

    $ res_location = "lab"
    $ res_event = "allocatefunds"

    $ gal_location = None
    jump dispatch

label ep3_asatalk:

    hide screen ship_map
    scene bg messhall
    show asaga uniform neutral happy
    with dissolve

    window show

    asa "Oh, did you need me for something, capt'n?"

    menu:
        "What are your thoughts about what happened with Icari?":
            jump thoughtshappenedicari

        "How are you adjusting to the Sunrider?":
            jump howasaadjustsunrider

        "Actually, nevermind.":
            jump gostaytroubleasaga

label howasaadjustsunrider:

    show asaga uniform armscrossed talk with dissolve

    asa "Eh, I think it's going pretty well. Warm food and a bed to sleep on, anyways. The Sunrider's also much cleaner than Chigara's workshop."

    show asaga uniform armscrossed sad with dissolve

    asa "Uuu... I really wish the first officer would stop chewing me out though..."
    kay "What happened?"
    asa "Well, first I tried to hook up my Game Master to the holovision in the lounge. Ugh, you won't imagine how red her face was when she told me off for that. Something about contaminating the ship's electronics."
    asa "And then, I tried playing some Duel Creatures with Chigara in the crew quarters. And then she comes marching in, saying no card games. Bleh..."

    if supportedasagacards:
        jump alreadyspokeavano
    else:
        jump weremilitarynow

label alreadyspokeavano:

    $ affection_asaga += 1

    kay "I've already spoken to Ava about it. She won't be giving you any more trouble."

    show asaga uniform excited grin with dissolve

    asa "Really? Ahaha, you're the best, capt'n!"
    kay "Just try to keep it in moderation, alright?"

    show asaga uniform neutral smile with dissolve

    asa "Understood..."

    menu:
        "What are your thoughts about what happened with Icari?":
            jump thoughtshappenedicari

        "I should go. Try to stay out of trouble, Asaga.":
            jump gostaytroubleasaga

label weremilitarynow:

    kay "You're on a military vessel now. I like to run a tight ship."
    asa "Understood..."

    menu:
        "What are your thoughts about what happened with Icari?":
            jump thoughtshappenedicari

        "I should go. Try to stay out of trouble, Asaga.":
            jump gostaytroubleasaga

label thoughtshappenedicari:

    if Saveddiplomats == False:

        show asaga uniform armscrossed sad with dissolve

        asa "I've been thinking about what happened, and I just don't feel good about it."
        asa "It's good that the Alliance is finally stepping up and getting ready to help us. But I can't believe we had to do something so horrible to get their help."

        show asaga uniform armscrossed mad with dissolve

        asa "I fly the Black Jack to protect innocents, captain. Letting those children die was wrong."

        menu:
            "I can't say it's been easy sleeping. But their deaths will not be in vain.":
                jump sleepingdeathsnotvain

            "This is war, Asaga.  War cannot be won without sacrifice.":
                jump warasagasacrifice

    if Saveddiplomats == True:

        show asaga uniform altneutral talk with dissolve

        asa "I'm glad we managed to save those kids, but I'm not so sure about keeping the mercenary."

        show asaga uniform armscrossed frown with dissolve

        asa "Eh... I'm not so sure about having a person like that on our team. Nobody should shoot at civilians."

        menu:
            "Icari had her reasons. It's not always so black and white, Asaga.":
                jump herreasonsblackasaga
            "I'm still keeping my eyes on her. If she causes any more trouble, I'll drop her off on the nearest rock.":
                jump stilleyesdroprock


label sleepingdeathsnotvain:

    show asaga uniform armscrossed frown with dissolve

    asa "I guess..."
    asa "I just hope something like that doesn't ever happen again."
    asa "Sigh..."

    jump supposedtohelp

label warasagasacrifice:

    show asaga uniform handsonhips shoutmad with dissolve

    asa "Don't think I don't know that already!"

    show asaga uniform neutral lookawayfrown with dissolve

    asa "W-well, I don't... But..."

    show asaga uniform armscrossed shoutclosedeyes with dissolve

    asa "Argh, nevermind..."

    jump supposedtohelp

label herreasonsblackasaga:

    show asaga uniform armscrossed frown with dissolve

    asa "Whatever her reasons were, shooting at kids is just too far."
    asa "You can't do something like that and still say you're one of the good guys. Anyone willing to stoop down to that level's no better than PACT!"

    jump guessnotstillsame

label stilleyesdroprock:

    show asaga uniform armscrossed confident with dissolve

    asa "Hmph. I'll tell you right away if I catch her stirrin' up trouble, capt'n!"

    jump guessnotstillsame

label supposedtohelp:

    show asaga uniform altneutral sad with dissolve

    asa "I was supposed to help those kids. That's why I decided to become a freelancer. To stand up for people who were being oppressed by PACT."
    asa "It's just... Disappointing. I've let those kids down."

    show asaga uniform neutral lookawayfrown with dissolve

    asa "And well, I guess they're not really around to give me a second chance, are they?"

    menu:
        "How are you adjusting to the Sunrider?":
            jump howasaadjustsunrider

        "I should go. Try to stay out of trouble, Asaga.":
            jump gostaytroubleasaga

label guessnotstillsame:

    show asaga uniform armscrossed talk with dissolve

    asa "Anyways, I guess it's not all bad since she is a good pilot and all. But still, just because we're on the same team doesn't mean we have to be friends."
    asa "By the way capt'n, did you find out what happened to those kids?"
    kay "They've been placed in Alliance protection. Versta's been annexed by PACT, so it's the best place for the kids right now."
    kay "With all the political attention the rescue's caused, you can bet they'll be well taken care of by the Alliance."

    show asaga uniform excited grin with dissolve

    asa "I guess it's for the best. Let's hurry up and kick PACT out of the Neutral Rim so that we can get those kids back to their parents!"
    kay "One step at a time, Asaga..."

    menu:
        "How are you adjusting to the Sunrider?":
            jump howasaadjustsunrider

        "I should go. Try to stay out of trouble, Asaga.":
            jump gostaytroubleasaga

label gostaytroubleasaga:

    show asaga uniform neutral happy with dissolve

    asa "Understood, capt'n!"

    jump dispatch

label ep3_chitalk:

    hide screen ship_map
    scene bg engineering
    show chigara uniform handsup surprise
    with dissolve

    window show

    chi "E-eah! Oh, sorry captain, I didn't see you coming there!"

    show chigara uniform handonchest forcedsmileblush with dissolve

    chi "Ehheh... T-that must be the third time that's happened..."
    kay "Sorry. You really get focused in your work, huh?"
    chi "Whenever I'm working on something, I tend to lose awareness of everything else..."

    show chigara uniform handstogether smile with dissolve

    chi "Was there something you needed, captain?"

    menu:
        "How are you adjusting to the Sunrider?":
            jump howchiajustsunrider
        "What do you think about what happened with the mercenary?":
            jump whatchimercenary
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater

label howchiajustsunrider:

    show chigara uniform handonchest smile with dissolve

    chi "The Sunrider's a wonderful vessel. In fact, I don't think I've ever been on a ship as advanced in my life."
    chi "In fact, I was just running some energy conversion models the other day and I can say that the Sunrider's core drive is one of the most efficient in the galaxy."
    chi "Since the Sunrider's powered through atomic fusion, we don't have to worry about radiation management. Now, I think if I were to upgrade the fuel feeder with..."

    show chigara uniform palmsup embarrasssurprise with dissolve

    chi "O-oh! I'm sorry, I didn't mean to bore you with techno babble... Er, I mean, y-you must be busy, so, erm... Uhh... What were we talking about again? "
    chi "C-can you please repeat your question?"

    menu:
        "Calm down, Chigara. I was just asking how you were doing.":
            jump calmchigaraaskingdoing

        "Actually, I was thinking of upgrading the fuel feeder with the new paraxium coating too.":
            jump actuallyparaxiumcoating

label calmchigaraaskingdoing:

    show chigara uniform handonchest smileblush with dissolve

    chi "O-oh! Everything's good actually!"

    show chigara uniform handstogether smile with dissolve

    chi "The first officer's helped me move in all of my things. I even managed to improve the research lab here in engineering too."
    kay "I'm glad to hear that."

    menu:
        "What do you think about what happened with the mercenary?":
            jump whatchimercenary
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater

label actuallyparaxiumcoating:

    show chigara uniform handonchest ooscienceblush with dissolve

    chi "Eh? You mean you knew about the mark II?"
    kay "That just came out a week ago, didn't it?"

    show chigara uniform handstogether smileblush with dissolve

    chi "Ooohh... I didn't know captain was a gearhead too."
    kay "They wouldn't give me the keys to this ship without me knowing something about it."
    chi "I guess that's true. Ehehe..."

    menu:
        "What do you think about what happened with the mercenary?":
            jump whatchimercenary
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater

label whatchimercenary:

    if Saveddiplomats == True:

        show chigara uniform neutral neutral with dissolve

        chi "Mm... So long as Icari's going to be working with us, I guess I don't see a big problem."
        chi "I haven't really spoken with her much since, but I think she regrets what she did."

        show chigara uniform handstogether smile with dissolve

        chi "I hope we can work together to stop PACT..."

    menu:
        "How are you adjusting to the Sunrider?":
            jump howchiajustsunrider
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater

    if Saveddiplomats == False:

        show chigara uniform handsonchest sad with dissolve

        chi "It was terrible seeing all those kids die..."
        chi "I..."
        chi "It's not the first time I've seen something like that happen. But you never get used to it."
        chi "I guess it's unavoidable that innocents die in war."
        ica "That's why I like machines. You can fix them back up even after they break."

    menu:
        "How are you adjusting to the Sunrider?":
            jump howchiajustsunrider
        "Keep up the good work, Chigara. I'll talk to you later.":
            jump keepgoodchilater


label keepgoodchilater:

    show chigara uniform altneutral neutral with dissolve

    chi "Good bye captain."

    jump dispatch

label ep3_icatalk:

    hide screen ship_map
    scene bg hangar
    show icari uniform handonhip neutral
    with dissolve

    window show

    ica "Captain."

    if Saveddiplomats == True:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "I noticed you liked swords.":
                jump noticedlikedswords

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "Your ryder was smashed up pretty badly last time. Is it operable?":
                jump rydersmashedlastoper

    if Saveddiplomats == False:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "I noticed you liked swords.":
                jump noticedlikedswords

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

label whatdomercenaryica:

    ica "Don't think I was just some goon for hire. I only took out PACT targets."
    ica "Blew up a couple refueling stations here and there. Sank some crippled cruisers. Even impersonated a low level PACT veniczar once."
    kay "I can't really imagine you as a veniczar."

    show icari uniform bothhandsonhips grin with dissolve

    ica "I had to put on a special latex suit to make myself look 80 pounds fatter. Haha."
    kay "Uh, wow. So what exactly were you doing?"

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "It was a slave sale bust. The Alliance hired me to bust a transaction between a pirate cell and this PACT veniczar."
    ica "PACT's been... Ah, liberating slaves by paying off their slavers. In exchange for serving as personnel on their ships, of course."
    ica "This was going to be one of the biggest sales ever. Nearly 200 adults. The Alliance got involved when PACT accidentally included a citizen in the group."
    ica "I guess they forgot to check their passports or something."
    kay "So you just impersonated the veniczar to pay the pirates off and free the slaves after?"

    show icari uniform handonhip neutral with dissolve

    ica "Tsch. If only if it were simple. You see, the cheapskates at the Alliance were only willing to pay to free their own citizen. Something about not wanting to fund piracy."
    ica "Anyways, that was all irrelevant, since it was a double cross and the pirates were planning to slit the veniczar's throat after they got the money anyways."
    ica "Got grazed by a couple of their shots, which melted through my latex suit. That was a sight to see."
    kay "I bet... So how did you get out of that alive?"

    show icari uniform altneutral smile with dissolve

    ica "I swapped places with the real veniczar just as she arrived. Haha, you should have seen the look on her face as the pirates grabbed her."
    ica "Meanwhile, all the slaves got loose. It was total pandemonium in there."
    ica "Finally, the pirates opened fire on the PACT star liner, spacing everyone on board."

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "I don't know what happened to the slaves. I managed to get the Alliance citizen out of there though, and in the end, that's all that mattered to my clients."

    menu:
        "That's pretty crazy. I can't believe you made it out of that in one piece.":
            jump crazybelieveonepiece
        "So you couldn’t save the slaves in the end?":
            jump couldntsaveend

label crazybelieveonepiece:

    show icari uniform bothhandsonhips grin with dissolve

    ica "Hahaha, and that's what I loved about mercenary work. It's my life or theirs. No time to stop and contemplate on philosophical questions."

    jump prettymuchmerclike

label couldntsaveend:

    ica "No. But I still took down a veniczar and a PACT star liner, so I'd call it a good day. "

    jump prettymuchmerclike

label prettymuchmerclike:

    show icari uniform handonhip neutral with dissolve

    ica "Anyways, that's pretty much what being a mercenary was like. It was risky work, but I liked the excitement. It kept my mind off other things."

    if Saveddiplomats == True:
        menu:
            "I noticed you liked swords.":
                jump noticedlikedswords

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "Your ryder was smashed up pretty badly last time. Is it operable?":
                jump rydersmashedlastoper

            "I need to get going.":
                jump dispatch

    if Saveddiplomats == False:
        menu:
            "I noticed you liked swords.":
                jump noticedlikedswords

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "I need to get going.":
                jump dispatch

label noticedlikedswords:

    show icari uniform handonhip neutral with dissolve

    ica "In the ancient times, they said the invention of gunpowder ended the age of swordsplay. Well, the creation of personal shielding's brought it back."
    ica "Now that people can emit shields that can deflect small arms, the only way to take them down in to draw your sword and get up close and personal with them."
    kay "Have you ever killed someone with your sword in person?"
    ica "Couple of PACT soldiers and pirates. When they pop up personal shielding, it's the best way to take them down."

    menu:
        "Sounds barbaric to me.":
            jump soundsbarbaric
        "Sounds like a good strategy. I'll keep it in mind.":
            jump soundsgoodkeepmind

label soundsbarbaric:

    show icari uniform handonhip snide with dissolve

    ica "Heh. Real world's different from officer school, captain. A lot less clean."
    jump stillmostfaces

label soundsgoodkeepmind:
    ica "It gets the job done, that's for sure."
    jump stillmostfaces

label stillmostfaces:

    show icari uniform handonhip neutral with dissolve

    ica "I can still remember most of their faces. It definitely makes you think about what you're doing more than pressing a button and firing a rocket at an enemy space ship."
    ica "They were armed enemies though. It was either their lives or mine."
    kay "Right."

    if Saveddiplomats == True:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "Your ryder was smashed up pretty badly last time. Is it operable?":
                jump rydersmashedlastoper

            "I need to get going.":
                jump dispatch

    if Saveddiplomats == False:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "How are you adjusting to the Sunrider?":
                jump howicaadjustsunrider

            "I need to get going.":
                jump dispatch


label howicaadjustsunrider:

    ica "I'm satisfied with my current accommodations. It's much better than what I'm used to. Thanks for your concern."

    if Saveddiplomats == True:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "I noticed you liked swords.":
                jump noticedlikedswords

            "Your ryder was smashed up pretty badly last time. Is it operable?":
                jump rydersmashedlastoper

            "I need to get going.":
                jump dispatch

    if Saveddiplomats == False:
        menu:
            "So what exactly did you do as a mercenary, Icari?":
                jump whatdomercenaryica

            "I noticed you liked swords.":
                jump noticedlikedswords

            "I need to get going.":
                jump dispatch


label rydersmashedlastoper:

    show icari uniform armscrossed lookawayannoyed with dissolve

    ica "Not without a bunch of repairs. Your pilot was pretty thorough about taking it down."
    kay "You're lucky you didn't get spaced. Asaga may look silly, but she's pretty dangerous with a ryder."

    show icari uniform armscrossed smilesidesmile with dissolve

    ica "Heh. That so? I wouldn't mind having a rematch. On the simulator, of course, captain."

    show icari uniform handonhip neutral with dissolve

    ica "Thankfully, your girl in engineering managed to fix most of the damage. She's really something. I've never seen someone as talented as her."
    kay "Chigara's one of the best minds in the galaxy. We're lucky to have her on our team."

    show icari uniform altneutral smile with dissolve

    ica "Good thing we're on the same side now. You've got a pretty good crew here."

    show icari uniform armscrossed sad with dissolve

    ica "... ... ..."

    show icari uniform armscrossed tsun with dissolve

    ica "Tsch. I can't believe I said that out loud."

    show icari uniform point embarassed tsun with dissolve

    ica "W-what!? Talk about something else before I embarrass myself even more!"

    menu:
        "So what exactly did you do as a mercenary, Icari?":
            jump whatdomercenaryica

        "I noticed you liked swords.":
            jump noticedlikedswords

        "How are you adjusting to the Sunrider?":
            jump howicaadjustsunrider

        "I need to get going.":
            jump dispatch

label missionfromryuvians:

    hide screen ship_map
    scene bg bridge
    show ava uniform neutral neutral
    with dissolve

    ava "Captain, I've just received a message from the neutral world of Ryuvia."
    kay "Ryuvia? You mean we've been contacted by royalty?"
    ava "Correct. Ryuvia's one of the oldest nations in the galaxy, with a history going back for over 10 000 years. In fact, some historians say that Ryuvia might even have been the birth place of humanity."
    kay "Let's hear what they've got to say. Put them on screen."

    show ava uniform neutral neutral:
        zoom 1.0
        ease 0.5 xpos 0.3
    pause 0.01
    show king:
        xpos 0.7
    with wipeup

    ryu "Hail Sunrider. I am King Brandr di Ryuvia."
    kay "Greetings, your highness. I'm Captain Kayto Shields of the starship Sunrider. This is my First Officer, Ava Crescentia."
    ryu "I have heard of your deeds in the Neutral Rim, and believe you may be of help."
    ryu "There is a treasure known to our people which we seek to retrieve from the Nomodorn Corridor. Perform well, and we shall bestow you with great riches."
    kay "What are you looking for?"
    ryu "The crown jewel of Ryuvia."
    kay "The crown jewel? I presume it's of value?"
    ryu "The kingdom of Ryuvia holds many secrets, captain. You have our request. I shall be waiting."

    hide king with wipedown

    kay "Uh, that's it? Not much to go off of, is it?"

    show ava uniform armscrossed neutral:
        ease 0.5 xpos 0.5

    ava "Well, maybe this might shed some light on the matter."
    kay "What?"
    ava "The rumor on the streets of Ryuvia is that the princess has been missing."
    kay "The princess? And what's the crown jewel have to do with that?"
    ava "I've been doing some research on Ryuvian treasures, and I came across this book."
    kay "The Lost Technology Catalogue?"
    ava "It's an encyclopedia of various Ryuvian treasures that have gone missing throughout history."
    ava "According to this book, the crown jewel isn't a carved gem, but rather a highly advanced crystalline device which can pin point the location of royal blood across astronomical distances."
    kay "Ah... And let me guess, the Ryuvians want this crown jewel to help find their princess?"

    show ava uniform handonhip neutral with dissolve

    ava "Bingo. At least, that's the best explanation I can think of."

    menu:
        "Debrief me on King Brandr and the Ryuvians.":
            jump debriefkingryuvians

        "Why would the Ryuvians invent such a crazy device in the first place?":
            jump whyryuvianscrazyplace

        "Tell me more about Lost Technology.":
            jump morelosttech

        "Well, since we could use the money, we might as well help the Ryuvians get their crown jewel back.":
            jump moneyhelpcrownback

label debriefkingryuvians:

    show ava uniform handonhip neutral with dissolve

    ava "A long time ago, the Ryuvian Empire stretched across the galaxy, its vast military powered by technologies which have become long forgotten."
    ava "It was a vast and mighty empire, where culture and the sciences flourished."
    ava "But their glory days could not last forever. Legend speaks of a vast calamity that shook the core of the Ryuvian Empire and caused its ultimate collapse."
    ava "The formation of the Solar Alliance further degraded Ryuvia's power, and today, all that is left of its former glory is the sole planet of Ryuvia. "
    ava "You can still find pieces of their former empire scattered throughout the galaxy though. Many archeologists and space explorers seek to find Ryuvian treasures, which may hold the secret to unlocking the power of their lost technology."

    menu:
        "Why would the Ryuvians invent such a crazy device in the first place?":
            jump whyryuvianscrazyplace

        "Tell me more about Lost Technology.":
            jump morelosttech

        "Well, since we could use the money, we might as well help the Ryuvians get their crown jewel back.":
            jump moneyhelpcrownback

label whyryuvianscrazyplace:

    show ava uniform alt neutral neutral with dissolve

    ava "Dynastic succession. During ancient times, whoever succeeded the Ryuvian throne essentially ruled the galaxy. Needless to say, there were many imposters who claimed the throne."
    ava "The crown jewel of Ryuvia was made with the utmost precision to detect royal blood. You could even say the fate of the galaxy depended upon its accuracy."
    ava "Much of what we've dug up of the ancient Ryuvian's technology escapes comprehension though. Some of the details of the device may never be understood."

    menu:
        "Debrief me on King Brandr and the Ryuvians.":
            jump debriefkingryuvians

        "Tell me more about Lost Technology.":
            jump morelosttech

        "Well, since we could use the money, we might as well help the Ryuvians get their crown jewel back.":
            jump moneyhelpcrownback

label morelosttech:

    show ava uniform neutral neutral with dissolve

    ava "It's ancient technology left behind by the former Ryuvian Empire."
    ava "A long time ago, even before the formation of the Solar Alliance, the Ryuvian Empire conquered the entire galaxy using technology we could not even conceive of."
    ava "When their empire collapsed, much of their technology was lost in the ensuing chaos."
    ava "You could say that humanity's scientific knowledge peaked at the height of the Ryuvian Empire, and with its collapse, entered into a dark age."
    ava "We've been trying to catch up to the Ryuvian's level of sophistication ever since, but it'll still take decades until we have anything as good as the ancient Ryuvians."
    ava "We call the pieces of technology left by the ancient Ryuvians Lost Technology. Whenever one is found, it can dramatically change the power balance of the galaxy."

    menu:
        "Debrief me on King Brandr and the Ryuvians.":
            jump debriefkingryuvians

        "Why would the Ryuvians invent such a crazy device in the first place?":
            jump whyryuvianscrazyplace

        "Well, since we could use the money, we might as well help the Ryuvians get their crown jewel back.":
            jump moneyhelpcrownback

label moneyhelpcrownback:

    show ava uniform neutral neutral with dissolve

    ava "Understood captain. I've punched in the coordinates for the Nomodorn Corridor. Just set our course on the star map and we'll be underway."

    $ warpto_nomodorn = True
    $ amissionforalliance = False
    $ missionforryuvia = True

    $ captaindeck = 1
    $ gal_location = "bridge"
    $ pro_location = None

    jump dispatch

label jumptonomodorn:

    $ warpto_nomodorn = False

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

    scene map_nomodorn:
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

    scene bg bridge
    show ava uniform alt neutral neutral
    with fade

    window show

    ava "Warp successful, captain. We are arriving at the Nomodorn Corridor."
    kay "This is going to be like trying to find a needle in a haystack. Any ideas where we should start looking?"
    ava "The nearest planet in this sector is the neutral world of Tautenia.  It's what we call a dark planet, or a world where technology has fallen to pre-warp era levels. We're talking civil unrest, violence, and warfare on the surface."
    ava "Nothing we need to worry about though. The Tautenian space force is... Kind of a joke."
    kay "Right. Keep our pilots on alert though. I want to be prepared for anything."
    ava "Aye sir."

    play music "Music/Driving_the_Top_Down.ogg" fadeout 1.5

    show ava uniform fistup angryshout with dissolve

    ava "Scratch that. Pirate signatures detected!"

    play sound "sound/redalert.ogg"
    scene bg bridgered
    show ava uniform fistup angryshout
    with dissolve

    kay "Red alert! Raise shields and power weapons! Ready all ryders for combat!"

    show asaga plugsuit excited happy:
        xpos 0.2
    with wipeup

    asa "We're all ready down here, capt'n!"

    show ava uniform alt neutral mad with dissolve

    ava "Wait a minute... I'm reading a distress beacon from another ship."
    kay "A Tautenian ship?"
    ava "No, it's Alliance. Civilian signature, designation \"Mochi.\" Possibly a transport vessel being targeted by the pirates."
    kay "Looks like this just turned into a rescue mission. Patch me through to our pilots."
    ava "Done."
    kay "Asaga, looks like it'll be a rescue mission this time. The pirates are targeting a civilian transport."

    show asaga plugsuit handsonhips happy with dissolve

    asa "Understood capt'n! We'll keep those civilians safe!"
    ava "The Sunrider will be vulnerable without our ryders. What are your orders, captain?"

    menu:
        "That's a risk that we'll have to take. I want all our ryders to go forward and save the civilian.":
            jump riskallforwardsave
        "The safety of the Sunrider comes first. Our ryders will stay back and escort the Sunrider.":
            jump safetyfirstwillescort

label riskallforwardsave:

    $ protectmochi = True
    $ captain_moralist += 2

    ava "Understood captain."

    jump oldfriendcosettetail

label safetyfirstwillescort:

    $ protectmochi = False
    $ captain_prince += 2

    ava "Understood captain."

    jump oldfriendcosettetail

label oldfriendcosettetail:

    kay "Our old friend Cosette Cosmos might be out there. Watch your tail, everyone."
    kay "All right! All units, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide asaga
    hide battlewarning

    $ check1 = False
    $ check2 = False

    call mission9_inits
    $ BM.mission = 9
    jump battle_start

label mission9:

    if check1 == False:
        $BM.draggable = False

        show cosette plugsuit armscrossed happy onlayer screens:
            xpos 0.8
        with dissolve

        cos "Heh-heh, I didn't fancy seeing you again, captain..."
        kay "Ah, my favorite space pirate. I see you've still been skimping on the milk."

        play sound "sound/hit.ogg"

        show cosette plugsuit neutralalt yandereshock onlayer screens:
            ease 0.02 xpos 0.8
            ease 0.02 xpos 0.79
            ease 0.04 xpos 0.81
            ease 0.02 xpos 0.8
            repeat 5
        with dissolve

        cos "G-gurk..."
        cos "Y-you've interfered with my plans for the last time..."

        show cosette plugsuit point yanderegrin onlayer screens with dissolve

        cos "Kill him!"

        hide cosette onlayer screens with dissolve

        play sound "sound/objectives.ogg"
        "Objective: Protect the civilian transport."

        if Saveddiplomats == True:
            "Tip:  The Phoenix can briefly become immune to blindside attacks by going into stealth mode."

        $ check1 = True

        $ BM.draggable = True  #this enables dragging the viewport again.

    if check2 == False and BM.turn_count == 3:

        $BM.draggable = False

        python:
            create_ship(PactMook(),(8,2),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(9,2),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactMook(),(8,15),[PACTMookLaser(),PACTMookMissile(),PACTMookAssault()])
            create_ship(PactBomber(),(9,15),[PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()])
            create_ship(PactCruiser(),(18,8),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(PactCruiser(),(18,6),[PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()])
            create_ship(MissileFrigate(),(5,2),[PactFrigateMissile()])
            create_ship(MissileFrigate(),(5,15),[PactFrigateMissile()])

        show cosette plugsuit point evilsmile onlayer screens:
            xpos 0.8
        with dissolve

        cos "Hahahaha! You won't win this time! We even brought in our friends from PACT!"
        kay "Working for the big bad now, huh? They say birds of the same feather flock together."

        hide cosette onlayer screens with dissolve

        show cullen onlayer screens:
            xpos 0.8
        with dissolve

        cul "Bwah-HAH-HAH! What do we have here? An uppity little rascal?"
        kay "That's Captain Kayto Shields of the starship Sunrider."
        cul "Bah! No matter! You are no match for I, the glorious Veniczar B. Cullen! I will rid the Neutral Rim of vermin like you and unify these poverty stricken worlds into our new galactic order!"
        kay "And where does orbital bombing millions of innocents fit into this unity of yours?"
        cul "Pah! The likes of you will never understand the necessities of war! Now en garde, captain! Allow me to show you the true power of PACT!"

        hide cullen onlayer screens with dissolve

        kay "(Looks like Veniczar Porkchops means business. We're heavily outnumbered here... Should we fall back?)"

        show cg_mochi 1 onlayer screens with dissolve

        ava "Captain, I'm reading weird readings coming from that civilian vessel."
        kay "Weird?"

        play sound "sound/mechchange.ogg"
        show cg_mochi 2 onlayer screens with dissolve

        ava "A sudden spike in power usage... Something inside it is coming online..."
        ava "Wait, this is-"

        show claude plugsuit fingeronlip kittysmile onlayer screens:
            xpos 0.8
        with dissolve

        cla "I guess it's time to get moving, huh...?"

        hide claude onlayer screens with dissolve

        show cg_mochi_bianca onlayer screens:
            xpos 0.5 ypos 0.3 zoom 0.2
            ease 1.0 xpos 0.0 ypos 0.0 zoom 1.0

        play sound1 "sound/Laser 1.ogg"
        show cg_mochi 4 onlayer screens with dissolve

        pause 0.1

        hide cg_mochi_bianca onlayer screens
        show cg_mochi 5 onlayer screens:
            ease 0.02 xpos 0.5
            ease 0.02 xpos 0.495
            ease 0.04 xpos 0.505
            repeat 12
        with dissolve
        play sound2 "sound/explosion2.ogg"

        pause 2.0

        hide cg_mochi onlayer screens

        show ava uniform alt neutral angry onlayer screens:
            xpos 0.8
        with dissolve

        python:
            BM.grid[13][6] = False
            try:
                BM.ships.remove(mochi)
                player_ships.remove(mochi)
            except:
                pass

        ava "Captain, a ryder! Hidden inside the storage compartment in the Alliance vessel!"

        python:

            bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp()]
            bianca = create_ship(Bianca(),(14,7),bianca_weapons)

        kay "Patch me through to her."
        kay "This is Captain Kayto Shields of the starship Sunrider, to the unidentified Alliance ryder. State your intentions."

        hide ava onlayer screens with dissolve
        show claude plugsuit altneutral neutral onlayer screens:
            xpos 0.8
        with dissolve

        cla "This is Claude Trillo. I was delivering some medical supplies to Tautenia when I was attacked by these pirates. I could sure use a hand here..."
        kay "(One extra ryder. This should even the odds.)"
        kay "All right, Claude. The Sunrider is at your service. Let's get these bogies off of you."
        play sound "sound/objectives.ogg"
        "New Objective: Defeat all enemies."

        hide claude onlayer screens with dissolve

        $BM.draggable = True

        $ check2 = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission9 #loop back
    else:
        pass #continue down to the next label

label aftermission9:

    python:
        #this code will be useful if you shift-P through last battle
        if mochi in player_ships:
            BM.ships.remove(mochi)
            player_ships.remove(mochi)
            bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp()]
            bianca = create_ship(Bianca(),None,bianca_weapons)


    hide screen commands
    hide screen battle_screen

    play music "music/The_Beginning_Of_The_Adventure.ogg"

    scene bg bridge with dissolve

    window show

    show cullen:
        xpos 0.8
    with wipeup

    cul "Fools! What are you doing!? How could you let yourself be beat by a single ship!?"
    kay "Looks like today's not your day, Veniczar Porkchops."
    cul "T-tsch... How dare you! I will not stand for this mockery!"
    cul "Mark my words... You will regret crossing me, captain!"

    show cosette plugsuit point evilsmile:
        xpos 0.5
    with wipeup

    cos "Hah! Your days are numbered now!"
    kay "I'm truly shaking in my boots."

    hide cullen with wipedown
    hide cosette with wipedown

    show ava uniform handonhip neutral with dissolve

    ava "The remaining enemy units are pulling back."
    kay "Good. Let them go for now."
    ava "Aye sir."
    kay "Let's bring our new friend on board."

    scene bg hangar with dissolve
    play music "Music/As_I_Figure.ogg" fadeout 1.5

    show claude plugsuit neutral kittyclosedeyessmile with dissolve

    cla "Pwahhh... That was close..."
    kay "Welcome aboard the Sunrider."

    show claude plugsuit excited hearteye with dissolve

    cla "Oooaaahh..."

    play sound "sound/chime.ogg"
    scene cg_shojocaptain with dissolve

    cla "M-my captain in shining armor..."

    show ava uniform facepalm:
        xpos 0.8
    with dissolve

    ava "Ugh... And so another bizarre being washes up on our hangar..."

    scene bg hangar with dissolve

    show claude plugsuit fingeronlips hearteyekittyblush with dissolve

    cla "O-oh my... Eh-heh... You're cuter in person than you looked on the monitor."

    menu:
        "What were you doing out here alone? This area of space is dangerous.":
            jump hereareaisdangerous

        "You don't look so bad yourself.":
            jump youlooksoyourself

label youlooksoyourself:

    $ affection_claude += 1

    show claude plugsuit fingerup smileblush with dissolve

    cla "Ahahaha, oh my. It's still too soon to be flirting with your damsel in distress, capt'n. Especially with a hangar full of other women watching."

    show ava uniform facepalm:
        xpos 0.7
    with dissolve

    ava "Captain! Just please get to business already! Arggghh!"

    show chigara plugsuit handonchest sadblush:
        xpos 0.3
    with dissolve

    chi "Uuuu... I guess the captain is into girls with big boobs, huh..."

    show asaga plugsuit thinking confident:
        xpos 0.12
    with dissolve

    asa "Shhh, Chigara... This could be a special form of interrogation!"

    show icari plugsuit armscrossed seriously:
        xpos 0.88
    with dissolve

    ica "Seriously..."

    hide asaga with dissolve
    hide chigara with dissolve
    hide ava with dissolve
    hide icari with dissolve

    jump hereareaisdangerous

label hereareaisdangerous:

    cla "I was just delivering some medical supplies to a clinic on Tautenia when I was stopped by those pirates. I imagine I would have been killed had you not arrived in time."

    show claude plugsuit handstogether hearteye with dissolve

    cla "Looks like I'm in your debt now, captain."
    kay "Medical supplies? But you don't look like a freighter pilot..."
    cla "Oh, no, no. I'm a doctor."
    kay "A doctor, huh? Well, that makes more sense."
    kay "Well, uh, aside from the ryder piloting part."

    show claude plugsuit fingerup smileblush with dissolve

    cla "Eh-heh... You pick strange skills like that up when you've stayed in the Neutral Rim too long."
    kay "Well then, we'll just drop you off at Tautenia and you can take a shuttle to the surface. Glad we could be of help."

    show claude plugsuit excited surpriseblush with dissolve

    cla "Oh, no, captain! I couldn't possibly leave without first repaying my debt."

    show claude plugsuit handstogether drool with dissolve

    cla "Eh-heh... not to mention it'd be a shame to leave a total hottie behind so soon..."
    kay "What's that?"

    show claude plugsuit excited surpriselaugh with dissolve

    cla "Oh, nothing, captain!"

    show claude plugsuit fingerup smileblush with dissolve

    cla "Say... I don't suppose you need a doctor on board this ship?"
    kay "Actually... We do! Our sickbay's been closed ever since we've left port without our doctor!"

    show claude plugsuit excited happyblush with dissolve

    cla "Ka-ching! Dr. Trillo at your service, captain!"
    kay "Haha, what good luck! Hey Ava, we finally have a doctor for our ship!"

    show claude plugsuit excited closedsmilelaugh with dissolve

    cla "Oh captain! I'm so glad we could meet!"
    kay "Nah, I'm glad you're here to help. Haha, I was getting worried about the sickbay!"

    show ava uniform facepalm:
        xpos 0.15
    with dissolve

    ava "...unbelievable. He's eating completely out of her hand."

    show asaga plugsuit handsonhips annoyed:
        xpos 0.7
    with dissolve

    asa "Uu-uwah... Chigara, I think you've met quite a formidable rival here..."

    show chigara plugsuit palmsup surpriseblush:
        xpos 0.85
    with dissolve

    chi "M-me? E-eh? Eehhh!?"

    $ asa_location = None
    $ chi_location = None
    $ ica_location = None
    $ ava_location = "bridge"
    $ ava_event = "dubious_credentials"
    $ pro_location = "sickbay"
    $ pro_event = "medical_examination"

    $ captaindeck = 2

    jump dispatch

label dubious_credentials:

    hide screen ship_map

    play music "Music/The_Rest_of_the_Ents.ogg" fadeout 1.5

    scene bg bridge
    show ava uniform armscrossed frowntalk
    with dissolve

    window show

    ava "Captain. A word with you."
    kay "Is there an issue?"
    ava "I've done some research into our new \"doctor.\" The only problem is that I can't find her medical license on the Alliance Medical Association's database."
    kay "Strange. Maybe she's licensed with a different medical organization?"

    show ava uniform handonhip neutral with dissolve

    ava "Possibly. Despite the AMA being the most reputable, many neutral planets run their own medical licensing schemes."
    ava "Still, I've checked through all of the major neutral medical circles too and she's nowhere to be found."
    kay "...weird..."
    kay "Well, keep up the search, Ava. She's gotta be licensed with someone."

    show ava uniform armscrossed skeptical with dissolve

    ava "Wouldn't it be better to just ask, captain?"
    kay "Oh right, I suppose I could do that."
    ava "Really?"
    kay "Really."
    ava "... ... ..."
    kay "I should go."

    $ captaindeck = 1
    $ ava_location = None

    jump dispatch

label medical_examination:

    hide screen ship_map

    stop music fadeout 1.5

    scene bg sickbay
    show chigara uniform handonchest sadblush
    with dissolve

    window show

    chi "... ... ..."
    kay "Chigara? Are you all right? You don't look so good..."

    show chigara uniform handsup surprise with dissolve

    chi "O-oh! C-captain..."

    show chigara uniform twiddlefingers forcedsmile with dissolve

    chi "I-it's nothing... I... was just here for my medical exam..."
    kay "It's important to get checked, Chigara. We've been without a doctor for long. You never know what you'll pick up with all the people and goods which come and go from the ship."

    show chigara uniform twiddlefinger forcedhappy with dissolve

    chi "O-oh yes... C-checked..."

    show chigara uniform handonchest sadblush with dissolve

    chi "... ... ..."
    chi "I... think I should get going now."
    kay "All right."

    show chigara uniform palmsup closedeyesscared:
        zoom 1
        pause 0.75
        ease 0.75 xpos -0.5
    with dissolve

    chi "G-good bye!!"

    hide chigara

    kay "(That was strange... I wonder what happened to her...)"

    play music "Music/As_I_Figure.ogg" fadeout 1.5

    show claude uniform handstogether closedeyeshappy with dissolve

    cla "Oh captain! I was waiting for you!"
    cla "It's time for your medical exam!"
    kay "Okay..."

    show claude uniform fingerup kittyblush with dissolve

    cla "I hear you've operated this ship without a doctor for nearly a month! Now that simply will not do!"
    kay "Let's just say we didn't have much of a choice."
    "Shields took a seat at one of the beds."

    show claude uniform excited perv with dissolve

    cla "Well, time to unbutton your shirt~"
    "Shields took his shirt off and laid it on the bed, exposing his abs."

    show claude uniform neutral drool:
        zoom 1
        ease 1.00 zoom 1.5 ypos 1.4
    with dissolve

    cla "O-oohh...."
    kay "Uh, is something the matter, doc? You're staring pretty intensely here..."

    show claude uniform fingeronlip forcedsmileblush with dissolve

    cla "O-oh? N-no! Absolutely nothing wrong!"

    show claude uniform excited happyblush with dissolve

    cla "I'll just feel up your ribs, make sure nothing misplaced! Haha! Hah!"
    "Claude felt up Shield's chest, running her palms against Shield's ribs."

    show claude uniform neutral drool with dissolve

    cla "O-oh my..."
    kay "W-what's wrong?"

    show claude uniform fingeronlip forcedsmileblush with dissolve

    cla "N-nothing! Absolutely nothing!"
    kay "(There's something fishy going on here...)"

    show claude uniform excited heartdrool with dissolve

    cla "Heh-heh-heh... Now, time for you to stand and take your trousers off too."
    kay "All right..."
    "Shields undid his belt and took his pants off, placing them next to the bed."
    cla "Oooohhh..."
    "Shields eyed Claude."
    kay "...Well?"

    show claude uniform fingerup heartdrool with dissolve

    cla "Well, it's time for you to take your underwear off too. Haven't you ever had a medical exam done before?"
    kay "None quite like this one."

    show claude uniform fingerup poutblush with dissolve

    cla "Now, now captain... Don't be shy. I'm just a trained professional doing her job."

    show claude uniform excited happyblush with dissolve

    cla "Now, off! This is for your sake, captain."
    kay "Sigh..."
    "Shields reluctantly pulled down his underwear."

    show claude uniform fingeronlip drool with dissolve

    cla "Ufufufufu..."
    "Shields grimaced as Claude poked and prodded his privies. For what purpose, he couldn't really tell."
    cla "O-oh my...!"
    "Shields eyed Claude suspiciously."
    kay "(Suspicious... Highly suspicious!)"
    kay "Say... you are a doctor, aren't you?"
    cla "What do you mean, captain? Of course I'm a doctor!"
    kay "Uh... Y-you wouldn't happen to have a certificate, do you?"

    show claude uniform altneutral smileblush with dissolve

    cla "Of course I do! Unfortunately, it was on the Mochi when the pirates got to it."
    kay "I-is that... REALLY!?"
    kay "W-WHAT ARE YOU DOING!?"

    show claude uniform neutral hearthappy with dissolve

    cla "Getting a semen sample! What else!?"
    kay "I-isn't there a standardized device you can use for that!?"

    show claude uniform excited hearthappy with dissolve

    cla "Who needs a fancy device when I got a strong hand right here!"
    kay "(This is so far from protocol not even I can handle it!)"

    play music "Music/Run Amok.ogg" fadeout 1.5

    show ava uniform fistup shout:
        xpos 0.2
    with dissolve

    ava "CAPTAIN!"
    kay "HURK! A-Ava!?"
    ava "I found it here!!!"
    kay "F-found what!?"

    show ava uniform point angry with dissolve

    ava "That little skeever isn't a doctor at all! Look here on this form!"
    ava "Medical license suspended due to malpractice!"
    ava "WARNING: This individual is known to mascaraed as a medical practitioner. Her skills fall beyond all reasonable standards of modern medical care. Patients are advised to seek the advice of a professional medical practitioner instead of this individual."
    kay "I-I knew it!"

    show ava uniform salute angry with dissolve

    ava "Orders, captain!?"
    kay "F-fire vanguards!"
    kay "... ... ..."
    kay "I mean, get me my clothes damnit!"

    show ava uniform alt neutral angry with dissolve

    ava "You're under arrest!"

    show claude uniform neutral ooshock:
        ease 0.5 ypos 1.0 zoom 1.0
    with dissolve

    cla "G-GONG... F-for what?"
    ava "For impersonating as a medical professional!"
    kay "(And molesting a starship captain!)"

    show chigara uniform handsonchest sad:
        xpos 0.8
    with dissolve

    chi "U-um... I think I forgot my badge here... and what's all this commotion a-"

    show chigara uniform palmsup surpriseblush with dissolve

    chi "H-EH!? C-c-c-c-captain!?"

    show chigara uniform neutral dazed:
        zoom 1
        pause 0.5
        ease 0.8 ypos 2.0
    with dissolve

    pause 0.5

    play sound "sound/hit.ogg"
    show layer master at shake1

    chi "O-oh my...."

    kay "C-Chigaraaa...!"

    scene bg captainsoffice with fade

    stop music fadeout 1.5

    show ava uniform armscrossed frown with dissolve
    show claude uniform neutral sob:
        xpos 0.75
    with dissolve

    ava "Captain, I've placed our \"doctor\" under arrest. What should we do with her?"
    kay "Send a transmission to the Alliance. We'll just turn her over to the authorities."
    cla "Sniff... sniff..."
    kay "... ... ..."

    show claude uniform handstogether puppy with dissolve #####REPLACE

    cla "Y-you wouldn't do that to ol' Claude now, captain, would you?"
    cla "You see... Claude was just trying to help! I didn't mean any harm by it."
    cla "Whenever I see someone in need, I just can't stop myself from trying to help..."

    show ava uniform armscrossed lookawaymad with dissolve

    ava "Hmph."
    kay "(This girl's good, I'll give her that. But she's not going to fool me twice.)"
    kay "We're here on serious Ryuvian business. A warship is no place to fool around, Claude."

    show claude uniform handstogether closedeyesblush with dissolve

    cla "Sniff... If you're looking for Ryuvian treasure, the place you're looking for is the Mnemosyne Abyss."
    kay "(Damnit! I accidently let slip what we were here for. That was careless.)"

    show ava uniform alt neutral mad with dissolve

    ava "The Mnemosyne Abyss? What do you know about it?"

    show claude uniform neutral sadblush with dissolve

    cla "It's pretty well known among the locals on Tautenia as the site of an ancient Ryuvian battle. Thousands of derelict ships litter the area."
    cla "This area's largely unexplored, so many hidden treasures still remain there."
    kay "(Hidden treasures? This sounds like a possible lead for the Crown Jewel...)"

    show ava uniform handonhip neutral with dissolve

    ava "What do you think, captain? Could this be a possible lead?"
    kay "It's the best we have right now. It's worth investigating."
    kay "We'll set course for the Mnemosyne Abyss."
    ava "Oh. And what of our \"doctor?\""
    kay "Looks like we'll have to delay turning her over to the authorities."

    menu:
        "She'll be confined to quarters in the meantime until we're finished with our mission.":
            jump confineduntilwithmission

        "Get her to the hangar. She'll be more useful as a pilot than a doctor.":
            jump hangarusefulpilotdoc

label confineduntilwithmission:

    $ ClaudeConfine = True

    show ava uniform salute neutral with dissolve

    ava "Understood, sir."

    show claude uniform neutral sob with dissolve

    cla "No way! Captain..."

    show ava uniform armscrossed angry with dissolve

    ava "Come on, this way! Unless you want to be zapped again."
    cla "Sniffle sniffle..."

    jump jumptograveyard

label hangarusefulpilotdoc:

    $ ClaudeConfine = False

    $ affection_claude += 1

    show claude uniform neutral smallsurprise with dissolve

    cla "Does this mean..."

    show claude uniform excited hearthappy with dissolve

    cla "You're still giving me another chance!?"

    play sound "sound/chime.ogg"
    scene cg_shojocaptain with dissolve

    cla "Oh captain... My hero!"

    scene bg captainsoffice
    show claude uniform excited hearthappy:
        xpos 0.75
    show ava uniform handonhip neutral:
        xpos 0.5
    with dissolve

    show ava uniform facepalm with dissolve

    ava "Unbelievable... Come on, the hangar's below us."
    cla "Oh captain! Thank-you so much! I won't let you down!"

label jumptograveyard:

    scene bg black with screenwipe
    scene bg bridge with screenwipe
    show ava uniform neutral neutral with dissolve

    play music "Music/La_Busqueda_de_Lanna.ogg"

    ava "Setting in coordinates. Are you sure you want to jump there?"
    kay "Who knows? Maybe we might also find lost technology which can make the Veniczar magically disappear."
    ava "Coordinates are in. Spooling up warp drive."
    kay "Jump!"

    window hide
    scene map_nomodorn:
        ypos -0.2
    show sunrider_warpout_standard:
        xpos 700 ypos 350
    with dissolve

    pause 2.0

    play sound "Sound/large_warpout.ogg"
    show sunrider_warpout_standard_flash:
        xpos 426 ypos 0 alpha 0
        linear 0.1 alpha 1
        linear 0.1 alpha 0
    show sunrider_warpout_standard out:
        xpos 700 ypos 350
        ease 0.2 xpos 200 ypos 300 zoom 0
    pause 2.0

    stop music fadeout 1.5

    scene bg bridge
    show ava uniform neutral neutral
    with dissolve

    window show

    ava "Arrival on target."
    ava "I'm reading... something strange on scanners."
    kay "Strange?"

    play music "Music/Arcadia.ogg"
    scene cg_graveyard:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.25
        ease 10.0 ypos 0.7
    with dissolve

    kay "Sweet mother of god..."
    kay "I've never seen anything like this. Ava, what am I seeing here?"
    ava "An... ancient warship of some kind. Over four kilometers long."
    kay "This could be the biggest finding of lost technology of this decade. All this time, this was hidden here..."
    ava "So do you really think the crown jewel is out here?"

    scene bg bridge
    show ava uniform neutral neutral
    with dissolve

    kay "Let's find out. Asaga, are you there?"

    show asaga plugsuit neutralalt alert:
        xpos 0.2
    with wipeup

    asa "We're ready down here, capt'n! What're your orders?"
    kay "I want our ryders to launch and provide recon for the Sunrider. Find out what's out there and figure out where all this wreckage came from."
    asa "Understood, captain! Alright, you heard the man! All units, launch after me!"

    scene cg_graveyard:
        yanchor 0.5 xanchor 0.5 xpos 0.5 ypos 0.6
    with dissolve

    chi "It's... eerily beautiful."
    ica "In all my years of flying, I've never seen anything like this. Are you seeing this, captain?"
    kay "Yeah..."
    ica "Look up ahead!"
    chi "It's... a vessel. Almost perfectly preserved, even after all these years."
    asa "There're more of them! T-they're everywhere!"
    kay "A dark starship graveyard."
    ava "My father used to tell me ghost stories about space graveyards when I was younger to scare me... This looks like something that could be right out of one of his tales..."
    chi "I've dated those ships, captain. They're over two thousand years old."
    chi "According to those markings, these ships belonged to the Ryuvian princess' royal guard."
    kay "Then the crown jewel could be nearby. Chigara, we're looking for some kind of crystalline device. See if it's on any of those ships."
    ica "A battle took place here, there's no doubt about it."
    ava "How do you know the ships weren't just abandoned here?"
    ica "Because I'm reading organic material inside the ships. The crews were perfectly preserved in the vacuum of space."
    ica "Look into the windows. There're frozen body parts inside..."
    chi "Uuu... C-Chigara's closing her eyes now..."
    kay "What could have caused this...?"
    ica "It looks like some kind of... blast. The ships are more and more damaged the deeper we head into the field."
    kay "Can you determine the epicenter?"
    chi "It's the super dreadnought, captain. A massive energy blast must have emanated from it, while still keeping most of its own structure intact."
    chi "The technology inside that ship alone could... improve our current technology by a hundred fold. If you factor in all the ships in this field..."
    chi "This could be the biggest discovery of Lost Technology in the past hundred years!"
    kay "I think we've hit the jackpot. Asaga, get us a closer view of that Ryuvian super battleship."
    asa "Understood sir."
    asa "I'm... seeing some kind of a hangar bay."
    asa "Eh-heh... I'm going to check out what's inside that thing. I'm goin' ahead, capt'n!"

    scene bg bridge with dissolve
    show ava uniform alt neutral neutral with dissolve

    kay "Hold on Asaga. We don't know what we're up against yet."

    show asaga plugsuit handsonhips happy:
        xpos 0.2
    with wipeup

    asa "Ah c'mon capt'n, it's just a big old frozen ghost ship! What's there to be scared about?"
    kay "Seriously... Would you listen to yourself for a moment?"

    show asaga plugsuit neutral content with dissolve

    asa "The inside of the ship's pretty spacious..."
    asa "It looks like this ship was definitely a carrier... I'm seeing a lot of open space. Enough to store a thousand ryders!"

    show chigara plugsuit altneutral neutral:
        xpos 0.75
    with wipeup

    chi "The Ryuvians were the ones who originally invented ryder technology. So of course they must have the carriers to support a battalion of ryders."
    asa "The design of this ship's nothing like any ship I've been on though. It's like the whole ship is one big hangar. Almost like... the inside of a hive."
    asa "I think the ship's command center should be up above."

    show icari plugsuit armscrossed confident:
        xpos 0.9
    with wipeup

    ica "Think the crew's still frozen up there?"
    asa "Who knows? We haven't seen any other crewmen here though."

    show chigara plugsuit handonchest neutral with dissolve

    chi "Could the ship have been fully AI controlled? If the ship was depressurized in the middle of a battle, you'd think there'd be frozen crewmen..."

    show icari plugsuit handonhip neutral with dissolve

    ica "An AI? Control something this big?"
    chi "Anything could be possible with Ryuvian technology."

    show asaga plugsuit neutral neutral with dissolve

    asa "I've made it to what looks like the entrance to the ship's bridge."
    asa "I'm detecting a faint energy signal beyond that airlock. The life support systems are still functional in the bridge!"

    show asaga plugsuit excited closedeyessmile with dissolve

    asa "I'm going to leave my ryder and head in there for a closer look!"

    show icari plugsuit point mad with dissolve

    ica "Are you crazy! You don't know what's in there!"

    scene cg_ryuvianbridge with dissolve

    asa "I'm out of my cockpit. I'm feeding you the POV camera on my suit, capt'n."
    kay "I see it..."
    asa "It's definitely unlike any bridge I've seen. Only one control station. Was this entire ship meant to be flown by just one person?"
    asa "Wait a minute... I'm seeing... Something weird..."
    asa "There's... some kind of a capsule..."
    asa "Oh..."
    asa "Are you seeing this, captain?"
    kay "I'll be damned. She's been... perfectly preserved."
    chi "No... Not preserved....."

    play music "Music/Poltergeist_Attack.ogg"
    play sound "sound/Ryuvian klaxon.ogg"

    scene cg_ryuvianbridge_red with dissolve

    asa "Uh oh!"
    kay "What did you do!?"
    asa "N-nothing! I swear! The thing just came to life on its own!"
    "Ship" "Ga'rk! Sharn-la ree seath ta!"
    asa "Uuhh... Anyone understand what it's saying?"
    chi "Captain, I'm reading a sudden increase in power! The super battle ship..."
    chi "I-It's coming back to life!"

    scene bg bridge
    show ava uniform alt neutral angry
    with dissolve

    ava "Warning! All the Ryuvian vessels have powered up!"
    kay "What-!? B-but the crew-"

    show icari plugsuit neutral surprise:
        xpos 0.8
    with wipeup

    ica "I-it's a ghost fleet! This whole place is cursed!"
    ava "The Ryuvian fleet is powering weapons, sir! Your orders!"

    play sound "Sound/redalert.ogg"
    scene bg bridgered
    show ava uniform alt neutral angry
    show icari plugsuit neutral surprise:
        xpos 0.8
    with dissolve

    kay "Red alert! All hands, battle stations!"
    kay "Asaga, GET OUT OF THERE!"

    scene cg_ryuvianbridge_empty with dissolve

    asa "U-uh... c-captain..."
    show sola face awakened:
        ypos 1.0 xpos 0.5 yanchor 935
        ease 0.5 zoom 2.0 yanchor 1600 alpha 0
    with dissolvequick

    show white:
        alpha 0
        ease 0.5 alpha 1.0

    pause 0.75

    scene bg bridge with dissolve
    show ava uniform alt neutral angry
    with dissolve

    ava "We've lost contact with Asaga!"
    kay "What in hell's-"
    ava "The enemy vessels are firing on us! Shall we return fire!?"
    kay "Tsch... No choice! All units! Defend the Sunrider!"

    if ClaudeConfine == True:

        show ava uniform armscrossed frown with dissolve

        ava "What about the Black Jack?"
        kay "Asaga's a tough girl.  She'll make it out of there."
        kay "(We're still one ryder short though... This is going to be a challenge...)"

        show claude plugsuit excited determined:
            xpos 0.2
        with wipeup

        cla "Captain!"
        kay "Claude? What are you doing on this line!"
        cla "Let me help! I might not be a licensed doctor, but I can still fight!"
        kay "...All right. Doesn't look like we have much of a choice."
        kay "All units, launch!"

    play sound "Sound/battle.wav"
    show battlewarning:
        xpos 0.5 ypos 0.5 zoom 20
        ease 0.5 zoom 1
    pause 0.5
    play sound "Sound/drum.ogg"
    $ renpy.pause(2)

    window hide
    hide bg bridgered
    hide ava
    hide icari
    hide claude
    hide battlewarning

    $ check1 = False
    $ check2 = False

    call mission10_inits
    $ BM.mission = 10
    jump battle_start

label mission10:

    $BM.battle_bg = "CG/graveyard.jpg"

    if check1 == False:

        $BM.draggable = False

        "Tip: Take cover in the wreckage to avoid enemy attacks."

        $ check1 = True

        $BM.draggable = True

    if check2 == False and BM.turn_count == 2:

        $BM.draggable = False

        show asaga plugsuit excited focushappy onlayer screens:
            xpos 0.8
        with dissolve

        python:
            blackjack.set_location(10,3)
            player_ships.append(blackjack)

        asa "Ompf. Sorry I'm late, captain!"
        kay "Asaga! Are you all right?"

        show asaga plugsuit handsonhips annoyed onlayer screens with dissolve

        asa "Fine... just..."

        python:

            create_ship(SeraphimEnemy(),(16,8),[SeraphimEnemyKinetic()])
            create_ship(SeraphimEnemy(),(17,9),[SeraphimEnemyKinetic()])
            create_ship(SeraphimEnemy(),(16,10),[SeraphimEnemyKinetic()])

        hide asaga onlayer screens
        show icari plugsuit point mad onlayer screens:
            xpos 0.8
        with dissolve

        ica "Watch it Black Jack! You have three ryders on your tail!"

        show asaga plugsuit handsonhips determined onlayer screens:
            xpos 0.8
        hide icari onlayer screens
        with dissolve

        asa "Ryder! There's just one pilot!"
        kay "Did I just hear you right? Pilot!?"

        show chigara plugsuit excited determined onlayer screens:
            xpos 0.8
        hide asaga onlayer screens
        with dissolve

        chi "Captain, two of those three ryders are copies! The super dreadnought appears to be using some kind of holographic emitter!"

        show asaga plugsuit handsonhips determined onlayer screens:
            xpos 0.8
        hide chigara onlayer screens
        with dissolve

        asa "I don't know what kind of holograms these are though, 'cause the two fake ones are just as deadly as the real thing!"

        show icari plugsuit neutral mad onlayer screens:
            xpos 0.8
        hide asaga onlayer screens
        with dissolve

        ica "Tsch...! Even after 2000 years of decay, these enemies are still insane!"

        hide icari onlayer screens

        $ check2 = True

        $BM.draggable = True

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission10 #loop back
    else:
        pass #continue down to the next label

label aftermission10:

    hide screen commands
    hide screen battle_screen

    python:
        if not blackjack in player_ships:
            player_ships.append(blackjack)

    scene bg bridgered with dissolve

    window show

    show claude plugsuit excited happy with wipeup

    cla "Ah-hah! We got all of them!"

    play music "Music/Battle_Against_Time.ogg"

    scene space back1
    show seraphimenemy:
        xpos 0.5 ypos 0.5
    with dissolve

    asa "Uwah oh! Negative, captain! All three ryders were decoys! The real one's still here!"
    kay "Take it out!"

    asa "Chigara, watch out! It's targeting you!"

    window hide

    play sound "sound/mech1.ogg"
    show seraphimenemy kinetic with dissolve

    pause 0.1

    play sound1 "sound/Sola Sniper.ogg"
    pause 0.6
    show seraphimenemy_charge1 with dissolve
    pause 0.6

    show layer master at shake1(pausetime=0.1)

    show seraphimenemy_charge2:
        xpos 0.5 ypos 0.5 alpha 0
        ease 0.1 alpha 1
        pause 0.1
        ease 0.1 alpha 0 zoom 1.5
    show seraphimenemy_bullet:
        alpha 0 xpos 0.5 ypos 0.5
        pause 0.1
        alpha 1.0
        ease 0.2 xpos -2.0 ypos 4.0

    pause 0.8

    scene cg_deflectbullet1 with dissolve

    chi "H-eh??"
    asa "Argh... As if...!"

    play sound "sound/boasters.ogg"
    pause 0.7
    show cg_deflectbullet2:
        xpos -0.8
        ease 0.7 xpos 0.0

    pause 1.0

    play sound2 "sound/Sword Shing 2.ogg"
    scene cg_deflectbullet3 with dissolve

    pause 1.0

    play sound3 "sound/explosion1.ogg"
    scene cg_deflectbullet4:
        ease 0.01 xpos 0.02
        ease 0.02 xpos -0.02
        ease 0.01 xpos 0.0
        repeat 8
    with dissolve
    play sound4 "sound/explosion2.ogg"
    scene cg_deflectbullet5:
        ease 0.01 xpos 0.02
        ease 0.02 xpos -0.02
        ease 0.01 xpos 0.0
        repeat 8
    with dissolve
    pause 2.0

    window show

    scene bg bridgered with dissolve

    kay "Chigara! Report! Are you safe!?"

    show chigara plugsuit excited scared with wipeup

    chi "Y-yes, captain! A-Asaga just deflected the bullet!"

    show icari plugsuit point angry:
        xpos 0.8
    with wipeup

    ica "A-are you kidding me!? T-that bullet was traveling at 150 percent the speed of light! That's absolute bullshit! There's no way she did that!!!"

    scene space back1
    show seraphimenemy:
        xpos 0.5 ypos 0.5
    with dissolve

    show sola plugsuit neutral madglow:
        xpos 0.2
    with dissolve

    sol "You... are..."
    sol "... ... ..."
    sol "There is only one capable of fighting like you."
    sol "Impossible... There cannot be another... And..."
    sol "How is it that I yet live?"

    show asaga plugsuit point angry:
        xpos 0.8
    with dissolve

    asa "You're not makin' any sense!"

    show sola plugsuit altneutral neutral:
        xzoom -1 xpos 0.2
    with dissolve

    sol "I yield. The battle has been decided."
    ava "The Seraphim has powered down!"

    hide asaga
    show icari plugsuit neutral angry:
        xpos 0.8
    with dissolve

    ica "Tsch! The rest of the cruisers are still coming online though! We've got more enemies inbound!"
    sol "My control over the fleet has been lost. But their power shall soon fail."

    play music "Music/Coming_Soon_Part1.ogg" fadeout 1.5
    scene bg bridgered with dissolve
    show chigara plugsuit neutral scared:
        xpos 0.8
    with dissolve

    chi "A-ah! C-captain! I'm reading massive power fluctuations coming from the super battleship!"
    chi "I-it is attempting to power its main weapon!"
    kay "All ryders! Fall back! We're getting out of here!"

    show chigara plugsuit excited scared with dissolve

    chi "No... The ship's structure has been too badly damaged!"
    chi "It's overloading its main reactor... At this rate..."
    chi "There'll be a total reactor core meltdown! We have to get out of here now!"

    play music "Music/Coming_Soon_Part2.ogg" fadeout 0.5 noloop

    kay "Everyone, emergency landing procedures! We're getting out of here!"
    asa "All units have returned! We're ready here, captain!"

    window hide

    scene cg_graveyardescape1
    show cg_graveyardescape4
    with dissolve

    chi "The core's going critical! It's going to-"

    play sound1 "sound/explosion5.ogg"
    scene cg_graveyardescape2
    show cg_graveyardescape5
    with dissolve

    ava "Holy sweet---"
    kay "Spool up warp drive! WARP! WARP! Get us out of here!!"

    pause 1.0

    play sound2 "sound/large_warpout.ogg"
    show cg_graveyardescape6:
        alpha 0
        ease 0.2 alpha 1
        ease 0.2 alpha 0
    hide cg_graveyardescape5
    show cg_graveyardescape7:
        xpos 0.5 ypos 0.5
        ease 0.6 xpos -1.0 ypos 2.0 zoom 10.0

    pause 2.0

    play sound3 "sound/explosion4.ogg"
    scene cg_graveyardescape3 with dissolve
    scene white with dissolvelong

    scene bg bridgered with dissolvelong

    window show

    show ava uniform handonhip neutral with dissolve

    ava "Warp successful, captain. All sections are reporting in."
    kay "What happened to the Ryuvian ships?"
    ava "All vaporized by the blast."
    kay "(Damn! There goes our chance to recover all that lost technology!)"
    kay "All right.  Stand down red alert."

    scene bg bridge
    show ava uniform handonhip neutral
    with dissolve

    ava "The Ryuvian girl has been taken into custody in the hangar. Your orders?"
    kay "Let's go down there. She's the only clue we have at figuring out what happened back there."

    play music "Music/Mission_Briefing.ogg"
    scene bg hangar with dissolve

    show sola plugsuit altneutral neutral with dissolve

    sol "... ... ..."
    kay "I'm Captain Kayto Shields. Welcome aboard the Sunrider."
    sol "You... are the leader?"
    kay "What's your name?"

    show sola plugsuit handonchest neutral with dissolve

    sol "I... I am Princess Sola vi Ryuvia."
    kay "P-Princess!? Are you the Princess who's been missing from Ryuvia all this time?"

    show chigara plugsuit palmsup surprise:
        xpos 0.2
    with dissolve

    chi "No... T-that's impossible!"
    chi "Sola vi Ryuvia's been dead for two thousand years!"

    show sola plugsuit altneutral neutral with dissolve

    sol "... ... ..."

    hide chigara with dissolve

    menu:
        "Why did you attack us?":
            jump whydidyouattack
        "Do you know what destroyed all those Ryuvian ships?":
            jump destroyedallryuvianships
        "What were you doing on board that super dreadnought?":
            jump boardthatsuperdreadnought
        "You've been frozen for over two millennia on board that ship!":
            jump youfrozentwomillenia
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label whydidyouattack:

    sol "The last I remember before the Final Tear was battle."
    sol "The Fallen had overwhelmed our position. They were about to end us."
    sol "Then... a flash, followed by utter destruction."
    sol "To me... the sleep felt like an instant. I did not even realize that the battle had been interrupted, or that my adversary had changed."
    kay "(I'm not sure I follow what she's saying... But it seems like she attacked us by mistake.)"

    menu:
        "Do you know what destroyed all those Ryuvian ships?":
            jump destroyedallryuvianships
        "What were you doing on board that super dreadnought?":
            jump boardthatsuperdreadnought
        "You've been frozen for over two millennia on board that ship!":
            jump youfrozentwomillenia
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label destroyedallryuvianships:

    show sola plugsuit neutral neutral with dissolve

    sol "Such is the ultimate weapon of the Sharr'Lac."
    sol "The Final Tear. A devastating power to destroy everything within half a light year radius. And one which cannot be unleashed without paying the ultimate sacrifice."
    kay "(The Sharr'Lac? She must be referring to the super-dreadnought.)"
    kay "(To think that single ship was capable of such destruction... It could destroy entire systems!)"

    menu:
        "Why did you attack us?":
            jump whydidyouattack
        "What were you doing on board that super dreadnought?":
            jump boardthatsuperdreadnought
        "You've been frozen for over two millennia on board that ship!":
            jump youfrozentwomillenia
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label youfrozentwomillenia:

    show sola plugsuit neutral sad with dissolve

    sol "... ... ..."
    kay "You must be even more shocked than us. Uh, welcome to the future."
    sol "What of the Fallen? Was... my mission successful?"
    kay "I don't know. It happened so long ago. Much of our knowledge of your time has been lost."
    sol "... ... ..."
    sol "I see..."

    menu:
        "Why did you attack us?":
            jump whydidyouattack
        "Do you know what destroyed all those Ryuvian ships?":
            jump destroyedallryuvianships
        "What were you doing on board that super dreadnought?":
            jump boardthatsuperdreadnought
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label boardthatsuperdreadnought:

    show sola plugsuit altneutral neutral with dissolve

    sol "... ... ..."
    sol "In battle."
    kay "Battle? You mean before you were frozen?"
    sol "Yes."
    sol "... ... ..."
    kay "Who were you fighting?"
    sol "The Fallen."
    kay "Who are they?"
    sol "Imposters to the throne, led by the pretender Crow Harbour."
    kay "(She's not revealing much... It sounds like she's referring to some kind of civil war within Ryuvia during her time period.)"

    menu:
        "Why did you attack us?":
            jump whydidyouattack
        "Do you know what destroyed all those Ryuvian ships?":
            jump destroyedallryuvianships
        "You've been frozen for over two millennia on board that ship!":
            jump youfrozentwomillenia
        "That's enough questions. We are seeking a Ryuvian artifact known as the crown jewel. Do you know where to find it?":
            jump enoughryuvianknownjewel

label enoughryuvianknownjewel:

    sol "The... crown jewel?"
    ava "It is a crystalline device which shows the location of members of the royal family."

    show sola plugsuit handonchest neutral with dissolve

    sol "You speak of the talbur. It is in my possession."

    show sola plugsuit back neutral with dissolve

    sol "Shall I retrieve it from the Seraphim?"
    kay "Sure, can you go get it?"

    hide sola with dissolve

    "... ... ..."

    show sola plugsuit neutral neutral with dissolve
    show item_jewel:
        xpos 0.2
    with dissolve

    sol "It is here."

    show claude plugsuit altneutral surprise:
        xpos 0.8
    with dissolve

    cla "O-oohh... It's... glowing!"
    sol "Yes. The talbur illuminates in the presence of the royal family."

    show sola plugsuit handonchest sad with dissolve

    sol "And yet... It shall never glow for I."

    play music "Music/Invasion of Chaos.ogg" fadeout 1.5
    play sound "sound/redalert.ogg"

    "-warning-"
    kay "The hell? What's wrong?"

    hide claude
    show ava uniform altneutral angry:
        xpos 0.8
    with dissolve

    ava "Proximity warning! PACT signatures detected!"
    kay "Damn! Not a moment's peace!"
    kay "C'mon people, return to battle stations!"

    scene bg bridgered with dissolve

    kay "What's our status!"
    ava "Multiple PACT signatures detected! U-uh..."
    kay "How many!?"

    play music "Music/Posthumus_Regium.ogg"
    scene porkfleet_back with dissolve

    show portfleet_1a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound "sound/large_warpout.ogg"
    show portfleet_1b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_1c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_2a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound1 "sound/large_warpout.ogg"
    show portfleet_2b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_2c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_3a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound2 "sound/large_warpout.ogg"
    show portfleet_3b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_3c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_4a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound3 "sound/large_warpout.ogg"
    show portfleet_4b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_4c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_5a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound4 "sound/large_warpout.ogg"
    show portfleet_5b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_5c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_6a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound5 "sound/large_warpout.ogg"
    show portfleet_6b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_6c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_7a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound6 "sound/large_warpout.ogg"
    show portfleet_7b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_7c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_8a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound7 "sound/large_warpout.ogg"
    show portfleet_8b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_8c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_9a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound8 "sound/large_warpout.ogg"
    show portfleet_9b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_9c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.

    show portfleet_10a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound1 "sound/large_warpout.ogg"
    show portfleet_10b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_10c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    show portfleet_11a:
        xpos 2.0 ypos -0.05
        ease 0.5 xpos 0.0 ypos 0.0
        alpha 0
    play sound2 "sound/large_warpout.ogg"
    show portfleet_11b:
        alpha 0
        pause 0.5
        ease 0.1 alpha 1.0
        ease 0.1 alpha 0.0
    show portfleet_11c:
        alpha 0
        pause 0.5
        alpha 1.0

    pause 0.1

    ava "Forty - no... sixty ships, captain! I-it's an entire fleet!"
    kay "Spool up the warp drive! Get ready to-"
    ava "It'll take another half hour before we can warp again after our last emergency warp, captain!"
    kay "Tsch..."

    scene bg bridgered with dissolve
    show cullen with wipeup

    cul "Haaah-hahahaha! Did I not tell you that you would regret crossing me!?"
    kay "Veniczar Porkchops!"
    cul "T-tsch! Curse you and your foul ship!"
    cul "You are hopelessly outnumbered! I know you have the crown jewel aboard. Why don't you be a good lad and turn it over, eh?"
    kay "The crown jewel? And what would PACT want with it?"
    cul "Hah! It seems that little contraption can let us find our dear leader's runaway bride. I have been tasked with finding it on his behalf!"
    kay "(Veniczar Arcadius' bride? The princess of Ryuvia's engaged to Arcadius?)"
    kay "(...no wonder she's run away.)"

    menu:
        "You can take the crown jewel from my cold, dead hands.":
            jump jewelcolddead

        "All right. But in exchange, you promise me the safety of my crew.":
            jump exchangepromisesafety

label jewelcolddead:

    cul "Tsk. I was afraid it would come to this."
    cul "Men! Open fire! Perhaps a little show of force will mellow out this boggart!"

    hide cullen with wipedown

    jump porkfleetopenfire

label exchangepromisesafety:
    cul "Hah! That's a good boy now."
    cul "You have my word! Your crew shall not come to harm!"
    kay "Tsch."
    "... ... ..."

    show ava uniform alt neutral mad:
        xpos 0.2
    with dissolve

    ava "The transfer is complete, captain. PACT has taken the crown jewel."

    hide ava with dissolve

    kay "There. We kept our end of the bargain."
    cul "Hehh... Too bad for you captain, but a certain pirate has paid me quite handsomely for your head."
    cul "Men! Open fire! Rid this vermin from my sight!"
    kay "(I should have known better than to trust this python!)"

    hide cullen with wipedown

    jump porkfleetopenfire

label porkfleetopenfire:

    scene porkfleet_assembled with dissolve
    pause 0.5

    play sound "sound/legion_laser.ogg"
    show porkfleet_fire with horizontalwipereversefast
    hide porkfleet_fire with horizontalwipereversefast

    pause 2.0

    scene bg bridgered with dissolve

    show ava uniform alt neutral angry with dissolve

    ava "The PACT fleet has opened fire!"

    play sound "sound/explosion1.ogg"
    show layer master:
        ease 0.02 xpos 0.05
        ease 0.04 xpos -0.05
        ease 0.02 xpos 0
        repeat 8

    ava "A-argh! W-we can't-"
    kay "L-launch our ryders!"

    play sound "sound/explosion1.ogg"
    show layer master:
        ease 0.02 xpos 0.05
        ease 0.04 xpos -0.05
        ease 0.02 xpos 0
        repeat 8

    ava "Massive damage reports coming from all sectors! W-we're..."
    ava "Ugh!"

    show ava uniform neutral surpriseangry with dissolve

    ava "T-there's too many of them, captain!"

    play sound "sound/explosion1.ogg"
    show layer master:
        ease 0.02 xpos 0.05
        ease 0.04 xpos -0.05
        ease 0.02 xpos 0
        repeat 8

    ava "We've sustained critical damage! O-our weapons are inoperative!"
    ava "Engineering reports our reactor is at critical levels!"
    kay "(Is this the end...?)"
    kay "(... ... ...)"
    ava "C-Captain!? Y-your orders!?"
    kay "It's all right, Ava."

    show ava uniform neutral surprise with dissolve

    ava "S-sir?"
    "Shields smiled wryly and held onto Ava's hand."
    kay "Been an honor."

    show ava uniform armscrossed tearsadblush with dissolve

    ava "...T-tsch..."
    "... ... ..."
    hide ava with dissolve
    show asaga plugsuit excited shout with wipeup
    stop music fadeout 1.5

    asa "WAIT!"
    asa "I'M THE ONE YOU'RE LOOKING FOR!"
    cul "Oh?"

    show asaga plugsuit handsonhips mad with dissolve

    asa "I... am Princess Asaga di Ryuvia. By my command, I order you to halt your assault, Cullen!"

    show cullen:
        xpos 0.8
    with wipeup

    cul "Well, I'll be."
    cul "My scans indicate that you are indeed the princess. Hah! Who would have ever thought that you'd be hiding here, my grace!"
    cul "Men, hold your fire! Retrieve the princess for me, and let us be off on our merry way."
    kay "What!? Asaga...!? All this time....?"
    kay "(Aarrggghhh... How could I have never known?)"

    show asaga plugsuit armscrossed sadtear with dissolve

    asa "Captain... I'm sorry for lying to you all this time."
    asa "B-but... this is for the best. Ok?"
    cul "Bwaahahahaha! You had best say your good byes now, captain. Onwards to the state wedding! Set course for Ryuvia Prime!"

    hide cullen with wipedown

    asa "...F-farewell, captain! A-and..."

    show asaga plugsuit neutral forcedsmiletear with dissolve

    asa "Thanks for all the fun!"

    hide asaga with dissolvelong

    kay "T-tsch..."
    kay "(No... This isn't our farewell...)"

    show ava uniform handonhip mad with dissolve

    ava "Captain?"
    kay "Get our repair drones online."

    play sound "sound/ToBeContinued.ogg"
    scene cg_tobecontinued

    pause 5.0

    window hide

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
    show credits16b:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits16c:
        xalign 0.5
        ypos 1.1
        linear 15 ypos -0.25
    $ renpy.pause(3.0)
    show credits16d:
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

    jump aftercreditsep3

label aftercreditsep3:

    scene black with dissolve

    window show
    play music "Music/March_of_Immortals.ogg"

    "NEXT TIME ON SUNRIDER..."
    "Captain Shields and the Sunrider crew race against time to rescue Asaga from the clutches of Veniczar Arcadius!"
    "A daring rescue!"
    "Will the Alliance arrive in time to help?"
    "The full Sunrider team is assembled!"
    "An ancient secret is revealed!"
    "Two armadas clash to determine the fate of the galaxy!"
    "And don't forget... There'll also be lots of space whales next time too!"

    show dontmissit:
        zoom 10
        ease 0.5 zoom 1

    pause 0.5
    play sound "sound/drum.ogg"

    $ renpy.pause(1.0)

    stop music fadeout 1.5
    scene white with dissolvelong

    play sound "sound/drumroll.ogg"

    "And now... The results of our second character popularity contest!"
    "And the winner is..."

    show polltwo:
        xalign 0.5 yalign 0.5
    with dissolve

    show icari plugsuit armscrossed embarassedtsun:
        xpos 0.8
    with dissolve

    ica "S-seriously... Winning such an embarrassing contest..."

    show icari plugsuit point angry with dissolve

    ica "This doesn't mean that I'm gonna do anything special for you in the beach episode, all right!?"

    show icari plugsuit point angry:
        ease 0.5 zoom 2.0 ypos 1.7

    ica "ALL RIGHT!?"

    "Who will win next time? Don't forget to vote at our forums!"

    return

label aftercreditsep2:

    window show
    play music "Music/SAMFREE.ogg" fadeout 1.5

    scene asagacorner with dissolve
    show asaga uniform neutral happy with dissolve



    play sound "sound/drumroll.ogg"
    show asaga uniform neutral happy with dissolve

    asa "With 33 votes counted, the winner is..."

    show pollone:
        xpos 0.01 ypos 0.4

    show asaga uniform neutral surprise with dissolve

    asa "E-eh!? Chigara!?"

    hide pollone with dissolve

    show chigara uniform handsup surprise:
        xpos 0.8
    with dissolve

    chi "O-oh? M-me? *Never expected to win*"

    show asaga uniform armscrossed sad with dissolve

    asa "N-no way... And I'm supposed to be the main girl... *100 percent expected to win*"

    show asaga uniform excited grin with dissolve

    asa "I guess this just means that the winner will get extra fan service shots in the beach episode!"

    show chigara uniform palmsup surpriseblush with dissolve

    chi "Eh!? N-no way..."
    asa "That's right people! Go root for your favorite girl in the next popularity poll! Who knows what nice things will happen to the winner in the beach episode. Heh-heh..."

    show chigara uniform twiddlefingers embarassed with dissolve

    chi "N-nice things huh..."

    show asaga uniform handsonhips happy with dissolve

    asa "And now... the moment you've been waiting for..."
    asa "We have some exclusive previews of our next big Kickstarter project, Doki Doki Space Whale and the Adventures of Unknown Pilot-kun!"
    asa "Ufufufu... Even though this is supposed to be top secret, I guess we can spill the beans on this."
    asa "Sit back... and watch our amazing pitch video!"

    window hide
    scene crash

    pause 1.0

    window show

    asa "EEEEEHHHHHHHHHH!?"

    return

label devconsoleshow:
    show screen devconsole


