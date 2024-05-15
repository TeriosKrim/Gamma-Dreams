define config.developer = "true" 

init:

# This section defines all characters in the game

    
    define m = Character("m_name", color="#faed00", what_prefix='"', what_suffix='"')
    default m_name = "Maria"
    define u = Character("???", what_prefix='"', what_suffix='"')
    define md = Character("md_name", color= "#cf1f1f", what_prefix='"', what_suffix='"')
    default md_name = "Mandy"
    define mc = Character("[name]", what_prefix='"', what_suffix='"')
    define a = Character("Aynat", color= "#a131de", what_prefix='"', what_suffix='"')
    define t = Character("Terios", color= "#444444", what_prefix='"', what_suffix='"')
    define k = Character("Kevin", color= "#14a861", what_prefix='"', what_suffix='"')
    define r = Character("Ren", color= "#de7104", what_prefix='"', what_suffix='"')
    define az = Character("Azul", color= "#a114a8", what_prefix='"', what_suffix='"')
    define g = Character("????", color= "#fa0202", what_prefix='"', what_suffix='"')

# This section defines all BG pics

    define dream_bedroom = "images/characters/BG/interiors/Bg room_morning_light_off.jpg"
    define school_d = "images/characters/BG/School/Bg day01.jpg"
    define school_lab = "images/characters/BG/School/Bg school_science_lab_day01.jpg"
    define portal = "Bg portal.png"
    define mc_bed = 'images/characters/BG/Base/Bed 3.png'
    define base_out = 'images/characters/BG/Base/Building.png'
    define bed2 = 'images/characters/BG/Base/Bed 2.png'
    define bed1 = 'images/characters/BG/Base/Bed 1.png'
    define lab = 'images/characters/BG/Base/Lab 3.png'
    define rooftop_base = 'images/characters/BG/Base/rooftop.png'
    define hallway_base = 'images/characters/BG/Base/Hallway 4.png'
    define sky_day = 'images/characters/BG/Base/Skyline 3.png'
    define sky_midday = 'images/characters/BG/Base/Skyline 4.png'
    define sky_evening = 'images/characters/BG/Base/Skyline 2.png'
    define sky_night = 'images/characters/BG/Base/Skyline 1.png'
    define meeting = 'images/characters/BG/Base/Table 2.png'
    define lobby = 'images/characters/BG/Base/Lobby 2.png'
    define cell = 'images/characters/BG/Base/Cell.png'
    define base = 'images/characters/BG/Base/Computer 1.png'
    define empty_com = 'images/characters/BG/Base/Computer 2.png'

    




# This one defines audios (music and sfx)

    define audio.fire = "audio/fireball Whoosh.mp3"
    define config.main_menu_music = "music/Distant Transmissions.mp3"
    define audio.dreams = "music/Forestdreams.mp3"
    define audio.school = "music/Cutscene normal.mp3"
    define audio.danger = "music/Gate to the rift.mp3"
    define audio.cut = "audio/swordsound2.mp3"
    define audio.punch = "audio/punch 2.Mp3"

# Special effects section

    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')








# Defines all characters expressions

image mandy norm = "images/characters/Mandy/Mandy 1A Normal.png"
image mandy norm2 = "images/characters/Mandy/Mandy 1A Normal2.png"
image mandy away = "images/characters/Mandy/Mandy 1A Away.png"
image mandy away2 = "images/characters/Mandy/Mandy 1A Away2.png"
image mandy happy = "images/characters/Mandy/Mandy 1A happy.png"
image mandy happy2 = "images/characters/Mandy/Mandy 1A happy2.png"
image mandy happy3 = "images/characters/Mandy/Mandy 1A happy3.png"
image mandy happy4 = "images/characters/Mandy/Mandy 1A happy4.png"
image mandy think = "images/characters/Mandy/Mandy 1A think.png"
image mandy think2 = "images/characters/Mandy/Mandy 1A think2.png"
image mandy think3 = "images/characters/Mandy/Mandy 1A think3.png"
image mandy think4 = "images/characters/Mandy/Mandy 1A think4.png"
image mandy upset = "images/characters/Mandy/Mandy 1A upset.png"
image mandy upset2 = "images/characters/Mandy/Mandy 1A upset2.png"
image mandy upsetl = "images/characters/Mandy/Mandy 1A Upsetl.png"
image mandy upsetl2 = "images/characters/Mandy/Mandy 1A Upsetl2.png"

