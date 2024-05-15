#ONLY USE FOR TESTING PURPOSES ONLY REMOVE OR COMMENT debuger AT SCRIPT.RPY WHEN RELEASING

label debuger:
    scene black
    "Welcome to the Debug room"

    menu:
        "Maria":
            jump mm

        "Mandy":
            jump md

        "Aynat":
            jump ay

        "Scenes"(disabled=True):
            "Umm you are not suppose to see this"
            "Go away now"
            jump debuger

        "Change names":
            jump bug_name


        "Exit":
            $ renpy.quit()

label mm:

    show maria happy at center

    menu:
        "Give points":
            "Enter a number to add from: "
            $ input_value = renpy.input("")
            $ maria_point += int(input_value)
            

            show maria happy2

            m "Yay!"
            jump mm

        "Take away points":
            "Enter a number to subtract from: "
            $ input_value = renpy.input("")
            $ maria_point -= int(input_value)

            show maria sad2

            m "Awww"
            jump mm

        "Show total number of points":
            "Total: [maria_point]"
            jump mm

        "Enable/Disable route":

            if mariaroute == True:
                $ mariaroute = False
                "Disable!"
                jump mm

            else:
                $ mariaroute = True
                "Enable!"
                jump mm

        "Test route":
            if mariaroute == True:

                m "[username] you are doing my route so kool."

                if maria_point == 1:
                    m "Even though we just met I feel like we have a bond between us"

                    m "Let's do our best!"

                    jump mm


                if maria_point == 5:
                    m "Hey [username]"

                    m "How are you feeling today?"

                    m "Make sure you don't over do it ok?"

                    m "You are important to this group."

                    m "Stay strong and don't lose heart I'm here with you."

                    jump mm

                if maria_point >= 9:
                    show maria sad2
                    m "Say [username].."

                    m "I want you to know that we are good friends and I'll always protect you no matter what"

                    m "Like all my other friends you are special to me"

                    m " I can't imagine you not being here with us"

                    show maria happy2

                    m "After all this is over why don't you come with us we can help you for a better future."

                    show maria away2

                    m "If you want I mean but promise me one thing"

                    m "Promise me that you'll take care of yourself"

                    show maria smile2

                    m "OK?"

                    jump mm

                else:
                    jump mm

            else:
                show maria sad2
                m "[username] you are not doing my route bummer"

                jump mm

        "Back":
            jump debuger


label md:

    show mandy norm at center

    menu:
        "Give points":
            "Enter a number to add from: "
            $ input_value = renpy.input("")
            $ mandy_point += int(input_value)

            show mandy happy2

            md "Wow thanks"
            jump md

        "Take away points":
            "Enter a number to subtract from: "
            $ input_value = renpy.input("")
            $ mandy_point -= int(input_value)

            $ mandy_point -= 1

            show mandy away2

            md "Ugh..."
            jump md

        "Show total number of points":

            "Total: [mandy_point]"

            jump md

        "Enable/Disable route":
            if mandyroute == True:
                $ mandyroute = False
                "Disable!"
                jump md

            else:
                $ mandyroute = True
                "Enable!"
                jump md

        "Test route":
            if mandyroute == True:

                show mandy norm2

                md "Seem you are doing my route"

                if mandy_point == 2:
                    show mandy upset2

                    md "HEY [username]!"

                    md "Pick up your own weight because if you die it will be the end for all of us"

                    md "So tread carefully"

                    jump md

                if mandy_point == 6:
                    show mandy upset2
                    md "[username]!"

                    md "What are you doing?"

                    md "Maria told me to come check on you because you haven't been eating"

                    show mandy upsetl2

                    md "Soo I brought you some food"

                    md "I know that you are going through a lot right now"

                    md "Just know that...we are here so"

                    md "Save your strength until the time comes to use your power to save us all"
                    jump md


                if mandy_point >= 9:
                    show mandy think2
                    md "You know something [username]"

                    md "You never cease to surprise me"

                    md "Not only you lost your love ones"

                    md "But you have the strength to keep forward"

                    show mandy away2

                    md "Do you also worry about the future of what's to come, and wished that you knew what is coming"

                    md "That very thought scares me knowing the fact eventually I will lose everyone one day"

                    md "But after looking at your memories I realized that though they may be gone"

                    show mandy happy2

                    md "They will never be forgotten they will live on in your heart"

                    md "Thank you for showing me this and I swear to you I will protect you"

                    md "Even if it cost me my life because you are a good friend to have"

                    md "I won't let anything to you"

                    md "I promise"

                    jump md

            else:
                "You didn't enable my route"
                jump md

        "Back":
            jump debuger


label ay:

    show aynat norm at center

    menu:
        "Give points":
            "Enter a number to add from: "
            $ input_value = renpy.input("")
            $ aynat_point += int(input_value)

            show aynat flirt

            a "How cute"

            jump ay

        "Take away points":
            "Enter a number to subtract from: "
            $ input_value = renpy.input("")
            $ aynat_point += int(input_value)

            show aynat upset

            a "Asshole"

            jump ay

        "show total number of points":
            "Total: [aynat_point]"
            jump ay

        "Back":
            jump debuger

    return


label bug_name:
    python:
            while True:
                name = renpy.input(_("I think my name is?"))

                name = name.strip() or __("Rei")

                if name.lower() in ["terios", "terioskrim", "terios krim"]:
                    renpy.notify("Sorry, that name is already taken.")

                elif name.lower() in ["mandy nakai", "mandynakai"]:
                    renpy.notify("Hey, get your own name.")

                elif name.lower() in ["aynat"]:
                    renpy.notify("Sorry sweetheart, the names taken.")

                elif name.lower() in ["marialuz", "maria luz"]:
                    renpy.notify("Silly goose, that name is taken.")

                else:
                    break  # Exit the loop if the name is not the names above"

    jump debuger

