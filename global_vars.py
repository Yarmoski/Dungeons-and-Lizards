
YES_LIST = ["yes", "affirmative", "sure", "yea", "ye", "ok", "alright", "okay", "roger", "y"]
BONUS_NAMES = ["nathan gelfand", "nathan gary gelfand", "nathang", "nathan"]




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