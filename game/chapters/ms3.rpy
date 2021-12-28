label ms3:
    $ quest_ms3.increaseProgressCount()
    scene shim el yasmine title with fade
    pause
    scene bg uni with fade
    show mustafa sketchbook grumpy at right
    with dissolve
    "God, Mo3tazz and his friends always treat you like such a baby. It's infuriating."
    "You're just as much of a revolutionary as any of them. You're the one who read Spectres of Marx in the original French for Mo3tazz for class when he was lazy ..."
    "You're the one who explained to him 'what Deleuze and Guattari were on about.'"
    "And now he can't stop talking about how the ideological state apparatus manufactures the consent of the subaltern."
    "They think they're so badass but they're just kids playing at revolution, just like you."
    "It seems like they're really going to do something now. God! If only they'd included you."
    show mustafa sketchbook happy
    "It's not a total loss though, after all ..."
    show farid closed happy
    with dissolve
    "The rice pudding guy {i}is{/i} cute."
    x "Hi, Farid!"
    f @ happy "Mustafa!"
    show farid neutral with dissolve
    f "Have you heard what happened! The president was assassinated!!"
    x "Farid, I'm pretty sure the whole universe has heard by now."
    x "It is scary, though."
    f @ suspicious "I heard some students saying it may have been the military themselves. I mean--assassinating the president at a military parade! That is so brazen!"
    show mustafa sketchbook neutral with dissolve
    x "Yes it is very strange. Though I think it's not a good idea to talk about things like that in public."
    x "Actually, I was just with a group of like-minded students who are discussing what to do about this--"
    show mustafa sketchbook horny with dissolve
    x "-- if you'd like to come with me?"
    show farid blink horny with dissolve
    pause
    show farid happy with dissolve
    f "I would love to come. Thank you for inviting me!"
    show farid neutral with dissolve
    f "I have about 15 minutes left of my shift ... can you wait until I'm done?"
    menu:
        "Yes":
            $ farid_points += 1
            x "Sure I'll wait, I don't have anywhere to be."
            show farid happy with dissolve
            f "That's great! Please have some rice pudding, on me!"
            "He points you over to a bench across the small campus plaza."
            show farid closed happy with dissolve
            "You eat the rice pudding as you watch Farid chat with another customer. It's coconut and pistachio, your favorite."
            "After that you pull out your sketchbook and begin to draw, but it's hard to focus."
            "Farid is boxing up the toppings and the leftover puddings, wiping down the surfaces of the stall."
            scene bg uni with fade
            "Farid's hand is warm on your shoulder, so much nicer than your bunched backpack smooshed against your face, or the hard bench you're laying on, the stone so cold you can feel it through your shirt."
            show farid closed happy with zoomin
            pause
            show mustafa embarrassed at right
            with vpunch
            "You must have fallen asleep!!"
            x "Aah!! I'm sorry! I didn't mean to!!"
            f @ happy "Hey man, it's okay. You must have been very tired."
            show mustafa blink embarrassed
            with dissolve
            x "I guess so. I did stay up late trying to finish my philosophy reading last night. And my brother's readings, too."
            show mustafa neutral
            show farid happy
            with dissolve
            f "Well, I'm ready to go if your invitation is still open?"
            menu:
                "Yep!":
                    show mustafa happy with dissolve
                    x "Of course!"
                    hide mustafa happy
                    "You walk across campus with Farid. It's dusk and a chilly wind is coming in off the desert. It's the beginning of winter, you can feel it."
                    "Farid is admiring the fig trees heavy with fruit that line the way toward the chemistry building where your brother and his friends are."
                    show farid closed horny with dissolve
                    ## replace iwth farid embarrassed?
                    "He seems to have noticed you watching him."
                    label menu_ms3:
                    $ time = 5
                    $ timer_range = 5
                    $ timer_jump = 'menu_ms3_slow'
                    show screen countdown
                    menu:
                        "Ask him about himself":
                            hide screen countdown
                            $ farid_points += 1
                            x "So Farid, where are you from?"
                            show farid happy with dissolve
                            f "Well, I was born in Delta and that's where most of my family lives. But now I live with my aunt and sister in 3ashwa2eyya."
                            f "What about you?"
                            x "My brother and I grew up in Bahr, but now we live together here in the New City for school."
                            jump menu_ms3_end
                        "Say nothing":
                            hide screen countdown
                            show farid neutral with dissolve
                            f "So, where are you from?"
                            x "My brother and I grew up in Bahr, but now we live together here in the New City for school."
                            label menu_ms3_2:
                            $ time = 5
                            $ timer_range = 5
                            $ timer_jump = 'menu_ms3_end'
                            show screen countdown
                            menu:
                                "Say nothing":
                                    hide screen countdown
                                    $ farid_points -= 1
                                    show farid suspicious with dissolve
                                    pause
                                    jump menu_ms3_end
                                "'What about you?''":
                                    hide screen countdown
                                    x "Where did you grow up, Farid?"
                                    $ farid_points += 1
                                    show farid happy with dissolve
                                    f "Well, I was born in Delta and that's where most of my family lives. But now I live with my aunt and sister in 3ashwa2eyya."
                                    jump menu_ms3_end
                    label menu_ms3_slow:
                        f @ blink horny "Is there something on my face?"
                        show mustafa embarrassed at right
                        with vpunch
                        x "N-no!!"
                        x "Sorry, I just ... got distracted."
                        f "Wow, you must be exhausted."
                    label menu_ms3_end:
                        show farid neutral with dissolve
                        f "Do you stay up late doing your brother's homework often?"
                        show mustafa neutral at right
                        x "Yeah, sometimes I guess."
                        f "That doesn't sound very fair."
                        x "Well, he's learning about a lot of important and interesting stuff as a political science student. And he's a revolutionary!"
                        x "... I guess I'm just glad to help."
                        f @ suspicious "But what about you?"
                        show farid happy with dissolve
                        f "Don't you have your own interests?"
                        x "Eh, I mostly just study."
                        f "I've seen you drawing in that sketchbook of yours."
                        show mustafa embarrassed with vpunch
                        f "I bet you're a really great artist"
                        x "I don't know about that ..."
                        show mustafa neutral with dissolve
                        label menu_ms3_3:
                        $ time = 5
                        $ timer_range = 5
                        $ timer_jump = 'menu_ms3_3_end'
                        show screen countdown
                        menu:
                            "Say nothing":
                                hide screen countdown
                                $ farid_points -= 1
                                show farid suspicious with dissolve
                                pause
                                jump menu_ms3_3_end
                            "'What about you?''":
                                hide screen countdown
                                x "What do you like to do? Aside from make amazing rice pudding of course."
                                $ farid_points += 1
                                show farid happy with dissolve
                                f "I guess I like to make music, and to take care of animals."
                                f @ blink happy "Mostly I like to meet cool new people and get to know them!"
                                "He smiles at you. You realize his eyes are a hazel, almost green color. The afternoon sunlight sparkles in them."
                                show mustafa embarrassed with vpunch
                                "Wait ... did he mean you?? Are you 'cool new people'??"
                                jump menu_ms3_3_end
                        label menu_ms3_3_end:
                            f "Hey, you said it's the chemistry building, right? Is this it?"
                            # mustafa surprised
                            show mustafa neutral with dissolve
                            x "I guess so!"
                            pause
                            $ quest_ms3.completed = True
                            $ quest_ms4.available = True
                            $ quest_farid1.available = True
                            jump quest_list
                "No":
                    $ farid_points -= 1
                    show mustafa grumpy with dissolve
                    x "You know, I think my brother is in class now actually."
                    x "We took too long. They probably won't be there any more."
                    show farid closed sad with dissolve
                    f "Oh ... okay ..."
                    f "I guess I'll see you some other time, %(pov)s."
                    pause
                    $ quest_ms3.completed = True
                    $ quest_ms4.available = True
                    $ quest_farid1.available = True
                    jump quest_list
        "No":
            show mustafa sketchbook grumpy with dissolve
            x "No, I have to go actually."
            show farid closed sad with dissolve
            f "Oh ... okay ..."
            f "I guess I'll see you some other time, %(pov)s."
            pause
            $ quest_ms3.completed = True
            $ quest_ms4.available = True
            $ quest_farid1.available = True
            jump quest_list
