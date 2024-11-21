label og:
    $ player = "Mc"
    scene bg club_day
    with wipeleft
    show monika 1a at t11 zorder 1
    m "[player], I just wanted to make sure you're enjoying your time at this club."
    m "I would really hate to see you unhappy."
    m 2m "I feel kind of like I'm responsible for that, as President..."
    stop music
    m 4e "And I really do care about you...you know?"
    m "I don't like seeing the other girls give you a hard time."
    m 4r "With how mean Natsuki is and everything..."
    m 4m "And Yuri being a little bit...you know."
    m 5a "Ahaha..."
    m "Sometimes it feels like you and I are the only real people here."
    m "You know what I mean?"
    m 1g "But it's weird, because in all the time you've been here, we've hardly gotten to spend any time together."
    m 1n "Ah...I mean..."
    m "I guess it's technically only been a couple days..."
    m 1l "Sorry, I didn't mean to say something weird!"
    m 1e "There are just some things I've been hoping to talk about with you..."
    m "Things I know only you could understand."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "So that's why--\"{space=5000}{w=0.75}{nw}"
    m 1g "Wait, not yet!\"{space=5000}{w=0.5}{nw}"
    m "No!\"{space=5000}{w=0.5}{nw}"
    m "Stop it!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front




    return