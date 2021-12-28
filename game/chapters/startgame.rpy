# The game starts here.
label start_game:
scene prison cell with fade
"You wake up in a prison cell."
"The cot springs dig harshly into your sides."
"Two guards walk by guffawing together, one of them swings his nightstick as he walks."
"You make eye contact and he winks at you."
"What the hell is going on?"
menu:
    "Set name/pronouns":
        jump name
    "Main Storyline 1":
        jump ms1

label quest_list:
scene prison cell
show mo3tazz cards neutral at left
with dissolve
"Here we are again ..."
"A dark trickle of water runs down the wall in the far corner of your cell ..."
"Mo3tazz is shuffling his cards ..."
"What should I do?"
menu:
    "Name":
        jump name
    "Main Storyline 1" if quest_ms1.shouldShow():
        jump ms1
    "Main Storyline 2" if quest_ms2.shouldShow():
        jump ms2
    "Main Storyline 3" if quest_ms3.shouldShow():
        jump ms3
    "Main Storyline 4" if quest_ms4.shouldShow():
        jump ms4
    "Main Storyline 5" if quest_ms5.shouldShow():
        jump ms5
    "Main Storyline 6" if quest_ms6.shouldShow():
        $ quest_ms6.increaseProgressCount()
        "This is where Main Storyline 6: ?? will go."
        $ quest_ms6.completed = True
        jump quest_list
    "Farid 1" if quest_farid1.shouldShow():
        jump farid1
    "Mo3tazz 1" if quest_mo3tazz1.shouldShow():
        jump mo3tazz1
    "Hanya 1" if quest_hanya1.shouldShow():
        jump hanya1
    "Amira 1" if quest_amira1.shouldShow():
        jump amira1
    "Ezzeldin 1" if quest_ezz1.shouldShow():
        $ quest_ezz1.increaseProgressCount()
        "This is where Ezzeldin 1 will go ... in a future version ..."
        $ quest_ezz1.completed = True
        jump quest_list
    "Redo completed quests":
        jump retry

label retry:
menu:
    "Main storyline 1" if quest_ms1.completed == True:
        jump ms1
    "Main Storyline 2" if quest_ms2.completed == True:
        jump ms2
    "Main Storyline 3" if quest_ms3.completed == True:
        jump ms3
    "Main Storyline 4" if quest_ms4.completed == True:
        jump ms4
    "Main Storyline 5" if quest_ms5.completed == True:
        jump ms5
    "Main Storyline 6" if quest_ms6.completed == True:
        $ quest_ms6.increaseProgressCount()
        "This is where Main Storyline 6: ?? will go."
        $ quest_ms6.completed = True
        jump quest_list
    "Farid 1" if quest_farid1.completed == True:
        jump farid1
    "Mo3tazz 1" if quest_mo3tazz1.completed == True:
        jump mo3tazz1
    "Hanya 1" if quest_hanya1.completed == True:
        jump hanya1
    "Amira 1" if quest_amira1.completed == True:
        jump amira1
    "Ezzeldin 1" if quest_ezz1.completed == True:
        $ quest_ezz1.increaseProgressCount()
        "This is where Ezzeldin 1 will go ... in a future version ..."
        $ quest_ezz1.completed = True
        jump quest_list
return
