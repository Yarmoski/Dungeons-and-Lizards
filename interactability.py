import random
import sys
import os
import time
import msvcrt

from text_effects import *
from global_vars import *
from functionality import *
from events import *

def print_location(myplayer):
    print("\n" + "=" * len(world[myplayer.location][DESCRIPTION]))
    name_to_display = world[myplayer.location][ZONENAME].upper()
    scrolling_text_fast(name_to_display)
    description_to_display = "\n" + world[myplayer.location][DESCRIPTION]
    scrolling_text_fast(description_to_display)
    print("\n" + "=" * len(world[myplayer.location][DESCRIPTION]))
    print("\n" + world[myplayer.location][MAP])

def player_item_update(myplayer):
    player_items = "\nYou now have " + str(myplayer.tickets) + " tickets and " + str(myplayer.minions) + " minions."
    scrolling_text(player_items)

def prompt(myplayer, suspicious_shop, regular_shop, lizard_sentry, lizard_guard, lizard_queen, sweaty_man, old_man, raccoon, proud_warrior, corrupted_demon):
    if myplayer.level >= 16:
        congrats = "\nCongrats! You have defeated the enemies that are currently present in the game. This game is unfinished and may see further development in the future. Thank you for playing!"
        scrolling_text(congrats)
        myplayer.gameover = True
    print_location(myplayer)
    what_would_you_like_to_do = "\nWhat would you like to do?"
    scrolling_text_super_fast(what_would_you_like_to_do)
    action = input(">>> ")
    action_list = ['move', 'look', 'quit', 'inventory', 'help', 'move right', 'move left', 'move up', 'move down']
    while action.lower() not in action_list:
        you_clearly_need_help_menu = "You clearly need to look at the help menu\n"
        scrolling_text_fast(you_clearly_need_help_menu)
        action = input(">>> ")
    if action.lower() == "quit":
        confirmation = "\nAre you sure you want to quit?\n"
        scrolling_text(confirmation)
        choice = input(">>> ")
        if choice in YES_LIST:
            sys.exit()
        print("...")
    elif action.lower() == 'move':
        player_move(myplayer)
    elif action.lower() == 'move up':
        player_move(myplayer, 'up')
    elif action.lower() == 'move left':
        player_move(myplayer, 'left')
    elif action.lower() == 'move right':
        player_move(myplayer, 'right')
    elif action.lower() == 'move down':
        player_move(myplayer, 'down')
    elif action.lower() == 'look':
        player_examine(myplayer, suspicious_shop, regular_shop, lizard_sentry, lizard_guard, lizard_queen, sweaty_man, old_man, raccoon, proud_warrior, corrupted_demon)
    elif action.lower() == 'help':
        print("- Use 'move' or 'move <direction>' to move")
        print("- Use 'look' to look")
        print("- Use 'quit' to quit")
        print("- Use 'inventory' to check inventory")
        print("=========COMBAT=========")
        print("- COMBAT MOVES: Slash High, Slash Low, Parry, Sidestep, Jump")
        print("- In combat, you have a limited time to enter your move depending on the enemy")
        print("- Make sure to enter your combat moves correctly or you will stumble!")
    elif action.lower() == 'inventory':
        os.system('cls')
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
            if choice in YES_LIST:
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

def player_move(myplayer, direction = None):
    if direction != None:
        if direction == "up":
            if world[myplayer.location][UP] == "":
                print("\nYou cannot go up from here.")
            else:
                destination = world[myplayer.location][UP]
                movement_handler(myplayer, destination)
        elif direction == "down":
            if world[myplayer.location][DOWN] == "":
                print("\n You cannot go down from here.")
            elif world[myplayer.location][DOWN] == "c4":
                if old_man in myplayer.defeated_enemies:
                    destination = world[myplayer.location][DOWN]
                    movement_handler(myplayer, destination)
                else:
                    deal = "\nYou have to deal with the old man first."
                    scrolling_text(deal)
            else:
                destination = world[myplayer.location][DOWN]
                movement_handler(myplayer, destination)
        elif direction == "left":
            if world[myplayer.location][LEFT] == "":
                print("\n You cannot go left from here.")
            else:
                destination = world[myplayer.location][LEFT]
                movement_handler(myplayer, destination)
        elif direction == "right":
            if world[myplayer.location][RIGHT] == "":
                print("\n You cannot go right from here.")
            else:
                destination = world[myplayer.location][RIGHT]
                movement_handler(myplayer, destination)
    else:
        what_direction_would_you_like = "What direction would you like to move?"
        scrolling_text_super_fast(what_direction_would_you_like)
        destination = input(">>> ")
        if destination.lower() == "up":
            if world[myplayer.location][UP] == "":
                print("\nYou cannot go up from here.")
            else:
                destination = world[myplayer.location][UP]
                movement_handler(myplayer, destination)
        elif destination.lower() == "down":
            if world[myplayer.location][DOWN] == "":
                print("\n You cannot go down from here.")
            elif world[myplayer.location][DOWN] == "c4":
                if old_man in myplayer.defeated_enemies:
                    destination = world[myplayer.location][DOWN]
                    movement_handler(myplayer, destination)
                else:
                    deal = "\nYou have to deal with the old man first."
                    scrolling_text(deal)
            else:
                destination = world[myplayer.location][DOWN]
                movement_handler(myplayer, destination)
        elif destination.lower() == "left":
            if world[myplayer.location][LEFT] == "":
                print("\n You cannot go left from here.")
            else:
                destination = world[myplayer.location][LEFT]
                movement_handler(myplayer, destination)
        elif destination.lower() == "right":
            if world[myplayer.location][RIGHT] == "":
                print("\n You cannot go right from here.")
            else:
                destination = world[myplayer.location][RIGHT]
                movement_handler(myplayer, destination)


def movement_handler(myplayer, destination):
    os.system('cls')
    moved = "\n" + "!!!You have moved to " + world[destination][ZONENAME] + "."
    scrolling_text_super_fast(moved)
    myplayer.location = destination


