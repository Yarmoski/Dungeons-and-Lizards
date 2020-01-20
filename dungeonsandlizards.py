#Dungeons and Lizards
#Ted Yarmoski

import random
import sys
import os
import time
import msvcrt

import player
import shops
import menus
import text_effects
import interactability
import combat
import enemies
import events
import functionality

myplayer = Player()
suspicious_shop = suspicious_shop()
regular_shop = regular_shop()

###Instantiation for enemies
lizard_sentry = lizard_sentry()
lizard_guard = lizard_guard()
lizard_queen = lizard_queen()
sweaty_man = sweaty_man()
old_man = old_man()
raccoon = raccoon()
proud_warrior = proud_warrior()
corrupted_demon = corrupted_demon()



###START THE GAME
title_screen()