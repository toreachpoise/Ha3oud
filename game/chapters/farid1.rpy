label farid1:
    $ quest_farid1.increaseProgressCount()
    if farid_points >= 2:
        scene kalam title with fade
        pause
        scene prison cell with dissolve
        "It's late in the afternoon. You're sitting in your cell like always, reading a book."
        "It's a weird story, by some old Italian dude. The book is about a series of characters finding a series of books, each character opening the book and beginning a new chapter, starring a new character, on a quest for another book."
        "And when they open that book--you get the idea."
        "You're just starting to lose interest in this whole premise when a brick moves in the cinderblock wall beside you."
        scene brick wall with pushleft
        "A little shower of dust falls onto your bunk, then the brick is pulled out."
        scene brick wall hole onlayer overlay
        show farid happy behind overlay
        with dissolve
        "Farid's two eyes are visible through the rectangular hole. The effect is a bit like niqab. His bright expression makes you smile."
        f "I thought I heard your voice through there!"
        f "Are you alright?"
        x "I'm physically unharmed, at least. Are you okay?"
        show farid blink horny
        with dissolve
        f "Well, this isn't my first time in jail..."
        show farid happy
        with dissolve
        f "But the processing was certainly nicer than last time."
        x "What? When were you in prison before?"
        show farid blink neutral
        with dissolve
        f "Well, you know, I didn't have the best growing up. I was in and out of jail a lot of times."
        x "Oh wow. I'm so sorry Farid, I had no idea."
        show farid neutral
        with dissolve
        f "It's okay, you know. Just bad luck. Bad situation, bad fate."
        x "Do you really believe that how you turn out is just fate? That everything that happens to us is just based on how you were born?"
        f "Maybe, maybe not. I mean, you don't see Miss Amira in here with us, do you?"
        x "But that's all part of the plan! We need someone on the outside. That's what my brother told me."
        show farid happy
        with dissolve
        f "You know, you're very smart, Mustafa, but you need to use that intelligence for yourself more, instead of being channeled by other people."
        x "Wow, thanks for saying I'm smart."
        show farid blink horny
        with dissolve
        f "You're very smart."
        show farid neutral
        with dissolve
        f "Anyway, I'm sorry if I spoke out of turn. I'm just glad you're okay."
        f "I should probably pretend to be asleep--the guard is coming. Good night, %(pov)s."
        scene brick wall with dissolve
        "Farid replaces the brick quickly. You lie down, feeling a bit flushed. Sure enough, the guard comes by a minute later and looks into your cell."
        scene prison cell with pushright
        show mo3tazz flirty
        "Your brother makes eye contact with you and grins from the opposite bunk."
        "You flop over and bury your hot face in your pillow."
        scene black with fade
        "Farid is so kind and cute. The fact that he was so excited to see you makes your heart rush."
        "Still, you wonder about his childhood. Where he grew up and how it was. It sounds like your own upbringing was very different."
        "... You hope you'll be able to get to know him more."
        pause
        $ quest_farid1.completed = True
        jump quest_list
    else:
        "I wonder if Farid is in here ... Maybe if I had more of a relationship with him, he would check in on me ..."
        menu:
            "replay main story 3?":
                jump ms3
            "eh, I don't really care ...":
                jump quest_list
