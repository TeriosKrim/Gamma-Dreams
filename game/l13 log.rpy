label l13_log:
    $ mc = "???"
    menu:
        "1-1":
            call l1
        "1-2":
            call l2

label l1:    
    
    scene black
    pause 5.0
    show screen console_screen
    pause 3.0
    $ run_input("open Project_l13_log 1-1", "\"opening....\"")
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    hide screen console_screen
    scene black
    pause 5.0
    $ ma_name = "Women"
    ma "So how is our test subject?"
    play music lab
    
    show bg lab_pod:
        matrixcolor darken_matrix
        matrixcolor sepia_matrix
        truecenter
        zoom 1.0
    show vignette:
        alpha 1.0
    with dissolve_cg


    # show layer master at heartbeat
    
    mn "In combat she does phenomenal as she just eliminated {glitch_ran}"
    mn "But health wise not so good"
    show layer master at heartbeat
    mn "With her newly unlocked powers her body and mind are too unstable"
    extend" and she haven't recovered from that battle either unfortunately."
    ma "I see so another failure huh..."
    extend "well at least this one didn't melt like the rest"
    extend " it's a good thing we went with the embryo method this time around."
    mn "Ma'am with all due respect don't you think this is inhumane?"
    mn "I mean she just a child..."
    ma "You may be new to the team "
    extend "but I don't pay you nor your team for your morals and beliefs, I pay you to create the ultimate weapon."
    ma "Do you know how much governments will pay for this?"
    window hide(dissolve)
    pause 2.0
    ma "Tsk"
    ma "Well with this failure, this will bring my company one step closer to it's goal."
    ma "Anyway get rid of this subject"
    mn "Ma'am if I may...."
    ma "Ugh what now?"
    mn "Instead of the usual method of getting rid of the subjects how about we send her to an orphanage?"
    ma "An orphanage?"
    ma "For what?"
    mn "I mean I would thi-{nw}"
    ma "Enough of your humane shit..."
    ma "...."
    ma "Tsk fine do what you want"
    extend " but this better not come back to bite me or my company in the ass."
    ma "Once your done with that tell your team to resume with the project with the new test subject."
    ma "Understood?"
    mn "Yes...."
    "The woman left"
    mn "Of course..."
    mn "Oh lord forgive me...."
    stop music
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    scene black
    show bg class_day:
        matrixcolor grayscale_matrix
    show vignette:
        alpha 1.0
    l "GASP"
    l "..."
    "I always wake up to that dream..."
    "A dream from my past..."
    "To be dispose of like trash..."
    play music hb
    show layer master at heartbeat
    "I'll make them pay for what they done to me"
    "To make me kill...."
    "To be used and discarded..."
    "To take away my childhood..."
    "To shorten my lifespan...."
    $ style.say_dialogue = style.normal
    "I'll..."
    $ style.say_dialogue = style.edited
    "I'll...."
    $ style.say_dialogue = style.normal
    stop music
    show layer master
    mc "Hey!"
    l "!"
    $ mc = "Rai"
    "I heard familar voice"
    "It's was [mc]..."
    "With no one else in the classroom he just came in the classroom and approached me"
    show mc turned mc e1f at t11
    mc "Why are you sleeping here?"
    mc "Don't you know it's lunchtime?"
    show mc turned mb e1f
    l "Oh..."
    l "No I must of slept through class..."
    show mc turned mg e1c at h11
    mc "WHAT!?"
    show mc turned mg e1c at t11
    mc "You of all people sleeping through class?"
    show mc turned mc e1f
    mc "Ms A+ student Libitina asleep through class hahaha"
    show mc turned mb e1f
    l "H-hey..."
    "For [mc] to catch me sleeping ugh how embarrassing..."
    show mc cross mc
    mc "I'm just joking with ya"
    extend " I know everyone has their days."
    show mc cross mb
    "But yet I didn't mind it with him as being with him puts me at ease for some reason..."
    hide vignette
    with dissolve
    show bg class_day:
        matrixcolor identity_matrix
    with dissolve
    play music son_jam
    show mc cross me e1a at t11
    mc "So are you doing to come to the cafeteria Libitina?"
    show mc cross ma e1a
    l "Oh..no I usually eat here alone"
    "I smiled wryly"
    show mc cross mc e1a
    mc"Well hey I'll join ya"
    show mc cross mb e1a
    "[mc] pulled a chair from the desk above me and turned it and sat down in front of me."
    l "Oh no you don't have to [mc] I don't want to be a bother..."
    show mc turned mc
    mc "Oh no it's fine I actually wanted to talk to you about the latest chapter"
    show mc turned mb
    "Rai and I was reading the same graphic novel book"
    "It's about a mouse that's going through different trials to get his girlfriend back from his arch nemesis"
    "You guess it from another bigger mouse"
    "The newest chapter dropped yesterday"
    l "Yeah I actually read it"
    show mc turned mg e1e
    mc "I swear the amount of plot armor the main character have is just crazy."
    mc "There's no way he should had survived the last trial when he went against that hawk girl."
    show mc turned ma e1e
    l "But you remember he trained in the mountains for 6 months before doing the next trial..."
    l "And his master actually taught him a secret technique to defeat his next trial...."
    show mc cross mg e1e
    mc "I still call bullshit"
    mc "I think the writers got lazy due to the fans pressuring them.."
    show mc cross mc e1a
    mc "I do have to admit the fight scene was so good I can't wait for them to animate that"
    show mc cross mc e1f
    mc "It's going to look sooo good on TV"
    show mc cross mb e1f
    l "Same here hehe"
    "As Rai and I was enjoying our conversation..."
    stop music fadeout 2.0
    $ s_name = "???"
    s "Hey Rai!"
    "We heard a voice and as we both turned our heads a girl with a bow on her head came in the classroom "
    show mc cross mb e1f at t21 zorder 1
    show sayori turned mc:
        matrixcolor grayscale_matrix
        r22()
    s "There you are I was looking for you "
    show mc cross me e1c b1a at h21
    show sayori turned ma at t22
    mc "S-sayori!?"
    show mc cross me e1a b1a at t21
    mc "Why are you here?"
    show mc cross ma e1a b1a
    show sayori turned rup mb e4b
    s "I was looking for you silly~"
    show sayori turned rup ma e4b
    show mc cross mg e1e b1a
    mc "Is this about another club meeting..."
    show mc cross ma e1e b1a
    show sayori turned rdown mb e1a b1c
    s "Nooo..."
    show mc cross mg e1a b1a
    show sayori turned rdown ma e1a b1c
    mc "Okay then what do you want then?"
    show mc cross ma e1a b1a
    window hide(dissolve)
    pause 3.5
    show sayori turned awkw rdown ma e1b b1c
    pause 3.5
    show sayori turned awkw rdown ma e1c b1c
    pause 3.5
    show sayori tap awkw m1
    s "Hehe you're right it's another club meeting..."
    show mc turned mg b1c
    show sayori turned lup rup ml e4c b1b at h22
    mc "AGAIN SERIOUSLY!?"
    show sayori turned lup rup mk e1a b1b at t22
    mc "Didn't we had like"
    extend " back to back meetings like 3 times this week?"
    show mc turned ma b1c
    show sayori turned awkw lup rup ml e4b b1b at pf22
    s "But Monika says it was an urgent"
    s "Super important club meeting!"
    show mc turned mg b1c
    mc "It's always urgent with her"
    mc "And it never be urgent"
    show mc turned mg e1e b1b at s21
    mc "*sigh...*"
    show sayori turned nobl ldown rdown mb e4a b1a at t22
    show mc turned ma e1e b1b at t21
    s "You know how Monika is"
    s "If it's super important then it's super important"
    show sayori turned nobl ldown rdown mb e4b b1a
    s "Hehe"
    show sayori turned ldown rdown ma e4b b1a
    "Who is this girl"
    extend " and why she overly familiar with my beloved...."
    "Is she trying to steal him away from me"
    show vignette:
        alpha 1.0
    play music hb
    show layer master at heartbeat
    "Maybe I should get rid of her before my beloved falls in love with her..."
    "But what if he will hate me for getting rid of her?"
    "I can't have him hating me I rather die than for him to hate me"
    "I can't {nw}"
    "{cps=30}I won't {/cps}{nw}"
    "{cps=30}{nw}He's mines {/cps}{nw}"
    "{cps=30}{nw}all mines{/cps}{nw}"
    "{cps=30}{nw}He belongs to me {/cps}{nw}"
    "{cps=30}{nw}no one else {/cps}{nw}"
    "{cps=30}{nw}I won't share him {/cps}{nw}"
    "{cps=30}{nw}all mines {/cps}{nw}"
    "{cps=30}{nw}He belongs to me {/cps}{nw}"
    "{cps=30}{nw}no one else  {/cps}{nw}"
    "{cps=30}{nw}I won't share him {/cps}{nw}"
    "{cps=30}{nw}He belongs to me{/cps}{nw}"
    "{cps=30}{nw}no one else {/cps}{nw}"
    "{cps=30}{nw}we belong together {/cps}{nw}"
    "{cps=30}{nw}He's mines {/cps}{nw}"
    "{cps=30}{nw}forever and ever {/cps}{nw}"
    "{cps=30}{nw}and ever {/cps}{nw}"
    "{cps=30}{nw}and ever {/cps}{nw}"
    stop music
    hide vignette
    show layer master
    show mc cross mg e1a b1d
    show sayori turned nobl me e1a
    mc "Hey Lib you good?"
    show mc cross ma e1a b1d
    l "OH!"
    l "Umm..."
    show mc cross mg e1c b1a
    show sayori turned shoc ldown rdown b1a
    mc "Oh sorry I forgot to introduce y'all to each other"
    show mc turned mc e1a
    show sayori turned ldown rdown ma b1a
    mc "Libitina this is Sayori"
    mc "Sayori this is Libitina"
    show mc turned mb
    
    $ s_name = "Sayori"
    play music t2
    show sayori turned lup rup mc e4b b1a:
        matrixcolor identity_matrix
        i22()
            
    show sayori turned lup rup mc e4b b1a at t22 zorder 2
            
    s "Nice to meet y-{nw}"
    show sayori turned lup rup mh e2a b1a at h22
    pause 0.5
    s "Wait are you the new transfer student?"
    show sayori turned lup rup me e2a b1a at t22
    l "..Yeah..."
    show sayori turned lup rup mg e2a b1a at h22
    s "Oh "
    show sayori turned lup rup mi e2a b1a
    extend "my "
    show sayori turned lup rup mc e1a b1a
    extend "god"
    show mc turned md e1c b1a at lhide
    hide mc
    show sayori turned lup rup ma e1a b1a at t11 zorder 2
    pause 0.7
    with Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=15) 
    pause 0.7
    show sayori turned ldown rdown mc e1a b1a at t11
    s "SO YOU GOT THE TOP SCORE IN THE SCHOOL!{nw}"
    s "HOW DID YOU MANAGED TO DO THAT?{nw}"
    s "HOW MANY HOURS DO YOU STUDY?{nw}"
    show sayori turned ldown rdown mc e1a b1a at face(y=600)
    s "WHAT'S YOUR BEDROOM LOOK LIKE?{nw}"
    s "DO YOU HAVE PETS?{nw}"
    s "DO YOU READ?{nw}"
    s "HOW MANY BOOK DO YO-{nw}"
    show mc cross mg b1c at t31
    show sayori turned lup rup mk e1a b1b
    mc "SAYORI!"
    show sayori tap awkw m1
    show mc cross ma b1c
    s "Oh hehe sorry..."
    show mc cross ma b1c at t21
    show sayori tap awkw m1 e2 at t22
    extend "I might of overwhelmed you with my questions hehe"
    l "It's...alright I guess..."
    l "So what's your relationship with [mc]"
    show sayori turned blus mc e1b b1b at w22
    s "Oh umm [mc] and I-"
    show sayori turned blus ma e1b b1b at t22
    show mc cross mg e1e
    mc "Are childhood friends"
    show mc cross ma e1e
    show sayori turned nobl rup ml e4c b1b at h22
    s "Hey I was going to say that [mc]..."
    show sayori turned rup mj e4c b1b at t22
    l "I see.."
    "Childhood friends huh?"
    "Usually in stories childhood never get together..."
    "Maybe I don't have to worry about her I guess..."
    show mc cross ma e1a b1a
    show sayori turned rup mb e1a b1a
    s "Anyway it's very nice to meet you Libitina"
    show sayori turned rup mb e4b b1a
    extend " I hope we become the bestest of friends!"
    show sayori turned rup ma e4b b1a
    l "Yeah...same here..."
    show sayori turned lsur rup e2d mi b1a
    s "Oh!"
    show sayori turned lsur rdown mc e1a b1a
    extend" [mc] why don't you invited her to the clubroom"
    show sayori turned lsur rdown mc e4b b1a
    s "I'm sure she'll have a blast with us!"
    show sayori turned lsur rdown ma e4b b1a
    l "Wait...clubroom?"
    show mc cross mg e1a b1a
    show sayori turned lsur rdown ma e1a b1a
    mc "Oh ahh yeah Me, her and a few other people are in a club together."
    show mc cross ma e1a
    l "And you mention this Monika?"
    show sayori turned lsur rdown mb e1a b1a
    s "Oh yeah she's the president of the club that we're in"
    play sound shock
    show bg class_day:
        matrixcolor InvertMatrix(1.0)

    show mc cross ma e1a:
        matrixcolor InvertMatrix(1.0)

    show mc cross ma e1a at i21 zorder 1

    show sayori turned lsur rdown ma e1a b1a:
        matrixcolor InvertMatrix(1.0)

    show sayori turned lsur rdown ma e1a b1a at i22 zorder 2
    with flashbulb
    show bg class_day:
        matrixcolor identity_matrix
    with dissolve

    show mc cross ma e1a:
        matrixcolor identity_matrix
    

    show mc cross ma e1a at i21 zorder 1

    show sayori turned lsur rdown ma e1a b1a:
        matrixcolor identity_matrix

    show sayori turned lsur rdown ma e1a b1a at i22 zorder 2

    pause 1.0
    show sayori turned lsur lup rup mb e4b b1a
    s "And I'm the vice president!"
    show sayori turned lsur lup rup ma e4b b1a
    play sound shock2
    show bg class_day:
        matrixcolor InvertMatrix(1.0)

    show mc cross ma e1a:
        matrixcolor InvertMatrix(1.0)

    show mc cross ma e1a at i21 zorder 1

    show sayori turned lsur lup rup ma e4b b1a:
        matrixcolor InvertMatrix(1.0)

    show sayori turned lsur lup rup ma e4b b1a at i22 zorder 2
    with flashbulb
    show bg class_day:
        matrixcolor identity_matrix
    with dissolve

    show mc cross ma e1a:
        matrixcolor identity_matrix
    

    show mc cross ma e1a at i21 zorder 1

    show sayori turned lsur lup rup ma e4b b1a:
        matrixcolor identity_matrix

    show sayori turned lsur lup rup ma e4b b1a at i22 zorder 2

    pause 1.0
    # beyond shocked
    "Wait another girl...."
    "My beloved might get snatched away if I don't act now."
    l "I'll....."
    extend "join your club..."
    show sayori turned lsur lup rup mb e2a b1a
    s "OMG!"
    s "YOU SERIOUS!"
    show sayori turned lsur lup rup mb e4b b1a at pf22
    "Sayori seems very excited for me to join."
    show mc cross mg e1a b1b
    mc "Hey you sure?"
    mc "I don't want Sayori pressuring you to join"
    show mc cross ma e1a b1b
    show sayori turned lsur ldown rdown mi e1d b1d at t22
    s "Hey...I'm standing right here you know"
    show sayori turned lsur ldown rdown md e1d b1d
    l "Oh no it's fine I wanted to expand my book collection anyway..."
    show sayori turned lsur ldown rup mc e1a b1a
    s "OMG I GOT TO TELL THE OTHERS WE HAVE A NEW MEMBER!"
    show sayori turned lsur ldown rup mc e1a b1a at rhide
    hide sayori
    stop music fadeout 2.0
    show mc turned mg at t11
    mc "Well if you say so anyway I gotta get the classroom before the bell ring."
    show mc turned mc
    mc "I'll catch you around Lib"
    show mc turned mb
    l "Ok see you later [mc]"
    show mc turned mb at rhide
    hide mc
    pause 0.5
    "Little did I know that day"
    extend " joining the club will bring about the end of the world that I once known."
    scene black
    with dissolve_scene_full
    pause 5.0
    show screen console_screen
    pause 3.0
    $ run_input("close Project_l13_log 1-1", "\"closing....\"")
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    hide screen console_screen
    scene black
    pause 1.0
    return

