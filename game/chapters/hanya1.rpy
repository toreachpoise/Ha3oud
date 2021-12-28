label hanya1:
    $ quest_hanya1.increaseProgressCount()
    scene salam title with fade
    pause
    scene prison cell with dissolve
    "The girl in the cell across from you seems to do nothing but work out."
    show hanya neutral at right with dissolve
    "She was the one from the protest, who gave the speech."
    "She seems to have boundless energy, pumping her rage into the weights."
    "Her thick arms flex underneath her sweater, biceps bulging and relaxing as she does curls."
    "She switches to tricep dips off the edge of her bunk. Her chest jiggles under her hijab as she pumps herself up and down. After a few, she switches to elevated push ups. A strand of hair comes loose from her isharb."
    "You realize you've been staring at her for a while. Your eyes are focused on the pool of sweat in her lower back, visible through her shirts."
    "Just as you realize how long you've been staring, she looks up at you."
    show hanya embarrassed with dissolve
    label menu_hanya1:
    $ time = 3
    $ timer_range = 3
    $ timer_jump = 'hanya1_slow'
    show screen countdown
    menu:
        "Look away":
            hide screen countdown
            $ hanya_points -= 1
            "You look down at your book, rolling over on your bunk in what you hope is a natural fashion."
            hide hanya embarrassed with moveoutright
            "After a few seconds, you hear her go back to working out."
            "Eventually she stops and lays down on her bunk."
            pause
            $ quest_hanya1.completed = True
            jump quest_list
        "Say something":
            hide screen countdown
            "At this point it seems like it would be less creepy to talk to her."
            x "That's one way to keep yourself occupied, Hanya."
            jump hanya1_continue
    label hanya1_slow:
        hide screen countdown
        show hanya neutral with dissolve
        h "Do you want something?"
        x "Sorry! I was just ... amazed by how much you work out."
        $ hanya_points += 1
        show hanya horny with dissolve
        jump hanya1_continue
label hanya1_continue:
    "She shrugs but looks pleased."
    show hanya happy with dissolve
    h "Oh, you know. Just gotta stay in shape somehow while we sit here doing nothing."
    h "I get really restless if I don't exercise or do some kind of physical labor every day."
    x "Have you always worked with your hands?"
    h "Oh yeah. I grew up in the Fertile Delta on a farm."
    h "My dad was in the first revolution, but after decolonization he settled down to farm cotton and vegetables and raise cows."
    show hanya sad with dissolve
    h "After he died, I worked the farm. My mom was very ill."
    h "She always told me that as long as we lived in a free Wilaya, the spirit of my dad--of the revolution--would always be alive."
    show hanya rage with dissolve
    h "Then the president got rid of socialized healthcare, and my mom died."
    show hanya sad with dissolve
    h "I couldn't keep the farm without her. I wasn't their child by blood. I had to come to the city ..."
    x "I'm so sorry, Hanya."
    show hanya neutral with dissolve
    "She shrugs again, this time forced and jerky."
    h "Don't be. It's not your fault."
    h "It's because of the system. Global capitalism, neocolonialism. Our state might have kept its healthcare if it didn't have foreign loan sharks forcing austerity down its throat."
    h "That's why we fight. To preserve the dream of revolution that our ancestors passed down to us."
    "She goes quiet after that."
    "She returns to pumping weights, seemingly lost in her own thoughts."
    "You can't think of anything to say that seems worth breaking her concentration."
    "You go back to the book you were re-reading for a third time. You were only a couple pages from finishing it."
    "When you're done, you sketch for a bit on one of the blank pages at the back of the book."
    hide hanya neutral with moveoutright
    "Hanya eventually stops working out but you feel restless still, weighed down."
    "The world feels like just a knot of oppression and injustice. Your stomach and mind are tangled in the threads."
    "The heavy mood stays with you for the rest of the day."
    scene black with dissolve
    pause
    $ quest_hanya1.completed = True
    jump quest_list
