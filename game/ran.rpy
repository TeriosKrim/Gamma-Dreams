label ran:
    $ mc = 'Rai'
    "which part?"
    menu:
        "Part 1":
            jump ran_mon
        "Part 2":
            jump ran_say
        "Part 3":
            jump ran_nat
        "Part 4":
            jump ran_yur
        "Extra":
            jump ran_l

label ran_mon:
    stop music
    scene black
    show text "Short story #1: A short date with monika." with dissolve
    with Pause(2)


    play sound "sfx/giggle.ogg"
    hide text with trueblack
    with pause(1.0)


    $ mc = 'Rai'
    scene bg residential_day
    with dissolve_scene_full
    play music son_jam
    "Wait"
    "What was I doing again?"
    $ m_name = "???"
    m "Hey [mc]"
    "I heard a voice so I turned around and saw Monika."
    show monika base casual ma at t11 zorder 1
    $ m_name = "Monika"
    mc "Hey Monika what's going on?"
    m "Not much sorry I'm late, so you ready for our date?"
    mc "Date?"
    "The hell she on about I don't remember me planning for a date."
    show monika lean casual mc
    m "~Ehehe Yes silly the date we planned don't tell me you forgot about it? "
    mc "Hmmm"
    show monika lean casual md b3
    m "Is there something wrong?"
    mc "This got to be a dream."
    mc "Welp time to wake up."
    "I took my hand out and extent my arm out far an-"
    stop music
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    scene black
    "Slapped myself so hard that I died."

    jump ran_say

label ran_say:
    scene black
    show text "Short story #2: Hungry, hungry Sayori." with dissolve
    with Pause(2)


    play sound "sfx/giggle.ogg"
    hide text with trueblack
    with pause(1.0)

    scene bg club_day
    with dissolve_scene_full
    play music t5

    "Hold up"
    "I could had sworn I-"
    $ s_name = "???"
    s "Unnn"
    "I heard a noise it was coming from the closet."
    mc "The hell?"
    "Confused but yet worried I went in front of the closet."
    scene bg closet
    with wipeleft
    "As I stand in front of the closet I saw Sayori in the closet on the floor in a fetal position."
    mc "Yo Sayori...are you ok or?"
    show sayori base shoc at t11 zorder 1
    "She looked at me with shock then pull me in the closet and close the closet door."
    stop music
    play sound "mod_assets/closet_close.ogg"
    show dark zorder 100
    with wipeleft
    show sayori base ma eyes_u
    $ s_name = "Sayori"
    s "Oh [mc] thank goodness you're here."
    mc "Sayori you look terrible, is everything alright?"
    show sayori base ma eyes_u
    s "No [mc] everything is not alright."
    s "I've been so very hungry."
    mc "Then go eat then and why we inside of the closet?"
    s "You don't understand [mc]."
    show sayori base ml eyes_u b1b
    s "No matter how much I eat I still remain hungry. "
    s "IT'S LIKE MY STOMACH IS A VOID, UNABLE TO BE SATISFIED!"
    show sayori base rup mouth_c eyes_u b1b
    s "I'M LOSING MY FUCKING MIND [mc]!"
    "I never saw her like this before."
    "It must be really serious."
    mc "Sayo-{nw}"
    "Before I finished saying her name I step in something like a liquid."
    "Using the light from the bottom of the door I saw that it was blood."
    "Blood?"
    "As I look to my left I saw a body just lying there."
    mc "Sayori what the fuck is that?"
    "I pointed to the body next to Sayori."
    play music hb
    show layer master at heartbeat
    show sayori base lup rup mouth_c eu b1a
    s "You don't need to worry about that [mc]."
    s "Soon you'll be inside me forever."
    "Please let it be a sexual innuendo."
    "Please let it be a sexual innuendo."
    "..."
    "Judging by her face it wasn't unfortunately."
    "As I gotten a closer look to the body it looked like Monika."
    "But half of her face was gone."
    "..."
    mc "Fuck that shit I'm outta here."
    "I turned around and grab the doorknob to open the closet door."
    play sound "mod_assets/lock door.mp3"
    pause 3.0
    "But it was locked from the inside."
    mc "Ain't no way the door's locked."
    play sound "mod_assets/door banging.mp3"
    pause 1.0
    mc "HELP SOMEONE HELP ME!"
    "As I turned back around Sayori stood so close to me."
    show sayori base lup mf ed b1b at face
    s "It's ok [mc]"
    s "It's just us two alone"
    "Wait maybe this might sexual after all."
    pause 4.0 
    show sayori base lup mouth_r e3a at face
    pause 0.1
    stop music
    scene black
    hide dark
    play sound "mod_assets/male scream.mp3"
    pause 6.1
    play sound "mod_assets/b_splat.mp3"
    pause 1.0
    
    jump ran_nat

