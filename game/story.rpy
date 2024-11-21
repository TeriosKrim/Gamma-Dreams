
label story_menu:
    show mask_2
    # show mask_3
    stop music fadeout 2.0
    $ style.say_dialogue = style.normal
    
    "Which story do you wish to view?"
    

    menu:
        # "Aftermath?":
        #     call after_part

        # "Her?":
        #     call play

        # "Short stories?":
        #         call ran

        # "Monika AI?":
        #     call  ai_part
            
        # "{glitch_ran}":
        #     show screen tear (20, 0.1, 0.1, 0, 40)
        #     play sound "sfx/s_kill_glitch1.ogg"
        #     pause 0.50
        #     hide screen tear
        #     call act3

        "Test":
            call test

        # "Sayori Ai?":
        #     call sayori_ai

        "Debug":
            call d_bug

        # "Origin":
        #     call lib_origin

        "Yuri Ai?":
            call yuri_ai
        "project l13":
            call l13_log

        "Origin pt 2":
            call froze

   