# The script of the game goes in this file.
init:
    $ timer_range = 0
    $ timer_jump = 0

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mo3tazz", who_color="#660000")
define f = Character("Farid", who_color="#006633")
define e = Character("Ezzeldin", who_color="#330000")
define h = Character("Hanya", who_color="#663366")
define a = Character("Amira", who_color="#993366")
define x = Character("[pov]", who_color="#663300")
define narrator = Character(None, what_color="#003333", what_italics=True)

default pov = "Mustafa"
default pronoun_1 = "they"
default pronoun_1_cap = "They"
default pronoun_2 = "them"
default pronoun_2_cap = "Them"
default pronoun_3 = "their"
default pronoun_3_cap = "Their"
default pronoun_4 = "theirs"
default pronoun_4_cap = "Theirs"
default pronoun_5 = "themself"
default pronoun_5_cap = "Themself"
default pronoun_6 = "they're"
default pronoun_6_cap = "They're"
default sibling = "sib"

transform midleft:
    xalign 0.33
transform midleft_down:
    xalign 0.33
    yalign -0.5
transform midright:
    xalign 0.66
define fade = Fade(1.0, 2.0, 1.0)


##quest system
label start:
$ my_quests.addQuest(quest_ms1)
$ my_quests.addQuest(quest_ms2)
$ my_quests.addQuest(quest_ms3)
$ my_quests.addQuest(quest_ms4)
$ my_quests.addQuest(quest_ms5)
$ my_quests.addQuest(quest_ms6)
$ my_quests.addQuest(quest_farid1)
$ my_quests.addQuest(quest_mo3tazz1)
$ my_quests.addQuest(quest_ezz1)
$ my_quests.addQuest(quest_hanya1)
$ my_quests.addQuest(quest_amira1)

## deck of cards
init python:
    import random

    class Card(object):
        def __init__(self, suit, val):
            self.suit = suit
            self.value = val

        # Implementing build in methods so that you can print a card object
        def __unicode__(self):
            return self.show()
        def __str__(self):
            return self.show()
        def __repr__(self):
            return self.show()

        def show(self):
            if self.value == 1:
                val = "Ace"
            elif self.value == 11:
                val = "Jack"
            elif self.value == 12:
                val = "Queen"
            elif self.value == 13:
                val = "King"
            else:
                val = self.value
            return "{} of {}".format(val, self.suit)

        def reading(self):
            for card in self.hand:
                if self.value == 1:
                    val = "Ace"
                    valuem = "Ace cards refer to a new beginning. It also points toward desire and drive, the motivation to start something new."
                elif self.value == 2:
                    val = self.value
                    valuem = "Two represents coming together, reaching out from your own experience to incorporate another's and create together."
                elif self.value == 3:
                    val = self.value
                    valuem = "Three brings change and impermanence. It incorporates both death and rebirth."
                elif self.value == 4:
                    val = self.value
                    valuem = "Four refers to stability, but it can also mean a situation is too rigid or oppressive."
                elif self.value == 5:
                    val = self.value
                    valuem = "Five represents power and the will to change, but it can also mean violence or conflict is coming."
                elif self.value == 6:
                    val = self.value
                    valuem = "Six is beauty, balance, and adjustment. Like the sun shining over everything, six invites us to find beauty everywhere."
                elif self.value == 7:
                    val = self.value
                    valuem = "Seven invites us to connect with our feelings and to share them with others. We may feel overwhelmed by the tide of our emotions, but we should always remember that we know how to swim."
                elif self.value == 8:
                    val = self.value
                    valuem = "Eight represents communicating outward. If the cards represent a journey of learning, eight is the point where we know enough to tell other people what we have found. Share your knowledge but be careful of how you do it."
                elif self.value == 9:
                    val = self.value
                    valuem = "Nine is the sphere of our imagination. Like the dark side of the moon, we know everything we know is paired with knowledge we have yet to find or create. What can you bring into the world?"
                elif self.value == 10:
                    val = self.value
                    valuem = "Ten represents completion. We have come through our main card journey, and learned all there is. We rest, grounded in reality, before setting off on another adventure ..."
                elif self.value == 11:
                    val = "Jack"
                    valuem = "The jack is a novice. They are enthusiastic and ambitious, but they may show a lack of focus or clumsiness. Things may seem promising, but you have to take care."
                elif self.value == 12:
                    val = "Queen"
                    valuem = "The queen has everything she needs, a manifestation of abundance. Regal, she sits atop her throne and shares her knowledge and resources with the community."
                elif self.value == 13:
                    val = "King"
                    valuem = "The king, like the queen, has everything, but he has become rigid, stilted. He must open himself back up to the people around him, perhaps by embarking on a new journey of discovery?"
                if self.suit == 'Hearts':
                    suitm = "Hearts correspond to the element of water, and refer to emotions, friendship, and potentially romantic relationships."
                elif self.suit == 'Clubs':
                    suitm = "Clubs are the fire element. They represent willpower, strength, ambition, and achievement."
                elif self.suit == 'Diamonds':
                    suitm = "Diamonds represent the earth element, referring to material things like money, safety, and security."
                elif self.suit == 'Spades':
                    suitm = "Spades are the element of air. This suit lets us know what's going on in the realm of ideas and communication."
            return "{} {}".format(suitm, valuem)

    class Deck(object):
        def __init__(self):
            self.cards = []
            self.build()

        # Display all cards in the deck
        def show(self):
            for card in self.cards:
                print card.show()

        # Generate 52 cards
        def build(self):
            self.cards = []
            for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
                for val in range(1,14):
                    self.cards.append(Card(suit, val))

        # Shuffle the deck
        def shuffle(self, num=1):
            length = len(self.cards)
            for _ in range(num):
                # This is the fisher yates shuffle algorithm
                for i in range(length-1, 0, -1):
                    randi = random.randint(0, i)
                    if i == randi:
                        continue
                    self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
                # You can also use the build in shuffle method
                # random.shuffle(self.cards)

        # Return the top card
        def deal(self):
            if self.cards:
                return self.cards.pop()
            else:
                self.build()
                self.shuffle()
                return self.cards.pop()


    class Player(object):
        def __init__(self, name, wins):
            self.name = name
            self.wins = 0
            self.hand = []

        def sayHello(self):
            print "Hi! My name is {}".format(self.name)
            return self

        # Draw n number of cards from a deck
        # Returns true in n cards are drawn, false if less then that
        def draw(self, deck, num=1):
            for _ in range(num):
                card = deck.deal()
                if card:
                    self.hand.append(card)
                else:
                    return False
            return True

        # Display all the cards in the players hand
        def showHand(self):
            print "You drew the {}".format(self.name, self.hand)
            return self

        def discard(self):
            return self.hand.pop()

jump start_game
