#Player class
class Player:
    def __init__(self):
        #the main game loop will continue until this is true
        self.gameover = False
        #Name of player
        self.name = ""
        self.level = 1
        #Combat
        self.hp = 100.0
        self.maxhp = 100.0
        self.power = 50 #make sure this is default 50
        self.defense = 0
        self.defeated_enemies = []
        self.location = "b2"
        self.potions = 1
        #Minions and tickets
        self.minions = 0 #make sure this is default 0
        self.tickets = 1
        #Completion Percentage WIP
        self.completion = 0
        #Money
        self.gold = 100
        #Fishing
        self.fishinglimit = 10
        self.fishingrod = False
        self.fish = []
        #Special Items
        self.sneakygloves = False
        self.flute = False
        self.revive = 0
        #Location specific trackers
        self.hometicket = True
        self.dojo = 0
        self.lizardqueen = 0 #0 = never seen, 1 = declined offer to fight, 2 = defeated

