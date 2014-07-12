init -1 python:

    bonusPage = 0
    
    doki_doki_space_whale = BonusItem("Background/renpytomback.jpg", " Doki Doki Space Whale:\n Dating Sim 3", "deleted_scene_1")

    scenes = [doki_doki_space_whale]

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
                            at zoom_button(0.09)
                            action [Hide('main_menu'),Start(scenes[i - 1].jumpLoc)]
                        text scenes[i - 1].text

                    else:
                        text str(bonusPage * columns * rows + i) + ". Deleted Scene"

init -1 python:

    chapter0 = Chapter("CG/cera.jpg", " Prologue", "start")
    chapter1 = Chapter("Background/captainsoffice.jpg", " Chapter 1", "chap1_start", 200, 1)
    chapter2 = Chapter("Background/captainsoffice.jpg", " Chapter 2", "chap2_start", 4570, 5)
    chapter3 = Chapter("CG/avateatime.jpg", " Chapter 3", "ep3_start", 11870, 8)
    chapter4 = Chapter("CG/asagakidnap_legion.jpg", " Chapter 4", "chap4_start", 15710, 10)

    chapters = [chapter0, chapter1, chapter2, chapter3, chapter4]

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

                    # Add the image and text.
                    if bonusPage * columns * rows + i - 1 < len(chapters):
                        imagebutton:
                            idle (chapters[i - 1].image)
                            hover hoverglow(chapters[i - 1].image)
                            at zoom_button(0.09)
                            action [Hide('main_menu'),chapters[i - 1]]
                        text chapters[i - 1].text

                    else:
                        text str(bonusPage * columns * rows + i) + ". Unwritten Chapter"