image mandy normb = "images/characters/Mandy/Mandy 1B Normal.png"
image mandy norm2b = "images/characters/Mandy/Mandy 1B Normal2.png"
image mandy awayb = "images/characters/Mandy/Mandy 1B Away.png"
image mandy away2b = "images/characters/Mandy/Mandy 1B Away2.png"
image mandy happyb = "images/characters/Mandy/Mandy 1B happy.png"
image mandy happy2b = "images/characters/Mandy/Mandy 1B happy2.png"
image mandy happy3b = "images/characters/Mandy/Mandy 1B happy3.png"
image mandy happy4b = "images/characters/Mandy/Mandy 1B happy4.png"
image mandy thinkb = "images/characters/Mandy/Mandy 1B think.png"
image mandy think2b = "images/characters/Mandy/Mandy 1B think2.png"
image mandy think3b = "images/characters/Mandy/Mandy 1B think3.png"
image mandy think4b = "images/characters/Mandy/Mandy 1B think4.png"
image mandy upsetb = "images/characters/Mandy/Mandy 1B upset.png"
image mandy upset2b = "images/characters/Mandy/Mandy 1B upset2.png"
image mandy upsetlb = "images/characters/Mandy/Mandy 1B upsetl.png"
image mandy upsetl2b = "images/characters/Mandy/Mandy 1B upsetl2.png"

image mandy Normc = "images/characters/Mandy/Mandy 1C Normal.png"
image mandy Norm2c = "images/characters/Mandy/Mandy 1C Normal2.png"
image mandy awayc = "images/characters/Mandy/Mandy 1C Away.png"
image mandy away2c = "images/characters/Mandy/Mandy 1C Away2.png"
image mandy happyc = "images/characters/Mandy/Mandy 1C happy.png"
image mandy happy2c = "images/characters/Mandy/Mandy 1C happy2.png"
image mandy happy3c = "images/characters/Mandy/Mandy 1C happy3.png"
image mandy happy4c = "images/characters/Mandy/Mandy 1C happy4.png"
image mandy thinkc = "images/characters/Mandy/Mandy 1C think.png"
image mandy think2c = "images/characters/Mandy/Mandy 1C think2.png"
image mandy think3c = "images/characters/Mandy/Mandy 1C think3.png"
image mandy think4c = "images/characters/Mandy/Mandy 1C think4.png"
image mandy upsetc = "images/characters/Mandy/Mandy 1C upset.png"
image mandy upset2c = "images/characters/Mandy/Mandy 1C upset2.png"
image mandy upsetlc = "images/characters/Mandy/Mandy 1C upsetl.png"
image mandy upsetl2c = "images/characters/Mandy/Mandy 1C upsetl2.png"


image maria happy = "images/characters/Maria/Maria 1A Happy.png"
image maria happy2 = "images/characters/Maria/Maria 1A Happy2.png"
image maria happy3 = "images/characters/Maria/Maria 1A Happy3.png"
image maria happy4 = "images/characters/Maria/Maria 1A Happy4.png"
image maria smile = "images/characters/Maria/Maria 1A Smile.png"
image maria smile2 = "images/characters/Maria/Maria 1A Smile2.png"
image maria smile3 = "images/characters/Maria/Maria 1A Smile3.png"
image maria smile4 = "images/characters/Maria/Maria 1A Smile4.png"
image maria away = "images/characters/Maria/Maria 1A Away.png"
image maria away2 = "images/characters/Maria/Maria 1A Away2.png"
image maria confuse = "images/characters/Maria/Maria 1A Confuse.png"
image maria confuse2 = "images/characters/Maria/Maria 1A Confuse2.png"
image maria faint = "images/characters/Maria/Maria 1A Faint.png"
image maria fear = "images/characters/Maria/Maria 1A Fear.png"
image maria fear2 = "images/characters/Maria/Maria 1A Fear2.png"
image maria hurt = "images/characters/Maria/Maria 1A Hurt.png"
image maria hurt2 = "images/characters/Maria/Maria 1A Hurt2.png"
image maria norm = "images/characters/Maria/Maria 1A Normal.png"
image maria sad = "images/characters/Maria/Maria 1A Sad.png"
image maria sad2 = "images/characters/Maria/Maria 1A Sad2.png"
image maria shock = "images/characters/Maria/Maria 1A Shock.png"
image maria sigh = "images/characters/Maria/Maria 1A Sigh.png"
image maria upset = "images/characters/Maria/Maria 1A Upset.png"
image maria upset2 = "images/characters/Maria/Maria 1A Upset2.png"


