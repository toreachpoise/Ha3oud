label ms4:
$ quest_ms4.increaseProgressCount()
scene lil watan title with fade
pause
scene black with dissolve
"A few weeks later an election is  held."
"The head of the military assured the international community that it would be a free and fair election."
"Still, you decided it would be good to join a pollwatching group with your brother and his friends."
scene bg protest with dissolve
"The situation became much more heated when the government announced that the election had been won by the former president's son, by 90 percent of the vote ..."
"... more than six hours before the polls were supposed to close, with thousands of people still in line to vote."
"The city is hot with the smell of chemical weapons. Crowds of people march through the street, surrounded by a growing number of riot police."
"A huge mass of people is gathered in the city square across from the grand museum."
show hanya molotov neutral with dissolve
"A young woman is standing in the center of the crowd, atop a marble plinth. The statue which used to stand on that plinth is laying crumpled on the ground below."
h "... for too long in this nation we have let the military speak for the people."
h "When they revolted against the colonizers who trained and equipped them, we assumed they did that for us. We were happy to let them take charge for us, to install their own men in power. We assumed those were the only ones of us who knew how to be leaders."
h "We called ourselves a liberated republic as we lived for decades under the martial rule of our first and only president. "
show hanya molotov rage with dissolve
extend "We didn't realize that our new masters learned at the feet of the old ones, when they were the colonizers' dogs."
h "We have allowed them to pillage our lands and violate our people just like the colonizers for too long."
h "BUT NO LONGER."
show hanya molotov neutral with dissolve
h "Tonight we must show them the dignity of the people of our nation, our strength and our bravery."
h "We demand justice, we demand freedom, and we'll burn this whole city down if that's what it takes to get it."
menu:
    "protest peacefully":
        hide hanya with easeoutleft
        "It seems like a section of the crowd has separated off to get rowdy. You hear the glass of business windows crashing down the street."
        "People are vandalizing foreign franchises. You can't really blame them. To many they symbolize the way colonialism seems to have hung around in the air..."
        "... how the people can't find stability or solid incomes even after years of so called liberation."
        "Still, you decide to hang back and stay safe."
        "Shortly after people begin entering the businesses to take food and souvenirs, the police move in."
        "They would have done so no matter what. They were just waiting for an excuse."
        "They began to beat and arrest people in the larger crowd, before breaking through to run after the looters."
        jump ms4_end
    "SMASH":
        $ hanya_points += 1
        "You join the growing mass of people streaming toward the foreign business district."
        "Amid the buildings that are hundreds of years old and the crumbling shacks that many of the people now live in, there they are: Pizza Butt, McDogass, Boner King, Starfucks."
        "The neon facades of the new colonialism seem to taunt you, and the crowd."
        show hanya molotov rage with dissolve
        h "Tonight we no longer wait beyond the plate glass of these plastic colonizers, struggling to find enough to eat for lack of their foreign money ..."
        h "... the same foreign money which lines our leaders' pockets ..."
        ## molotov happy??
        h "Tonight we take what we deserve. We will feed our families well, and we will show the government that they will no longer get fat off our backs and then turn around to sell us overpriced petroleum garbage!!"
        show hanya molotov neutral at right
        with move
        "Almost before Hanya is done speaking, groups of people rush toward the various businesses. With crowbars and bricks and with their bare fists they shatter the glass."
        "The smell of tear gas intensifies around you as people rush into the stores and restaurants, leaving with bags of frozen fries, cases of meat, and warm jackets."
        "You notice that people are beginning to scatter. You look up, across the street. A line of riot police are moving towards you."
        hide hanya with easeoutright
