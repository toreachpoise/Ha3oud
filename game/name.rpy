label name:
    show mustafa grumpy
    "I've been thinking about changing my name."
    $ pov = renpy.input("What should I call myself?")
    $ pov = pov.strip()
    if pov == "":
        $ pov = "Mustafa"
    "And what are my pronouns?"
    menu:
        "he/him/his":
            $ pronoun_1 = "he"
            $ pronoun_1_cap = "He"
            $ pronoun_2 = "him"
            $ pronoun_2_cap = "Him"
            $ pronoun_3 = "his"
            $ pronoun_3_cap = "His"
            $ pronoun_4 = "his"
            $ pronoun_4_cap = "His"
            $ pronoun_5 = "himself"
            $ pronoun_5_cap = "Himself"
            $ pronoun_6 = "he's"
            $ pronoun_6_cap = "He's"
            $ sibling = "bro"
        "they/them/theirs":
            $ pronoun_1 = "they"
            $ pronoun_1_cap = "They"
            $ pronoun_2 = "them"
            $ pronoun_2_cap = "Them"
            $ pronoun_3 = "their"
            $ pronoun_3_cap = "Their"
            $ pronoun_4 = "theirs"
            $ pronoun_4_cap = "Theirs"
            $ pronoun_5 = "themself"
            $ pronoun_5_cap = "Themself"
            $ pronoun_6 = "they're"
            $ pronoun_6_cap = "They're"
            $ sibling = "sib"
        "she/her/hers":
            $ pronoun_1 = "she"
            $ pronoun_1_cap = "She"
            $ pronoun_2 = "her"
            $ pronoun_2_cap = "Her"
            $ pronoun_3 = "hers"
            $ pronoun_3_cap = "Hers"
            $ pronoun_4 = "hers"
            $ pronoun_4_cap = "Hers"
            $ pronoun_5 = "herself"
            $ pronoun_5_cap = "Herself"
            $ pronoun_6 = "she's"
            $ pronoun_6_cap = "She's"
            $ sibling = "sib"
        "ze/hir/hirs":
            $ pronoun_1 = "ze"
            $ pronoun_1_cap = "Ze"
            $ pronoun_2 = "hir"
            $ pronoun_2_cap = "Hir"
            $ pronoun_3 = "hirs"
            $ pronoun_3_cap = "Hirs"
            $ pronoun_4 = "hirs"
            $ pronoun_4_cap = "Hirs"
            $ pronoun_5 = "hirself"
            $ pronoun_5_cap = "Hirself"
            $ pronoun_6 = "ze's"
            $ pronoun_6_cap = "Ze's"
            $ sibling = "sib"
        "other":
            show pronoun table with dissolve:
                xzoom 1.0 yzoom 1.0
            pause
            hide pronoun table
            show mustafa grumpy at right
            with dissolve

            x "Did you take a picture? We're going to get started now. You can always scroll the mouse wheel or click 'Back' to see the image again."

            label pronoun_system: #This is the copyable pronoun system
                show pronoun table with dissolve:
                    xzoom 0.5 yzoom 0.5
                x "Let's start with replacing 'they'!" #Eli specifies which pronoun form is needed

                label pronoun_label_1:

                    $ pronoun_1 = renpy.input("(Please type out your pronoun on your keyboard and press enter once you're done!)") #This allows the player to type a response to the question.
                    $ pronoun_1 = pronoun_1.strip() #if spaces were left behind the typed pronoun, these are removed
                    $ pronoun_1 = pronoun_1.lower() #regardless of the capitalization in the player's input, it is now lowercase. e.g. if 'They' is the player input, it is now 'they'.
                    $ pronoun_1_cap = pronoun_1.capitalize() #this is a seperate version of the pronoun, where the first letter in the pronoun is uppercase. This makes it possible to start sentences with a pronoun. e.g. if 'they' is the player input, it is now 'They'.

                    if pronoun_1 == "": #if nothing was typed in, Eli will prompt the player to type the pronoun again.
                        x "Sorry, I didn't catch that. Let's try again!"
                        jump pronoun_label_1

                x "Great, let's move on to the 'them'!"

                label pronoun_label_2: #same code structure as pronoun label 1; this can likely be reduced to one label by using a loop of some kind

                    $ pronoun_2 = renpy.input("(Please type out your pronoun on your keyboard and press enter once you're done!)")
                    $ pronoun_2 = pronoun_2.strip()
                    $ pronoun_2 = pronoun_2.lower()
                    $ pronoun_2_cap = pronoun_2.capitalize()

                    if pronoun_2 == "":
                        x "Sorry, I didn't catch that. Let's try again!"
                        jump pronoun_label_2

                show mustafa happy
                with dissolve
                x "You're doing awesome. Just three more now. Let's do 'their'!"

                label pronoun_label_3:

                    $ pronoun_3 = renpy.input("(Please type out your pronoun on your keyboard and press enter once you're done!)")
                    $ pronoun_3 = pronoun_3.strip()
                    $ pronoun_3 = pronoun_3.lower()
                    $ pronoun_3_cap = pronoun_3.capitalize()

                    if pronoun_3 == "":
                        x "Sorry, I didn't catch that. Let's try again!"
                        jump pronoun_label_3

                x "Last two... Time for 'theirs'!"

                label pronoun_label_4:

                    $ pronoun_4 = renpy.input("(Please type out your pronoun on your keyboard and press enter once you're done!)")
                    $ pronoun_4 = pronoun_4.strip()
                    $ pronoun_4 = pronoun_4.lower()
                    $ pronoun_4_cap = pronoun_4.capitalize()

                    if pronoun_4 == "":
                        x "Sorry, I didn't catch that. Let's try again!"
                        jump pronoun_label_4

                show mustafa grumpy
                with dissolve
                x "And the last one! Themself, or themselves."

                label pronoun_label_5:

                    $ pronoun_5 = renpy.input("(Please type out your pronoun on your keyboard and press enter once you're done!)")
                    $ pronoun_5 = pronoun_5.strip()
                    $ pronoun_5 = pronoun_5.lower()
                    $ pronoun_5_cap = pronoun_5.capitalize()

                    if pronoun_5 == "":
                        x "Sorry, I didn't catch that. Let's try again!"
                        jump pronoun_label_5
                show mustafa horny
                with dissolve
                x "Oh I almost forgot! You'll need to input 'your pronoun + to be'. So, for example, 'he's' or 'they're.' We'll use this one for contractions."

                label pronoun_label_6:

                    $ pronoun_6 = renpy.input("(Please type out your pronoun on your keyboard and press enter once you're done!)")
                    $ pronoun_6 = pronoun_6.strip()
                    $ pronoun_6 = pronoun_6.lower()
                    $ pronoun_6_cap = pronoun_6.capitalize()
                    $ sibling = "sib"

                    if pronoun_6 == "":
                        x "Sorry, I didn't catch that. Let's try again!"
                        jump pronoun_label_6
            hide pronoun table
            x "Okay! So if I'm referring to you, I should do it like this:"

            show mustafa happy
            with dissolve

            x "%(pronoun_1_cap)s went to the store this morning, and %(pronoun_1)s took %(pronoun_3)s bike with %(pronoun_2)s." #sample sentences uses all 5 pronouns in context to see if any need to be corrected
            x "That is %(pronoun_3)s bike. %(pronoun_1_cap)s didn't appear to be %(pronoun_5)s today."
            x "I believe that essay is %(pronoun_4)s. %(pronoun_6_cap)s going to submit it later today."
            x "Is that right?"

            menu:

                "Yes!":

                    jump pronoun_success

                "No.":

                    x "Not a worry, I'll try again!"

                    jump pronoun_system
    label pronoun_success:
        show mustafa horny with dissolve
        "You look at yourself in the mirror. With a wry grin, you say:"
        x "Pleased to meet you, [pov]!"
        if pronoun_1 == "he":
            x "Sadboy extraordinaire!"
        if pronoun_1 == "they":
            x "Thembo extraordinaire!"
        if pronoun_1 == "she":
            x "Queen of the gutter!"
        if pronoun_1 == "ze":
            x "Stone butch baddie!"
        if pronoun_1 == "fae":
            x "Fae riot queer!"
        else:
            x "Nonbinary goddexx!"
    jump quest_list
