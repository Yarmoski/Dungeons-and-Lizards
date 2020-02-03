#Dungeons and Lizards
#Ted Yarmoski

import random
import sys
import os
import time
import msvcrt

from player import *
from shops import *
from menus import *
from text_effects import *
from interactability import *
from combat import *
from enemies import *
from events import *
from functionality import *

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