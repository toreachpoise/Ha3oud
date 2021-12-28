label ms5:
  $ quest_ms5.increaseProgressCount()
  "This chapter contains mentions of sexual violence in a prison setting. Would you like to skip it?"
  menu:
    "skip":
        "You will not be able to romance Ezzeldin if you skip this chapter, but you can always come back and replay it another time."
        menu:
            "I don't want to romance Ezz":
                $ quest_ms5.completed
                jump quest_list
            "Actually, maybe I do ...":
                jump ms5_continue
    "continue":
        jump ms5_continue
label ms5_continue:
  scene 3al 7ajez title with fade
  pause
  scene prison cell
  show mo3tazz neutral at midright
  with dissolve
  "This being in jail thing is really starting to get old."
  "You've been here for almost three weeks. Mo3tazz has long since moved on from carving his wooden spoon. He's working on a wooden sculpture that looks suspiciously like the guard."
  "Your shitty dinner comes in through the slot in the door. Watery rice and vegetables cooked to a brown mush. The half loaf of pita bread it comes with is stiff and brittle."
  "You eat with no relish and stare at the ceiling. You wonder if there are birds flying overhead. Through the tiny window you rarely see anything other than the orange-grey sky."
  "You pull out your sketchbook and stubby pencil. You sketch some pigeons, like the ones that live on top of your apartment building."
  "The doorman would let them out every morning, the whole flock bursting from the coop all at once, and then returning together in the evening."
  "You wonder if those birds are flying home right now after a day of scavenging through the city's garbage. You wish you could join them."
  hide mo3tazz neutral with dissolve
  show mustafa sketchbook happy at left
  with dissolve
  "You look up and realize that your brother has fallen asleep. He is face down in a pile of wood shavings, with his little figurine beneath him."
  "You gently pry the knife out of his hand and place it on the bedside table."
  "A herby smell reaches your nose."
  show ezz joint neutral at right
  with dissolve
  "You look up and the guard is watching you, smoking on a fat hand-rolled cigar."
  "Despite the fact that he was your brother's friend, he seems to be acting just like the other guards."
  "Ezz and your brother have flirted back and forth, but he hasn't really helped you. And you're still stuck in prison."
  menu:
    "smoke with him":
      $ ezz_points += 1
      "Nevertheless, you decide to take a chance and strike up a conversation."
      x "Hey, are you gonna pass that or what?"
      "Ezz almost drops the blunt in surprise."
      show ezz joint blink with dissolve
      e "Hey, aren't you supposed to be asleep?"
      show ezz joint neutral with dissolve
      "Despite his protests, he passes you the blunt through the bars."
      show ezz horny with dissolve
      e "I shouldn't be doing this but whatever, it's not like you'll get up to any trouble in here tonight."
      x "Well, thanks I guess."
      show ezz flirty with dissolve
      e "Anything for a cutie like you."
      show mustafa rage with vpunch
      x "Don't flirt with me you piece of shit."
      "Your heart is racing and you feel cold."
      show ezz horny with dissolve
      "Even if this guy is supposedly your brother's friend, he's still been strip searching you every week, patting you down and making jokes with the other guards."
      "When you're naked in front of a crowd of strange men jeering, you realize that being strip searched is exactly the same as being sexually assaulted."
      "Maybe Ezz was kinder than the other guards. Certainly you received better treatment from him than you--"
      if pronoun_1 =="she":
        "--a butch woman--"
      if pronoun_1 == "he":
        "--a trans man--"
      else:
        "--a nonbinary person--"
      "--would have received from any other jail guard."
      "He certainly hadn't been the worst of them, but it certainly left its mark."
      show ezz flirty with dissolve
      e "Hey man, I'm just saying. We could share more than just this joint."
      x "Fuck you. You're just as sick as all the other pigs. Fucking rapists."
      show mustafa sad with dissolve
      "You realize that you're shaking. Your breath is coming in labored spurts."
      "Your face is wet with tears."
      show ezz embarrassed with dissolve
      e "Shit dude. I'm sorry--really--I just--I thought--"
      e "Your--your brother, he's my friend. I'm on your side I swear."
      e "I thought you were cute but I just--"
      show ezz sad with dissolve
      e "... I messed everything up."
      m "Hey, what's going on here?"
      show ezz horny with dissolve
      show mustafa grumpy at midleft
      with move
      show mo3tazz neutral at left
      with moveinleft
      "Your brother is standing behind you, blearily rubbing his eyes."
      if pronoun_1 == "she":
        m "Are you bothering my sister?"
      if pronoun_1 == "he":
        m "Are you bothering my brother?"
      else:
        m "Are you bothering my sibling?"
      m "Stop harassing %(pronoun_2)s."
      "GUARD" "Hey! What's going on down there?"
      show ezz embarrassed with vpunch
      e "Look guys, I'm sorry but we gotta keep it down. %(pov)s I'm sorry. I really am a piece of shit. Mo3tazz, go back to sleep."
      "He races off to reassure the other guard that nothing is happening."
      hide ezz embarrassed
      with moveoutright
      "Your body feels loose somehow, like you're wearing an outfit that's too big. Your breath rattles around in a hollow place. Your brother's voice seems like it's coming from a great distance."
      m "What the hell was that?"
      show mustafa sad at center
      with move
      x "Dude, what the fuck are we doing here? What is the point of this?"
      x "I thought we were trying to be revolutionaries, but this is fucked up shit."
      "Your brother steps toward you and tries to put his hand on your shoulder."
      m "Are you okay, bro?"
      show mustafa rage with hpunch
      "You slap his hand away."
      x "Of course I'm not okay! How is any of this okay?"
      x "We've just been rotting in prison for weeks. You just sit around and do art projects while your creepy friend plays guard and gets to strip search us all."
      show mo3tazz flirty with dissolve
      m "You know, technically this is jail, not prison. Cuz we haven't been tried, see?"
      show mustafa blink embarrassed with dissolve
      show mustafa blink happy with vpunch
      "His tone shocks you into a laugh. Your brother always knows just how to push your buttons."
      show mustafa grumpy with dissolve
      x "Fuck you dude."
      m "No thanks."
      show mo3tazz happy with dissolve
      "Mo3tazz comes to sit on your bunk and holds your shoulders. You lean into the familiar soothing smell of your older brother and it starts to calm you down."
      show mo3tazz neutral with dissolve
      m "Listen, I know you're frustrated and confused. Just know that there is a plan, and the reason you don't know the plan is for your safety."
      x "I'm pretty sure me being here at all is against my safety interests."
      show mo3tazz happy with dissolve
      m "I agree, and I wish you hadn't come. But we both know I couldn't stop you even if I tried."
      "You lay next to your brother side by side on your skinny bunk, like you haven't done since you were kids."
      "His raspy snoring calms you and brings you back to the present."
      scene black with fade
      "You fall asleep just as the sky gets light."
      pause
      $ quest_ms5.completed = True
      $ quest_ms6.available = True
      $ quest_ezz1.available = True
      jump quest_list
    "ignore him":
      "You make awkward eye contact with the guard before he looks away and walks off."
      "What a creep."
      "You wonder what he wanted ..."
      pause
      $ quest_ms5.completed = True
      $ quest_ms6.available = True
      $ quest_ezz1.available = True
      jump quest_list
