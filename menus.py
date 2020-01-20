
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