image maria happyb = "images/characters/Maria/Maria 1B Happy.png"
image maria happy2b = "images/characters/Maria/Maria 1B Happy2.png"
image maria happy3b = "images/characters/Maria/Maria 1B Happy3.png"
image maria happy4b = "images/characters/Maria/Maria 1B Happy4.png"
image maria smileb = "images/characters/Maria/Maria 1B Smile.png"
image maria smile2b = "images/characters/Maria/Maria 1B Smile2.png"
image maria smile3b = "images/characters/Maria/Maria 1B Smile3.png"
image maria smile4b = "images/characters/Maria/Maria 1B Smile4.png"
image maria awayb = "images/characters/Maria/Maria 1B Away.png"
image maria away2b = "images/characters/Maria/Maria 1B Away2.png"
image maria confuseb = "images/characters/Maria/Maria 1B Confuse.png"
image maria confuse2b = "images/characters/Maria/Maria 1B Confuse2.png"
image maria faintb = "images/characters/Maria/Maria 1B Faint.png"
image maria fearb = "images/characters/Maria/Maria 1B Fear.png"
image maria fear2b = "images/characters/Maria/Maria 1B Fear2.png"
image maria hurtb = "images/characters/Maria/Maria 1B Hurt.png"
image maria hurt2b = "images/characters/Maria/Maria 1B Hurt2.png"
image maria normb = "images/characters/Maria/Maria 1B Normal.png"
image maria sadb = "images/characters/Maria/Maria 1B Sad.png"
image maria sad2b = "images/characters/Maria/Maria 1B Sad2.png"
image maria shockb = "images/characters/Maria/Maria 1B Shock.png"
image maria sighb = "images/characters/Maria/Maria 1B Sigh.png"
image maria upsetb = "images/characters/Maria/Maria 1B Upset.png"
image maria upset2b = "images/characters/Maria/Maria 1B Upset2.png"


image maria happyc = "images/characters/Maria/Maria 1C Happy.png"
image maria happy2c = "images/characters/Maria/Maria 1C Happy2.png"
image maria happy3c = "images/characters/Maria/Maria 1C Happy3.png"
image maria happy4c = "images/characters/Maria/Maria 1C Happy4.png"
image maria smilec = "images/characters/Maria/Maria 1C Smile.png"
image maria smile2c = "images/characters/Maria/Maria 1C Smile2.png"
image maria smile3c = "images/characters/Maria/Maria 1C Smile3.png"
image maria smile4c = "images/characters/Maria/Maria 1C Smile4.png"
image maria awayc = "images/characters/Maria/Maria 1C Away.png"
image maria away2c = "images/characters/Maria/Maria 1C Away2.png"
image maria confusec = "images/characters/Maria/Maria 1C Confuse.png"
image maria confuse2c = "images/characters/Maria/Maria 1C Confuse2.png"
image maria faintc = "images/characters/Maria/Maria 1C Faint.png"
image maria fearc = "images/characters/Maria/Maria 1C Fear.png"
image maria fear2c = "images/characters/Maria/Maria 1C Fear2.png"
image maria hurtc = "images/characters/Maria/Maria 1C Hurt.png"
image maria hurt2c = "images/characters/Maria/Maria 1C Hurt2.png"
image maria normc = "images/characters/Maria/Maria 1C Normal.png"
image maria sadc = "images/characters/Maria/Maria 1C Sad.png"
image maria sad2c = "images/characters/Maria/Maria 1C Sad2.png"
image maria shockc = "images/characters/Maria/Maria 1C Shock.png"
image maria sighc = "images/characters/Maria/Maria 1C Sigh.png"
image maria upsetc = "images/characters/Maria/Maria 1C Upset.png"
image maria upset2c = "images/characters/Maria/Maria 1C Upset2.png"

image aynat norm = "images/characters/Aynat/Aynat 1A Normal.png"
image aynat norm2 = "images/characters/Aynat/Aynat 1A Normal2.png"
image aynat away = "images/characters/Aynat/Aynat 1A Away.png"
image aynat away2 = "images/characters/Aynat/Aynat 1A Away2.png"
image aynat fear = "images/characters/Aynat/Aynat 1A Fear.png"
image aynat fear2 = "images/characters/Aynat/Aynat 1A Fear2.png"
image aynat flirt = "images/characters/Aynat/Aynat 1A Flirt.png"
image aynat flirt2 = "images/characters/Aynat/Aynat 1A Flirt2.png"
image aynat flirt3 = "images/characters/Aynat/Aynat 1A Flirt3.png"
image aynat hurt = "images/characters/Aynat/Aynat 1A Hurt.png"
image aynat hurt2 = "images/characters/Aynat/Aynat 1A Hurt2.png"
image aynat hurt3 = "images/characters/Aynat/Aynat 1A Hurt3.png"
image aynat joking = "images/characters/Aynat/Aynat 1A Joking.png"
image aynat scary = "images/characters/Aynat/Aynat 1A Scary.png"
image aynat scary2 = "images/characters/Aynat/Aynat 1A Scary2.png"
image aynat smile = "images/characters/Aynat/Aynat 1A Smile.png"
image aynat smile2 = "images/characters/Aynat/Aynat 1A Smile2.png"
image aynat upset = "images/characters/Aynat/Aynat 1A Upset.png"
image aynat upset2 = "images/characters/Aynat/Aynat 1A Upset2.png"

