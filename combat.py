import random
import sys
import os
import time
import msvcrt

import os
from text_effects import *
from functionality import *
from global_vars import *
from enemies import *

##########COMBAT##############
def combat(myplayer, enemy, speed = 5):

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