from global_vars import *


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
                    "\n\nHe swings right for your face."],
                    #jump
                    7 : ["\n\nThe warrior tries to sweep you off of your feet.", 
                    "\n\nHe tries to kick you in the knees."]
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