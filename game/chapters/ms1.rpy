label ms1:
    $ quest_ms1.increaseProgressCount()
    scene ha3oud title with fade
    pause
    scene prison cell with dissolve
    "You wake up in a prison cell, again."
    "It's been a few weeks, you don't remember how long exactly."
    "You're being held in the basement of a government building."
    "It's not the proper Medina city jail--it was too close to the protest site where you were arrested. Though of course you don't know the exact location because you were blindfolded when they loaded you into the army police vans."
    "Sometimes you can hear the voices of children and their families laughing outside."
    "There's really no way of finding out where you are, though."
    "It seems like all you can do is just sleep listlessly in your dingy cinderblock cell, laying down and waking up again on the hard cot, wire springs digging into your side."
    "This time you wake up and it's the evening. The orange and pink glow of the polluted sunset filters through the barred window."
    show mo3tazz neutral at left
    with dissolve
    "Your brother is sitting on the cot across from you."
    "The radio next to him is playing slow tarayeb from the 1960s. Abdel Halim's voice croons and soars out the rusty bars."
    "He's got a knife and a piece of dowel. He's carving a wooden spoon with long, smooth strokes. The curled wood shavings are piling about his feet."
    x "How did you even get a knife in here?"
    "Your brother looks up and grins at you with one canine tooth missing."
    "He's had that lopsided grin since you were kids and he broke his tooth on a swimming pool bottom."
    "Your stepdad at the time was a dentist, obsessed with tooth care and hygeine."
    "He kicked your ass for rough housing with your brother, assuming that was the reason for the broken tooth."
    "But it was Mo3tazz's fault then, just as your being in this prison cell is his fault now."
    m "Don't worry about how I got the knife. I have my ways."
    "You roll your eyes."
    show ezz neutral at right
    with vpunch
    e "Hey! Keep it down in there! It's after lights out!"
    "The guard appears behind the barred door. He has a scar on one cheek, and his army uniform is rumpled and not buttoned all the way."
    "The more you look at the guard, the more oddly familiar he seems."
    m "Fuck you, Ezz!"
    show ezz horny with dissolve
    "The guard bangs on the cell door with his knight-stick."
    e "Maybe I will later if you don't watch yourself."
    show mo3tazz horny with dissolve
    "Is this guy one of your brother's friends?? Why would he joke about that?"
    "What the hell is going on here?"
    "How did I let Mo3tazz lead me into this situation?"
    pause
    $ quest_ms1.completed = True
    $ quest_ms2.available = True
    jump quest_list
