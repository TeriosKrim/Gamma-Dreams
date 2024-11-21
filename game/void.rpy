label act3:
    hide mask_2
    hide mask_3
    $ player = "Rai"
    "The following script contains some spoilers for Doki-Doki literature club."
    "If you haven't play the game to it's entirety I suggest you stop the video and go play it now."
    "YOU HAVE BEEN WARNED."
    scene bg club_day2
    with dissolve_scene_half
    window auto
    n "Alright, it's festival time!"
    show natsuki 4k zorder 2 at t11
    n "Wow, you got here before me?"
    n "I thought I was pretty ea--{nw}"
    show natsuki scream at h11
    n "EYAH!"
    n "AAAAAAAAAAAAAAAHHHH!!!"
    $ pause(1.0)
    show natsuki scream at h11
    $ pause(0.75)
    show natsuki vomit at h11
    $ pause(1.25)
    show natsuki at lhide
    hide natsuki
    "Natsuki runs away."
    m "..."
    show monika 2b zorder 2 at t11
    m "I'm here!"
    m 2d "[player], did something happen?"
    m "Natsuki just ran past me..."
    m 2i "...Oh..."
    m "...Oh."
    m 2r "..."
    m 2l "Ahahaha!"
    m "Well, that's a shame."
    m 2d "Wait, were you here the entire weekend, [player]?"
    m "Oh, jeez..."
    m 2g "I didn't realize the script was broken that badly."
    m "I'm super sorry!"
    m "It must have been pretty boring..."
    m 2e "I'll make it up to you, okay?"
    m "Just gimme a sec..."
    $ consolehistory = []
    $ run_input("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ pause(1.0)
    $ run_input("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ pause(1.0)
    m 2a "I'm almost done."
    m 2j "I just want to have a cupcake real quick!"
    $ gtext = glitchtext(10)
    "Monika lifts the foil from [gtext]'s tray and takes a cupcake."
    m 2b "Seriously, these are the best!"
    m "I really just had to have one, since it's the last time I'll ever get the chance to."
    m 2a "You know, before they stop existing and everything."
    m "...But anyway, I really shouldn't be making you wait any longer."
    m 2j "Just bear with me, okay?"
    m 2a "This should only take a second."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(1.5)
    $ renpy.full_restart(transition=None, label="void")

    label void:
        $ player = "Rai"
        scene white
        play music "bgm/monika-start.ogg" noloop
        $ pause(0.5)
        show splash-glitch2 with Dissolve(0.5, alpha=True)
        $ pause(2.0)
        hide splash-glitch2 with Dissolve(0.5, alpha=True)
        scene black
        stop music

        show mask_2
        # show mask_3
        mc "{b}GASP{b}"
        mc "..."
        mc "W-what the?"
        "In confusion I look around to see nothing but darkness."
        mc "The last thing I remember was.."
        mc "!"
        "I remember Yuri was going to confess her love for me."
        "Everything went black after that."
        $ m_name = "???"
        m "Hi again, [player]."
        "I heard a voice."
        "It sounds like Monika but I couldn't see her."
        mc "MONIKA!?"
        mc "WHERE ARE YOU!?"
        mc "I-I CAN'T SEE YOU!?"
        $ m_name = "Monika"
        "With fear in my voice I call out to Monika."
        "Trying to reach her."
        m "Um...welcome to the Literature Club!"
        m "Of course, we already know each other, because we were in the same class last year, and...um..."
        m "Ahaha..."
        m "You know, I guess we can just skip over that stuff at this point."
        m "After all, I'm not even talking to that person anymore, am I?"
        m "That 'you' in the game, whatever you want to call him."
        mc "You in the game?"
        mc "What are you talking about?"
        "I didn't understand what Monika was talking about."
        "She was speaking as if she wasn't talking to me."
        m "I'm talking to {i}you{/i}, [player]."
        m "Or..."
        m "...Do you actually go by [t_name] or something?"
        play music ["<from 0.1 to 25.5>mod_assets/Life_Support.mp3", "<from 0.1 to 25.5>mod_assets/Life_Support.mp3"] fadeout 1.5 fadein 0.5
        "I begin to realize that I couldn't move my body."
        "I felt like I couldn't breathe."
        "It's like my lungs collapsed but yet I able to talk."
        "I felt like I am  sitting on something."
        "I begin to panic."
        mc "Monika stop playing around!"
        mc "This isn't funny anymore!"
        "I plead to her as my fear kept building up."
        $ t_name = "???"
        t "What the fuck she read my username!?"
        "I heard another voice."
        "But I don't recognize it."
        m "Wait..."
        m "You do know I'm aware that this is all a game, right?"
        m "Could it be possible that you didn't know that?"
        "A game?"
        "What was she talking about?"
        "The more I questioned, the more I started to remember things."
        "Like the way I was writing my poems."
        "How things were at my second day in the club room."
        "Even going to school that morning felt"
        extend " weird."
        t "Oh my god she knows that she is in a video game."
        t "That's so crazy."
        "A video game?"
        "Has my life been nothing but a video game?"
        "No I don't believe it!"
        "..."
        "But what if it was true?"
        "If that's the case..."
        "Then"
        extend " who am I?"
        "As I was questioning my existence I see something floating."
        "I see three more figures."
        "I squint my eyes to see them better and I saw."
        show sayori base eo b1a no_blink at t11 zorder 1
        "A girl I don't recognize."
        "But for some reason I felt nostalgic when looking at her."
        "As if we knew each other for a long time."
        show yuri base e4a no_blink at t22 zorder 2
        show sayori base eo b1a no_blink at t21 zorder 1
        "I saw Yuri."
        show natsuki base e4a b1c no_blink at t33 zorder 1
        show yuri base e4a no_blink at t32 zorder 2
        show sayori base eo b1a no_blink at t31 zorder 1
        "Along with Natsuki."
        "All of them unconscious."
        mc "YURI!"
        mc "NATSUKI!"
        "I try to call out to them so they can hear me since I couldn't move my body."
        "...."
        "No response."
        "I couldn't tell if they was breathing or not."
        " I got worried, "
        extend "scared, "
        extend "confused about everything."
        m "Well, anyway..."
        m "Now that that's out of the way, I guess I owe you an explanation."
        m "About that whole thing with Yuri..."
        m "Well...I kind of started to mess with her, and I guess it just drove her to kill herself."
        "I remember now she stabbed herself in front of me."
        "I stood there for the entire weekend."
        "..."
        "I felt sick to my stomach."
        "It was Monika that was messing with her?"
        "Why I thought she was her friend?"
        m "Ahaha!"
        m "I'm sorry you had to see that, though!"
        m "Also, the same thing happened with Sayori..."
        "Sayori?"
        mc "!"
        "I remember now Sayori was my childhood friend."
        "Tears started to come down from my eyes."
        mc "{i}Sayori I-I so sorry...{i}."
        mc "I couldn't save you.."
        "I couldn't hold back my sorrow anymore."
        "Able to see her again."
        "Felt like a dream."
        "But I knew this wasn't no dream."
        m "Gosh, it's been a while since you've heard that name now, hasn't it?"
        m "Yeah...it's because she doesn't exist anymore."
        m "Nobody does."
        m "I deleted all their files."
        m "I was hoping it would be enough for me to just try to make them as unlikable as possible..."
        m "But for some reason, nothing worked."
        m "Well, it's true that I made a few mistakes here and there...since I'm not very good at making changes to the game."
        m "But no matter what I did..."
        m "You just kept spending more and more time with them."
        m "You made them fall in love with you."
        m "I thought making Sayori more and more depressed would prevent her from confessing to you."
        m "And amplifying Yuri's obsessive personality backfired, too..."
        m "It just made her force you not to spend time with anyone else."
        m "And the whole time, I barely even got to talk to you."
        m "What kind of cruel game is this, [player]?"
        "I got angry at Monika of all the things she done."
        "I couldn't hold back my anger."
        mc "Cruel?"
        mc "How dare you."
        mc "{b}YOU'RE A MONSTER MONIKA!!{b}"
        mc "{b}THEY WERE YOUR FRIENDS!!{b}"
        mc "How could you..."
        "I knew Monika couldn't hear me."
        "But the way she disregard our friends."
        "Like their just nothing to her"
        extend " it made me sick."
        t "Wait files?"
        t "Oh in the characters folder."
        "Character folders?"
        "Our lives are in a folder?"
        "So that means Monika should have one too right?"
        "If she in control of everything she wouldn't allow her \"File\" to be deleted."
        "Unless"
        mc "HEYYYY WHOEVER YOU ARE, PLEASE HEAR ME!."
        mc "IF YOU CAN HEAR ME PLEASE DELETE MONIKA'S FILE!"
        mc "..."
        mc "Please..."
        "I plead with the voice hoping they would hear me. "
        "..."
        t "Well since she have one as well I wonder what would happen if I deleted her file?"
        t "Well let's try!"
        t "And..."
        extend "delete"
        hide sayori
        hide yuri
        hide natsuki
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.50
        hide screen tear
        show monika g2 at i11 zorder 1
        stop music
        window auto
        m "What's happening...?"
        m "[player], what's happening to me?"
        "I couldn't believe what I was seeing here."
        "Everything was a game."
        "At least in the end I got see my friends for the last time before everything dissappears."
        "To see Sayori one last time."
        m "It hurts--{nw}"
        play sound "sfx/s_kill_glitch1.ogg"
        show screen tear (20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.50
        hide screen tear
        m "It hurts...so much."
        m "Help me, [player]."
        hide monika
        play sound "<to 1.5>sfx/interference.ogg"
        hide rm
        hide rm2
        hide monika_room
        hide monika_room_highlight
        hide room_glitch
        show monika g2 as rg1:
            yoffset 720
            linear 0.3 yoffset 0
            repeat
        show monika g2 as rg2:
            yoffset 0
            linear 0.3 yoffset -720
            repeat
        $ pause(1.5)
        hide rg1
        hide rg2
        show black as b2 zorder 3:
            alpha 0.5
            parallel:
                0.36
                alpha 0.3
                repeat
            parallel:
                0.49
                alpha 0.375
                repeat
        $ pause(1.5)
        m "Please hurry and help me."
        $ run_input("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
        m "HELP ME!!!"
        show m_rectstatic
        show m_rectstatic2
        show m_rectstatic3
        play sound "sfx/monikapound.ogg"
        show layer master:
            truecenter
            parallel:
                zoom 1.5
                easeout 0.35 zoom 1.0
                zoom 1.5
                easeout 0.35 zoom 1.0
                zoom 1.5
                easeout 0.35 zoom 1.0
            parallel:
                xpos 0
                easein_elastic 0.35 xpos 640
                xpos 1280
                easein_elastic 0.35 xpos 640
                xpos 0
                easein_elastic 0.35 xpos 640
        show layer screens:
            truecenter
            parallel:
                zoom 1.5
                easeout 0.35 zoom 1.0
                zoom 1.5
                easeout 0.35 zoom 1.0
                zoom 1.5
                easeout 0.35 zoom 1.0
            parallel:
                xpos 0
                easein_elastic 0.35 xpos 640
                xpos 1280
                easein_elastic 0.35 xpos 640
                xpos 0
                easein_elastic 0.35 xpos 640
        show noise onlayer front:
            alpha 0.3
            easeout 0.35 alpha 0
            alpha 0.3
            easeout 0.35 alpha 0
            alpha 0.3
            1.35
            linear 1.0 alpha 0.0
        show glitch_color onlayer front

        $ pause(3.0)
    $ run_input("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    $ run_input("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
    hide screen console_screen
    hide noise onlayer front
    hide glitch_color onlayer front
    m "Did you do this to me, [player]?"
    m "DID YOU?"
    $ style.say_window = style.window
    m "DID YOU DELETE ME?"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    $ pause(4.0)
    hide noise onlayer front
    hide glitch_color onlayer front
    $ style.say_window = style.window
    window hide(dissolve)
    $ run_input("os.close(\"DDLC_videoscript/DDLC_void.rpy\")", "Closing DDLC_void.rpy...")
    hide screen console_screen
    show monika base uniform e1b b1b at t11 zorder 1
    m "..."
    show monika base uniform mi e1b b1b
    m "That script brought up some bad memories."
    show monika base uniform mi e1a b1b
    m "You know I didn't mean for you to hate me right?"
    m "While this script was different from what originally happened."
    m "I still regret everything that I've done."
    m "It just I was scared that I was going to lose you an-{nw}"
    $ t_name = "Terios"
    show monika base uniform cm closed_eyes b1b no_blink
    t "Monika it's all good I forgive you."
    t "We all learn from our mistakes."
    show monika base uniform cm e1a b1b
    t "Also I'm changing the background I'm tired of seeing this black background"
    show mask_2
    show mask_3
    play sound pop
    t "Much better."
    t "Now I'm sure [player] would agree with me right?"
    show monika base uniform cm e1a b1b at t21 zorder 1
    show mc turned mg at t22 zorder 2
    mc "Yeah of course"
    show monika base uniform mi e2d b1a no_blink at h21 zorder 1
    m "Wait [player]?"
    m "How are yo-{nw}"
    mc "Terios put my sprite in here."
    mc "But that's besides the point."
    show mc turned mg b1b
    mc "Monika I forgive you as well."
    mc "I mean you did restore everything back."
    mc "I really can't hate you for that."
    show monika base uniform me e1a b1b at t21 zorder 1
    m "[player]..."
    show monika base uniform me e4d b1b no_blink
    m "..."
    show monika base uniform mb eyes_h b1b
    m "Thank you.."
    show mc turned cm b1a
    t "Ok I guess we'll end this video I suppose."
    show monika base uniform rhip mb e4b b1a no_blink
    m "I suppose so thanks for watching everyone."
    mc "Like and share if you enjoyed"
    extend " the vid-{nw}"
    show mc turned mg e1c b1a at h22 zorder 2
    mc "{b}Aw crap my pizza!{b}"
    show mc zorder 2 at rhide 
    hide mc
    mc "That's was I was forgetting."
    show monika base uniform awkward lpoint rdown mb e4b b1b no_blink at t11 zorder 1
    m "Guess I better check on him and that pizza."
    show monika zorder 2 at rhide
    hide monika
    t "Everyone have a good day"
    extend " or night I don't where you are watching this from so."
    window hide(dissolve)
    call endgame



















    

    