label l2:
    scene black
    pause 5.0
    show screen console_screen
    pause 3.0
    $ run_input("open Project_l13_log 1-2", "\"opening....\"")
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.5
    hide screen tear
    hide screen console_screen
    scene black
    pause 5.0

    #player point of view

    scene bg corridor
    with dissolve_scene_full

    l "(Today I was going to join the club)"
    l "(Not sure how this will turn out but I waited for [mc] as he told me to do so earlier during
    lunch.)"

    l"(I honestly couldn't care less about this club.)"
    l"(But it gave me an opportunity to get more closer to [mc].)"

    mc "Oh...you're already here"
    "Libitina turned around and saw [mc] just arriving in front of the clubroom."
    mc "Sorry about making you wait a bit I had to do some last minute things."
    l "Oh it's fine [mc] I wasn't waiting that long."
    mc "Oh okay but are you sure you want to join?"
    mc "Like I said yesterday I don't want you to feel pressured into joinning."
    l "I don't feel pressured [mc] I always wanted to expand my book collection."
    l "(To be honest I just wanted to spend more time with you and to make sure no other girl gets too close to him.)"
    l "(I won't allow anyone to get in between my beloved and I.)"
    mc "Yeah well about tha-"
    "Before [mc] even finish his sentence the door to the clubroom had open"
    "Sayori appears and looks very excited"
    s "Oh you came Libitina awesome!"
    s "Everyone is waitng to meet you, come on in!"
    "Sayori grabs Libitina's hand and pulled her into the clubroom"
    l "H-hey wait a minute!"
    "[mc] sighed as the three of them enter the room"
    scene club_day
    with wipeleft
    "As they enter Libitina sees two different girls that she seen a few times around the school"
    l"(I didn't think they were members of this club...)"
    s "Hey guys this is the person I was talking about yesterday!"
    $ n_name = "Girl 1"
    n "Finally another girl here I couldn't imagine another [mc]."
    mc "Oy I'm standing right here you know..."
    n "Oh relax [mc] I'm just kidding"
    s "Libitina this is Natsuki!"
    $ n_name = "Natsuki"
    n "Sup"
    s "She;s awesome and can bake some super duper delicous cupcakes!"
    n "H-hey you didn't need to teel her that Sayori!"
    "Sayori points at Yuri"
    s "And this tall beautiful girl here is Yuri she's super smart and loves to read!"
    $ y_name = "Yuri"
    y "S-sayori..."
    extend "Ermm"
    extend "It's....um"
    extend "n-nice to meet you..."
    s "Last but not least out club president Mo-"
    "Sayori stops and look around the clubroom"
    s "Huh?"
    s "Where's Monika at?"
    y "S-she said in the group chat that she was going to be a bit late."
    "Everyone except Libitina looks at their phones"
    mc "Oh wow she just sent that like 2 mins ago"
    s "I wonder what's keeping her?"
    n "Probably her piano lessions again..."
    n "This isn't the first time that this happpen"
    l "Piano...lessions?"
    s "Oh yeah our club president practices piano so this happens from time to time."
    mc "Well in the meantime we can just wait for her to come."
    n "Well while we're waiting..."
    "Natsuki turns to Libitina"
    n "Ain't you that new transferred student that the whole school was talking about 2 week ago?"
    l "Yes I did transfer here 2 weeks ago"
    n "So what made you want to join the literature club anyway?"
    l "Well I told [mc] this eariler but I wanted to expand my book collection."
    l "(And to make sure none of you are too close to [mc].)"
    y "Umm what kind of books do you read?"
    l "Well I read just about anything but I really like to read graphic novel books."
    s "OH WOW!"
    s "So like comic books and stuff?"
    l "Well ac-"
    $ m_name = "???"
    m "SORRY I'M LATE EVERYONE!"
    "Everyone turns their head as Monika just enter the clubroom"
    s "Oh there's our club president!"
    mc "What took you so long?"
    n "Let me guess your piano lession again?"
    m "Yeah...sorry guys"
    y "It must be so awful having to run from the other side of the school building to the clubroom"
    m "I'll be ok Yuri don't worry"
    m "So you're the new member?"
    s "Yeah she was the one I was talking about yesterday."
    s "Libitina this is Monika!"
    s "Monika, Libitina"
    $ m_name = "Monika"
    m "It's nice to meet you Libitina and thanks for joining!"
    "Monika extended her arm and put her hand oout to shake Libitina's hand"
    "As Libitina grabs Monika's hand"
    #static noise here
    l "(What the hell!)"
    "Libitina pulls her hand back but not so quickly as she didn't want to cause a scene"
    l "(What was that just now?)"
    l "(That was so weird....there's something about this girl that cause my body to be on guard...)"
    l "(I've better keep an eye on this one)"
    m "So Libitina are you familiar with literature?"
    l "I would assume a book is a type of literature correct?"
    m "Yes you would be correct...well kinda"
    m "You see a book can be defined as literature, but actually literature is a collection of written works that can be defined in multiple ways."
    m "For example a book can be either be a written work or can be use for know ledge but another form of literature can be poetry."
    m "That's what we call a artistic work of literature which we do here."
    m "Oh and another th-"
    n "ALRIGHT MONIKA THAT'S ENOUGH!"
    n "Geez you're going to put everyone to sleep by the time you're done..."
    y "Natsuki..."
    m "It's alright...I have been rambling on long enough huh?"
    extend " hahaha"
    m "Well since we have a new member joinning today we don't have to do the usually thing today."
    n "Cool"
    y "Phew thank goodness..."
    s "Aww man..."
    mc "Alright"
    l "Usually thing?"
    mc "Oh yeah we would normally share out poems around this time."
    m "Allow me to explain what we do here"
    m "We normally-"
    "While Monika was explaining to Libitina what they do here Libitina was in her thoughts."
    l "(This girl rubs me the wrong way....)"
    l "(My gut is telling me not to trust her at all)"
    l "(And what was that eariler....)"
    l "(Did no one saw that static?)"
    l "(How weird...either way I have to to make sure my beloved is protected at all cost.)"
    m "With that being said Natsuki you can bring out the cupcakes now."
    s "Yeah you been waiting to"
    n "H-hey you didn't need to say anything Sayori ugh.."
    m "Yuri would you mind getting us some tea?"
    y "O-o-of course"
    "Awhile Yuri went to the back and grab her tea set Natsuki brings a large tray cover in foil and place it on top of the desk behind her."
    "As she took off the foil from the tray it revealed many well designed cupcakes with each of them having a different colors"
    "With some having cat whiskers on the sides and some hads cat ears and some had both."
    "As everyone took a cupcake from the tray Libitina looks at them in awe."
    l "Hmm.."
    mc "You good lib?"
    l "Oh yeah sorry they look so well designed like a professional made them."
    "She takes a cupcake from the tray"
    l "I've never seen anyone made cupcakes like this before..."
    "As she was admiring it she felt cold as someone was staring at her intensely"
    "She knew it was Natsuki"
    "She felt that her gaze was staring at her soul waiting for Libitina's reaction to her cupcake that she made."
    "As Libitina took a bite out of the cupcake."
    "Her thoughts can only describe the taste as tasting a bit of heaven."
    "With every chew bring life to her taste buds"
    l "It's...is"
    extend " soo good!"
    "Natsuki's eyes beammed as she was trying to hide her smile so no one would notice."
    s "Right? I told you that Natsuki is super duper good at baking!"
    s "She makes the bestest cupcakes!"
    n "Heh"
    extend " damn right I do."
    "Everyone was enjoying their cupcakes as Yuri brought out the tea and pour everyone a cup."
    #wide here
    "As hours went by it was getting dark adn everyone started to pack there things"
    m "Ok everyone that'll be all for today tomorrow we'll go back sharing out poems with each other!"
    y "H-have a good night everyone..."
    n "See y'all tomorrow"
    "Natsuki and Yuri left and as Libitina was leaving."
    m "Oh Libitina can I talk to you for a moment?"
    m "I promise it won't take long.."
    "[mc] and Sayori looked confused"
    mc "Is everything alright Monika?"
    m "Oh yeah everything is fine [mc] I just wanna talk to her about what's going to happen tomorrow!"
    mc "..."
    l "It's ok [mc] I'll be fine.."
    mc "Well if you say so I guess I'll see y'all tomorrow then.."
    s "Your such a worryhart [mc] come on let's go home!"
    "Sayori drags [mc] out the clubroom as Monika and Libitina was in the room alone."
    l "So...did you needed to tell me something?"
    m "Yeah sorry for keeping you here for a bit I just have a question to ask you."
    l "Ok?"
    m "Have you heard of the scholl festival coming up?"
    l "(What's with this at)"
    l "Hmm no it's the first I'm hearing about it."
    l "Why?"
    m "Well you see"





