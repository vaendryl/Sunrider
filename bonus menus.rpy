init -1 python:

    bonusPage = 0
    
    doki_doki_space_whale = BonusItem("Background/renpytomback.jpg", " Doki Doki Space Whale:\n Dating Sim 3", "deleted_scene_1", 0.09)
    after_ep2 = BonusItem("Background/poll1.jpg", " Beta 2 Post Credits", "aftercreditsep2", 0.205)
    after_ep3 = BonusItem("CG/popularity2.jpg", " Beta 3 Post Credits", "aftercreditsep3", 0.155)
    after_ep4 = BonusItem("CG/popularity3.jpg", " Beta 4 Post Credits", "aftercredits4", 0.165)
    after_ep5 = BonusItem("CG/popularity4.jpg", " Beta 5 Post Credits", "aftercredits5", 0.156)

    scenes = [doki_doki_space_whale, after_ep2, after_ep3, after_ep4, after_ep5]

screen deleted_scenes:

    modal True
    zorder 200
    
    imagemap:
        ground "Menu/deleted_scenes_base.png"
        hover "Menu/deleted_scenes_hover.png"

        # we need to make the screen update when the arrows are clicked
        hotspot (1221, 215, 30, 146) action BonusPagePrevious()
        hotspot (1221, 724, 30, 146) action BonusPageNext()
        hotspot (726, 59, 137, 44) action [ Hide('deleted_scenes'), Show('save', transition=dissolve) ]
        hotspot (948, 926, 107, 23) action [ Hide('deleted_scenes'), Show('bonus', transition=dissolve) ]
        hotspot (864, 59, 137, 44) action [ Hide('deleted_scenes'), Show('load', transition=dissolve) ]
        hotspot (1002, 59, 137, 44) action [ Hide('deleted_scenes'), Show('preferences', transition=dissolve) ]
        hotspot (1140, 59, 137, 44) action [ Hide('deleted_scenes'), Show('main_menu', transition=dissolve) ]

        #style "file_picker_frame"

        $ columns = 1
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            #style_group "file_picker"
            xpos 753
            ypos 216

            if hasattr(store,"BM"):
                $BM.phase = 'Player' # This is done to make sure that we can open the menu while in a bonus

            # Display five file slots, numbered 1 - 5.
            for i in range(1, columns * rows + 1):

                button:

                    xminimum 460
                    yminimum 130
                    background None #Solid(0,0,0,255)

                    has hbox

                    # Add the image and text.
                    if bonusPage * columns * rows + i - 1 < len(scenes):
                        imagebutton:
                            idle (scenes[i - 1].image)
                            hover hoverglow(scenes[i - 1].image)
                            at zoom_button(scenes[i - 1].zoom)
                            action [Hide('main_menu'),Start(scenes[i - 1].jumpLoc)]
                        text scenes[i - 1].text

                    else:
                        text str(bonusPage * columns * rows + i) + ". Deleted Scene"

init -1 python:

    chapter0 = Chapter("CG/cera.jpg", " Prologue", "start", 0.09)
    chapter1 = Chapter("Background/captainsoffice.jpg", " Chapter 1", "chap1_start", 0.08, 200, 1)
    chapter2 = Chapter("Background/captainsoffice.jpg", " Chapter 2", "chap2_start", 0.08, 4570, 5)
    chapter3 = Chapter("CG/avateatime.jpg", " Chapter 3", "ep3_start", 0.09, 11870, 8)
    chapter4 = Chapter("CG/asagakidnap_legion.jpg", " Chapter 4", "chap4_start", 0.09, 15710, 10)
    chapter5 = Chapter("cg/sola_beach.jpg"," Chapter 5", "beachepisode", 0.09, 20000, 12)
    chapter6 = Chapter("cg/ongess_port1.jpg"," Chapter 6", "afterrescue", 0.09, 25000, 15)

    chapters = [chapter0, chapter1, chapter2, chapter3, chapter4, chapter5, chapter6]

