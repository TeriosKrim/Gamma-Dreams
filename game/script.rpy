# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    import os
    username = os.getenv('username')



# The game starts here.
label splashscreen:

    $ splash = True
    scene black
    with Pause(1)

    show text "Terios Krim Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


label start:

    $ maria_point = 0
    $ mandy_point = 0
    $ aynat_point = 0



    # call debuger


    call act1