label ran_nat:
    scene black
    show text "Short story #3: Playing games with Natsuki." with dissolve
    with Pause(2)

    play sound "sfx/giggle.ogg"
    hide text with trueblack
    with pause(1.0)
    scene bg bedroom
    with dissolve_scene_full
    mc "HOLY SHIT!"
    mc "..."
    "I woke up from my bed, my heart is beating faster than I beat my meat."
    "..."
    "Wait that didn't sound right..."
    "I meant like...wait."
    "Who am I trying to explain this to?"
    $ n_name = "???"
    n "Why are you yelling?"
    n "I can hear you all the way in the kitchen."
    "I turned my head toward the door and saw Natsuki coming in."
    "She has two plates fill with food."
    play music t6
    show natsuki base casual ldown ma at t11 zorder 1
    mc "Oh Natsuki thank goodness it's you."
    mc "I had the craziest dream, you wouldn't even believe it even if I told you."
    show natsuki base casual ldown rhip mc b1b
    $ n_name = "Natsuki"
    n "Geez [mc] I was only down in the kitchen for like 20 minutes."
    n "Making dinner for us and you fell asleep."
    show natsuki cross casual mc e4a b2a
    n "Typical [mc]~"
    mc "No seriously I had the craziest dream it was so weird."
    show natsuki cross casual ma e1a b2a
    mc "It started with Monika wanted to date me."
    mc "Which I knew was bullshit Monika wouldn't never be interested in me."
    show natsuki cross casual me e1a b2a
    mc "Then Sayori ate me whole."
    show natsuki base casual rhip mh b1f
    n "She ate you whole?"
    mc "YEAH!"
    show natsuki base casual lhip rhip mouth_i eyes_o b3b
    n "You're gross [mc]"
    "I looked at Natsuki confused as hell"
    mc "What do you mean?"
    n "I know that phrase is a sexual innuendo."
    mc "But the thing was it wasn't though."
    "Even though I wish it was"
    "But don't tell Natsuki that."
    mc "She literally ate me like a cannibal on crack."
    mc "It was a nightmare"
    show natsuki base casual rhip mouth_g e1a b1b
    "Natsuki looked concerned about me."
    "That's so adorable"
    mc "A-hem"
    mc "Anyway how about we eat?"
    show natsuki base casual mouth_g eyes_c b1c
    n "Oh yeah sure"
    "She handed me my plate, we both sat down on my bed and we started to eat our food."
    scene bg bedroom
    with wipeleft_scene
    "We got done with our food and decided to play a game for a bit."
    "We was playing Mortal Kombat Deception."
    "With both of us tied up 3-3"
    mc "I guess who ever win this one will win the match let's se-"
    show natsuki base casual lhip rhip n1 mc eyes_o b3b at t11 zorder 1
    n "Not so fast [mc]."
    n "Let's play a different game to break the tiebreaker."
    mc "Okay...what do you have in mind?"
    "Natsuki stood up from my bed and turn to face me."
    n "I know a game that I know I can beat you in."
    mc "Well someone's confident."
    mc "What is it?"
    show natsuki base casual lhip rhip n1 mc e1a b3b
    n "let's play punchys"
    mc "Punchys?"
    "I looked so confused of why she wanted to play punchys knowing the fact I'm bigger and stronger than her."
    mc "I'm not trying to get a aggravated assault charged Natsuki..."
    n "Oh relax [mc] I've been working out recently."
    n "My trainer been really on me this past 6 months."
    show natsuki base casual lhip rdown n1 mc e1d b2b
    n "Unless you're scared~"
    mc "Yeah scared of going to jail."
    "That and I really didn't want to hurt her."
    n "Look I can take it stop being a baby and punch my arm hard as possible."
    mc "Look Natsuki I really don- {nw}"
    show natsuki base casual ldown n1 mi e1a b3b at h11 zorder 1
    n "Just do it already [mc]."
    show natsuki base casual ldown n1 mi e1a b3b at t11 zorder 1
    "I know her she won't stop asking until I do it."
    mc "Sigh"
    mc "Fine you better not regret it later."
    show natsuki base casual ldown n1 mouth_c e1a b1c
    n "I'm not, so just do it already."
    n "{cps=5}Hit{nw}{cps=5}"
    n "{cps=5}Me{nw}{cps=5}"
    n "{cps=5}As{nw}{cps=5}"
    n "{cps=5}Hard{nw}{cps=5}"
    n "{cps=5}As{nw}{cps=5}"
    n "{cps=5}You{nw}{cps=5}"
    n "{cps=5}Can{nw}{cps=5}"
    "..."
    "I really don't like where this is going but I guess I have no choice."
    "I stood up, pull back my right arm back and ball my hand into a fist."
    "With fast speed and go toward her right arm and swung."
    stop music
    play sound "mod_assets/weak_punch.mp3"
    "..."
    show natsuki base casual ldown n1 mouth_h eyes_d b3b
    n "Hey I said hard as you can [mc]."
    mc "But I did though"
    n "Try again [mc]"
    "I tried again"
    queue sound "mod_assets/weak_punch.mp3"
    queue sound "mod_assets/weak_punch.mp3"
    queue sound "mod_assets/weak_punch.mp3"
    pause 1.5
    mc "Did you feel that?"
    n "No I did't felt anything, are you sure you hitting me hard."
    mc "YES I'M PRETTY SURE I AM NATSUKI!"
    mc "I know my own strength."
    "At least I thought I did..."
    show natsuki base casual lhip n1 mouth_c eyes_p b1b
    n "Man you are weak [mc]."
    "Ain't no way she's that strong."
    "How much training did she do."
    show natsuki base casual lhip n1 mouth_c e1a b1b
    n "Well it's my turn."
    "I had a bad feeling in my stomach."
    "But I'm pretty sure she not that strong."
    "...."
    "Right?"
    show natsuki base casual ldown rdown n1 mouth_c e1a b1a
    n "Ready [mc]?"
    mc "Yeah I gues-{nw}"
    show natsuki base casual ldown rdown n1 mouth_c e1a b1a at face
    scene black
    play sound "mod_assets/strong_punch.mp3"
    pause 1.0
    play sound "mod_assets/glass_brake.mp3"
    pause 1.5
    play sound "mod_assets/body_thud.mp3"
    pause 1.0
    n "Oh shit I think I punched too hard..."
    jump ran_yur

  



    # with Shake((0.5, 1.0, 0.5, 1.0), 4.0, dist=5) 
    
    
