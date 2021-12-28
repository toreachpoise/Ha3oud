label ms2:
        $ quest_ms2.increaseProgressCount()
        scene wa nueid title with fade
        pause
        scene bg uni with fade
        "The president was assassinated yesterday."
        "Clusters of students huddle around campus, arguing in hushed tones."
        "The atmosphere is wound tight with fear. People look over their shoulders as they talk, not sure who is listening or what is acceptable to say."
        "People perform shock and fear, but you wouldn't say that people are sad, exactly. The president was not beloved, but people rightly fear for the nation's stability."
        "After all, he was the nation's first president. He ruled for 30 years."
        "While people might have wanted to see someone different, they are also concerned about what this shakeup might bring."
        scene student council room with dissolve
        "Your brother and his friends are holed up in an empty classroom, debating the day's news."
        show mo3tazz neutral at left
        with dissolve
        m "You don't understand! This is what the people needed! First we had to overthrow the colonizers, and now the old regime. Finally the scene is ripe for socialism to come to our nation."
        show amira neutral at midright
        with dissolve
        a "You're naive and an idiot to boot. This won't usher in the revolution or some utopian crap like that."
        show mo3tazz horny with dissolve
        a "Even if our government collapses, you know the other powerful countries won't allow us to rule ourselves. If one of their puppets isn't in charge, they'd rather see us as a colony again."
        scene assassination with pixellate
        a "Besides, the assassination was clearly by the government itself. How else could they have orchestrated it during a military parade ..."
        a "... and yet had the perpetrators escape? That's amazing luck for a lone gunner ... if that's who it really was."
        scene student council room with pixellate
        show amira neutral at midright
        show mo3tazz neutral at left
        a "Not that the military won't use this as an opportunity to crack down. They will be on high alert for terrorists and dissidents of all stripes to make a public example of."
        show ezz neutral at right
        e "I'm sure that will include any political or leftist groups, not just actual terrorists."
        m "Well, we'd better be on watch for that. We wouldn't want to get caught up."
        show mo3tazz neutral with vpunch
        m "... Actually, that gives me an interesting idea!"
        m "Hey [pov]!"
        show mustafa horny with vpunch
        x "What??"
        hide mustafa horny
        m "Can you go get us some roz bel laban?"
        menu:
            "Get your brother and his friends some rice pudding":
                $ mo3tazz_points += 1
                x "Ugh, sure."
                "You guess you can go get them a snack. It will be nice to go for a walk across campus after being shut up in classrooms all day."
                "And besides, the guy who works at the rice pudding stand is really cute."
                "Maybe you'll get to spend some time with him ..."
                m "Cool, we'll see you after our discussion for film class."
                m "Let's go."
                hide mo3tazz neutral with easeoutleft
                hide ezz neutral with easeoutleft
                hide amira neutral with easeoutleft
                pause
                $ quest_ms2.completed = True
                $ quest_ms3.available = True
                $ quest_mo3tazz1.available = True
                $ quest_amira1.available = True
                jump quest_list
            "Refuse":
                $ amira_points += 1
                x "Why can't I stay? I'm a revolutionary too!!"
                "Amira laughs, covering her mouth but not bothering to stay quiet."
                a "Aww, how cute. The baby thinks %(pronoun_6)s a revolutionary too."
                show mustafa horny with vpunch
                a "You shouldn't let your brother fill your head with revolutionary nonsense, kid. Those who believe themselves to be revolutionaries have a way of finding early deaths."
                "When you glare at her, she winks. You can feel your cheeks are beet red."
                e "Yo, we should actually go to class Mo3tazz."
                "Your brother glances at his watch."
                m "Oh, shit! I guess we should. See you after class, %(pov)s."
                hide mo3tazz neutral with easeoutleft
                hide ezz neutral with easeoutleft
                a "Why did you make such a fuss when we all know you have a crush on the rice pudding guy?"
                a "At least I assume that's why you're there so often."
                a "... Though maybe you're just in love with pudding. That would make sense judging by your love handles."
                label menu_ms2:
                $ time = 5
                $ timer_range = 5
                $ timer_jump = 'menu_ms2_slow'
                show screen countdown
                menu:
                    "Say something biting back":
                        hide screen countdown
                        $ amira_points += 1
                        x "At least something in my life gives me joy."
                        x "Maybe your miserable ass could find something to love too."
                        show amira embarrassed with vpunch
                        pause
                        show amira happy with dissolve
                        a "So you do have a spine ... maybe there is something revolutionary in you after all."
                        a "Anyway, I have to go ..."
                        jump menu_ms2_end
                    "Say nothing":
                        label menu_ms2_slow:
                        hide screen countdown
                        ".........."
                        a "Well, anyway, I have better things to do than simply stand here looking at your dumbstruck face."
                        "Damn it! You can never think of what to say back to Amira. She always gets you so flustered."
                label menu_ms2_end:
                if pronoun_1 == "she":
                    a "Au revoir ma petite pois."
                else:
                    a "Au revoir mon chou fleur."
                "Man, Amira thinks she's so cool, but she's actually kind of mean. You wonder what made her and your brother become friends."
                "She's right though ..."
                "... the rice pudding guy is cute ..."
                pause
                $ quest_ms2.completed = True
                $ quest_ms3.available = True
                $ quest_mo3tazz1.available = True
                $ quest_amira1.available = True
                jump quest_list
