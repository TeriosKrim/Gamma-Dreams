label act1:

    $ rotation_angle = 0

    $ m.name = "???" #Use this to change the names of maria and mandy when first appearing
    $ md.name = "???"

    stop music fadeout 1.0

    scene black
    with Pause(1)

    show text "ACT I: MIRAGE" with dissolve
    with Pause(2)


    hide text with dissolve
    with Pause(1)


    play music dreams

    u "Where am I?"

    u "...."

    u "......."

    u "Who am I?"

    u "My name?"

    label enter_name:
        python:
            while True:
                name = renpy.input(_("I think my name is?"))

                name = name.strip() or __("Rai")

                if name.lower() in ["terios", "terioskrim", "terios krim", 'krimterios' 'krim terios']:
                    renpy.notify("Sorry, that name is already taken.")

                elif name.lower() in ["mandy nakai", "mandynakai", "nakai mandy", "nakaimandy"]:
                    renpy.notify("Hey, get your own name.")

                elif name.lower() in ["aynat"]:
                    renpy.notify("Sorry sweetheart, the names taken.")

                elif name.lower() in ["marialuz", "maria luz", "luzmaria", "luz maria"]:
                    renpy.notify("Silly goose, that name is taken.")

                else:
                    break  # Exit the loop if the name is not the names above"


    mc "My name is [name] yeah I remember that name"

    mc "But where am I"

    mc "I don't remember being here."

    mc "I must be asleep or-"

    mc "Huh?"

    show e_f:
        matrixcolor OpacityMatrix(0.1)
        center
        
    "A mysterious entity appears in front of me."

    "By the looks of it, it isn't human."

    mc "Who ar-"

    u "Y----u"

    u "--U-s--"

    mc "What? I don't understand wha-"

    u "e---P-"

    mc "Wait!"

    stop music fadeout 1.0

    scene bg room_morning_light_off
    with flashbulb

    mc "AHHHHHHHHHH!"

    "I suddenly woke up as my heart was pounding hard."

    mc "*Gasp*"

    mc "Holy hell"

    mc "Was it a dream?"

    mc "It felt soo-"

    "I look over my bed and see the time."

    mc "Holy crap it's seven O'clock, I'm going to be late for school."

    "I rushed out the bed as fast as possible, got dressed and ran out of my home."

    scene bg day01 at close
    with fade

    play music school fadein 1.0

    "It's a good thing I live close to my school, but my class is on the 3rd floor."

    "It's not easy living alone with both of my parents traveling abroad due to my dad's business."

    "Leaving me a 16-year-old in high school alone."

    "It's not as bad as my father left me a lot of cash for me to spend."

    "So I get food for myself and stuff."

    "But kinda wished a had at least one person I can call a friend."

    mc "Ugh I have science today"

    scene bg school_science_lab_day01
    with fade

    "My science teacher hates my guts and wants me to drop her class."

    "But she knows I usually get my work done so she can't say anything bad about me."

    "So she's waiting until the day I slip up so she can use all her power to get rid of me."

    u "OK EVERYONE SIT DOWN I HAVE AN ANNOUNCEMENT TO MAKE!"

    mc "Ugh what is it this time...."

    u "We have a new student that transferred from another school today."

    "Oh yeah she mention someone was transferring her at mill high, everyone is wondering if it is a boy or a girl."

    "I personally don't care so, it's not like I'm popular or anything."

    u "Ok come on out sweetheart"

    "Suddenly we see a girl but with."


