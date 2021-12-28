init python:
    import renpy.store as store
    import renpy.exports as renpy

    ## this is the quest class that's used to store the chapters
    class Quest (store.object):
        def __init__(self, name, description, available = False, completed = False, goal = 1):
            self.name = name
            self.description = description
            self.available = available
            self.completed = completed
            self.goal = goal
            self._progressCount = 0

        @property
        def progressCount(self):
            return self._progressCount
        @progressCount.setter
        def progressCount(self, a):
            self._progressCount = a
            if self.progressCount >= self.goal:
                self.completed = True
        def increaseProgressCount(self):
            self.progressCount = self._progressCount + 1

        ## ShouldShow
        def shouldShow(self):
            if self.available and not(self.completed):
                return True
            return False

    ## This is a class for creating a list of quest.
    class QuestList(store.object):
        def __init__(self):
            self.quest_list = []

        def addQuest(self, quest):
            self.quest_list.append(quest)

        def removeQuest(self, quest):
            self.quest_list.remove(quest)

## A variable for the class Quest_List is created.
default my_quests = QuestList()


## quest list
default quest_ms1 = Quest("Ha3oud", "Wait, where am I?", True)
default quest_ms2 = Quest("Wa Nueid", "Let's go back to the beginning ...")
default quest_ms3 = Quest("Shim El Yasmine", "Go see the rice pudding guy.")
default quest_ms4 = Quest("Lil Watan", "Election Day")
default quest_ms5 = Quest("3al 7agez", "What's with the guard? (CW: sexual harassment, prison searches)")
default quest_ms6 = Quest("Ada", "What will you do?")
default quest_farid1 = Quest("Farid 1", "How is Farid doing?")
default quest_mo3tazz1 = Quest("Mo3tazz 1", "Play cards with your brother")
default quest_hanya1 = Quest("Hanya 1", "Isn't that the girl from the protest across the hall?")
default quest_amira1 = Quest("Amira 1", "You have a visitor!")
default quest_ezz1 = Quest("Ezzeldin 1", "Confront Ezzeldin")

## character points

default mo3tazz_points = 0
default farid_points = 0
default amira_points = 0
default hanya_points = 0
default ezz_points = 0
