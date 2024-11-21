default no_mon = False

label play:
    $ mc = 'Rai'
    stop music fadeout 2.0

    # call test

    scene bg residential_day
    with dissolve_scene_full

    
    mc "Seem like a nice day today."

    scene bg clear_sky_day
    with dissolve

    mc "With no clouds in the sky must be my lucky day."

    scene bg residential_day
    with dissolve
    
    mc "Ok I'm ready!"

    "Ahem"


    

    play music son_jam

    'Today is a beautiful saturday.'
    "It's been only four days since I joined the literature Club."
    "I stepped outside to go see Monika."
    "Apparently she wanted to see me about something."
    "She said it was urgent."
    "On a saturday though."
    "I gave a big sigh before seeing Sayori walking out of her door."
    "She looked at me with the biggest smile waving at me before coming up to me."

    show sayori base casual neut lup rup mb ce at t11 zorder 1

    $ s_name = "Sayori"

    s "Hey [mc]!"
    
    mc "What's up Sayori where are you going?"

    show sayori base casual happy mouth_c

    s  "I have to run some errands."

    s "Running low on my snacks."

    mc "Oh Sayori.."

    show sayori base casual ldown rdown ml ei at h11 zorder 1

    "I gently pat her head"

    mc "You know eating junk food is not good for you."

    show sayori base casual rup mouth_i eyes_a brow_e at t11 zorder 1

    s "Like you're the one to talk."

    s "Mister {b}KING OF ALL JUNK FOOD{b}!"

    mc "Point taken.."

    show sayori base casual mb ep b1a at t11 zorder 1

    "We both laughed a little."

    show sayori base casual rdown mouth_b eyes_a brow_a

    s "So what about you, where are you going?"
    
    mc "Well Monika wanted to see me today."

    mc "Apparently it's urgent."

    show sayori base casual rup mi b1f

    s "Huh on a saturday?"

    mc "That's what I said!"

    mc "Anyway I plan to see her at school."

    show sayori base casual ldown rdown me b1a
    
    mc "Since I have nothing better to do why not right?"

    show sayori base casual mi b1a

    s "I suppose.."

    show sayori base casual ldown rdown mi b1b

    s  "Just be careful [mc].."

    show sayori base casual me b1b

    mc "Sayori..."

    mc "You know I'm the most cautious person you know."

    show sayori base casual doub closed_mouth

    mc "You remember I was hesitant about joining the literature club."

    mc "{nw}Because you wa-{nw}"

    show sayori base casual angry rup mb closed_eyes b1c
    
    s "Okay, okay, geez."

    s "But I also know how you can get."

    s "Anyway Monika is waiting for you, don't keep her waiting."

    show sayori base casual lup rup mb eyes_p b1a

    s "I'll see you later [mc]."

    "Sayori then turned me around and pushed me forward."

    hide sayori
    with dissolve

    mc "{b}Okay I'll text you if anything goes wrong{b}!"

    s "{b}Okay{b}!"

    "I waved to her as I run toward the direction of the school."

    stop music fadeout 2.0

    scene black 
    with dissolve_scene_full

    scene bg club_day
    with wipeleft_scene

    play music t5

    "As I arrived to the club room I saw Monika was sitting on the desk."

    "She was waiting for my arrival."

    "As she turned her head to me."

    "She stood up and walked toward me until she got close."

    $ m_name = "Monika"

    show monika base casual mouth_b  at t11 zorder 1

    m "Hey there [mc]"

    mc "Sorry I'm late Monika I ran into Sayori."

    mc "So what's the urgency?"

    show monika base casual rhip mouth_b ej brow_i

    m "Ah yeah sorry for calling you on a saturday but there's something I needed to ask you."

    mc "Okay?"

    mc "What is it?"

    show monika base casual unease mb

    m "Well I kinda need a favor."

    mc "A favor?"

    "Monika needs a favor from me?"

    "I would what it could be?"

    "Must be important since she brought me out here."

    "On a saturday"

    "But I thought to myself is it really important?"

    "Not saying I have things to do on saturday."

    "But I really don't want to be at school."

    "Let alone on a saturday."

    "I think to myself of what to say next."

   
label me:
    show monika base casual mouth_b e2b b2c
    menu:
        
        "So what's the favor?":
            show monika lean casual happ m3

            m "I knew I can count on you [mc]~."

            "Monika seems happy"

            "I mean plus I'm not really doing anything at the moment anyway."

            "I just hope it's not something that required me to lift an heavy object."
            jump her

        "You can't wait until monday?" if not no_mon:
            $ no_mon = True
            show monika base casual md e1d b1e
            m '...'
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.5
            hide screen tear
            jump me

        "Is that Natsuki?":
            "I see Natsuki in the closet reading one of her mangas"

            "While eating a protein bar, I wonder why she's here on a saturday."

            "As I said that Monika looked back and saw Natsuki as well."

            show monika base casual neut ldown rdown closed_mouth e2a brow
label her:

    show monika base casual neut awkw ldown rdown mb e4b brow_b

    m "So I wanted introduce you to someone."

    m "She's a foreign exchange student."

    mc "Wait that's it?"

    show monika base casual neut ldown rhip mb ea brow_b

    m "Yeah I guess she heard about the literature club and wanted to see the club."

    m "I guess you can say I'm a bit nervous."

    mc "You? nervous?"

    m "Well even I get nervous [mc]."

    mc "It doesn't seem like it tho Monika."

    show monika base casual neut lpoint rdown mb ep brow_a

    m "Remember what we talked about having \"Fake confidences\"."

    mc "Oh yeah I think I remember that"

    "I actually don't remember..."

    mc "Anyway what does she look like?"

    mc "What does she do?"

    mc "Come on Monika details."

    show monika base casual neut ldown rdown ma ea brow_a

    m "You'll find out soon enough she's actually on her way here."

    mc "Ah ok gotcha."

    mc "{nw}So whe-{nw}"

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    hide monika
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    play music t4g
    $ m_name = glitchtext(25)
    show vignette:
        alpha 3
    show noise:
        alpha 3
    play sound("sfx/glitch2.ogg")

    $ style.say_window = style.window_monika
    $ style.say_dialogue = style.edited
    $ gtext = glitchtext(19)
    
    "[gtext]"
    "[gtext]"
    "[gtext]"
    # show miyuki 4a at face(y=600)
    mi 'Love is eternal...'
    mi 4f 'Remember?'
    scene black
    with trueblack

            









    return