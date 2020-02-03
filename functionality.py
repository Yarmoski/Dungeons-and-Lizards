import os
from text_effects import *
from player import *
from global_vars import *
from interactability import *

###CORE GAME LOOP


def main_game_loop(myplayer):
    while myplayer.gameover == False:
        prompt(myplayer)

def gameover(myplayer):
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
def setup_game(myplayer):
    os.system('cls')



    #NAME
    setup_question1 = "What is your name?\n"
    scrolling_text(setup_question1)
    player_name = input(">>> ")
    myplayer.name = player_name

    if myplayer.name.lower() in BONUS_NAMES:
        myplayer.gold += 100
        myplayer.fishinglimit -= 2
    else:
        setup_question2 = "Are you prepared for a perma-death adventure that will challenge you?\n"
        scrolling_text(setup_question2)
        question2_input = input(">>> ")
        if question2_input.lower() in YES_LIST:
            question2_added = "You may continue.\n"
            scrolling_text(question2_added)
        else:
            sys.exit()

    
    welcome_message = "Please enjoy your Dungeons and Lizards experience.\n"
    dots = "......"
    scrolling_text(welcome_message)
    scrolling_text_slow(dots)
    
    os.system('cls')    
    main_game_loop(myplayer)        