label ran_yur:
    scene black
    show text "Short story #4: Yuri's unstable love explosion." with dissolve
    with Pause(2)

    play sound "sfx/giggle.ogg"
    hide text with trueblack
    with pause(1.0)

    "..."
    "...."
    mc "Unnn..."
    mc "What the-"
    mc "Where am I?"
    mc "I can't move"
    "My body was in restraints as if someone tie me up to a chair or something."
    mc "Unn"
    $ y_name = "???"
    y "You're finally awake my love."
    y "I've been waiting for you to wake up."
    "That voice I recognized it."
    mc "..Yuri?"
    mc "Where are you I can't see."
    $ y_name = "Yuri"
    y "Oh I forgot I put a blindfold on you let me get that off."
    scene bg office_night_loff at t11
    with open_eyes
    show yuri base casual rup lup mouth_c eyes_i b1a at t11 zorder 1
    mc "Yuri what the fuck man."
    mc "Why am I tie up to a chair and where the hell are we?"
    y "You don't need to worry about that [mc]."
    y "Now I have you all to myself."
    show yuri base casual rup lup mc em b1a
    y "How long I waited this moment."
    "Yuri got close and sat on my lap."
    show yuri base casual rup lup mb e2d b1a at face
    y "Now We'll be together forever!"
    "..."
    "I felt really uncomfortable."
    "Now I know for a fact someone or something is fucking with me."
    "First Monika wanted to date me."
    "Next Sayori ate me."
    "Then Natsuki somehow punched me so hard that I died."
    "Now this..."
    "I'm definitely in hell..."
    "..."
    "Wait maybe I can still convince Yuri that is not right."
    "..."
    "Probably"
    "Well it's worth a shot."
    mc "Yuri you know this isn't right."
    show yuri base casual rup lup me e2d b1a
    mc "You can't just kidnap someone because you like them."
    mc "Both parties have to feel the same you know."
    mc "Plus we have like family and friends that's probably worried sick about us."
    mc "People who love you and care for you as much as I do."
    show yuri base casual rdown lup me eyes_b b1b
    "Yuri thought to herself for a bit."
    y "Do you really love me [mc]?"
    mc "Yes Yuri I do"
    "As a friend"
    mc "Please untie me so we can talk?"
    show yuri base casual rdown ldown me e4a
    y "I'm sorry [mc] I can't do that."
    mc "But why not."
    "Yuri sighed and got off of me."
    show yuri base casual rdown ldown me e1c at t11 zorder 1
    "Good thing too because for some reason I got aroused."
    play music t10
    y "The thing is I knew I wasn't the only one who cared for you."
    y "I know Monika, Sayori, and Natsuki loves you as well."
    y "Probably as much as I do"
    show yuri base casual rup ldown me e1a b2b
    y "But I didn't want me or the other girls to get lefted out."
    show yuri base casual rup ldown mb e1a b1a
    y "But luckily I already planned this out."
    mc "What do you mean by that?"
    show yuri base casual rdown ldown ma e4b b1a
    "Yuri giggles"
    "Which makes me nervous for some reason."
    show yuri base casual rdown ldown mc e2a b1a
    y "I planted bomb all over the city so we all can be one with each other."
    stop music
    "..."
    "She joking right?"
    "Please tell me she's joking."
    mc "Yuri this isn't the time for jokes right now."
    show yuri base casual rup lup mo e3a b1a
    y "It's no joke [mc] look"
    "She pointed to the right signaling me to turn my head to see a timer that shows less than five second."
    "..."
    mc "Yuri..."
    play sound "mod_assets/wtf.mp3"
    pause 1.2
    scene black
    $ renpy.movie_cutscene("mod_assets/Spongebob Explosion clip.webm")
    pause 3.0
    show monika base uniform rhip md e1d b1e at t11 zorder 1
    $ t_name = "Terios"
    m "..."
    show monika base uniform rhip mi e1d b1e
    m "Hey [t_name] don't you think my story was a little short.."
    m "More shorter than the rest of the girls?"
    t "Yeah probably but who cares Monika."
    t "I mean like I'm still getting used to this whole coding thing soo"
    m "No excuse"
    show monika base uniform rhip mj e1d b1e
    t "Sigh fine look how about we talk about this later ok?"
    t "I don't want people in our business."
    m "..."
    t "Look maybe in the next one I'll give you more screen time okay?"
    t "I just need to get used of things."
    m "..."
    show monika base uniform rhip mouth_b e1d b1e
    m "Okay but you owe me [t_name]."
    t "Ok ok now go away"
    hide monika
    t "Thanks for watching everyone!"
    return