label girl_choice:

    $ renpy.notify("Remember to save often!")

    menu:

        "Short black hair.":

            jump maria_choice

        "Long blond hair":
            jump mandy_choice

    label maria_choice:



        $ renpy.fix_rollback()

        $ mariaroute = True

        show maria happy at center
        with dissolve

        "Short black hair, looks very friendly."

        "Also kinda cute geez if only I can talk to her."

        u "Tell the class your name please"

        show maria happy2

        m "Heya claass my name is Maria Luz and I hope I can be friends with everyone."

        u "Ain't you a sweet, so did you have friends in your last school?"

        $ m.name = "Maria"

        m "Yeah about five friends over there, but I want lots of friends here."

        hide maria
        show maria happy2b at center

        "Wow, this girl is too friendly, seems kinda sus I don't think I met someone that was too friendly."

        u "Well why don't you take a seat with [name] over there near the window."

        u "Since it's the only available seat."

        "Maria looks at me and walks over to where I was and sat next to me."

        show maria happy2b

        m "Hi your [name] right?"

    menu:

        "Yeah.":
            jump yes

        "Actually no":
            jump no


    label yes:

        hide maria

        show maria happy2 at center

        $ maria_point += 1

        if name.lower() == "maria":

            m "Oh we share the same name [name]."

            mc "It would seem so Maria."

            m "What a coincidence!"

            m "But still..."

        else:
            pass

        m "It's nice to meet you"

        mc "Yeah nice to meet you too, so what do you think about your first time in mill high school?"

        m "Well it's very interesting people in here and..."

        show maria norm

        m "..."

        "Maria looks out the window like she saw something."

        "I wonder was there something wrong with her?"

        "Maybe I should ask her?"

        mc "Hey you ok? Is something wrong?"

        hide maria
        show maria sad2b at center
        stop music fadeout 1.0

        m "Is this really what you want?"

        mc "Want what, what are you talking about?"

        m "All of this is not real you're living in a mirage you have to wake up."

        "Ok, this girl is definitely weird."

        mc "Wake up?"

        mc "...Right.."

        mc "Listen I-"

        "But I suddenly felt very sick for some reason."

        with flashbulb

        "And then my head all of a sudden is starting to hurt a lot."

        "Like someone is stabbing my brain."

        mc "Ugh, My head"

        m "You have to wake up"

        mc "What are you talking about"

        "My head feels like it's splitting in two"

        "It felt like someone with pull my brain apart"

        with flashbulb

        m "We need to get out of here it's not safe here for you to be here, especially when you're being hunted."

        mc "Hunted?"

        hide maria
        with dissolve

        "I don't what's going on here the more she talked, the more reality was dissolving."

        "I look around and I see all of the students in the room are starting to disappear and my teacher Ms. Karren is melting?"

        mc "What the hell is going on here."

        "I rub my eyes to see if this was fake."

        "Turns out it was real everything was really slowly disappearing."

        "I don't know if she's doing this or not nor I should believe her, but at the same time I don't think she would lie to me."

        "Should I believe her?"

        menu:
            "Yes":
                jump yeah

            "Hell No":
                jump nope


        label yeah:

            $ maria_point += 3

            mc "Ok since we're being hunted can you get us out of here?."

            hide maria
            show maria happy2 at center

            m "YEAH!"

            m "Hang on tight to me."

            with flashbulb

            "As if it was like magic we were suddenly in a bubble-like thing."

            "It kinda looks like some sort of barrier."

            m "Here we go"

            mc "UGHHH"

            "My headache got worse and before I know it everything fades to black"

            scene black

            with flashbulb

            jump choice1_done



        label nope:

        mc "Why should I believe you!"

        mc "If anything you could be the one behind this."

        show maria upset2 at center

        m "Why would I do all of this, if I was the one behind this I wouldn't be helping you."

        mc "You could be trying to trick me."

        m "I'm trying to save your life, we don't have a lot of time."

        hide maria
        show maria sad2b at center

        m "Just Please come with me."

        menu:
            "OK Fine":
                jump yeah

            "Nope":
                jump bad


        label bad:

        hide mariab
        show maria upset2 at center

        m "Why are you being so stubborn."

        mc "You really expect me to believe you when I literally just met you?"

        mc "Like seriously?"

        mc "Like I said before how do I know you are not doing any of this right now."

        m "And I told you before we d-"

        play sound punch

        show maria shock

        "Suddenly Maria stopped talking"

        show maria faint

        m "....."

        hide maria faint
        with dissolve

        "And collapse into the floor"

        mc "What the?"

        show dark at center
        with dissolve

        play music danger fadein 1.0

        "A shadow-like thing suddenly appeared where Maria was standing at."

        "I ran to Maria as quickly as possible."

        mc "Hey you ok?"

        "I tried to wake her up but she wasn't waking up."

        "I look at the creature as it starts to get close to us."

        mc "What are you, get away."

        "It's started to walk faster toward me."

        "What Should I do?"

        label quick:

        menu:
            "Help Maria":

                $ saved = True

                "I know I'm going to regret this."

                "But I can't leave her here."

                "I grabbed Maria and lifted her with both of my arms and ran as fast as I can toward the door."

                "But suddenly out of thin air."

                show dark at right

                show male at left behind dark
                with dissolve

                "Another one appears and it's blocking the door."

                "I wanted to jump out the window but I didn't want to risk Maria getting hurt."

                "I didn't know what to do."

                scene black
                with fade

                "I closed my eyes hoping something miracle happens."

                play sound fire

                "I heard a noise and as I reopen my eyes."

                scene bg school_science_lab_day01
                with fade

                "I didn't see the shadow beings anymore."

                m "Umm can you put me down."

                "I look down in my arm and saw Maria awake."

                mc "Oh sorry"

                "I put Maria down as she stood up on her own."

                show maria upset2b at center

                m "GEEZ IF YOU WOULD LISTEN TO ME EARLIER WE COULD HAVE AVOIDED THIS PROBLEM!"

                mc "Sorry but how did that hap-{nw}{fast}"

                m "No time we have to go now."

                with flashbulb

                mc "My head again."

                "As I look across the room before I lose consciousness."

                show aynat norm at slightright behind maria
                with dissolve

                $ aynat_point += 1

                "I saw a demon girl with purple wings grinning as if she was toying with us."

                scene black
                with flashbulb

                stop music fadeout 1.0

                jump choice1_done

            "RUN!":
                jump run


        label run:

        mc "OH SHIT I GOTTA GO!"

        "Forgetting to grab Maria I ran toward the door but suddenly appeared from thin air."

        show male at left behind dark
        with dissolve

        "Another one appears and it's blocking the door."

        "I tried to run toward the window but I couldn't move my legs."

        mc "WHAT THE HELL!?"

        "My legs went through the floor as if was quicksand and I couldn't move at all."

        "Both of this shadow being got closer and closer to me."

        "And they both grab both of my arms."

        show dark at right

        show aynat norm at center behind dark
        with dissolve


        "Suddenly a woman came out of nowhere."

        show aynat norm2

        u "Hehehe I was worried for a second there, thought you might of escape."

        mc "What ar-"

        "The demon girl shush me by placing one finger on my lips"

        u "Just look into my eyes"

        "As she said that I started to get sleepy"

        with fade

        mc "Wai-who"

        scene black
        with fade

        u "Sweet dreams"

        stop music fadeout 1.0


        jump badend1



    label badend1:
        $ renpy.fix_rollback()

        scene bg room_morning_light_off

        mc "AHHHHHH!!"

        mc "...."

        mc "Was it a dream?"

        mc "Man it felt so real though."

        "I look over my bed and see the time."

        mc "Oh, no school today welp."

        "Yawn{i}"

        mc "Guess I could go back to sleep."

        scene black
        with fade

        u "Yes a very long sleep hehehe~"

        "BAD END"

        $ persistent.endbad1 = True

        jump end

        jump choice1_done

    label no:

    hide maria

    show maria away2c at center

    m "Oh sorry I told I was in this seat."

    "Maria looks embarrassed"

    mc "Hahaha actually I am [name]"

    hide maria
    show maria upset2 at center

    m "That's not even funny you jerk."

    "Maria looked upset but seem like she was embarrassed"

    mc "Sorry I really wanted to see your reaction."

    m "Geez"

    show maria sigh

    "Maria gave a big sigh as a sign of relief. "

    m "Anyway"

    jump yes

    label mandy_choice:
        $ renpy.fix_rollback()

        $ mandyroute = True

        show mandy norm at center
        with dissolve

        "A girl with long blond hair shows up."

        "And she looking sexy, like very sexy."

        mc "Wow what a hottie"

        "As I said that the girl walked towards me"

        show mandy upset2

        md "You're coming with me right now"

        "She grabbed my shirt with a good grip and started pulling my shirt."

        mc "Hey w-wait can't we at least get to know each other first?"

        "She definitely wants the D, P snakey see"

        u "Excuse me, you were supposed to introduce yourself."

        u "You can jus-"

        stop music fadeout 1.0

        play sound cut
        pause 2.0
        play sound cut

        u "AHHHH!"

        "As if like paper my teacher split into two."

        mc "HOLY SHIT!"

        "But as I thought there was going to be blood all over the room, she just dissolve into nothingness."

        mc "What the hell?"

        md "Let's go before trouble appears."

        "As she said that"

        show darkl at right
        with dissolve

        show male at left
        with dissolve

        play music danger fadein 1.0


        "Two shadows-like beings appear"

        mc "WHAT ARE THOSES!?"

        "As I look around all of the students were turning into them."

        hide mandy
        show mandy upset2b at center

        md "Damn"

        show mandy upsetb behind male

        play sound cut

        hide male
        with dissolve

        show mandy upsetb behind darkl

        play sound cut

        hide darkl
        with dissolve

        "She was cutting them down with lighting speed that I didn't even know she even moved."

        "But as she was cutting them down."

        show darkl at right
        with dissolve

        show male at left
        with dissolve

        "Two more took their place."

        show mandy upsetb

        md "I don't have time for this."

        $ k.name = "???"

        k "Don't waste time with them just grab [name], I will teleport you out of there."

        md "As you command"

        "She grabbed me and suddenly a see a bright light from above."

        show mandy upsetb

        with flashbulb

        mc "UGH m-my head"

        "Like a knife just went inside my brain, my head started to hurt."

        "My eyes got heavier, I start to lose consciousness."

        scene black
        with flashbulb
        stop music fadeout 1.0

        jump choice1_done

    label choice1_done:

        mc "...."

        mc "....."

        mc "......Ugh"

        mc "Whoa where am I now?"

        "I look around and see nothing but darkness."

        mc "...."

        "Not a single person around."

        mc "HELLO!"

        "..."

        "Was I dreaming again?"

        mc "Anyone?"

        "....."

        "No this felt different this was no dream I thought."

        "I wonder if I was going to be here forever..."

        "I kneel as tears started to build up in my eyes."

        mc "Anyone..."

        mc "Please.."

        mc "Help me..."

        "As I said those words suddenly."

        show vortex
        with dissolve

        play music dreams

        "A portal appears before me."

        mc "What is going on here."

        "I look at the portal and see someone coming out."


        if mandyroute:
            jump mandy

        if mariaroute:
            jump maria


    label maria:



        show maria happy2 at center
        with flashbulb

        "The person that came out was Maria."

        m "Hey [name]"

        mc "MARIA!?"

        "I wiped the tear from my eyes so that maria doesn't see."

        mc "What the hell is going on here."

        mc "Is this a dream?"

        m "It's not a dream [name]"

        hide maria

        show maria upset2c at center

        m "Everything you thought was real was a lie"

        "I didn't know what she was talking about I was so confused."

        mc "What do you mean it wasn't real?"

        m "Like your whole life from school to your home from your friends and family."

        m "All you experienced wasn't real"

        m "It all was an illusion"

        "An illusion?"

        "My whole life?"

        "No way that's impossible."

        "..."

        "But what if she was telling the truth."

        "I mean I don't think she has no reason to lie to me."

        "..."

        "If all my life was a lie then.."

        "I knew I needed answers."

        "So I asked Maria..."

        mc "If my whole life was a lie then where am I.."

        show maria away2c

        m "It's very complicated but let me putting in simple words."

        m "As we stand we are in the dream realm."

        show maria upset2c at center

        m "And you [name] are one of the strongest agents of our secret headquarters."

        m "That was assigned to investigate the disturbance of the dream realm."

        m "But we lost your signal about 3 days ago."

        "Me an agent?"

        "I don't believe what's she saying"

        mc "How can I 16-year-old be an agent?"

        hide maria

        show maria sad2b at center

        m "[name] you're not 16 look in your pockets"

        "I checked my pocket and see a wallet that I haven't seen before."

        "I opened the wallet and saw my name [name] and my birthday."

        "A 22-year-old male and right next to it I see a picture of a baby and a woman."


    label time:

        m "That was your family"

        m "They died about 4 years ago in a horrible accident."

        mc "..."

        "Why I can't remember them."

        "This is me in the picture."

        "It must be true"

        "My whole life..."
        extend "was a lie."
       

        "I was in disbelief for a moment."

        "Realizing that everything was a lie my parents, my home, my school, the friends I made, everything."

        "I felt sick to my stomach."

        "But I need remember who I really am."

        "Who was I before this?"

        "I hid my fears and doubts and spoke."

        mc "But I don't remember anything of my past."

        show maria happy2b at center

        m "It's ok [name] me and my teammates will help you get your memories back."

        mc "What happened to me, Maria?"

        m "We believe someone must have taken your memories and tried to use your powers for their own purpose."

        mc "What do you mean \"My powers?\""

        m "I'll explain more once we go back to headquarters."

        m "Which is through this portal."


        if saved:

            mc "Before we go who was that demon lady."

            hide maria

            show maria shockc at center

            m "Oh you saw her I'm not sure who she is but our intel tells us that she working with the enemy."

            m "Also she can manipulate a person's dreams to steal a person's memory to increase her powers."

            mc "I see"

            m "Don't worry [name] we will get your memories back from her."

            hide maria

            show maria happy4 at center

            m "Plus I owe you for saving me back there."

            mc "It was nothing I'm pretty sure you would do the same."

            $ maria_point += 2
            $ aynat_point += 1

            "Maria seems to be really appreciated that I saved her."

            m "Come on [name] let's figure out how to get your memories back."

            hide maria happy4
            with dissolve

            "Maria went into the portal"

            "I followed her I need to know who am I."

            "And this is my only lead to discover the truth."

            scene black
            with flashbulb

            mc "WHOA!"

            # mc "This place seems familiar"

            stop music fadeout 1.0


            jump base

        else:

            m "Come on [name] let's figure out how to get your memories back."

            hide maria
            with flashbulb

            "Maria went into the portal"

            "I followed her I need to know who am I."

            "And this is my only lead to discover the truth."

            scene black
            with flashbulb

            mc "WHOA!"

            # mc "This place seems familiar"

            stop music fadeout 1.0


            jump base









    label mandy:
        show mandy upset at center
        with flashbulb

        "It's the blond hair girl from earlier."

        "I quickly wiped my tears so that she doesn't see them."

        mc "It's you, the new girl from school."

        md "That wasn't a real school."

        md "Don't even realize that you were being used."

        "I didn't understand what she was talking about I was so confused."

        mc "What are you talking about, who are you and why did you bring me here?"

        show mandy upset2

        $ md.name = "Mandy"

        md "Name's Mandy and all your answers will be answered once you step into this portal."

        mc "No disrespect but why should I go with you I don't even know you."

        md "Because if you don't this portal will close and you'll be stuck here forever."

        md "So it either you come with me or be stuck in darkness forever."

        "I guess she does have a point."

        "I mean she did saved me from those black creatures."

        "But I also just met her."

        "Hmm..."

        "What do I do?"

        menu:
            "Guess I have no choice but to go with her":
                jump nodark

            "Darkness is my friend":
                jump dark



        label nodark:

            $ mandy_point += 1

            md "Good choice now let's go"

            "I follow Mandy into the portal"

            "Because I don't want to be here any longer plus she might know what the hell is going on here."

            scene black
            with flashbulb

            stop music fadeout 1.0

            mc "WHOAA!"

            #mc "This place..."


            jump base

        label dark:
            "I just met her and I don't know if I can trust her."

            mc "Yeah I'm just going to stick here in this dark place."

            show mandy upset

            md "..."

            "Judging by her facial expression she did not liked my answer."

            "Mandy slowly walked in front of me."

            "I started to back away from her."

            mc "Wait a min what ar- {nw}{fast}"

            hide mandy

            play sound punch

            stop music fadeout 1.0

            "I felt a small pinch on my back and suddenly my body lost all its strength."

            "I started to lose consciousness again"

            scene black
            with fade

            md "You don't have a choice in the matter."

            "Moments later"

            u "Hey dumbass..WAKE UP!!"

            "I felt really cold liquid as it continued to pour on me."

            mc "WHAAAAAAAAAAAAAAA"

            mc "WHAT THE HELL!"

            "I looked around"


            jump base



        label base:

            scene bg beach6
            with dissolve

            "This place I remember this place."


            with flashbulb

            mc "Ugh my head"

            if mariaroute == True:
                m "Hey you ok?"

                "I turned around and see Maria near the waves of the ocean."

                show maria happy at center
                with dissolve

                mc "I remember something from my past just a small bit though."

                mc "Maria are we back in the real world?"

                show maria away2b

                m "I don't think so, I think something went wrong."

                mc "What do you mean?"

                $ md.name = "???"

                md "It means something or someone is interfering with us."

                "Suddenly we hear a mysterious voice."

                mc "Um who jus-"

                "Before I finished my sentence"

                show maria shock at left

                show vortex behind maria
                with dissolve

                pause 1.5

                "The portal opened up again."

                "Something was emerging from the portal."

                show mandy norm at right
                with flashbulb

                hide vortex
                with dissolve

                pause 1.5

                "And we see a long blonde hair woman."

                "And she does look sexy {nw}{fast}"

                "Wait I can't be think about that I asked the blonde woman."

                mc "Who are you?"

                show mandy think2 at right

                $ md.name = "???"


                md "My name is not importan-"

                show maria happy2

                m "That's Mandy she is one of my friends that is here to help you."

                $ md.name = "Mandy"


                md "..."

                m "But why are you here Mandy?"

                md "...."

                show maria confuse2b

                m "Mandy?"

                show mandy think4

                md "Maria how many times do I have to tell you"

                md "{size=+10}STOP GIVING RANDOM PEOPLE MY NAME!{/size}"

                show maria sad2b

                m "Aw sorry Mandy"

                jump question

                return

            if mandyroute == True:

                if name.lower() == "mandy":
                    md "For one who shares the same name as me."
                    md "I hope You're not this weak."

                else:
                    pass



                "I turned around and see Mandy near the ocean"

                mc "Mandy?"

                show mandy norm at center
                with dissolve

                md "What?"

                mc "Why are we here"

                show mandy away

                md "..."

                mc "Is this the real world?"

                md "..."

                mc "MANDY!?"

                show mandy upsetl2

                md "I DON'T KNOW OK!?"

                md "We were supposed to be back in HQ, but for some reason it brought us here."

                mc "What do you mean?"

                $ m.name = "???"

                m "Actually something or someone is interfering with the portal."

                "Suddenly we hear a mysterious voice."


                show mandy upsetb at right

                show vortex behind mandy
                with dissolve

                pause 1.5

                "The portal opened up again"

                "Something was emerging from the portal"

                show maria happy at left
                with flashbulb

                hide vortex
                with dissolve

                pause 1.5

                "We see a short black hair girl"

                "She looks friendly enough"

                "But the question is she friend or foe?"

                show mandy away2b

                md "Oh it's you"

                mc "I take it you two know each other?"

                md "Yeah she's a teammate{nw}{fast}"

                show maria happy2c

                $ m.name = "Maria"

                m "My name is Maria I've come to help."

                m "Nice to meet you [name]"

                show mandy upset

                mc "How do you know me?"

                mc "Do you know you from somewhere?"

                m "No we have been watc-{nw}"

                show mandy upset2

                md "{size=+10}MARIA!{/size}"

                show maria away2

                m "Oops"

                jump question


        label question:

                mc "Ok I'm not going anywhere unless I get some real answers."

                if mariaroute:
                    mc "I want to believe you Maria but I still have doubts about all this"

                if mandyroute:
                    mc "I want some real anwsers Mandy."

                "I knew I need some answers I can't just blindly trust these two without at least some answers."

                "Maria and Mandy look at each other noded then look back at me."

                show mandy think2

                show maria sadb

                md "You want answers fine but you better ask the right questions then."

                mc "Ok"

                jump answers

        label answers:

            show maria happy

            show mandy norm

            "Let's see..."

            menu:
                "Who do you work for?" if not work:

                    md "We work for a top-secret organization that specializes in the supernatural."

                    md "Rarely we also work with multiverses as well."

                    show mandy norm2

                    md "But in this case."

                    md "There are enemies that are trying to use your powers for evil."

                    mc "What powers I'm just a normal person."

                    show maria upset2


                    m "Maybe in the real world but not in the dream realm."

                    m "Your power is very powerful here."

                    mc "What are my powers exactly?"

                    show mandy think2

                    md "You'll have to ask that question."

                    mc "..."

                    $ work = True


                    jump answers

                "About my powers" if work and black and place and not power:
                    mc "Now what powers do I have?"

                    show mandy think2

                    md "We are not sure ourselves but it seems like you can manipulate certain actions here."

                    md "But we don't know what action you can control here."

                    show maria happy2

                    m "Think of it as you are in a dream, you are not aware you are in a dream."

                    m "So you can't control your dream, but when you are aware you can control them."

                    mc " I see so all I have to do is to be aware that everything is a dream?"

                    show maria away2

                    m "I guess? it's a weird case here."

                    show mandy norm2

                    md "Even if you are aware, you can't really control your powers."

                    if work:
                        md "It's why I said before there are enemies here that are trying to use your powers."

                        md "But it won't just be in your dream it'll be in everyone's dream."

                        mc "I see then I better be careful then."

                        show maria happy2

                        m "Next question"

                        $ power = True

                        jump answers

                    else:
                        md "There are people here trying to use your powers for themselves."

                        md "But not only they'll use your powers, but they'll use them to conquer or destroy this realm."

                        show maria happy2

                        m "And that's why we are here to stop them and rescue you."

                        mc "I see...well I have to be careful."

                        md "Anything else?"

                        $ power = True

                        jump answers

                "What is this place that we are in?" if not place:
                    if work:
                        show mandy upset2

                        show maria happyb

                        md "Didn't Maria mention this is the dream realm."

                        mc "Well yeah but where is the \"dream realm\" exactly?"

                        md "The dream realm is where everyone goes when they sleep."

                        md "When you sleep your soul leaps out your body and goes into the astral plane."

                        md "This is only half of the astral plane that we are in right now."

                        mc "Half?"

                        show mandy think2

                        md "Yes the other half is where all life goes after death in other words the dead world."

                        md "'The land of the dead'"

                        show maria happy2

                        m "We can't enter the dead world because we are still alive only supernatural beings can go into the dead world."

                        m "You know like angels, demons etc"

                        show maria shock

                        m "But I heard a rumor that if a living person goes into the dead world they'll die in their sleep."

                        mc "I see..."

                        mc "That explains why we all are standing here on the beach."

                        mc "Ok I think I have an understanding of where we're at."

                        show mandy norm2

                        md "Good"

                        $ place = True

                        jump answers


                    else:
                        show mandy norm2

                        show maria happyb

                        md "The dream realm is where everyone goes when they sleep."

                        md "When you sleep your soul leaps out your body and goes into the astral plane."

                        md "This is only half of the astral plane that we are in right now."

                        mc "Half?"

                        show mandy think2

                        md "Yes the other half is where all life goes after death in other words the dead world."

                        md "Where everyone goes when they die."

                        show maria happy2

                        m "We can't enter the dead world because we are still alive only supernatural beings can go into the dead world."

                        m "You know like angels, demons etc."

                        mc "Whoa that's kinda hard to believe but looking at where we're at."

                        mc "It might be true"

                        m "Do you have any other questions?"

                        $ place = True

                        jump answers


                "What are those black creatures?" if not black:

                    show mandy think2

                    md "We are not sure but we do have a code name for them."

                    md "We call them 'Night terrors'"

                    mc "Night terrors?"

                    mc "I mean if you really think about it they do look a bit creepy."

                    if saved:
                        show maria shock
                        m "Oh my god right?"

                        m "They looked like faceless monsters"

                        show maria sad2

                        m "I don't know what would had happen if you didn't save me"

                        mc "Don't mention it"

                        "Even tho it was me that we almost got caught in the first place..."

                        md "It's why we need to find the source of where they are coming from."

                        mc "Yeah otherwise more of them will just replace the other one."

                        show maria happy2

                        m "Yeah we will stop them no matter what"

                        m "Anything else?"

                        $ black = True

                        jump answers

                    elif mariaroute:
                        show maria happy2b

                        m "It's a good thing we got away from them huh [name]?"

                        mc "Yeah you definitely saved me Maria thank you."

                        $ maria_point += 2

                        show maria happy4b

                        m "Aww you making me blush [name]."

                        show mandy think2b

                        md "But we need to definitely find the source of where are they coming from."

                        mc "We need to for sure otherwise we might end up dying."

                        show maria happy

                        m "Don't worry [name] I'll protect you no matter what."

                        mc "Much appreciate it I'll do my best as well t-"

                        show mandy upset2b

                        md "WE DON'T HAVE TIME FOR THIS!"

                        md "NEXT QUESTION!"

                        mc "Ok ok geez"

                        $ black = True

                        jump answers

                    else:
                        show mandy think2c

                        md "I suppose they do look creepy."

                        md "But we have to find out where they are coming from."

                        md "So we can destroy them and the place they're coming from."

                        mc "Yeah"

                        show maria away2c

                        m "I didn't come across them yet so I guess I'll take y'all word for it."

                        show mandy norm2b

                        md "So any more questions?"

                        mc "I think so"

                        $ black = True
                        jump answers

                "Who was that demon lady?" if saved and place:

                    show maria upset2b

                    m "You mean the one from before."

                    mc "Yeah"

                    show mandy upset2c

                    md "What demon lady?"

                    if black:
                        mc "Before we left the classroom I saw a demon lady with those night terrors."

                        show mandy think4b

                        md "I see it must have been one of the enemies I spoke of."

                        md "It seems demons are indeed involved."

                        mc "Demons huh?"

                        md "We need to be on our toes, demons are tough to fight against."

                        md "One wrong move and we may lose our very souls."

                        m "Yeah it was the purple one. "

                        md "From intel?"

                        m "Yeah"

                        md "She is especially dangerous."

                        mc "Oh man"

                        "If she's really that dangerous then I really need to be careful when coming across her."

                        md "Anything else?"

                        mc " Oh umm"

                        $ aynat_point += 1

                        $ saved = False
                        jump answers


                    else:
                        mc "Before we left the classroom I looked back and saw a demon lady with those black creature"

                        show mandy think4b

                        md "I see it must have been one of the enemies I spoke of"

                        md "It seems demons are indeed involved"

                        mc "Demons huh?"

                        md "We need to be on our toes, demons are tough to fight against"

                        md "One wrong move and we may lose our very souls"

                        m "Yeah it was the purple one "

                        md "From intel?"

                        m "Yeah"

                        md "She is especially dangerous"

                        mc "Oh geez"

                        "If she's really that dangerous then I really need to be careful when coming across her"

                        md "Anything else?"

                        mc " Oh umm"

                        $ aynat_point += 1

                        $ saved = False

                        jump answers

                "Continue" if work and place and black and power:
                    jump light


        label light:
            mc "I think that's everything for now."

            mc "So where do we go from here?"

            show mandy norm2b

            md "We need to return to HQ"

            if mariaroute:

                m "But how when the portals are messed up?"

                m "We don't even know how to get back..."

                $ az.name = "???"

                az "That because there's nothing to go back to."

                az "You all will die here."

            else:

                md "I'm trying to see how though"

                md "With the portal messing up there no telling where we'll end up."

                $ az.name = "???"

                az "You all will end up dead once I get through with you."

                az "Along with the rest of those puny humans."

            'We all turned to see who spoke to us'

            'Suddenly we met with a weird purple skin demon'

            md 'Maria get [name] and stand back now!'

            'As Mandy ended her sentence.'








            return
