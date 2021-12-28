label amira1:
if amira_points >= 1:
    $ quest_amira1.increaseProgressCount()
    scene djinn title with fade
    pause
    scene prison cell with dissolve
    "There's a guard at the end of your cell block, calling out the names for visiting hours."
    "Normally you ignore them, no one ever comes to visit you. But today ..."
    "GUARD" "%(pov)s, you have a visitor! %(pov)s to the visiting room."
    scene visiting room with dissolve
    "You've never gotten a visitor before. Who could it be?"
    show amira neutral at midleft_down with dissolve
    "It's Amira, immaculately dressed as always, looking around at the visiting room like the motes of dust are violating her personal style and sense of hygeine."
    show amira happy with dissolve
    a "Hey, cutie! Hope jail isn't treating you too badly."
    "You stare at her, wondering what she wants."
    show amira neutral with dissolve
    a "Tu ne vas pas me dire 'bienvenue'? Mon chou! Comment bête!"
    "She's eating a candy bar from the vending machine, gripping it delicately with her long fake nails, swinging it around as she talks."
    "Something about her just pisses you off--from her snooty, mediocre French to her condescension."
    show mustafa grumpy at right with dissolve
    x "What are you doing here?"
    show amira embarrassed with dissolve
    a "I can't come check on you? I was worried about how you were doing ..."
    show amira neutral with dissolve
    x "I'm pretty sure you're the reason we're all here."
    show amira rage with dissolve
    a "Hey, shut up!"
    "She's lowered her voice to a hiss and she's looking around suspiciously. She raises her voice for the benefit of the people around as she continues ..."
    show amira happy with dissolve
    a "I'm here for charitable purposes, don't you know? Visiting the degenerates who end up here and ministering to them."
    x "Fuck you, Amira."
    if amira_points == 1:
        jump amira1_continue
    else:
        "She lowers her voice again to a whisper."
        show amira horny with dissolve
        a "Or maybe I just like watching you get flustered."
        "Under the table, you can feel Amira's heel pressing against your calf."
        show mustafa horny with dissolve
        "The thin stiletto travels toward your knee, then to your thigh."
        "Your face flushes red."
        label menu_amira1:
        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'amira1_slow'
        show screen countdown
        menu:
            "Leave":
                hide screen countdown
                $ amira_points -= 1
                show amira sad with dissolve
                a "Hey, wait. I actually didn't come here to harass you."
                a "I'm sorry."
                menu:
                    "No, for real, leave":
                        $ amira_points == 0
                        "You get up and walk away from the visiting room."
                        "When you get back to your cell, you throw yourself on your bed, avoiding eye contact with Mo3tazz and everyone else."
                        scene black with dissolve
                        pause
                        $ quest_amira1.completed = True
                        jump quest_list
                    "Hear what she has to say":
                        show amira neutral with dissolve
                        jump amira1_continue
            "Flirt (mild sexual content)":
                hide screen countdown
                x "You are pretty good at getting me flustered ..."
                a "We did have fun that last night, didn't we?"
                scene black with dissolve
                "The night before the riot, you went to a packed apartment party."
                "Amira was there talking to your brother. He didn't seem to notice her, even though she was wearing some slinky dress you'd seen some Kardashian or another wearing on social media"
                "--reposted by Amira, of course--"
                "not that any influencer could compete with Amira. With every shift of her weight, the skirt threatened to bare her ass."
                "She looked like she had to be suctioned into the dress, and that it could burst at any moment."
                if quest_ms4.completed:
                    "She walked over to Hanya, in the corner,"
                else:
                    "She walked over to a buff hijabi in the corner,"
                "who was absorbed in conversation with three guys you'd never met."
                "Amira tried to get Hanya's attention and failed, clearly becoming frustrated."
                "Looking around, she spotted you staring at her and grinned at you."
                "Her canines were sharp, her gaze hot. You felt like prey."
                "She beelined toward the snack table where you were standing."
                a "Hey, you wanna dance?"
                x "No thanks, I can't."
                a "Come on! Les toutes pouvrons dancer! Here, drink this!"
                "She offered you a drink, maybe the first alcoholic one you'd ever had."
                "Next thing you knew, you were dancing with her."
                "You could feel every part of her body through her dress."
                "She was grinding against you insistently. Pressing back more and more."
                if pronoun_1 == "he":
                    "She seemed to be expecting something that she wasn't feeling behind her."
                    "She spun around and went straight for it, pushing her slim hands down your pants, to discover ... well, not a dick, that's for sure."
                    "Her breath was hot on your neck as she leaned in ..."
                    a "Oh, you should have told me earlier! This makes you way hotter than your brother ..."
                elif pronoun_1 == "ze":
                    "She seems to be expecting something that she's not feeling behind her."
                    "She spun around and went straight for it, pushing her slim hands down your pants, to discover ... well, not a dick, that's for sure."
                    a "Mm, tasty ..."
                else:
                    "She turned around to face you, her breath hot on your neck, pushing her slim hand down your pants to feel your clit."
                    a "Mm, tasty ..."
                "Suddenly, she withdrew her hand and kissed you on the cheek, an oddly chaste move after touching your junk."
                "Then she ran off."
                "Amira's slightly annoyed voice snaps you back to the present."
                show visiting room
                show amira neutral at midleft_down
                with dissolve
                a "Hey, focus, kid--I'm actually not here to flirt."
                jump amira1_continue
        label amira1_slow:
            hide screen countdown
            show amira embarrassed with dissolve
            a "Hey, are you alright?"
            a "Sorry, I didn't come here to harass you ..."
            show amira neutral with dissolve
            jump amira1_continue
    label amira1_continue:
        show mustafa grumpy at right with dissolve
        x "Then what are you here for?"
        a "I wanted to tell you that you'll be getting out soon, if you want. We're getting ready to make our move. You'll finally get to be part of the action, like you wanted."
        x "What does that mean??"
        "She ignores you and continues ..."
        a "... Oh, and I also want to talk to Hanya and your brother, in that order. Would you be a dear and go get them for me?"
        label amira_menu2:
        menu:
            "Who?":
                show amira horny with dissolve
                a "You mean you haven't noticed the stacked hijabi constantly pumping iron in the cell right across from you?"
                show amira neutral with dissolve
                a "The mind is a muscle, you know, %(pov)s. You have to use it, or else it stops working."
                jump amira_menu2
            "Fine, I'll go get them":
                a "You're such a doll."
                a "Au revoir."
                "You feel dismissed, somehow."
                "You get up and go back to your cell."
                scene black with dissolve
                pause
                jump quest_list
            "Screw you, Amira":
                $ amira_points += 1
                show amira horny with dissolve
                a "Who knows, maybe one day you might get to."
                show amira happy with dissolve
                a "... if you can."
                a "Now run along, my pet."
                "You get up and walk away from the visiting room, hoping no one can tell how flustered you are."
                "When you get back to your cell, you throw yourself on your bed, avoiding eye contact with Mo3tazz and everyone else."
                scene black with dissolve
                pause
                $ quest_amira1.completed = True
                jump quest_list
    $ quest_amira1.completed = True
else:
    "Man, wouldn't it be cool if someone you knew on the outside came to visit?"
    "Go back and try to make Amira like you more to unlock this quest..."
    jump quest_list