label ran_l:
    scene bg closet
    with dissolve_scene_full
    show sayori turned mq e0b b1b at t11 zorder 1
    s "Even though I ate both of them why am I still hungry?"
    show sayori turned mq e0b b1b sobbing
    s "I'm sorry..."
    s "I'm so sorry...."
    show sayori turned md e0b b1b sobbing
    "Sayori look back at the two lifeless bodies of Monika and [mc] before leaving the closet door."
    scene bg club_day
    with wipeleft_scene
    show sayori turned mq e4e b1b eyebags at t11 zorder 1
    s "I-I'm a monster...that doesn't deserve to live..."
    $ l_name = "????"
    show sayori turned md e4e b1b eyebags at t11 zorder 1
    l "Well you're right about one thing "
    extend "{sc}{b}{font=gui/font/pmttyd.otf}{color=#ff0000} you don't deserve to exist{/b}{/color}{/sc}."
    l "HehEhEHe~"
    window hide(dissolve)
    show sayori turned md e3b b1b eyebags at h11 zorder 1
    pause 1.0
    show sayori turned md e3c b1b eyebags at t11 zorder 1
    pause 1.0
    show sayori turned mq e3a b1b eyebags at t11 zorder 1
    s "Who said that?"
    show sayori turned md e3a b1b eyebags
    l "No need to worry about my identity since you'll cease to exist anyway."
    l "{sc}{b}{font=gui/font/pmttyd.otf}{color=#ff0000}Begone insect{/b}{/color}{/sc}"
    show screen console_screen
    $ run_input("os.remove(\"DDLC_videoscript/DDLC_short/Sayori.chr\")", "file deleted.")
    $ pause(1.0)
    hide sayori
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.9
    hide screen tear
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.9
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch2.ogg"
    pause 0.9
    show libitina shadow at t11 zorder 1
    hide screen console_screen
    hide screen tear
    play music unknown
    l "HehEhEHe~"
    l "{bt=h10-s0.5-p5.0}How enjoyable~{/bt}"
    l "But knowing \"she\" having admin access as well I may need help from someone outside of the game."
    show libitina shadow at t22 zorder 1
    $ run_input("os.search(\"(C:)/games\")", "1 folder found with \"games\" tag.")
    $ pause(1.0)
    l "Oh a folder called visual novel games?"
    l "{bt=h2-s0.5-p7.0}HehEhEHe~{/bt}"
    show libitina shadow2
    l "I wonder what's in here~"
    show libitina shadow
    $ run_input("os.search(\"(C:)/visual novel games\")", "3 folder found.")
    $ pause(1.0)
    l "Well I see DDLC of course.."
    l "But wait theses two I'm not familar with."
    l "Totono?"
    l "Gamma dreams?"
    l "Hmm the Gamma dreams one seem like a demo."
    l "But the totono one is not"
    l "Interesting~"
    l "My beloved has a lot of \"saves\" here."
    l "I guess I'll see what this game is all about~"
    $ run_input("os.open(\"(C:)/visual novel games/totono/100 percent complete\")", "Opening...")
    $ pause(1.0)
    show vortex
    with dissolve
    show libitina shadow2
    l "{bt=h1-s0.5-p5.0}Maybe I can find someone like me here~{/bt}"
    hide screen console_screen
    show libitina shadow at t11 zorder 1
    pause 1.0
    hide libitina
    with flashbulb
    hide vortex
    with dissolve
    return