image azul norm = "images/characters/Azul/Azul 1A norm.png"
image azul norm2 = "images/characters/Azul/Azul 1A norm2.png"
image azul disgust = "images/characters/Azul/Azul 1A disgust.png"
image azul disgust2 = "images/characters/Azul/Azul 1A disgust2.png"
image azul furious = "images/characters/Azul/Azul 1A furious.png"
image azul hurt = "images/characters/Azul/Azul 1A hurt.png"
image azul hurt2 = "images/characters/Azul/Azul 1A hurt2.png"
image azul sad = "images/characters/Azul/Azul 1A sad.png"
image azul sad2 = "images/characters/Azul/Azul 1A sad2.png"
image azul smug = "images/characters/Azul/Azul 1A smug.png"
image azul upset = "images/characters/Azul/Azul 1A upset.png"
image azul upset2 = "images/characters/Azul/Azul 1A upset2.png"
image azul angry = "images/characters/Azul/Azul 1A angry.png"

image azul normb = "images/characters/Azul/Azul 1B norm.png"
image azul norm2b = "images/characters/Azul/Azul 1B norm2.png"
image azul disgustb = "images/characters/Azul/Azul 1B disgust.png"
image azul disgust2b = "images/characters/Azul/Azul 1B disgust2.png"
image azul furiousb = "images/characters/Azul/Azul 1B furious.png"
image azul hurtb = "images/characters/Azul/Azul 1B hurt.png"
image azul hurt2b = "images/characters/Azul/Azul 1B hurt2.png"
image azul sadb = "images/characters/Azul/Azul 1B sad.png"
image azul sad2b = "images/characters/Azul/Azul 1B sad2.png"
image azul smugb = "images/characters/Azul/Azul 1B smug.png"
image azul upsetb = "images/characters/Azul/Azul 1B upset.png"
image azul upset2b = "images/characters/Azul/Azul 1B upset2.png"
image azul angryb = "images/characters/Azul/Azul 1B angry.png"

image azul normc = "images/characters/Azul/Azul 1C norm.png"
image azul norm2c = "images/characters/Azul/Azul 1C norm2.png"
image azul disgustc = "images/characters/Azul/Azul 1C disgust.png"
image azul disgust2c = "images/characters/Azul/Azul 1C disgust2.png"
image azul furiousc = "images/characters/Azul/Azul 1C furious.png"
image azul hurtc = "images/characters/Azul/Azul 1C hurt.png"
image azul hurt2c = "images/characters/Azul/Azul 1C hurt2.png"
image azul sadc = "images/characters/Azul/Azul 1C sad.png"
image azul sad2c = "images/characters/Azul/Azul 1C sad2.png"
image azul smugc = "images/characters/Azul/Azul 1C smug.png"
image azul upsetc = "images/characters/Azul/Azul 1C upset.png"
image azul upset2c = "images/characters/Azul/Azul 1C upset2.png"
image azul angryc = "images/characters/Azul/Azul 1C angry.png"

image e_f = "images/characters/Enemy/female.png"



#All Flags in the game

$ maria_point = 0
$ mandy_point = 0
$ aynat_point = 0
$ playthrough = 0


default playthrough = 0
default mandy_point = 0
default maria_point = 0
default aynat_point = 0
default mandyroute = False
default mariaroute = False
default aynatroute = False
default maria_choice = False
default work = False
default place = False
default black = False
default power = False

define saved = False
define male = False
define persistent.endbad1 = False


#Transform section

transform truecenter:
    zoom 0.4
    xalign 0.5
    yalign 0.3



transform slightleft:
    zoom 0.4
    xalign 0.25
    yalign 0.3


transform center:
    zoom 0.4
    xalign 0.5
    yalign 0.3

transform left:
    zoom 0.4
    xalign 0.0
    yalign 0.3

transform slightright:
    zoom 0.4
    xalign 0.75
    yalign 0.3

transform right:
    zoom 0.4
    xalign 1.0
    yalign 0.3

transform close:
    zoom 0.8
    xalign 0.5
    yalign 0.3



transform move_jump:
    xalign 1.0 yalign 0.0
    pause 1.0
    xalign 0.0
    pause 1.0
    repeat


transform move_slide:
    xalign 1.0 yalign 0.0
    linear 3.0 xalign 0.0
    pause 1.0
    repeat


transform spin:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    rotate 0
    linear 10 rotate 360
    repeat

image vortex:
    "vortex.png"
    xalign 0.5 yalign 0.5
    xanchor 0.5 yanchor 0.5
    rotate 0
    linear 4.0 rotate 360
    repeat



init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

    init:
        $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