screen chapter_select:

    modal True
    zorder 200

    imagemap:
        ground "Menu/chapter_select_base.png"
        hover "Menu/chapter_select_hover.png"

        # we need to make the screen update when the arrows are clicked
        hotspot (1221, 215, 30, 146) action BonusPagePrevious()
        hotspot (1221, 724, 30, 146) action BonusPageNext()
        hotspot (726, 59, 137, 44) action [ Hide('chapter_select'), Show('save', transition=dissolve) ]
        hotspot (948, 926, 107, 23) action [ Hide('chapter_select'), Show('bonus', transition=dissolve) ]
        hotspot (864, 59, 137, 44) action [ Hide('chapter_select'), Show('load', transition=dissolve) ]
        hotspot (1002, 59, 137, 44) action [ Hide('chapter_select'), Show('preferences', transition=dissolve) ]
        hotspot (1140, 59, 137, 44) action [ Hide('chapter_select'), Show('main_menu', transition=dissolve) ]

        #style "file_picker_frame"

        $ columns = 1
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            #style_group "file_picker"
            xpos 753
            ypos 216

            if hasattr(store,'BM'):
                $BM.phase = 'Player' # This is done to make sure that we can open the menu while in a bonus

            # Display five file slots, numbered 1 - 5.
            for i in range(1, columns * rows + 1):

                button:

                    xminimum 460
                    yminimum 130
                    background None #Solid(0,0,0,255)

                    has hbox
                    
                    $chaptercount = bonusPage*columns*rows + i -1

                    # Add the image and text.
                    if bonusPage * columns * rows + i - 1 < len(chapters):
                        imagebutton:
                            idle (chapters[chaptercount].image)
                            hover hoverglow(chapters[chaptercount].image)
                            at zoom_button(chapters[chaptercount].zoom)
                            action [Hide('main_menu'),chapters[chaptercount]]
                        text chapters[chaptercount].text
                    else:
                        text str(bonusPage * columns * rows + i) + ". Unwritten Chapter"

init -1 python:
    # needs to be here or else renpy won't recognize the list
    addon_scenes = []

screen mod_scenes:

    modal True
    zorder 200
    
    imagemap:
        ground "Menu/mod_scenes_base.png"
        hover "Menu/mod_scenes_hover.png"

        # we need to make the screen update when the arrows are clicked
        hotspot (1221, 215, 30, 146) action BonusPagePrevious()
        hotspot (1221, 724, 30, 146) action BonusPageNext()
        hotspot (726, 59, 137, 44) action [ Hide('mod_scenes'), Show('save', transition=dissolve) ]
        hotspot (948, 926, 107, 23) action [ Hide('mod_scenes'), Show('bonus', transition=dissolve) ]
        hotspot (864, 59, 137, 44) action [ Hide('mod_scenes'), Show('load', transition=dissolve) ]
        hotspot (1002, 59, 137, 44) action [ Hide('mod_scenes'), Show('preferences', transition=dissolve) ]
        hotspot (1140, 59, 137, 44) action [ Hide('mod_scenes'), Show('main_menu', transition=dissolve) ]

        #style "file_picker_frame"

        $ columns = 1
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            #style_group "file_picker"
            xpos 753
            ypos 216

            if hasattr(store,"BM"):
                $BM.phase = 'Player' # This is done to make sure that we can open the menu while in a bonus

            # Display five file slots, numbered 1 - 5.
            for i in range(1, columns * rows + 1):

                button:

                    xminimum 460
                    yminimum 130
                    background None #Solid(0,0,0,255)

                    has hbox

                    # Add the image and text.
                    if bonusPage * columns * rows + i - 1 < len(addon_scenes):
                        $ is_label = renpy.has_label(addon_scenes[i - 1].jumpLoc)
                        imagebutton:
                            idle (addon_scenes[i - 1].image)
                            hover hoverglow(addon_scenes[i - 1].image)
                            at zoom_button(addon_scenes[i - 1].zoom)
                            action If(is_label, true = [Hide('main_menu'),Start(addon_scenes[i - 1].jumpLoc)], false = [Hide('mod_scenes'),ShowMenu(addon_scenes[i - 1].jumpLoc)])
                        $ del is_label
                        text addon_scenes[i - 1].text

                    else:
                        text str(bonusPage * columns * rows + i) + ". No Scene Found"                        