
from text_effects import *

def player_examine():
    os.system('cls')
    examining = "\n!!!Inspecting location"
    scrolling_text(examining)
    line = "\n" + "=" * len(world[myplayer.location][EXAMINATION])
    scrolling_text_super_fast(line)
    examination_text_print = "\n" + world[myplayer.location][EXAMINATION]
    scrolling_text(examination_text_print)

    if world[myplayer.location][SOLVED]:
        this_area_already_explored = "\nThis area has been exhausted."
        scrolling_text(this_area_already_explored)
    else:
        this_place_is_unexplored = "\n..."
        scrolling_text(this_place_is_unexplored)
        #events for minion market a1
        if world[myplayer.location][ZONENAME] == "Minion Market":
            if myplayer.name.lower() in BONUS_NAMES:
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
            if choice in YES_LIST:
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
            if myplayer.name.lower() == "andy chou" or response in YES_LIST:
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
                        fish_1 = random.randrange(1000000, 20000000)
                        fish_fighting_1 = "\n The fish is fighting back! Type in " + str(fish_1) + " to fight back!"
                        scrolling_text(fish_fighting_1)
                        fish_input = timer(3)
                        if fish_input == str(fish_1):
                            fish_2 = random.randrange(100000000, 2000000000)
                            fish_fighting_2 = "\n The fish is struggling hard! Type in " + str(fish_2) + " to fight it!"
                            scrolling_text(fish_fighting_2)
                            fish_input = timer(4)
                            if fish_input == str(fish_2):
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
                                scrolling_text_fast("\n" + key + " which costs " + str(value) + " gold.")
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

                            if choice in YES_LIST:
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
                            if myplayer.name in BONUS_NAMES:
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
                if choice in YES_LIST:
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
                if choice in YES_LIST:
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
                    if choice in YES_LIST:
                        prepare = "\nYou prepare for intense combat."
                        scrolling_text(prepare)
                        while myplayer.potions >= 1:
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
            if choice.lower() in YES_LIST:
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
            if choice in YES_LIST:
                walking = "\nYou decide to walk inside to explore for a while."
                scrolling_text(walking)
                if "sweaty man" not in myplayer.defeated_enemies:
                    comes = "\nA large sweaty man comes up to you."
                    scrolling_text(comes)
                    talk = "\nMan: DO YOU WANNA BUY MY ANIME FIGURINE AND COSPLAY WITH ME"
                    scrolling_text(talk)
                    choice2 = input(">>> ")

                    if choice2 in YES_LIST:
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
                            if choice in YES_LIST:
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

                            if choice in YES_LIST:
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
                            if myplayer.name in BONUS_NAMES:
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
                if choice in YES_LIST:
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