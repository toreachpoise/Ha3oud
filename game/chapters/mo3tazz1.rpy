label mo3tazz1:
    $ quest_mo3tazz1.increaseProgressCount()
    scene taxi title with fade
    pause
    scene prison cell
    show mo3tazz cards neutral at midright
    with dissolve
    "You look up from your book to see that your brother is sitting on the opposite bunk, shuffling his ever-present carddeck of cards."
    show mo3tazz cards happy with dissolve
    "He catches your eye and grins."
    "Without saying anything he takes the blanket from his bunk and spreads it on the floor. He sits down, cross-legged."
    m "Wanna play cards, little %(sibling)s?"
    $ carddeck = Deck()
    $ mo3tazz = Player("Mo3tazz", 0)
    $ player = Player("%(pov)s", 0)
    $ carddeck.build()
    menu:
        "play cards":
            $ mo3tazz_points += 1
            label slapjack:
            x "Sure"
            m "Awesome, let's play slap jack."
            "He slowly and deliberately shuffles the deck."
            $ carddeck.shuffle()
            "Mo3tazz divides the deck evenly in half simply by cutting it."
            "You count your hand and to your surprise discover you have exactly twenty-six cards. Mo3tazz is watching you with a lopsided grin."
            m "You always doubt me--I knew I cut the deck right."
            "You begin to play slap-jack."
            "You take turns putting down a card until the card put down is a jack, then you try to smack it first."
            label slapjackdraw:
                menu:
                    "draw a card":
                        $ player.draw(carddeck, 1)
                        $ yourcard = player.hand[0]
                        "You drew the %(yourcard)s"
                        if player.hand[0].value == 11:
                            $ player.discard()
                            jump slap
                        else:
                            $ player.discard()
                            "Now' it's Mo3tazz' turn to draw a card."
                            $ mo3tazz.draw(carddeck, 1)
                            $ mo3tazzcard = mo3tazz.hand[0]
                            "Mo3tazz drew the %(mo3tazzcard)s"
                            if mo3tazz.hand[0].value == 11:
                                $ mo3tazz.discard()
                                jump slap
                            else:
                                $ mo3tazz.discard()
                                jump slapjackdraw
                    "let's be done":
                        x "Actually bro, I'm kind of over this game."
                        m "Fair enough. Want me to read your fortune?"
                        jump fortune
            label slaplose:
                hide screen countdown
                "Mo3tazz smacked the card faster than you. Your hand lands on top of his with a satisfying slap, which is only a small consolation for losing."
                $ mo3tazz.wins +=1
                if mo3tazz.wins > 3:
                    "Maybe I'm bored of this game ..."
                    menu:
                        "stop playing slapjack":
                            x "Hey bro, I think I'm over this."
                            m "No worries, want me to read your fortune?"
                            jump fortune
                        "keep going":
                            jump slapjackdraw
                else:
                    jump slapjackdraw
            label slap:
            if player.wins == 0:
                label slap1:
                $ time = 5
                $ timer_range = 5
                $ timer_jump = 'slaplose'
                show screen countdown
                menu:
                    "Slap":
                        hide screen countdown
                        "You are faster, but Mo3tazz' hand is heavier."
                        "The first time he slams his hand down on top of your fingers with all his might."
                        $ player.wins += 1
                        jump slapjackdraw
            if player.wins == 1:
                label slap2:
                $ time = 1
                $ timer_range = 1
                $ timer_jump = 'secondslap'
                show screen countdown
                menu:
                    "Slap":
                        hide screen countdown
                        $ player.wins += 1
                        jump slapjackdraw
                label secondslap:
                    "The next time the jack appears, you are distracted, and he gets there first."
                    $ mo3tazz.wins += 1
                    "Chastened, he seems not to hit as hard for a few rounds ..."
            if player.wins > 1:
                label slap3:
                $ time = 3
                $ timer_range = 3
                $ timer_jump = 'slaplose'
                show screen countdown
                menu:
                    "Slap":
                        hide screen countdown
                        $ player.wins += 1
                        if mo3tazz.wins >= 1:
                            "Your speed advantage begins to re-assert itself, and he starts to really whack his hand down, struggling for any extra speed."
                        "After a particularly strong hit you shake your hand out."
                        x "Ow, man, too much."
                        "Mo3tazz laughs."
                        m "Sorry %(sibling)s, you're just too fast for me. Again?"
                        menu:
                            "play again":
                                jump slapjackdraw
                            "do something else":
                                x "Nah, I need a break."
                                m "Well, do you want me to read your fortune?"
                                jump fortune
        "no thanks":
            "The last time you played cards with your brother it ended in a fight. Hard pass."
            x "No thanks man."
            show mo3tazz cards neutral with dissolve
            m "Well, do you want me to read your fortune?"
            jump fortune
    label fortune:
    x "Umm ... what?"
    m "It's something Amira has been teaching me. You can use the cards to make predictions about how the future will play out."
    x "Based on the two of you's predictions so far, I don't think you're very good at it."
    m "Oh shut up. It's not like you get to choose what happens in the future."
    m "The way I see it, there are two ways to look at divination: either the cards are telling you a fixed future, or it's just a way to interpret the present, to help you make decisions about what to do next."
    m "What do you think?"
    "What do I think ... ?"
    $ m1answer = renpy.input("What is the point of fortune telling?")
    $ m1answer = m1answer.strip()
    if m1answer == "":
        $ m1answer = "I don't know ..."
    x "%(m1answer)s"
    m "That's an interesting way to look at it."
    m "So, do you want me to read your fortune or not?"
    menu:
        "get fortune read":
            x "Sure, why the hell not?"
            show mo3tazz cards happy with dissolve
            m "That's the spirit!"
            "He shuffles the cards with renewed concentration."
            m "Think of a question--don't tell me what it is. Just keep it in your head."
            m "Do you have your question?"
            menu:
                "no":
                    x "I'm not sure what kind of question to ask."
                    m "It can be anything, but it's best if it's not a yes or no question."
                    m "For example you can ask--'how will I feel about my dinner today?', 'Are we going to get out of here soon?', 'Is my brother losing his mind?'"
                    x "That last one was a yes or no question."
                    m "Whatever. You get the point."
                    m "Do you have a question?"
                    menu:
                        "yes":
                            jump m1yes
                        "no":
                            x "No, I don't have a question."
                            m "Don't put so much pressure on yourself--just ask the first question that comes to mind."
                            "........."
                            menu:
                                "I've got it!":
                                    jump m1yes
                                "I still don't have it.":
                                    m "Hey, no worries dude. Maybe we can try again another time."
                                    m "It's after lights out, anyway. Why don't we just go to bed?"
                                    scene black with dissolve
                                    pause
                                    $ quest_mo3tazz1.completed = True
                                    jump quest_list
                "yes":
                    label m1yes:
                        x "I have my question."
                        $ carddeck.build()
                        $ carddeck.shuffle()
                        "Mo3tazz hands you the deck and asks you to cut it any way you like as you think of your question. You cut it into..."
                        menu:
                            "2":
                                "... two piles ..."
                                jump cut
                            "3":
                                "... three piles ..."
                                jump cut
                            "4":
                                "... four piles ..."
                                jump cut
                        label cut:
                        "... stacking the piles back together in a different order."
                        "Mo3tazz takes the deck from you and fans it out on the ground."
                        m "Pick any three, and place them face down in the order you chose them, from right to left."
                        "You do as he says, drawing three cards and laying them on the blanket."
                        $ player.draw(carddeck, 3)
                        $ player.hand.reading
                        $ card1 = player.hand[0]
                        $ card1reading = player.hand[0].reading
                        m "Okay, flip over your first card. This card represents your past, or the things that have brought you to this point."
                        "You drew the %(card1)s."
                        m "%(card1reading)s"
                        m "What do you think that refers to?"
                        $ cardinterp1 = renpy.input("How does this card relate to your past?")
                        $ cardinterp1 = cardinterp1.strip()
                        if cardinterp1 == "":
                            $ cardinterp1 = "I don't know ..."
                        x "%(cardinterp1)s"
                        if cardinterp1 = "I don't know ...":
                            m "That's okay, you don't have to have an interpretation yet. Actually, it's best if you"
                        else:
                            m "That's really interesting! Though ..."
                        m "try not to pass judgment about what the cards mean until the reading is over."
                        $ card2 = player.hand[1]
                        m "Okay, now flip over your second card, which represents the present, or where you are now ..."
                        "You drew the %(card2)s."
                        m "%(card2.suit_meaning)s %(card2.value_meaning)s"
                        m "What do you think that refers to?"
                        $ cardinterp2 = renpy.input("How does this card relate to your present?")
                        $ cardinterp2 = cardinterp1.strip()
                        if cardinterp2 == "":
                            $ cardinterp2 = "I don't know ..."
                            x "%(cardinterp2)s"
                            if cardinterp2 = "I don't know ...":
                                m "That's okay, you don't have to have an interpretation yet. Actually, it's best if you"
                            else:
                                m "That's really interesting! Though like I said before ..."
                                m "try not to pass judgment about what the cards mean until the reading is over."
                        m "Finally, the last card shows you what is coming in the future ..."
                        $ card3 = player.hand[2]
                        "You drew the %(card3)s."
                        m "%(card3.suit_meaning)s %(card3.value_meaning)s"
                        m "What do you think that refers to?"
                        $ cardinterp3 = renpy.input("How does this card relate to your future?")
                        $ cardinterp3 = cardinterp1.strip()
                        if cardinterp3 == "":
                            $ cardinterp3 = "I don't know ..."
                        x "%(cardinterp3)s"
                        m "Interesting, what do you think the cards mean all together?"
                        $ cardinterp = renpy.input("Apply this reading to your question ...")
                        if cardinterp = "":
                            $ cardinterp = "Dude, none of this makes sense to me ..."
                        if cardinterp = "Dude, none of this makes sense to me ...":
                            m "Sorry %(sibling)s. Thanks for trying it out I guess."
                        else:
                            $ mo3tazz_points += 1
                            m "Nice job dude! See, it's all about assigning meanings to the cards and then using it to make a new intepretation."
                            x "That was pretty fun, actually!"
                            m "Did it make you think differently about your question?"
                            menu:
                                "yes":
                                    $ mo3tazz_points += 1
                                    x "Yeah it definitely did--it gave me another perspective to see my problem from, like archetypes to fit my situation into."
                                    m "Cool!"
                                    jump mo3tazz1end
                                "no":
                                    x "Not really ..."
                                    m "Well, thanks for trying it out, anyway."
                                    jump mo3tazz1end
                        label mo3tazz1end:
                            x "Thanks for teaching me all about fortune reading, big bro!"
                            m "No problem, little %(sibling)s."
                            m "I think we should close it down for the night, though. It's getting late."
                            "Mo3tazz stands up, dusts himself off, shakes out his sheet, and then lays down in bed."
                            "You follow suit, mulling over the cards you got and what they might mean as you dri"
        "no thanks":
            $ mo3tazz_points -= 1
            x "Nah, man, sounds weird."
            m "Fine, suit yourself."
            "Mo3tazz stands up, dusts himself off, shakes out his sheet, and then lays down in bed."
            "You don't speak to each other for the rest of the night."
            "You wonder if you'll ever get out of prison, if you let yourself be led here by two dummies who believe in fortune telling."
            "You look up at the cement ceiling and imagine the sky, for what feels like the thousandth time."
            scene black with dissolve
            pause
            $ quest_mo3tazz1.completed = True
            jump quest_list