label ms4_end:
show mo3tazz rage with moveinright
"Your brother runs toward you, his face contorted with emotion."
m "Run! %(pov)s!! We've got to go!!"
## need mo sad/in pain
"Your brother leads you down an alleyway. Immediately you run into another line of cops."
"He turns and leads you in another direction."
"You realize that Mo3tazz is limping. His pants are ripped and he's leaving dark footprints that may be blood ..."
x "Mo!! Are you hurt?"
m "Dude, don't worry about that. We just have to go!!!!!"
"You keep running. Your breath gets ragged and your brother is struggling to keep pace, barely putting weight on his left leg."
"You move toward him and he swings his arm over your shoulder. Together, the two of you stagger down the sidewalk like a three-legged horse."
show mo3tazz neutral at left with move
"Still, it is quieter. After a few minutes you've managed to get to a place where the tear gas is less and there are no police around."
"... Except for one cop at the end of the alleyway. You try to pull Mo3tazz away, but he keeps moving toward him."
show ezz neutral at right
with dissolve
"Upon closer inspection, you realize it's Ezzeldin. He's standing next to a black box van with tinted windows."
e "Hey guys. You ready, Mo?"
m @ happy "Man, my leg is fucked. But yeah other than that everything is magical."
"Ezz rolls his eyes at Mo3tazz before opening the sliding door of the van. Amira is sitting inside, looking unscathed."
show amira neutral at midright
with dissolve
m "Nice of you to join us, Amira."
a @ happy "You know I'm a behind the scenes person, Mo3tazz."
e "Mo, show me your leg."
"Mo3tazz strips off his pants to reveal a gash on the outside of his left leg. It's long and deep. You can see the blood running all down his leg."
"He sits against the side of the van in his boxers as Ezz patches him up."
show ezz neutral at midleft
with move
m "Oww, man ... careful with that! It burns."
show ezz horny with dissolve
"You're such a whiny baby ..."
"Still, Ezz clearly begins treating Mo3tazz' leg more gently. He cleans the wound, dabs ointment on it, and wraps your brother's leg with a bandage."
"After that he helps Mo3tazz get into the back of the van, before placing a bag over his head."
"Wait, what??"
show ezz flirty at center
show amira happy at right
with move
"Ezzeldin holds out a black cloth bag for you too."
e "Come on, put it on or I gotta put it on for you."
x "What?? Why??"
a "It would look pretty weird if you showed up to jail looking regular and got out of the car on your own, wouldn't it?"
if amira_points >= 1:
    x "Lemme guess, you're not coming though, are you?"
    show amira horny with dissolve
    a "Don't worry, baby. I'll come visit you."
"Against your instincts, you let Ezzeldin place the bag over your head ..."
scene black with dissolve
"He leads you to a van seat and handcuffs you and Mo3tazz together."
"Then he gets in and begins to drive. You travel for what feels like hours through muffled sounds of explosions and shouting."
"At some point he drops Amira off. Ezzeldin drives for a while longer before the van stops. You hear him negotiating with someone in a brusque tone before the van starts again before stopping for a final time."
"He leads you through the back door of a building, down a set of stairs and then through a hallway to a prison cell."
scene prison cell
show mustafa grumpy at left
show mo3tazz neutral at midleft
show ezz neutral at right
with dissolve
e "Okay, act chill. As far as anyone is concerned, you came in an hour ago, there were two guards processing you, and I gave you that cut on your leg."
x "Uh ... okay ..."
show mo3tazz flirty with dissolve
m "Thanks babe."
show ezz horny with dissolve
e "Anytime, hot stuff."
hide ezz with moveoutright
show mo3tazz neutral at right
with move
"You hear Ezz talking to a guard a little up the hall from you."
e "... yeah, the cell on the end is empty, but the second one is full. Shahin and I brought those two in a little while ago."
"Mo3tazz has already picked a bunk and is laying on it. He hisses at you to do the same."
m "Act like you've been here for hours ... just lie down and go to sleep ..."
"guard" "Is all their paperwork in order?"
e "Yep, I straightened it all out, don't worry about them."
"You do what Mo3tazz told you, laying on the squeaky cot opposite him. Your head is spinning with the night's events."
"Half of you wants to keep observing, figure out what is going on and where you are ..."
"... but the other half of you is so tired. Before you even realize, you drift off to sleep ..."
scene black with dissolve
pause
$ quest_ms4.completed = True
$ quest_ms5.available = True
$ quest_hanya1.available = True
jump quest_list
