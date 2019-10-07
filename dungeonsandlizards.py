#Dungeons and Lizards
#Ted Yarmoski

#This game is not fully completed or fully polished; it was simply a fun learning experience for me that can be
#expanded upon and is still enjoyable


import random
import sys
import os
import time
import msvcrt


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

myplayer = Player()

class suspicious_shop:
    def __init__(self):
        self.inventory = {"colorful flute" : 100, "mysterious amulet" : 150, "sneaky gloves" : 250}
class regular_shop:
    def __init__(self):
        self.inventory = {"fishing rod" : 100,
                          "crude sword" : 100, 
                          "glinting sword" : 970, 
                          "wooden shield" : 50, 
                          "iron shield" : 150, 
                          "health potion" : 35, 
                          "perma-power potion" : 200}


suspicious_shop = suspicious_shop()
regular_shop = regular_shop()

#Title screen options
def title_screen_selections():
    option = input(">>> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "quit", "gelfegg", "please help"]:
        print("Please choose a valid option.")
        option = input(">>> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

#Help menu options
def help_menu_selections():
    option = input(">>> ")
    if option.lower() == ("main menu"):
        title_screen()
    elif option.lower() == ("please help"):
        print("======================================")
        print("    Welcome to Dungeons and Lizards!  ")
        print("======================================")
        print("Fine here you go:")
        print("- Use 'move' to move")
        print("- Use 'look' to look")
        print("- Use 'quit' to quit")
        print("- Use 'inventory' to check inventory")
        print("=========COMBAT=========")
        print("- COMBAT MOVES: Slash High, Slash Low, Parry, Sidestep, Jump")
        print("- In combat, you have a limited time to enter your move depending on the enemy")
        print("- Make sure to enter your combat moves correctly or you will stumble!")
        print("- Remember the Honourable Lizard Code")
        typingh = input("Now type 15 'h' characters without messing up to return to the main menu: ")
        if typingh.lower() == "hhhhhhhhhhhhhhh":
            title_screen()
        else:
            sys.exit()
    while option.lower() not in ["main menu", "please help"]:
        print("CHOOSE A VALID OPTION YOU DINGUS")
        option = input(">>> ")
        if option.lower() == ("main menu"):
            title_screen()
        elif option.lower() == ("please help"):
            print("======================================")
            print("    Welcome to Dungeons and Lizards!  ")
            print("======================================")
            print("Fine here you go:")
            print("- Use 'move' to move")
            print("- Use 'look' to look")
            print("- Use 'quit' to quit")
            print("- Use 'inventory' to check inventory")
            print("=========COMBAT=========")
            print("- COMBAT MOVES: Slash High, Slash Low, Parry, Sidestep, Jump")
            print("- In combat, you have a limited time to enter your move depending on the enemy")
            print("- Make sure to enter your combat moves correctly or you will stumble!")
            print("- Remember the Honourable Lizard Code")
            typingh = input("Now type 15 'h' characters without messing up to return to the main menu: ")
            if typingh.lower() == "hhhhhhhhhhhhhhh":
                title_screen()
            else:
                sys.exit()


def title_screen():
    os.system('cls')
    print("======================================")
    print("    Welcome to Dungeons and Lizards!  ")
    print("======================================")
    print("                -PLAY-                ")
    print("                -HELP-                ")
    print("                -QUIT-                ")
    title_screen_selections()

def help_menu():
    print("======================================")
    print("    Welcome to Dungeons and Lizards!  ")
    print("======================================")
    print("Are you so terrible that you need help??")
    print("           -MAIN MENU-            ")
    print("          -PLEASE HELP-           ")
    help_menu_selections()


def scrolling_text(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.025)

def scrolling_text_slow(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.2)

def scrolling_text_fast(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.01)

def scrolling_text_super_fast(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.001)

def player_item_update():
    player_items = "\nYou now have " + str(myplayer.tickets) + " tickets and " + str(myplayer.minions) + " minions."
    scrolling_text(player_items)

yes_list = ["yes", "affirmative", "sure", "yea", "ye", "ok", "alright", "okay", "roger"]
bonus_names = ["nathan gelfand", "nathan gary gelfand", "nathang", "nathan"]




#MAP
ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "info"
SOLVED = False
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
MAP = """
            ---------------------------------------
              ^   X        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^v^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """

#This is unused, it is serving as a temporary map visual for ted

# solved_places = {'a1' : False, 'a2' : False, 'a3' : False, 'a4' : False,
#                 'b1' : False, 'b2' : False, 'b3' : False, 'b4' : False,
#                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    VVVVVVV
#                 'c1' : False, 'c2' : False, 'c3' : False, 'c4' : False,
#                 'd1' : False, 'd2' : False, 'd3' : False, 'd4' : False,
#                 }

world = {
        'a1' : {
            ZONENAME: "Minion Market",
            DESCRIPTION : "Buying and selling of minions takes place here.",
            EXAMINATION : "The area is very busy and loud.",
            SOLVED : False,
            UP : "",
            DOWN : "b1",
            LEFT : "",
            RIGHT : "a2",
            MAP : """
            ---------------------------------------
              ^   X        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'a2' : {
            ZONENAME: "Your Backyard",
            DESCRIPTION : "A great plantation stretches before you.",
            EXAMINATION : "There is a huge variety of plants present here.",
            SOLVED : False,
            UP : "",
            DOWN : "b2",
            LEFT : "a1",
            RIGHT : "a3",
            MAP:"""
            ---------------------------------------
              ^   0        X        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'a3' : {
            ZONENAME: "River Bank",
            DESCRIPTION : "A quaint place along a calming river.",
            EXAMINATION : "The good fishing spots have been taken by those damn millenials.",
            SOLVED : False,
            UP : "",
            DOWN : "b3",
            LEFT : "a2",
            RIGHT : "a4",
            MAP:"""
            ---------------------------------------
              ^   0        0        X        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'a4' : {
            ZONENAME: "Regular Shop",
            DESCRIPTION : "A shop that appears to be normal.",
            EXAMINATION : "The shop's doors are open.",
            SOLVED : False,
            UP : "",
            DOWN : "b4",
            LEFT : "a3",
            RIGHT : "",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        X      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """

        },
        'b1' : {
            ZONENAME: "Lizard Den",
            DESCRIPTION : "An ominous place said to be occupied by dangerous creatures.",
            EXAMINATION : "You have a feeling that there is danger inside the caves.",
            SOLVED : False,
            UP : "a1",
            DOWN : "",
            LEFT : "",
            RIGHT : "b2",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    X        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'b2' : {
            ZONENAME: "Your Abode",
            DESCRIPTION : "Your beautiful home.",
            EXAMINATION : "It is filled with paintings.",
            SOLVED : False,
            UP : "a2",
            DOWN : "",
            LEFT : "b1",
            RIGHT : "b3",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        X        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'b3' : {
            ZONENAME: "Anime Expo",
            DESCRIPTION : "The ultimate neckbeard gathering place.",
            EXAMINATION : "Wow! There are even SNAFU and Monogatari booths!",
            SOLVED : False,
            UP : "a3",
            DOWN : "",
            LEFT : "b2",
            RIGHT : "b4",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        X        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'b4' : {
            ZONENAME: "Mountain Path",
            DESCRIPTION : "A trail leading into the Southern Mountains.",
            EXAMINATION : "An old man is standing ominously in the middle of the path.",
            SOLVED : False,
            UP : "a4",
            DOWN : "c4",
            LEFT : "b3",
            RIGHT : "",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        X     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'c1' : {
            ZONENAME: "",
            DESCRIPTION : "description",
            EXAMINATION : "info",
            SOLVED : False,
            UP : "",
            DOWN :"d1",
            LEFT : "",
            RIGHT : "c2",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   X        0        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'c2' : {
            ZONENAME: "",
            DESCRIPTION : "",
            EXAMINATION : "",
            SOLVED : False,
            UP : "",
            DOWN : "d2",
            LEFT : "c1",
            RIGHT : "c3",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        X        0        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'c3' : {
            ZONENAME: "",
            DESCRIPTION : "description",
            EXAMINATION : "info",
            SOLVED : False,
            UP : "",
            DOWN : "d3",
            LEFT : "c2",
            RIGHT : "c4",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        X        0     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'c4' : {
            ZONENAME: "High Mountain Pass",
            DESCRIPTION : "This is a dangerous place.",
            EXAMINATION : "The weather is extremely cold and snow covers most of the ground.",
            SOLVED : False,
            UP : "b4",
            DOWN : "d4",
            LEFT : "",
            RIGHT : "",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        X     ^ ^^^^
            ^^^   0        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'd1' : {
            ZONENAME: "",
            DESCRIPTION : "description",
            EXAMINATION : "info",
            SOLVED : False,
            UP : "c1",
            DOWN : "",
            LEFT : "",
            RIGHT : "d2",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   X        0        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'd2' : {
            ZONENAME: "",
            DESCRIPTION : "description",
            EXAMINATION : "info",
            SOLVED : False,
            UP : "c2",
            DOWN : "",
            LEFT : "d1",
            RIGHT : "d3",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        X        0        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'd3' : {
            ZONENAME: "Suspicious Shop",
            DESCRIPTION : "The shop only contains a few oddly specific items.",
            EXAMINATION : "As you enter the shop, the long-haired shopkeeper stares you down.",
            SOLVED : False,
            UP : "",
            DOWN : "",
            LEFT : "",
            RIGHT : "d4",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        X        0      ^^ ^ ^^^
            ---------------------------------------
            """
        },
        'd4' : {
            ZONENAME: "Lonely Passage",
            DESCRIPTION : "There is barely anything here.",
            EXAMINATION : "There is nothing of interest.",
            SOLVED : False,
            UP : "c4",
            DOWN : "",
            LEFT : "d3",
            RIGHT : "",
            MAP:"""
            ---------------------------------------
              ^   0        0        0        0      ^^^^^  
            ^^    0        0        0        0     ^ ^^  ^ ^^                               
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|   |^^^^  ^^^^
            ^ ^   0        0        0        0     ^ ^^^^
            ^^^   0        0        0        X      ^^ ^ ^^^
            ---------------------------------------
            """
        },

        #Hidden locations
        'Dojo' : {
        ZONENAME : "Dojo",
        DESCRIPTION : "A hidden place full of elite fighters.",
        EXAMINATION : "Only the mighty should tread here.",
        SOLVED : False
        }
    

            
            }


###INTERACTIVITY
def print_location():
    print("\n" + "=" * len(world[myplayer.location][DESCRIPTION]))
    name_to_display = world[myplayer.location][ZONENAME].upper()
    scrolling_text_fast(name_to_display)
    description_to_display = "\n" + world[myplayer.location][DESCRIPTION]
    scrolling_text_fast(description_to_display)
    print("\n" + "=" * len(world[myplayer.location][DESCRIPTION]))
    print("\n" + world[myplayer.location][MAP])



def prompt():
    if myplayer.level >= 16:
        congrats = "\nCongrats! You have defeated the enemies that are currently present in the game. This game is unfinished and may see further development in the future. Thank you for playing!"
        scrolling_text(congrats)
        myplayer.gameover = True
    print_location()
    what_would_you_like_to_do = "\nWhat would you like to do?"
    scrolling_text_super_fast(what_would_you_like_to_do)
    action = input(">>> ")
    action_list = ['move', 'look', 'quit', 'inventory', 'help']
    while action.lower() not in action_list:
        you_clearly_need_help_menu = "You clearly need to look at the help menu\n"
        scrolling_text_fast(you_clearly_need_help_menu)
        action = input(">>> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() == 'move':
        player_move()
    elif action.lower() == 'look':
        player_examine()
    elif action.lower() == 'help':
        print("- Use 'move' to move")
        print("- Use 'look' to look")
        print("- Use 'quit' to quit")
        print("- Use 'inventory' to check inventory")
        print("=========COMBAT=========")
        print("- COMBAT MOVES: Slash High, Slash Low, Parry, Sidestep, Jump")
        print("- In combat, you have a limited time to enter your move depending on the enemy")
        print("- Make sure to enter your combat moves correctly or you will stumble!")
    elif action.lower() == 'inventory':
        level = "\nYou are level " + str(myplayer.level)
        scrolling_text_fast(level)
        hp = "\nYour current HP is %d/%d" % (myplayer.hp, myplayer.maxhp)
        scrolling_text_fast(hp)
        gold = "\nYour current gold amount is: " + str(myplayer.gold)
        scrolling_text_fast(gold)
        tickets = "\nYour current Redeem Ticket amount is: " + str(myplayer.tickets)
        scrolling_text_fast(tickets)
        minions = "\nYour current minion count is: " + str(myplayer.minions)
        scrolling_text_fast(minions)
        if myplayer.fishingrod == True:
            rod = "\nYou have a fishing rod."
            scrolling_text_fast(rod)
        if myplayer.potions >= 1:
            potions = "\nYou have {} potions.".format(str(myplayer.potions))
            scrolling_text(potions)
            potion = "\nWould you like to quaff a potion and restore 100 HP?"
            scrolling_text_fast(potion)
            choice = input(">>> ")
            if choice in yes_list:
                myplayer.potions -= 1
                myplayer.hp += 100
                if myplayer.hp > myplayer.maxhp:
                    myplayer.hp = myplayer.maxhp
                health = "\n+100 HP"
                scrolling_text_fast(health)
                current = "\nYour health is now {}.".format(myplayer.hp)
                scrolling_text(current)
            else:
                put = "\nYou put your potions away."
                scrolling_text_fast(put)

def player_move():
    what_direction_would_you_like = "What direction would you like to move?"
    scrolling_text_super_fast(what_direction_would_you_like)
    destination = input(">>> ")
    if destination.lower() == "up":
        if world[myplayer.location][UP] == "":
            print("\nYou cannot go up from here.")
        else:
            destination = world[myplayer.location][UP]
            movement_handler(destination)
    elif destination.lower() == "down":
        if world[myplayer.location][DOWN] == "":
            print("\n You cannot go down from here.")
        elif world[myplayer.location][DOWN] == "c4":
            if old_man in myplayer.defeated_enemies:
                destination = world[myplayer.location][DOWN]
                movement_handler(destination)
            else:
                deal = "\nYou have to deal with the old man first."
                scrolling_text(deal)
        else:
            destination = world[myplayer.location][DOWN]
            movement_handler(destination)
    elif destination.lower() == "left":
        if world[myplayer.location][LEFT] == "":
            print("\n You cannot go left from here.")
        else:
            destination = world[myplayer.location][LEFT]
            movement_handler(destination)
    elif destination.lower() == "right":
        if world[myplayer.location][RIGHT] == "":
            print("\n You cannot go right from here.")
        else:
            destination = world[myplayer.location][RIGHT]
            movement_handler(destination)

        

def movement_handler(destination):
    os.system('cls')
    moved = "\n" + "!!!You have moved to " + world[destination][ZONENAME] + "."
    scrolling_text_super_fast(moved)
    myplayer.location = destination


#returns the player's input within the time
def timer(timeout = 5):
    start_time = time.time()
    print("")
    print(">>> ")
    enter = ""
    while True:
        if msvcrt.kbhit():
            c = msvcrt.getche()
            if ord(c) == 13: # enter_key
                break
            elif ord(c) >= 32: #space_char
                enter += str(c)
        if (time.time() - start_time) > timeout:
            break

    if len(enter) > 0:
        return enter.replace("b'", "").replace("'", "")
    else:
        return "Stumble"


##########COMBAT##############
def combat(enemy, speed = 5):

    ### The system for player input timing out is only fully compatible with command line, did not find other solution to this problem

    #speed is time for player to react (HIGHER SPEED = EASIER FIGHT)
    #type is to pull from a specific list of enemy attack lines
    entering = "\n!!!You are now entering combat!!!"
    scrolling_text(entering)
    dots = "\n\n..."
    scrolling_text_slow(dots)
    os.system('cls')
    #COMBAT:
    while enemy.hp > 0 and myplayer.hp > 0:
        dots = "\n\n..."
        scrolling_text_slow(dots)
        os.system('cls')
        current_player_hp = "\n\nYour current HP is %d/%d" % (myplayer.hp, myplayer.maxhp) 
        current_enemy_hp = "\nEnemy HP is %d/%d" % (enemy.hp, enemy.maxhp)
        scrolling_text_fast(current_player_hp)
        scrolling_text_fast(current_enemy_hp)
        dots = "\n\n..."
        scrolling_text_slow(dots)
        random_key = random.randint(1, len(enemy.movedict))
        random_attack_string = random.randint(0, len(enemy.movedict[random_key]) - 1)
        random_attack = enemy.movedict[random_key][random_attack_string]
        scrolling_text_fast(random_attack)
        #Begin player turn
        action = timer(speed)
        if action.lower() == "slash high":
            if random_key in[1,3]:
                success = "\nSuccessful attack!"
                scrolling_text(success)
                damage_dealt = random.randint(int(myplayer.power / 1.5), myplayer.power)
                damage = "\nYou deal " + str(damage_dealt) + " damage!"
                scrolling_text(damage)
                enemy.hp -= damage_dealt
            else:
                damage_taken = random.randint(int(enemy.power / 1.5), enemy.power) - int(myplayer.defense * enemy.power) 
                take_hit = "\nYou take " + str(damage_taken) + " HP damage."
                myplayer.hp -= damage_taken
                scrolling_text(take_hit)


        elif action.lower() == "slash low":
            if random_key in [2,3]:
                success = "\nSuccessful attack!"
                scrolling_text(success)
                damage_dealt = random.randint(int(myplayer.power / 1.5), myplayer.power)
                damage = "\nYou deal " + str(damage_dealt) + " damage!"
                scrolling_text(damage)
                enemy.hp -= damage_dealt
            else:
                damage_taken = random.randint(int(enemy.power / 1.5), enemy.power) - int(myplayer.defense * enemy.power) 
                take_hit = "\nYou fail and are hurt for " + str(damage_taken) + " HP."
                myplayer.hp -= damage_taken
                scrolling_text(take_hit)

        elif action.lower() == "parry":
            if random_key == 4:
                success = "\nSuccessful counter!"
                scrolling_text(success)
                damage_dealt = random.randint(int(myplayer.power / 1.5), myplayer.power)
                damage = "\nYou deal " + str(damage_dealt) + " damage!"
                scrolling_text(damage)
                enemy.hp -= damage_dealt
            else:
                damage_taken = random.randint(int(enemy.power / 1.5), enemy.power) - int(myplayer.defense * enemy.power) 
                take_hit = "\nYou take " + str(damage_taken) + " points of damage."
                myplayer.hp -= damage_taken
                scrolling_text(take_hit)
        elif action.lower() == "sidestep":
            if random_key == 5:
                if myplayer.sneakygloves == True:
                    success = "\nSuccessful dodge!"
                    scrolling_text(success)
                    damage_dealt = random.randint(int(myplayer.power / 2.5), int(myplayer.power / 2)) 
                    damage = "\nYou dealt " + str(damage_dealt) + " counter damage!"
                    scrolling_text(damage)
                    if myplayer.minions > 0:
                        minion_damage = random.randint(int(myplayer.minions * 8), int(myplayer.minions * 11))
                        minion_damage_text = "\nYour minions dealt " + str(minion_damage) + " additional damage!"
                        scrolling_text(minion_damage_text)
                        enemy.hp -= (damage_dealt + minion_damage)
                    else:
                        enemy.hp -= damage_dealt
                else:
                    success = "\nSuccessful dodge!"
                    scrolling_text(success)
                    if myplayer.minions > 0:
                        minion_damage = random.randint(int(myplayer.minions * 8), int(myplayer.minions * 11))
                        minion_damage_text = "\nYour minions dealt " + str(minion_damage) + " counter damage!"
                        scrolling_text(minion_damage_text)
                        enemy.hp -= (minion_damage)
            else:
                damage_taken = random.randint(int(enemy.power / 1.5), enemy.power) - int(myplayer.defense * enemy.power) 
                take_hit = "\nYou are damaged by " + str(damage_taken) + " HP."
                myplayer.hp -= damage_taken
                scrolling_text(take_hit)
        elif action.lower() == "duck":
            if random_key == 6:
                if myplayer.sneakygloves == True:
                    success = "\nSuccessful dodge!"
                    scrolling_text(success)
                    damage_dealt = random.randint(int(myplayer.power / 2.5), int(myplayer.power / 2)) 
                    damage = "\nYou dealt " + str(damage_dealt) + " counter damage!"
                    scrolling_text(damage)
                    if myplayer.minions > 0:
                        minion_damage = random.randint(int(myplayer.minions * 8), int(myplayer.minions * 11))
                        minion_damage_text = "\nYour minions dealt " + str(minion_damage) + " additional damage!"
                        scrolling_text(minion_damage_text)
                        enemy.hp -= (damage_dealt + minion_damage)
                    else:
                        enemy.hp -= damage_dealt
                else:
                    success = "\nSuccessful dodge!"
                    scrolling_text(success)
                    if myplayer.minions > 0:
                        minion_damage = random.randint(int(myplayer.minions * 8), int(myplayer.minions * 11))
                        minion_damage_text = "\nYour minions dealt " + str(minion_damage) + " counter damage!"
                        scrolling_text(minion_damage_text)
                        enemy.hp -= (minion_damage)
            else:
                damage_taken = random.randint(int(enemy.power / 1.5), enemy.power) - int(myplayer.defense * enemy.power) 
                take_hit = "\nYou face " + str(damage_taken) + " damage."
                myplayer.hp -= damage_taken
                scrolling_text(take_hit)
        elif action.lower() == "jump":
            if random_key == 7:
                if myplayer.sneakygloves == True:
                    success = "\nSuccessful dodge!"
                    scrolling_text(success)
                    damage_dealt = random.randint(int(myplayer.power / 2.5), int(myplayer.power / 2)) 
                    damage = "\nYou dealt " + str(damage_dealt) + " counter damage!"
                    scrolling_text(damage)
                    if myplayer.minions > 0:
                        minion_damage = random.randint(int(myplayer.minions * 8), int(myplayer.minions * 11))
                        minion_damage_text = "\nYour minions dealt " + str(minion_damage) + " additional damage!"
                        enemy.hp -= (damage_dealt + minion_damage)
                    else:
                        enemy.hp -= damage_dealt
                else:
                    success = "\nSuccessful dodge!"
                    scrolling_text(success)
                    if myplayer.minions > 0:
                        minion_damage = random.randint(int(myplayer.minions * 8), int(myplayer.minions * 11))
                        minion_damage_text = "\nYour minions dealt " + str(minion_damage) + " counter damage!"
                        scrolling_text(minion_damage_text)
                        enemy.hp -= (minion_damage)
            else:
                damage_taken = random.randint(int(enemy.power / 1.5), enemy.power) - int(myplayer.defense * enemy.power) 
                take_hit = "\nYou lost " + str(damage_taken) + " HP."
                myplayer.hp -= damage_taken
                scrolling_text(take_hit)
        else:
            damage_taken = random.randint(int(enemy.power / 1.5), enemy.power) - int(myplayer.defense * enemy.power) 
            take_hit = "\nYou stumbled! You are hurt for " + str(damage_taken) + " HP."
            myplayer.hp -= damage_taken
            scrolling_text(take_hit)
        if enemy.hp <= 0:
            line = "\n================="
            scrolling_text(line)
            defeated = "\n\n\n==You are victorious!=="
            scrolling_text(defeated)
            gold = "\nYou have gained " + str(enemy.goldgain) + " gold from combat."
            scrolling_text(gold)
            myplayer.gold += enemy.goldgain
            new = "\nNew gold amount: " + str(myplayer.gold)
            scrolling_text(new)
            if enemy.levelgain > 0:
                myplayer.level += enemy.levelgain
                myplayer.power += 9 * enemy.levelgain
                myplayer.maxhp += 10 * enemy.levelgain
                myplayer.hp += 5 * enemy.levelgain
                level_up = "\n[[[You leveled up! You are now level " + str(myplayer.level) + ".]]]"
                scrolling_text(level_up)
            enemy.hp = enemy.maxhp
            dots = "\n...."
            scrolling_text_slow(dots)
            os.system('cls')
            break
        elif myplayer.hp <= 0:
            if myplayer.revive >= 1:
                revive = "\nYou took fatal damage, but your revival amulet saved you!"
                scrolling_text(revive)
                myplayer.revive -= 1
                myplayer.hp = myplayer.maxhp
            else:
                gameover()            

                





##############ENEMIES#################

##LIZARDS:
class lizard_sentry:
    def __init__(self):
        self.hp = 70
        self.maxhp = self.hp
        self.power = 15
        self.goldgain = 10
        self.levelgain = 0
        self.movedict = {#slash High
                     1 : ["\n\nThe sentry momentarily drops its shield on the ground.", 
                     "\n\nIts sword is near to the ground." ],
                     #slash Low
                     2 : ["\n\nThe lizard lifts its shield to its face.", 
                     "\n\nIt raises its sword to the ceiling."],
                     #slash high or low (resting)
                     3 : ["\n\nThe sentry trips and is stunned for a few seconds."],
                     #Parry
                     4 : ["\n\nIt slashes its sword straight at you.", 
                     "\n\nThe lizard aims right for your face."],
                     #Sidestep
                     5 : ["\n\nThe sentry rapidly charges at you.", 
                     "\n\nIt spits a vertical column of acid at you."],
                     #Duck
                     6 : ["\n\nThe lizard sprays a line of acid from left to right.", 
                     "\n\nThe sentry quickly pulls out a bow and shoots an arrow toward your chest.",],
                     #Jump
                     7 : ["\n\nIt sweeps the ground under your feet with its sword."]
    }

class lizard_guard:
    def __init__(self):
        self.hp = 200
        self.maxhp = self.hp
        self.power = 20
        self.goldgain = 25
        self.levelgain = 1
        self.movedict = {#slash High
                     1 : ["\n\nThe royal guard blocks low with its spear.", 
                     "\n\nSmall helper lizards begin applying protective coating to the guard's legs." ],
                     #slash Low
                     2 : ["\n\nThe lizard raises its spear to its face.", 
                     "\n\nIt is prepared for a high-slashing attack."],
                     #slash high or low (resting)
                     3 : ["\n\nThe guard stops to adjust its royal uniform."],
                     #Parry
                     4 : ["\n\nIt aims toward your face in an attack.", 
                     "\n\nThe lizard performs a standard attack with its spear."],
                     #Sidestep
                     5 : ["\n\nThe guard tries to body slam onto you."],
                     #Duck
                     6 : ["\n\nAs helpers approach with an extra spear, the lizard throws its old one at your face.", 
                     "\n\nHelper lizards throw a flurry of rocks at your face.",],
                     #Jump
                     7 : ["\n\nTiny helper lizards charge at your feet.",
                     "\n\nThe guard sweeps your feet with its spear."]
    }

class lizard_queen:
    def __init__(self):
        self.hp = 555
        self.maxhp = self.hp
        self.power = 50
        self.goldgain = 0
        self.levelgain = 3
        self.movedict = {#slash High
                     1 : ["\n\nShe lashes out, exposing her face."],
                     #slash Low
                     2 : ["\n\nShe puts her claws in an X formation to protect her face."],
                     #slash high or low (resting)
                     3 : ["\n\nThe queen pauses to adjust her crown."],
                     #Parry
                     4 : ["\n\nShe slashes her claw directly at your face.", 
                     "\n\nThe queen swipes at your face."],
                     #Sidestep
                     5 : ["\n\nThe queen triggers a boulder to fall right on top of you.", 
                     "\n\nShe throws a bundle of helper lizards to land on top of you."],
                     #Duck
                     6 : ["\n\nThe queen commands lizard sentries to fire arrows at you.", 
                     "\n\nHelper lizards are rapidly thrown in a straight line toward your face.",],
                     #Jump
                     7 : ["\n\nThe floor is collapsing, get to high ground!"]
    }

##END OF LIZARDS

class sweaty_man:
    def __init__(self):
        self.hp = 100
        self.maxhp = self.hp
        self.power = 20
        self.goldgain = 100
        self.levelgain = 1
        self.movedict = {#slash High
                     1 : ["\n\nHe runs straight toward you with his face exposed.", 
                     "\n\nSprinting toward you, he holds his sword near the ground" ],
                     #slash Low
                     2 : ["\n\nThe man momentarily covers his face and cries an ear-deafening roar for his mommy.", 
                     "\n\nAn anime cosplayer walks by and the man raises his hands in excitement."],
                     #slash high or low (resting)
                     3 : ["\n\nMoving around proves too much for him as he stands still to catch his breath."],
                     #Parry
                     4 : ["\n\nThe man swings his antique Samurai sword directly at you.", 
                     "\n\nHe attempts a complicated screaming, spinning attack which just ends up as a regular sword swing."],
                     #Sidestep
                     5 : ["\n\nWhile running toward you, the man trips and comes hurtling like a massive boulder.", 
                     "\n\nWhile trying his spinning attack, he falls backwards straight toward you."],
                     #Duck
                     6 : ["\n\nThe man pulls anime figurines out of his pocket and throws several at you.", 
                     "\n\nReaching into his anime expo swag bag, the man pulls out origami ninja stars and chucks them at you.",],
                     #Jump
                     7 : ["\n\nHe prepares to sweep the area beneath you with his sword."]
    }

class old_man:
    def __init__(self):
        self.hp = 10
        self.maxhp = self.hp
        self.power = 50
        self.goldgain = 100
        self.levelgain = 1
        self.movedict = {#slash high
                    1 : ["\n\nHis face is exposed."],
                    #slash low
                    2 : ["\n\nHe blocks his upper body.",
                    "\n\nHis legs are exposed."],
                    #slash high or low resting
                    3 : ["\n\nHe rests momentarily."],
                    #parry
                    4 : ["\n\nHe swings his cane at you."],
                    #sidestep
                    5 : ["\n\nHe prepares to lunge straight through you."],
                    #duck
                    6 : ["\n\nHe throws his cane like a boomerang towards your face."],
                    #jump
                    7 : ["\n\nHe throws his cane like a boomerang towards your legs."]
        }

class raccoon:
    def __init__(self):
        self.hp = 350
        self.maxhp = self.hp
        self.power = 35
        self.goldgain = 250
        self.levelgain = 1
        self.movedict = {#slash high
                    1 : ["\n\nThe raccoon gets on its hind legs to prepare for an attack."],
                    #slash low
                    2 : ["\n\nIt sniffs the ground to get your scent.", "\n\nThe raccoon gets low to the ground for an attack."],
                    #slash high or low resting
                    3 : ["\n\nThe raccoon stumbles backwards and leaves itself open."],
                    #parry
                    4 : ["\n\nIt slashes its claws directly at you."],
                    #sidestep
                    5 : ["\n\nThe raccoon falls on top of you, aiming to crush you with its belly."],
                    #duck
                    6 : ["\n\nIts claws slash for your head.", "\n\nIt slashes high."],
                    #jump
                    7 : ["\n\nIt slashes low.", "\n\nThe raccoon tries to reach for your feet.", "It aims for your legs."],

        }

class proud_warrior:
    def __init__(self):
        self.hp = 300
        self.maxhp = self.hp
        self.power = 75
        self.goldgain = 400
        self.levelgain = 2
        self.movedict = {#slash high
                    1 : ["\n\nHe drags his warhammer behind his feet while approaching you.", 
                    "\n\nHe winds up for an attack with his hammer at a low position."],
                    #slash low
                    2 : ["\n\nThe warrior heaves his hammer onto his shoulder and prepares to block.",
                    "\n\nHe brings the hammer to his face."],
                    #slash high or low resting
                    3 : ["\n\nHe takes a moment to catch his breath."],
                    #parry
                    4 : ["\n\nHe swings the hammer directly at you.",
                    "\n\nThe hammer comes directly at you."],
                    #sidestep
                    5 : ["\n\nHis hammer swings down on a trajectory to crush you.",
                    "\n\nThe hammer comes down about to crush your puny body."],
                    #duck
                    6 : ["\n\nThe warrior executes a swinging uppercut.", 
                    "He swings right for your face."],
                    #jump
                    7 : ["\n\nThe warrior tries to sweep you off of your feet.", 
                    "He tries to kick you down and make you unstable."]
        }

class shadow_figure:
    def __init__(self):
        self.hp = 300
        self.maxhp = self.hp
        self.power = 70
        self.goldgain = 850
        self.levelgain = 3
        self.movedict = {#slash high
                    1 : ["\n\n"]






        }

class corrupted_demon:
    def __init__(self):
        self.hp = 500
        self.maxhp = self.hp
        self.power = 70
        self.goldgain = 1000
        self.levelgain = 4
        self.movedict = {#slash high
                    1 : ["\n\nS̶͖͕̟̹͙̗̟͐̂ͅͅL̷̡̡̙͍͎̩̱͇̦͕͍̿͌͝Ą̶̨̛͚̰̱͔͇͉͙̽̏͐͆̂̀̄̓̒̒͜͝S̸͖̮̰͕̫͖̱̰̾͋̿͘̚H̵͎́͌́̓͂̉͐͘͘ ̷̧̠͇̜̇̊͋͊̔́̿͗Ḧ̵̡̘͔̮̟̻͈̟̺̞͂̄͐́̆̓̽̂̕I̵̡̫̮̲̣̠̜͂G̵̗͖͙̦͓̹̣͎͔̙̠̔̽̈́͝H̴̩̥̠̤̄͆̅͂̔̑̑̊͌̾͘͘͝"],



                    2 : ["\n\nŞ̸̧̼̺͍̃́̀̄̽̓̀̋̈́͑̈́̕L̶̡̨̛͉̰͈͎̬̣̗̜͖̼̖̽͗͑̇̈́̔̅̔͊̓͒̈́͝͠A̴̝̲͈̜͛͐̄̄́̈͑͐̿͝S̷̡̛͎̱̮͉͙̩̪̖̹̫͑̓́͑̿̉̈́̈́̎̊̆́́̿͊̍Ȟ̵̹̟̥͇̓͘͝ ̶̧̭̬̲̟̻̤̩̠̖̰̯̫̭͕͑͌̉̍͊̏͐̆̓̊͝͠Ḽ̵̨̭͚̤̪̹͍̥̮̘̪̔͛͜O̸̧̨̠̦̫͇͙̤̺̰̩̭͉͓̞͈̍̍̂W̶̬̝̳̘͈̻̬̙͍̠͇̣͂̌̌̃̐̆̀̋̉͋͋̽͝͝"],


                   
                    3 : ["\n\nŞ̴̯̦̱̻̠͍̩͋̅̎̀̑͋̋ͅL̴̨̧͍̬͖͙̞̯̀́̄̋̉̑̒̆́̚͜͠ͅẠ̴̟͈̦̿̓̉͊̈́̔̉͐̅̚͘̚ͅS̶̛͚̲̜̦͉̰̺̻̼͚̔͑̒́́̀̆̿̕̕̚͜ͅͅH̴̨̫̅̏̓͊̎̇͗̚͝"],


                    4 : ["\n\nP̶̡̛̜̦̫̫͖̠̬͎͕̩̱̝̳̪̬͊̇̈́͐͌͑͌̅̏́̏̀̚͠Ă̶̗̙̆̽̐̆̿̈͗̍͑̆͋̃̎͘̕͜͝ͅR̶̙̫̩̀̎̈̏̇́͆͐͗̂͗́̽̃̉̏͜͝R̴̨̨̨͎̝̹̘͔̭̦͉̙̗͔̲̽̀͆͜ͅY̷̧̦̳̔̈́́́̑͘"],


                    5 : ["\n\nS̵̰̒̂͠Į̵͙͎̯̹͙̠̻̉̅͆͗̇̑͋͒̉͒͋͗̌͛̕͘̚ͅḊ̴͉͍̠̳̥̘̻̰̻̿̽͐̒̔͑̍̅̄̂͗̕̕͝Ȩ̶̪̭̘̞͕̪͇̯̿́͆̄̀́̉͝S̸̨̟̖̪͓͈̖͎͑̔͑͒̀̊Ṭ̴̢̧͚̝̥̮͍͓̺̏́̐̽͋̆̈́̚Ĕ̵̛͔͍̤̩̰̩̔̈̈̒̐́̒̒̀̿̅͠P̴̧̮͎̝̯̝͎͒̓̾̔̇̄͒̑͗̒̒"],


                    6 : ["\n\nḐ̶̞͍̎͛̓̒͌͋̂͊͗̒̂͌͘Ǔ̷̢͇̯͇͚̹̖͙̘͎̿̎̊̎́̊̾̄̈́̓̓̅̌͐͜͠C̴̢̫̩̻̠̳̬̹̜̦̳̳͆͜ͅK̴̖̻̠̄̽̈́̃̐̕͝"],


                    7 : ["\n\nJ̵̧̛̻̣͓͓̞̫̞̼̯̫̏̎̽͂̎̿̌̌̌͒̽͜͜ͅỤ̶̧̨̢̡̡͖̲̩̝͖̤͔̿̾̀̽͂̋̈́̔̚͜͝ͅM̷͎̩̎̀̆̀̿͝P̵̧̑̾͒̿̏̎̐̇͋̓́̓̕̕͠͝"]
                    }

###Instantiation for enemies
lizard_sentry = lizard_sentry()
lizard_guard = lizard_guard()
lizard_queen = lizard_queen()
sweaty_man = sweaty_man()
old_man = old_man()
raccoon = raccoon()
proud_warrior = proud_warrior()
corrupted_demon = corrupted_demon()

############

def player_examine():
    os.system('cls')
    examining = "\n!!!Inspecting location"
    scrolling_text(examining)
    line = "\n" + "=" * len(world[myplayer.location][EXAMINATION])
    scrolling_text_super_fast(line)
    examination_text_print = "\n" + world[myplayer.location][EXAMINATION]
    scrolling_text(examination_text_print)

    bonus_names = ["Nathan Gelfand", "Nathan Gary Gelfand", "NathanG"]
    yes_list = ["yes", "affirmative", "sure", "yea", "ye", "ok", "alright", "okay", "roger"]

    if world[myplayer.location][SOLVED]:
        this_area_already_explored = "\nThis area has been exhausted."
        scrolling_text(this_area_already_explored)
    else:
        this_place_is_unexplored = "\n..."
        scrolling_text(this_place_is_unexplored)
        #events for minion market a1
        if world[myplayer.location][ZONENAME] == "Minion Market":
            if myplayer.name.lower() in bonus_names:
                frequent = "\nThis is your favorite place."
                scrolling_text(frequent)
            if myplayer.name.lower() == "nathang":
                greetings = "\nHello Nathan!"
                scrolling_text(greetings)
            else:
                greetings = "\nHello " + myplayer.name.title() + "!"
                scrolling_text(greetings)
            question_purchase = "\nMinion Master: Would you like to make a purchase?"
            scrolling_text(question_purchase)
            response = input(">>> ")
            if response.lower() == "yes":
                if myplayer.name.lower() in ["nathan gelfand", "nathan gary gelfand", "nathan"]:
                    valuable_customer = "\nMinion Master: Ah yes, our most valuable customer! Have one on us!"
                    scrolling_text(valuable_customer)    
                    myplayer.minions += 1
                    minions_count_minion_market_1 = "(You now have " + str(myplayer.minions) + " minions.)"
                    scrolling_text(minions_count_minion_market_1)
                    myplayer.name = "NathanG"
                else:
                    purchase_cost_ticket = "\nMinion Master: A purchase is going to cost you a Redeem Ticket."
                    scrolling_text(purchase_cost_ticket)
                    if myplayer.tickets > 0:
                        print("")
                        print("===========")
                        oh_you_have_ticket = "\nMinion Master: Oh, you have a ticket!"
                        scrolling_text(oh_you_have_ticket)
                        how_many_would_you_like = "\nMinion Master: How many would you like?"
                        scrolling_text(how_many_would_you_like)
                        purchase_amt = input(">>> ")
                        if int(purchase_amt) > myplayer.tickets:
                            print("================================")
                            no_ticket_stop_wasting_time = "\nMinion Master: You don't have enough tickets. Stop wasting my time and come back when you do."
                            scrolling_text(no_ticket_stop_wasting_time)
                            player_item_update()
                        elif int(purchase_amt) == myplayer.tickets:
                            print("====================================================")
                            you_want_to_spend_all_tickets = "\nMinion Master: You want to spend all of your tickets? Alright then."
                            scrolling_text(you_want_to_spend_all_tickets)
                            myplayer.minions += myplayer.tickets
                            myplayer.tickets = 0
                            player_item_update()
                        elif int(purchase_amt) < myplayer.tickets:
                            minion_master_here_you_go = "\nMinion Master: Here you go!"
                            scrolling_text(minion_master_here_you_go)
                            myplayer.minions += int(purchase_amt)
                            myplayer.tickets -= int(purchase_amt)
                            player_item_update()
                    else:
                        no_ticket_text = "\nMinion Master: Return once you have tickets."
                        scrolling_text(no_ticket_text)
                         
            else:
                on_your_way = "\nMinion Master: On your way then."
                scrolling_text(on_your_way)


                

        #events for your backyard a2
        elif world[myplayer.location][ZONENAME] == "Your Backyard":
            gaze = "\nYou gaze upon the large expanse in peace, but something catches your eye."
            scrolling_text(gaze)
            fight = "\nYou see a wild minion fighting with a gigantic raccoon!"
            scrolling_text(fight)
            question = "\nWould you like to try to save the minion?"
            scrolling_text(question)
            choice = input(">>> ")
            if choice in yes_list:
                if myplayer.flute == True:
                    play = "\nYou attempt to play your flute. It's so terrible that the creature runs at you to make it stop."
                    scrolling_text(play)
                    combat(raccoon, 4)
                    yay = "\nThe minion is relieved and joins up with you!"
                    scrolling_text(yay)
                    myplayer.minions += 1
                else:
                    prepare = "\nYou try to grab the creature's attention but it doesn't notice you and continues chasing the minion."
                    scrolling_text(prepare)
            else:
                problem = "\nIt's the minion's problem anyways."
                scrolling_text(problem)

        #events for River Bank a3
        elif world[myplayer.location][ZONENAME] == "River Bank":
            do_you_want_fish = "\n Do you want to go fishing?"
            scrolling_text(do_you_want_fish)
            response = input(">>> ")
            if myplayer.name.lower() == "andy chou" or response in ["yes", "sure", "ok"]:
                why_ask = "\n Of course you do!"
                scrolling_text(why_ask)
                if myplayer.fishingrod == True and myplayer.fishinglimit > 0:
                    cast_rod = "\nYou cast your rod into the calm river."
                    scrolling_text(cast_rod)
                    waiting = "\n" + (random.randint(3, 10) * ".")
                    scrolling_text_slow(waiting)
                    quick_catch = "\nQuickly! Type 'catch' to get the fish!"
                    scrolling_text(quick_catch)
                    catch_input = timer(2)
                    if catch_input == "catch":
                        fish_1 = random.randrange(10000, 20000)
                        fish_fighting_1 = "\n The fish is fighting back! Type in " + str(fish_1) + " to fight back!"
                        scrolling_text(fish_fighting_1)
                        fish_input = timer(7)
                        if fish_input == str(fish_1):
                            fish_2 = random.randrange(10000, 200000)
                            fish_fighting_2 = "\n The fish is struggling hard! Type in " + str(fish_2) + " to fight it!"
                            scrolling_text(fish_fighting_2)
                            fish_input = timer(9)
                            if fish_input == str(fish_2):
                                fish_3 = random.randrange(10000, 200000)
                                fish_fighting_3 = "\n Wow this fish is tough! Type in " + str(fish_3) + " to combat it!"
                                scrolling_text(fish_fighting_3)
                                fish_input = timer(10)
                                if fish_input == str(fish_3):
                                    fish_4 = random.randrange(10000, 20000000)
                                    fish_fighting_4 = "\n Its strength is surely waning! Type in " + str(fish_4) + " for a final push!"
                                    scrolling_text(fish_fighting_4)
                                    fish_input = timer(15)
                                    if fish_input == str(fish_4):
                                        fish_weight = random.randrange(5, 50)
                                        caught_fish = "\nCongratulations! You caught a " + str(fish_weight) + " pound Blob Fish! Wow!"
                                        scrolling_text(caught_fish)
                                        myplayer.fish.append(fish_weight)
                                        myplayer.fishinglimit -= 1
                                        limit = "\nYour fishing permit only allows " + str(myplayer.fishinglimit) + " more catches!"
                                        scrolling_text(limit)

                                    else:
                                        got_away = "\nThe fish got away!"
                                        scrolling_text(got_away)
                                else:
                                    got_away = "\nThe fish got away!"
                                    scrolling_text(got_away)
                                    
                            else:
                                got_away = "\nThe fish got away!"
                                scrolling_text(got_away)
                                
                        else:
                            got_away = "\nThe fish got away!"
                            scrolling_text(got_away)
                            
                    else:
                        got_away = "\nThe fish got away!"
                        scrolling_text(got_away)


                else:
                    if myplayer.fishingrod == False:
                        you_need_rod = "\n You require a fishing rod for that!"
                        scrolling_text(you_need_rod)
                    if myplayer.fishinglimit < 1:
                        you_fish_too_much = "\n You have fished too much, go do something else"
                        scrolling_text(you_fish_too_much)


            else:
                leave_area = "\nYou decide not to fish."
                scrolling_text(leave_area)

        #events for regular shop a4
        elif world[myplayer.location][ZONENAME] == "Regular Shop":
            keeper = "\nThe shopkeeper greets you with a smile and asks what you would like."
            scrolling_text(keeper)
            shopping = True
            while shopping:
                prompt = "\nWould you like to buy, sell, or leave?"
                scrolling_text(prompt)
                choice = input(">>> ")
                if choice.lower() in ["buy", "sell", "leave"]:
                    if choice.lower() == "buy":
                        if len(regular_shop.inventory.items()) == 0:
                            no_items = "\nThere are no more items available."
                            scrolling_text(no_items)
                        else:
                            gold = "\nYou have " + str(myplayer.gold) + " gold available."
                            scrolling_text(gold)
                            available = "\nThe available items are: "
                            scrolling_text(available)

                            for key, value in regular_shop.inventory.items():
                                scrolling_text("\n" + key + " which costs " + str(value) + " gold.")
                            selection = input(">>> ")
                            if selection.lower() in regular_shop.inventory:
                                #All valid item choices:

                                #Make sure to:
                                ##Check player gold, give player the item (effect),
                                ##take away player gold, delete item from inventory
                                ##if no gold, let player know
                                if selection.lower() == "fishing rod":
                                    if myplayer.name in ["andy", "andy chou"]:
                                        i_knew = "\nI knew you were going to buy that."
                                        scrolling_text(i_knew)
                                    else:
                                        do_you = "\nShopkeeper: Do you know someone named Andy? Nevermind."
                                        scrolling_text(do_you)
                                    if myplayer.gold >= 100:
                                        myplayer.fishingrod = True
                                        myplayer.gold -= 100
                                        here = "\nShopkeeper: Here is your very own fishing rod."
                                        scrolling_text(here)
                                        del regular_shop.inventory["fishing rod"]
                                    else:
                                        no_gold = "\nShopkeeper: You can't even afford a fishing rod, you're a failure."
                                        scrolling_text(no_gold)
                                elif selection.lower() == "crude sword":
                                    if myplayer.gold >= 100:
                                        myplayer.power += 14
                                        myplayer.gold -= 100
                                        del regular_shop.inventory["crude sword"]
                                        here = "\nHere is your sword!"
                                        scrolling_text(here)
                                        power = "\n(Your power has increased!)"
                                        scrolling_text(power)
                                    else:
                                        no_gold = "You don't have enough gold."
                                        scrolling_text(no_gold)
                                elif selection.lower() == "glinting sword":
                                    if myplayer.gold >= 970:
                                        myplayer.power += 100
                                        myplayer.gold -= 970
                                        del regular_shop.inventory["glinting sword"]
                                        here = "\nTake care of that one, she's a beauty."
                                        scrolling_text(here)
                                        power = "\n(Your power has increased!)"
                                        scrolling_text(power)
                                    else:
                                        no_gold = "You don't have enough gold."
                                        scrolling_text(no_gold)
                                elif selection.lower() == "wooden shield":
                                    if myplayer.gold >= 50:
                                        myplayer.defense += 0.1
                                        myplayer.gold -= 50
                                        del regular_shop.inventory["wooden shield"]
                                        here = "\nGlad to get that off of my hands."
                                        scrolling_text(here)
                                        power = "\n(Your defense has increased!)"
                                        scrolling_text(power)
                                    else:
                                        no_gold = "You don't have enough gold."
                                        scrolling_text(no_gold)
                                elif selection.lower() == "iron shield":
                                    if myplayer.gold >= 150:
                                        myplayer.defense += 0.3
                                        myplayer.gold -= 150
                                        del regular_shop.inventory["iron shield"]
                                        here = "\nThis one will protect you well."
                                        scrolling_text(here)
                                        power = "\n(Your defense has increased!)"
                                        scrolling_text(power)
                                    else:
                                        no_gold = "You don't have enough gold."
                                        scrolling_text(no_gold)
                                elif selection.lower() == "health potion":
                                    if myplayer.gold >= 35:
                                        myplayer.potions += 1
                                        myplayer.gold -= 35
                                        add = "\n+1 potion"
                                        scrolling_text(add)
                                    else:
                                        no_gold = "You don't have enough gold."
                                        scrolling_text(no_gold)
                                elif selection.lower() == "perma-power potion":
                                    if myplayer.gold >= 200:
                                        myplayer.power += 23
                                        myplayer.gold -= 200
                                        del regular_shop.inventory["perma-power potion"]
                                        here = "\nFound that one in a random cave."
                                        scrolling_text(here)
                                        power = "\n(Your power has increased!)"
                                        scrolling_text(power)



                            else:
                                insult = "\nHm. We don't carry that."
                                scrolling_text(insult)

                    elif choice.lower() == "sell":
                        let_me = "\nShopkeeper: Let me see what you have."
                        scrolling_text(let_me)
                        dots = "..."
                        scrolling_text_slow(dots)
                        #Fish selling
                        if len(myplayer.fish) > 0:
                            for weight in myplayer.fish:
                                gold_amt = weight * 2
                                selling = "\nFish sold for " + str(gold_amt) + " gold."
                                scrolling_text_fast(selling)
                                myplayer.gold += gold_amt
                                myplayer.fish.remove(weight)

                        else:
                            no_fish = "\nShopkeeper: It seems like you don't have any fish..."
                            scrolling_text(no_fish)

                        if myplayer.minions > 0:
                            ask = "\nShopkeeper: Would you like to sell any minions for 50 gold each?"
                            scrolling_text(ask)
                            choice = input(">>> ")

                            if choice in yes_list:
                                player_item_update()
                                how_many = "\nShopkeeper: How many would you like to sell?"
                                scrolling_text(how_many)
                                amount_choice = input(">>> ")

                                if int(amount_choice) >= myplayer.minions:
                                    alright = "\nShopkeeper: Nice doing business."
                                    scrolling_text(alright)
                                    for i in range(0, int(amount_choice)):
                                        minion_sell = "\nMinion sold for 50 gold."
                                        scrolling_text(minion_sell)
                                        myplayer.minions -= 1
                                        myplayer.gold += 50


                                if int(amount_choice) < myplayer.minions:
                                    dont = "\nShopkeeper: You don't have that many minions."
                                    scrolling_text(dont)

                            else:
                                moving_on = "\nShopkeeper: Alright moving on then."
                                scrolling_text(moving_on)

                        else:
                            if myplayer.name in bonus_names:
                                no_minions = "\nShopkeeper: Hm. You don't have any minions. Very surprising."
                                scrolling_text(no_minions)
                            else:
                                no_minions2 = "\nShopkeeper: You don't have minions."
                                scrolling_text(no_minions2)

                    elif choice.lower() == "leave":
                        leaving = "\nThank you for visiting."
                        scrolling_text(leaving)
                        shopping = False

                else:
                    invalid = "\nPlease choose a valid option."
                    scrolling_text(invalid)

        #events for Lizard Den b1
        elif world[myplayer.location][ZONENAME] == "Lizard Den":
            #skips to lizard queen offer again if offer already made
            if myplayer.lizardqueen == 1:  #This is placed before initial visit to avoid triggering on first visit 
            #I know this is repetitive code, but for the purposes of this game it has very little impact
                again = "\nQueen Lizard: Ah, so you have returned."
                scrolling_text(again)
                speak = "\nQueen Lizard: If you can beeest me in combat, I wiiiill reward you with my gold bounty cheeest."
                scrolling_text(speak)
                accept = "\nDo you accept her offer?"
                scrolling_text(accept)
                choice = input(">>> ")
                if choice in yes_list:
                    prepare = "\nYou prepare for intense combat."
                    scrolling_text(prepare)
                    combat(lizard_queen, 10)
                    myplayer.lizardqueen = 2 #player has defeated the dungeon
                    win = "\nLizard Queen: Alriiight, you wiin. Take my gold and never come baaack."
                    scrolling_text(win)
                    myplayer.gold += 1000
                    gain = "\nYou gained 1000 gold! You're rich!"
                    scrolling_text(gain)
                    walking = "\nAs you walk to the exit, you sense that something is wrong."
                    scrolling_text(walking)
                    while myplayer.potions >= 1:
                        potion = "\nWould you like to quaff a potion and restore 100 HP?"
                        scrolling_text_fast(potion)
                        choice = input(">>> ")
                        if choice in yes_list:
                            myplayer.potions -= 1
                            myplayer.hp += 100
                            if myplayer.hp > myplayer.maxhp:
                                myplayer.hp = myplayer.maxhp
                            health = "\n+100 HP"
                            scrolling_text_fast(health)
                            current = "\nYour health is now {}.".format(myplayer.hp)
                            scrolling_text(current)
                        else:
                            put = "\nYou put your potions away."
                            scrolling_text_fast(put)
                            break
                    dots = "\n......."
                    scrolling_text_slow(dots)
                    voice = "\nThe voice of the Queen echoes around you."
                    scrolling_text(voice)
                    voice2 = "\nLizard Queen: You thought it would be that eaaasy?"
                    scrolling_text(voice2)
                    dots = "\n....."
                    scrolling_text_slow(dots)
                    burst = "\nSmall lizards start to rush out of every crack in every wall of the cave like a tsunami! You begin to run."
                    scrolling_text(burst)
                    dots = "\n......."
                    scrolling_text_slow(dots)
                    intercept = "\nYou are intercepted by a couple of fast ones."
                    scrolling_text(intercept)
                    combat(lizard_sentry)
                    combat(lizard_sentry)
                    more = "\nHow many are there?! The walls and ceiling start to rumble and collapse."
                    scrolling_text(more)
                    combat(lizard_guard)
                    combat(lizard_guard)
                    another = "\nAnother one grabs at your feet."
                    scrolling_text(another)
                    combat(lizard_sentry)
                    almost = "\nYou escape with the cave collapsing behind you! You're safe!"
                    scrolling_text(almost)
                    print_location()
                    what_would_you_like_to_do = "\nWhat would you li"
                    scrolling_text(what_would_you_like_to_do)
                    suddenly = "\nWait! The lizards have one more card to play."
                    scrolling_text(suddenly)
                    large = "\nA massive raccoon leaps out of the top of the den, breaking off the last of the chains placed upon it by the lizards."
                    scrolling_text(large)
                    combat(raccoon)
                    wow = "\nFinally! You've made it to complete safety and defeated the lizards! You have a feeling that you might meet again..."
                    scrolling_text(wow)
                    congrats = "\nCongratulations!"
                    scrolling_text(congrats)
                    print_location()
                    what_would_you_like_to_do = "\nWhat would yo"
                    scrolling_text(what_would_you_like_to_do)
                    another = "\nOne last sentry digs through the rocks and sprints toward you!"
                    scrolling_text(another)
                    combat(lizard_sentry)
                    last = "\nAlright. That should be the last of them."
                    scrolling_text(last)
                    print_location()
                    what_would_you_like_to_do = "\nWhat would you like to"
                    scrolling_text(what_would_you_like_to_do)
                    another = "\nA lizard guard crawls its way from out under a rock. It stands to face you!"
                    scrolling_text(another)
                    dots = "\n..."
                    scrolling_text_slow(dots)
                    collapse = "\n...And it collapsed and passed out."
                    scrolling_text(collapse)
                    get = "\nTime to get out of there!"
                    scrolling_text(get)

            if myplayer.lizardqueen == 0: #first visit
                smell = "\nThere is an extremely strong smell coming from the depths of the cave. Do you still wish to continue? (VERY CHALLENGING)"
                scrolling_text(smell)
                choice = input(">>> ")
                if choice in yes_list:
                    venture = "\nYou venture deeper and encounter a small lizard sentry. You try to sneak around it."
                    scrolling_text(venture)
                    if myplayer.sneakygloves == True:
                        #skips sentry fight
                        sneak = "\nYou sneak past the sleepy sentry using your gloves!"
                        scrolling_text(sneak)
                    else:
                        without = "\nWithout a stealth item to aid you, the sentry easily detects you."
                        scrolling_text(without)
                        combat(lizard_sentry)
                        ticket_loot = random.randint(1, 10)
                        if ticket_loot == 5:
                            found = "\nYou found an additional redeem ticket on the sentry's body!"
                            scrolling_text(found)
                            myplayer.tickets += 1

                    go = "\nYou continue deeper into the cave in search of more loot."
                    scrolling_text(go)
                    mother = "\nYou turn the corner to see the queen lizard on her throne guarded by more lizards!"
                    scrolling_text(mother)
                    tight = "\nThe tight cave space allows you to position yourself strategically and face each guard one on one!"
                    scrolling_text(tight)
                    combat(lizard_guard)
                    another = "\nAnother lizard guard approaches!"
                    scrolling_text(another)
                    combat(lizard_guard)
                    another = "\nAnother lizard guard attacks!"
                    scrolling_text(another)
                    combat(lizard_guard)
                    another = "\nAnother lizard guard runs toward you!"
                    scrolling_text(another)
                    combat(lizard_guard)
                    another = "\nHow many are there?!!"
                    scrolling_text(another)
                    combat(lizard_guard)
                    mother2 = "\nFinally, with the unconcious bodies of the guards lying around her, the queen lizard has had enough."
                    scrolling_text(mother2)
                    speak = "\nQueen Lizard: If you can beeest me in combat, I wiiiill reward you with my gold bounty cheeest."
                    scrolling_text(speak)
                    accept = "\nDo you accept her offer?"
                    scrolling_text(accept)
                    choice = input(">>> ")
                    if choice in yes_list:
                        prepare = "\nYou prepare for intense combat."
                        scrolling_text(prepare)
                        while myplayer.potions >= 1:
                            potion = "\nWould you like to quaff a potion and restore 100 HP?"
                            scrolling_text_fast(potion)
                            choice = input(">>> ")
                            if choice in yes_list:
                                myplayer.potions -= 1
                                myplayer.hp += 100
                                if myplayer.hp > myplayer.maxhp:
                                    myplayer.hp = myplayer.maxhp
                                health = "\n+100 HP"
                                scrolling_text_fast(health)
                                current = "\nYour health is now {}.".format(myplayer.hp)
                                scrolling_text(current)
                            else:
                                put = "\nYou put your potions away."
                                scrolling_text_fast(put)
                                break
                        combat(lizard_queen, 10)
                        myplayer.lizardqueen = 2 #player has beat the dungeon
                        win = "\nLizard Queen: Alriiight, you wiin. Take my gold and never come baaack."
                        scrolling_text(win)
                        myplayer.gold += 1000
                        gain = "\nYou gained 1000 gold! You're rich!"
                        scrolling_text(gain)
                        walking = "\nAs you walk to the exit, you sense that something is wrong."
                        scrolling_text(walking)
                        voice = "\nThe voice of the Queen echoes around you."
                        scrolling_text(voice)
                        voice2 = "\nLizard Queen: You thought it would be that eaaasy?"
                        scrolling_text(voice2)
                        burst = "\nSmall lizards start to rush out of every crack in every wall of the cave like a tsunami! You begin to run."
                        scrolling_text(burst)
                        intercept = "\nYou are intercepted by a couple of fast ones."
                        scrolling_text(intercept)
                        combat(lizard_sentry)
                        combat(lizard_sentry)
                        more = "\nHow many are there?! The walls and ceiling start to rumble and collapse."
                        scrolling_text(more)
                        combat(lizard_guard)
                        combat(lizard_guard)
                        another = "\nAnother one grabs at your feet."
                        scrolling_text(another)
                        combat(lizard_sentry)
                        almost = "\nYou escape with the cave collapsing behind you! You're safe!"
                        scrolling_text(almost)
                        print_location()
                        what_would_you_like_to_do = "\nWhat would you li"
                        scrolling_text_super_fast(what_would_you_like_to_do)
                        suddenly = "\nWait! The lizards have one more card to play."
                        scrolling_text(suddenly)
                        large = "\nA massive raccoon leaps out of the top of the den, breaking off the last of the chains placed upon it by the lizards."
                        scrolling_text(large)
                        combat(raccoon)
                        wow = "\nFinally! You've made it to complete safety and defeated the lizards! You have a feeling that you might meet again..."
                        scrolling_text(wow)
                        congrats = "\nCongratulations!"
                        scrolling_text(congrats)
                        print_location()
                        what_would_you_like_to_do = "\nWhat would yo"
                        scrolling_text_super_fast(what_would_you_like_to_do)
                        another = "\nOne last sentry digs through the rocks and sprints toward you!"
                        scrolling_text(another)
                        combat(lizard_sentry)
                        last = "\nAlright. That should be the last of them."
                        scrolling_text(last)
                        print_location()
                        what_would_you_like_to_do = "\nWhat would you like to"
                        scrolling_text_super_fast(what_would_you_like_to_do)
                        another = "\nA lizard guard crawls its way from out under a rock. It stands to face you!"
                        scrolling_text(another)
                        dots = "\n..."
                        scrolling_text_slow(dots)
                        collapse = "\n...And it collapsed and passed out."
                        scrolling_text(collapse)
                        get = "\nTime to get out of there!"
                        scrolling_text(get)





                    else:
                       myplayer.lizardqueen = 1 #when player comes back, skip to lizard queen fight prompt
                       exit = "\nLizard Queen: Feel free to come back any tiiiime."
                       scrolling_text(exit)
            
                else:
                    away = "\nYou decide that it's a good idea to quickly get out of there."
                    scrolling_text(away)

            

            if myplayer.lizardqueen == 2:
                won = "\nYou don't wish to look around the area after what happened last time."
                scrolling_text(won)



        #events for Your Abode b2 (starting area)
        elif world[myplayer.location][ZONENAME] == "Your Abode":
            tasty = "\nThere is some tasty cheese on the kitchen table. Would you like to eat it?"
            scrolling_text(tasty)
            choice = input(">>> ")
            if choice.lower() in yes_list:
                if myplayer.hp < (myplayer.maxhp / 2):
                    yum = "\nDelicious! Your HP was restored to 50%!"
                    scrolling_text(yum)
                    myplayer.hp = int(myplayer.maxhp / 2)
                else:
                    full = "\nYou're too full to consume the delicious cheese..."
                    scrolling_text(full)
                    yours = "\n(Your HP is %d/%d)" % (myplayer.hp, myplayer.maxhp)
                    scrolling_text(yours)
            else:
                say = "\nIf you say so..."
                scrolling_text(say)

            if myplayer.hometicket == True:
                found = "\n\nYou found a spare redeem ticket on your table."
                scrolling_text(found)
                myplayer.tickets += 1
                myplayer.hometicket = False

        #events for Anime Expo b3
        elif world[myplayer.location][ZONENAME] == "Anime Expo":
            walk = "\nWould you like to enter?"
            scrolling_text(walk)
            choice = input(">>> ")
            if choice in yes_list:
                walking = "\nYou decide to walk inside to explore for a while."
                scrolling_text(walking)
                if "sweaty man" not in myplayer.defeated_enemies:
                    comes = "\nA large sweaty man comes up to you."
                    scrolling_text(comes)
                    talk = "\nMan: DO YOU WANNA BUY MY ANIME FIGURINE AND COSPLAY WITH ME"
                    scrolling_text(talk)
                    choice2 = input(">>> ")

                    if choice2 in yes_list:
                        if myplayer.gold >= 10:
                            ok = "\nMan: HERE YOU GO"
                            scrolling_text(ok)
                            gold = "\n-10 gold"
                            scrolling_text(gold)
                            myplayer.gold -= 10
                            inspect = "\nYou inspect the figurine and realize that it's worthless."
                            scrolling_text(inspect)
                            fight = "\nWould you like to fight the sweaty man?"
                            scrolling_text(fight)
                            choice = input(">>> ")
                            if choice in yes_list:
                                prepare = "\nMan: PREPARE TO ENGAGE IN A SAMURAI SWORD DUEL WITH ME!!!!"
                                start = "\nHe approaches with a plastic sword."
                                scrolling_text(prepare)
                                scrolling_text(start)
                                combat(sweaty_man, 10)
                                myplayer.defeated_enemies.append("sweaty man")
                            else:
                                nope = "\nYou resist the urge to destroy the man in combat."
                                scrolling_text(nope)

                        else:
                            not_enough = "\nMan: YOU DONT HAVE ENOUGH GOLD :("
                            scrolling_text(not_enough)


                    else:
                        prepare = "\nMan: PREPARE TO ENGAGE IN A SAMURAI SWORD DUEL WITH ME!!!!"
                        start = "\nHe approaches with a plastic sword."
                        scrolling_text(prepare)
                        scrolling_text(start)
                        combat(sweaty_man, 10)
                        myplayer.defeated_enemies.append("sweaty man")

            else:
                go = "\nYou continue on your way."
                scrolling_text(go)

        #events for Mountain Path b4
        elif world[myplayer.location][ZONENAME] == "Mountain Path":
            the_man_suddenly_turns = "\nThe old man suddenly and rapidly turns toward you."
            scrolling_text_fast(the_man_suddenly_turns)
            old_man_asks_riddle = "\nOld Man: I POSSESS REDEEM TICKETS, BUT YOU MUST ANSWER MY RIDDLE"
            scrolling_text(old_man_asks_riddle)
            do_you_want_to_answer_riddle = "\n\nDo you want to answer his riddle?"
            scrolling_text(do_you_want_to_answer_riddle)
            answer = input(">>> ")
            if answer.lower() == "yes":
                old_man_asks_riddle_2 = "\nOld Man: BEFORE MOUNT EVEREST WAS DISCOVERED, WHAT WAS THE TALLEST MOUNTAIN IN THE WORLD?"
                scrolling_text(old_man_asks_riddle_2)
                riddle_answer = input(">>> ")
                if riddle_answer.lower() in ["mt. everest", "mount everest", "everest", "mteverest", "mt everest", "mt everest ", "mounteverest"]:
                    answered_old_man_correct = "\nOld Man: YOU HAVE ANSWER CORRECTLY! YOU HAVE EARNED MY REDEEM TICKETS AND GOLD."
                    scrolling_text(answered_old_man_correct)
                    myplayer.tickets += 3
                    myplayer.gold += 150
                    player_item_update()
                    world[myplayer.location][SOLVED] = True
                    myplayer.completion += 6.25
                    old_man_returns = "\n The old man returns to his spot and continues standing there."
                    scrolling_text(old_man_returns)
                    myplayer.defeated_enemies.append(old_man)
                    level_up = "\nYou leveled up! You are now level " + str(myplayer.level) + "."
                    scrolling_text(level_up)
                else:
                    answered_old_man_incorrect = "\nOld Man: YOU IDIOT! NOW YOU DIE."
                    scrolling_text(answered_old_man_incorrect)
                    fast = "\nThe old man sprints with incredible speed toward you."
                    scrolling_text(fast)
                    combat(old_man, 1)
                    world[myplayer.location][SOLVED] = True
                    gain = "\nYou looted redeem tickets from the man's body!"
                    scrolling_text(gain)
                    myplayer.tickets += 3
                    myplayer.defeated_enemies.append(old_man)

            else:
                you_walk_away = "\nYou choose to walk away."
                scrolling_text(you_walk_away)

        

        #events for Suspicious Shop d3
        elif world[myplayer.location][ZONENAME] == "Suspicious Shop":
            greetings = "\nShopkeeper: What do you want"
            scrolling_text(greetings)
            a_voice = "\n(The faint voice of a woman can be heard from the back of the shop)"
            scrolling_text(a_voice)
            shut_up = "\nShopkeeper: MOM SHUT UP"
            scrolling_text(shut_up)
            shopping = True
            while shopping:
                prompt = "\nWould you like to buy, sell, or leave?"
                scrolling_text(prompt)
                choice = input(">>> ")
                if choice.lower() in ["buy", "sell", "leave"]:
                    if choice.lower() == "buy":
                        if len(suspicious_shop.inventory.items()) == 0:
                            no_items = "\nThere are no more items available."
                            scrolling_text(no_items)
                        else:
                            gold = "\nYou have " + str(myplayer.gold) + " gold available."
                            scrolling_text(gold)
                            available = "\nThe available items are: "
                            scrolling_text(available)
                            for key, value in suspicious_shop.inventory.items():
                                scrolling_text("\n" + key + " : " + str(value))
                            selection = input(">>> ")
                            if selection in suspicious_shop.inventory:
                                #All valid item choices:
                                if selection.lower() == "colorful flute":
                                    if myplayer.gold >= 100:
                                        myplayer.flute = True
                                        here = "\nShopkeeper: Here is your very own flute."
                                        scrolling_text(here)
                                        del suspicious_shop.inventory["colorful flute"]
                                    else:
                                        no_gold = "\nShopkeeper: You can't even afford a flute, you're a failure."
                                        scrolling_text(no_gold)
                                elif selection.lower() == "mysterious amulet":
                                    if myplayer.gold >= 150:
                                        myplayer.revive += 1
                                        here = "\nShopkeeper: No idea what this does. I'm happy to take your gold for it."
                                        scrolling_text(here)
                                        del suspicious_shop.inventory["mysterious amulet"]
                                    else:
                                        no_gold = "\nShopkeeper: Wow are you a hobo or something? Not enough gold."
                                        scrolling_text(no_gold)
                                elif selection.lower() == "sneaky gloves":
                                    if myplayer.gold >= 250:
                                        myplayer.sneakygloves = True
                                        here = "\nShopkeeper: You just bought gloves for 250 gold. Nice."
                                        scrolling_text(250)
                                        del suspicious_shop.inventory["sneaky gloves"]
                                    else:
                                        no_gold = "\nShopkeeper: Can't afford gloves. Wow."
                                        scrolling_text(no_gold)
                                #elif selection.lower() == 
                            else:
                                insult = "\nDo you even know how to speak properly?? Try again."
                                scrolling_text(insult)
         
                    elif choice.lower() == "sell":
                        let_me = "\nShopkeeper: Let me see what you have."
                        scrolling_text(let_me)
                        dots = "..."
                        scrolling_text_slow(dots)
                        #Fish selling
                        if len(myplayer.fish) > 0:
                            for weight in myplayer.fish:
                                gold_amt = weight * 2
                                selling = "\nFish sold for " + str(gold_amt) + " gold."
                                scrolling_text_fast(selling)
                                myplayer.gold += gold_amt
                                myplayer.fish.remove(weight)

                        else:
                            no_fish = "\nShopkeeper: It seems like you don't have any fish..."
                            scrolling_text(no_fish)

                        if myplayer.minions > 0:
                            ask = "\nShopkeeper: Would you like to sell any minions for 50 gold each?"
                            scrolling_text(ask)
                            choice = input(">>> ")

                            if choice in yes_list:
                                player_item_update()
                                how_many = "\nShopkeeper: How many would you like to sell?"
                                scrolling_text(how_many)
                                amount_choice = input(">>> ")

                                if int(amount_choice) >= myplayer.minions:
                                    alright = "\nShopkeeper: Nice doing business."
                                    scrolling_text(alright)
                                    for i in range(0, amount_choice):
                                        minion_sell = "\nMinion sold for 50 gold."
                                        scrolling_text(minion_sell)
                                        myplayer.minions -= 1
                                        myplayer.gold += 50


                                if int(amount_choice) < myplayer.minions:
                                    dont = "\nShopkeeper: You don't even have enough minions dumbass"
                                    scrolling_text(dont)

                            else:
                                moving_on = "\nShopkeeper: Alright moving on then."
                                scrolling_text(moving_on)

                        else:
                            if myplayer.name in bonus_names:
                                no_minions = "\nShopkeeper: Hm. You don't have any minions. Very surprising."
                                scrolling_text(no_minions)
                            else:
                                no_minions2 = "\nShopkeeper: You don't have minions."
                                scrolling_text(no_minions2)

                    elif choice.lower() == "leave":
                        leaving = "\nShopkeeper: (Mumbling to himself) Finally, I can keep watching SNAFU and playing League of Legends."
                        scrolling_text(leaving)
                        shopping = False

                else:
                    invalid = "\nPlease choose a valid option."
                    scrolling_text(invalid)


        #events for high mountain pass b4
        elif world[myplayer.location][ZONENAME] == "High Mountain Pass":
            snow = "\n\nThe snow chills you to the bone."
            scrolling_text(snow)
            myplayer.dojo += 1
            if "proud_warrior" not in myplayer.defeated_enemies:
                wandering = "\nA large armoured man carrying a huge hammer is walking along the path."
                scrolling_text(wandering)
                if myplayer.flute == True:
                    flute = "\nYour flute makes a sound and attracts the attention of the warrior. He runs right toward you!"
                    scrolling_text(flute)
                else:
                    spotted = "\nYou were spotted! He runs right toward you."
                    scrolling_text(spotted)
                combat(proud_warrior)
            if myplayer.dojo == 2:
                search = "\nHm. Your searching does not seem to be very productive."
                scrolling_text(search)
            if myplayer.dojo == 3:
                search = "\nIt's white snow in all directions."
                scrolling_text(search)
            if myplayer.dojo in [5,6]:
                search = "\nYou may be getting closer to finding something, but you doubt it."
                scrolling_text(search)
            if myplayer.dojo in [7,8]:
                search = "\nYou start giving up, it seems hopeless."
                scrolling_text(search)
            if myplayer.dojo in [9,10,11]:
                search = "\nYou decide that it's time to leave."
                scrolling_text(search)
            if myplayer.dojo >= 12:
                found = "\nYou found it! The legendary Mountain Dojo!"
                scrolling_text(found)
                enter = "\nWould you like to enter?"
                scrolling_text(enter)
                warning = "\nWARNING: DO NOT ENTER UNLESS PROPERLY GEARED. THE DOJO IS EXTREMELY DIFFICULT."
                scrolling_text(warning)
                choice = input(">>> ")
                if choice in yes_list:
                    ##change location to dojo
                    movement_handler("Dojo")
                else:
                    decide = "\nYou decide not to enter."
                    scrolling_text(decide)

        #events for Lonely Passage d4
        elif world[myplayer.location][ZONENAME] == "Lonely Passage":
            nothing = "\nThe surrounding landscape is barren and leaves you with an eerie feeling."
            scrolling_text(nothing)
            sentry = "\nWait... A lizard here??"
            scrolling_text(sentry)
            combat(lizard_sentry)
            weird = "\nThat was strange."
            scrolling_text(weird)






        

            








###CORE GAME LOOP


def main_game_loop():
    while myplayer.gameover == False:
        prompt()

def gameover():
    failed = "\n You have failed in your journey..."
    scrolling_text_slow(failed)
    luck = "\nBetter luck next time!"
    scrolling_text(luck)
    level = "\nYou were level" + str(myplayer.level)
    scrolling_text_fast(level)
    gold = "\nYour gold amount was: " + str(myplayer.gold)
    scrolling_text_fast(gold)
    minions = "\nYour minion count was: " + str(myplayer.minions)
    scrolling_text(minions)
    if myplayer.lizardqueen == 2:
        defeated = "\nYou defeated the lizard queen once."
        scrolling_text(defeated)
    input("\nPress Enter to quit.")
    sys.exit()



###SETUP
def setup_game():
    os.system('cls')



    #NAME
    setup_question1 = "What is your name?\n"
    scrolling_text(setup_question1)
    player_name = input(">>> ")
    myplayer.name = player_name

    if myplayer.name.lower() in bonus_names:
        myplayer.gold += 100
        myplayer.fishinglimit -= 2
    else:
        setup_question2 = "Are you prepared for a perma-death adventure that will challenge you?\n"
        scrolling_text(setup_question2)
        question2_input = input(">>> ")
        if question2_input.lower() in yes_list:
            question2_added = "You may continue.\n"
            scrolling_text(question2_added)
        else:
            sys.exit()

    
    welcome_message = "Please enjoy your Dungeons and Lizards experience.\n"
    dots = "......"
    scrolling_text(welcome_message)
    scrolling_text_slow(dots)
    
    os.system('cls')    
    main_game_loop()           





title_screen()