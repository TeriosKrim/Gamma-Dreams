image lib_blink:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_af.png"
        0.035
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_af.png"
        0.065
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_af.png"
        0.095
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_af.png"
        0.035
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_af.png"
        0.035
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blink_am.png"
        0.015
    repeat

image lib_blinkl:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_af.png"
        0.035
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_af.png"
        0.065
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_af.png"
        0.095
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_af.png"
        0.035
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_af.png"
        0.035
        "mod_assets/gov.sdc.libitina_exp/Eyes/_blinkl_am.png"
        0.015
    repeat

   


layeredimage libitina base:
    at Flatten

    group outfit:
        attribute uniform default:
            "mod_assets/gov.sdc.libitina_exp/Poses/1.png"
        attribute regalia:
            "mod_assets/gov.sdc.libitina_exp/Poses/1k.png"

    group mood: 
        attribute happ null # happy
        attribute amus null # amused
        attribute plea null # pleased
        attribute teas null # teaseful/teasing
        attribute flat null # flattered
        
        attribute neut default null # neutral (b)
        attribute unim null # unimpressed
        attribute sad null # sad
        attribute angr null # angry

        attribute neut2 null # neutral 2 (c)
        attribute unsu null # unsure
        attribute conc null # concentraiting
        attribute upse null # upset
        attribute worr null # worried

        attribute lsur null # lightly surprised
        attribute vsur null # very surprised
        attribute vple null # very pleased
        attribute vtea null # very teaseful
        attribute awkw null # awkward
    
    group blush:
        attribute nobl default:
            "mod_assets/gov.sdc.libitina_exp/Blushes/a.png"
        attribute lblu:
            "mod_assets/gov.sdc.libitina_exp/Blushes/b.png"
        attribute blus:
            "mod_assets/gov.sdc.libitina_exp/Blushes/c.png"

    group nose:
        attribute nose_a default:
            "mod_assets/gov.sdc.libitina_exp/Noses/a.png"

    group mouth:
        attribute cm default if_any(['happ', 'amus', 'plea', 'teas', 'flat', 'vsur', 'lsur', 'vple', 'vtea']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/a.png"
        attribute cm default if_any(['neut', 'unim', 'sad', 'angr']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/b.png"
        attribute cm default if_any(['neut2', 'unsu', 'conc', 'upse', 'worr', 'awkw']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/c.png"

        attribute om if_any(['happ', 'vsur', 'flat', 'vple', 'vtea']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/d.png"
        attribute om if_any(['lsur', 'amus', 'plea', 'worr', 'awkw']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/e.png"

        attribute mouth_a:
            "mod_assets/gov.sdc.libitina_exp/Mouths/a.png"
        attribute mouth_b:
            "mod_assets/gov.sdc.libitina_exp/Mouths/b.png"
        attribute mouth_c:
            "mod_assets/gov.sdc.libitina_exp/Mouths/c.png"
        attribute mouth_d:
            "mod_assets/gov.sdc.libitina_exp/Mouths/d.png"
        attribute mouth_e:
            "mod_assets/gov.sdc.libitina_exp/Mouths/e.png"
        attribute mouth_f:
            "mod_assets/gov.sdc.libitina_exp/Mouths/f.png"

        attribute mouth_g:
            "mod_assets/gov.sdc.libitina_exp/Mouths/g.png"

        attribute mouth_h:
            "mod_assets/gov.sdc.libitina_exp/Mouths/h.png"
        attribute mouth_i:
            "mod_assets/gov.sdc.libitina_exp/Mouths/i.png"

        attribute mouth_j:
            "mod_assets/gov.sdc.libitina_exp/Mouths/j.png"
        attribute mouth_k:
            "mod_assets/gov.sdc.libitina_exp/Mouths/k.png"
        attribute mouth_l:
            "mod_assets/gov.sdc.libitina_exp/Mouths/l.png"




        attribute mouth_yand:
            "mod_assets/gov.sdc.libitina_exp/Mouths/yand.png"


    group eyes:
        attribute oe default if_any(['happ', 'neut', 'neut2', 'amus', 'vsur', 'vple', 'plea']):
            "mod_assets/gov.sdc.libitina_exp/Eyes/a.png"
        attribute oe default if_any(['flat', 'unim', 'unsu', 'lsur', 'angr', 'upse', 'worr', 'teas', 'vtea', 'awkw', 'sad', 'conc']):
            "mod_assets/gov.sdc.libitina_exp/Eyes/b.png"

        attribute ce if_any(['happ', 'amus', 'vsur', 'flat', 'lsur', 'teas', 'vtea', 'vple']):
            "mod_assets/gov.sdc.libitina_exp/Eyes/c.png"
        attribute ce if_any(['plea', 'unim', 'unsu', 'sad', 'awkw', 'worr']):
            "mod_assets/gov.sdc.libitina_exp/Eyes/d.png"

        attribute eyes_a:
            "mod_assets/gov.sdc.libitina_exp/Eyes/a.png"
        attribute eyes_b:
            "mod_assets/gov.sdc.libitina_exp/Eyes/b.png"
        attribute eyes_c:
            "mod_assets/gov.sdc.libitina_exp/Eyes/c.png"
        attribute eyes_d:
            "mod_assets/gov.sdc.libitina_exp/Eyes/d.png"
        attribute eyes_white:
            "mod_assets/gov.sdc.libitina_exp/Eyes/white.png"
        attribute eyes_wink:
            "mod_assets/gov.sdc.libitina_exp/Eyes/wink.png"
        attribute eyes_winkd:
            "mod_assets/gov.sdc.libitina_exp/Eyes/wink_d.png"
        attribute eyes_heart:
            "mod_assets/gov.sdc.libitina_exp/Eyes/hearts.png"
        attribute eyes_yand:
            "mod_assets/gov.sdc.libitina_exp/Eyes/yand.png"
        attribute yand_wink:
            "mod_assets/gov.sdc.libitina_exp/Eyes/yand_wink.png"

    
    group eyebrows:
        attribute brow default if_any(["happ", 'neut', 'neut2', 'amus', 'lsur', 'vsur', 'flat', 'umim', 'unsu', 'plea', 'vple', 'conc', 'unim']):
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/a.png"
        attribute brow default if_any(['teas', 'vtea', 'angr', 'upse']):
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/b.png"
        attribute brow default if_any(['sad', 'awkw', 'worr']):
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/c.png"

        attribute eyebrows_a:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/a.png"
        attribute eyebrows_b:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/b.png"
        attribute eyebrows_c:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/c.png"
        attribute eyebrows_d:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/d.png"
        attribute eyebrows_e:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/e.png"

    group blink:
        attribute blink_a default if_not(["ce", "eyes_c", "eyes_d","eyes_wink","eyes_winkd","yand_wink"]):
            "lib_blink"
        attribute no_blink:
            "sprite_blank"



layeredimage libitina leaning:
    at Flatten
    
    group outfit:
        attribute uniform default:
            "mod_assets/gov.sdc.libitina_exp/Poses/2.png"
        attribute yandere:
            "mod_assets/gov.sdc.libitina_exp/Poses/3.png"
        attribute regalia:
            "mod_assets/gov.sdc.libitina_exp/Poses/2k.png"
        attribute regalia_yandere:
            "mod_assets/gov.sdc.libitina_exp/Poses/3k.png"

    group mood: 
        attribute happ null # happy
        attribute amus null # amused
        attribute plea null # pleased
        attribute teas null # teaseful/teasing
        attribute flat null # flattered
        
        attribute neut default null # neutral (b)
        attribute unim null # unimpressed
        attribute sad null # sad
        attribute angr null # angry

        attribute neut2 null # neutral 2 (c)
        attribute unsu null # unsure
        attribute conc null # concentraiting
        attribute upse null # upset
        attribute worr null # worried

        attribute lsur null # lightly surprised
        attribute vsur null # very surprised
        attribute vple null # very pleased
        attribute vtea null # very teaseful
        attribute awkw null # awkward

        attribute yand null # yandere
    
    group blush:
        attribute nobl default:
            "mod_assets/gov.sdc.libitina_exp/Blushes/a2.png"
        attribute lblu:
            "mod_assets/gov.sdc.libitina_exp/Blushes/b2.png"
        attribute blus:
            "mod_assets/gov.sdc.libitina_exp/Blushes/c2.png"

    group nose:
        attribute nose_a default if_not(["yand"]):
            "mod_assets/gov.sdc.libitina_exp/Noses/a2.png"
        attribute nose_b default if_any(["yand"]):
            "mod_assets/gov.sdc.libitina_exp/Noses/a3.png"

    group mouth:
        attribute cm default if_any(['happ', 'amus', 'plea', 'teas', 'flat', 'vsur', 'lsur', 'vple', 'vtea']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/a2.png"
        attribute cm default if_any(['neut', 'unim', 'sad', 'angr']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/b2.png"
        attribute cm default if_any(['neut2', 'unsu', 'conc', 'upse', 'worr', 'awkw']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/c2.png"

        attribute om if_any(['happ', 'vsur', 'flat', 'vple', 'vtea', 'worr', 'awkw']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/d2.png"
        attribute om if_any(['lsur', 'amus', 'plea']):
            "mod_assets/gov.sdc.libitina_exp/Mouths/e2.png"
        attribute om if_any(["yand"]):
            "mod_assets/gov.sdc.libitina_exp/Mouths/a3.png"

        attribute mouth_a:
            "mod_assets/gov.sdc.libitina_exp/Mouths/a2.png"
        attribute mouth_b:
            "mod_assets/gov.sdc.libitina_exp/Mouths/b2.png"
        attribute mouth_b2:
            "mod_assets/gov.sdc.libitina_exp/Mouths/c2.png"
        attribute mouth_c:
            "mod_assets/gov.sdc.libitina_exp/Mouths/d2.png"
        attribute mouth_c2:
            "mod_assets/gov.sdc.libitina_exp/Mouths/e2.png"
        attribute mouth_c3:
            "mod_assets/gov.sdc.libitina_exp/Mouths/k2.png"
        attribute mouth_d:
            "mod_assets/gov.sdc.libitina_exp/Mouths/a3.png"
        attribute mouth_e:
            "mod_assets/gov.sdc.libitina_exp/Mouths/f2.png"
        attribute mouth_f:
            "mod_assets/gov.sdc.libitina_exp/Mouths/g2.png"
        attribute mouth_g:
            "mod_assets/gov.sdc.libitina_exp/Mouths/h2.png"
        attribute mouth_h:
            "mod_assets/gov.sdc.libitina_exp/Mouths/i2.png"
        attribute mouth_i:
            "mod_assets/gov.sdc.libitina_exp/Mouths/j2.png"
        attribute mouth_yand:
            "mod_assets/gov.sdc.libitina_exp/Mouths/yand2.png"
            
    group eyes:
        attribute oe default if_any(['happ', 'neut', 'neut2', 'amus', 'vsur', 'vple', 'plea']):
            "mod_assets/gov.sdc.libitina_exp/Eyes/a2.png"
        attribute oe default if_any(['flat', 'unim', 'unsu', 'lsur', 'angr', 'upse', 'worr', 'teas', 'vtea', 'awkw', 'sad', 'conc']):
            "mod_assets/gov.sdc.libitina_exp/Eyes/b2.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/gov.sdc.libitina_exp/Eyes/a3.png"

        attribute ce if_any(['happ', 'amus', 'vsur', 'flat', 'lsur', 'teas', 'vtea', 'vple']):
            "mod_assets/gov.sdc.libitina_exp/Eyes/c2.png"
        attribute ce if_any(['plea', 'unim', 'unsu', 'sad', 'awkw', 'worr']):
            "mod_assets/gov.sdc.libitina_exp/Eyes/d2.png"

        attribute eyes_a:
            "mod_assets/gov.sdc.libitina_exp/Eyes/a2.png"
        attribute eyes_b:
            "mod_assets/gov.sdc.libitina_exp/Eyes/b2.png"
        attribute eyes_c:
            "mod_assets/gov.sdc.libitina_exp/Eyes/c2.png"
        attribute eyes_d:
            "mod_assets/gov.sdc.libitina_exp/Eyes/d2.png"
        attribute eyes_e:
            "mod_assets/gov.sdc.libitina_exp/Eyes/a3.png"
        attribute eyes_f:
            "mod_assets/gov.sdc.libitina_exp/Eyes/b3.png"
        attribute eyes_g:
            "mod_assets/gov.sdc.libitina_exp/Eyes/c3.png"
    
    group eyebrows:
        attribute brow default if_any(["happ", 'neut', 'neut2', 'amus', 'lsur', 'vsur', 'flat', 'umim', 'unsu', 'plea', 'vple', 'conc', 'unim']):
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/a2.png"
        attribute brow default if_any(['teas', 'vtea', 'angr', 'upse']):
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/b2.png"
        attribute brow default if_any(['sad', 'awkw', 'worr']):
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/c2.png"
        attribute brow default if_any(['yand']):
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/a3.png"

        attribute eyebrows_a:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/a2.png"
        attribute eyebrows_b:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/b2.png"
        attribute eyebrows_c:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/c2.png"
        attribute eyebrows_d:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/a3.png"
        attribute eyebrows_e:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/b3.png"
        attribute eyebrows_f:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/c3.png"
        attribute eyebrows_g:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/d2.png"
        attribute eyebrows_g2:
            "mod_assets/gov.sdc.libitina_exp/Eyebrows/d3.png"

    group blink:
        attribute blink_a default if_not(["ce", "eyes_c", "eyes_d"]):
            "lib_blinkl"
        attribute no_blink:
            "sprite_blank"

    

