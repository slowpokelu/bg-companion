#!/usr/bin/env python

# TODO Requires Python 3.10+ as soon as 'match' is involved :)

from os import system, name
import time
import webbrowser

# from src.mtg.player import Player
from src.mtg.collection import interactive_search
from src.mtg.edh_powerlevel import get_powerlevel
import src.rng as rng
import src.clock
import src.mtg.lifetracker as tracker

version = "0.1_alpha_cli"

options = {
    0: "Main Menu",
    "g": ["General Tools", 'create_menu(general_tools)'],
    "m": ["Magic the Gathering", 'create_menu(mtg_options)'],
#     "dnd": ["Dungeons & Dragons", 'create_menu(dnd_options)'],
#     "4": ["Chess / Shogi", 'create_menu(chess_shogi_options)'],
#     "bg": ["Other Boardgames", 'create_menu(boardgames)'],
    "l": ["Links", "create_menu(link_options)"]
}

general_tools = {
    0: "General Tools",
    "r": ["RNG Menu", "create_menu(rng_options)"],

    'b': 'start()',
}

mtg_options = {
    0: "Magic the Gathering",
    "l": ["Life Counter", "tracker.start_tracking(); create_menu(tracking_options, f'{tracker.showhp()}')"],
    "r": ["RNG Menu", 'create_menu(rng_options)'],
#    "3": ["Counters", ""],
#    "e": ["External Resources", "create_menu(mtg_resources)"],
    "c": ["Find cards in collection", "interactive_search(); create_menu(mtg_options)"],
    "p": ["Calculate EDH Powerlevel", "clear(); create_menu(mtg_options, f'Powerlevel: {str(get_powerlevel())}')"],
    "d": ["Deck Chooser", "create_menu(deck_choose_options)"],

    'b': 'start()',
}

def gethp():
    return tracker.showhp()

tracking_options = {
    0: "Life Tracker",
    #"s": ["Show HP of all players", "create_menu(tracking_options, f'{gethp()}')"],
    "i": ["Increase HP of a player", "tracker.modify_hp('+');create_menu(tracking_options, f'{gethp()}')"],
    "d": ["Decrease HP of a player", "tracker.modify_hp('-');create_menu(tracking_options, f'{gethp()}')"],
    "ac": ["Add a counter to a player", ""],
    "rc": ["Remove a counter from a player", ""],
    "am": ["Add Mana to a player's mana pool", ""],
    "rm": ["Remove Mana from a player's mana pool", ""],


    "b": 'create_menu(mtg_options)',
}

deck_choose_options = {
    0: "Deck Chooser",
    "a": ["EDH + cEDH", "clear(); create_menu(deck_choose_options, deck_choose_text(get_random_deck()))"], 
    "e": ["EDH only", "clear(); create_menu(deck_choose_options, deck_choose_text(get_random_deck(mode=1), mode=1))"], 
    "c": ["cEDH only", "clear(); create_menu(deck_choose_options, deck_choose_text(get_random_deck(mode=2), mode=2))"], 

    'b': 'create_menu(mtg_options)',
}
'''
dnd_options = {
    0: "Dungeons & Dragons",
    1: ["D&D Beyond", "webbrowser.open('https://dndbeyond.com')"],
    2: ["Character Sheet", ""],
    3: ["Dice", 'create_menu(rng_options)'],

    'b': 'start()',
}

chess_shogi_options = {
    0: "Chess & Shogi", 
    1: ["Chess Clock", ""],

    'b': 'start()',
}

boardgames = {
    0: "Board Games",
    1: ["BoardGameGeek", "webbrowser.open('https://boardgamegeek.com/')"],
    1: ["Scythe", ""],
    2: ["Terraforming Mars", ""],
    3: ["Wingspan", ""],
    4: ["ROOT", ""],
    5: ["Ganz Schoen Clever ", "webbrowser.open('https://boardgamegeek.com/filepage/164221/printable-score-sheets')"], # TODO Doppelt so Clever / Clever hoch drei
    6: ["Hanamikoji", ""],
    7: ["Machi Koro", ""],
    8: ["Poker", ""],
    9: ["52 cards", ""],
    
    'b': 'start()',
}

mtg_resources = {
    0: "Magic Resources",
    "1": ["Deckstats", "webbrowser.open('https://deckstats.net/')"],
    "2": ["Moxfield", "webbrowser.open('https://www.moxfield.com/')"],
    "3": ["Scryfall", "webbrowser.open('https://scryfall.com/')"],
    "4": ["EDHREC", "webbrowser.open('https://edhrec.com/')"],
    "5": ["cedh decklist database", "webbrowser.open('https://cedh-decklist-database.com/')"],
    "6": ["Secret Lair EU", "webbrowser.open('https://secretlair.wizards.com/eu')"],

    'b': 'create_menu(mtg_options)',
}
'''
rng_options = {
    0: "Random Number Generator",
    "1": ["Random Number", "min_max_num()"],
    "2": ["Coinflip", "coinflip()"],
    "4": ["d4", "dice_roller(4)"],
    "6": ["d6", "dice_roller(6)"],
    "8": ["d8", "dice_roller(8)"],
    "10": ["d10", "dice_roller(10)"],
    "12": ["d12", "dice_roller(12)"],
    "20": ["d20", "dice_roller(20)"],
    "100": ["d100", "dice_roller(100)"],
    
    'b': 'start()',
}

link_options = {
    0: "Useful Links",
    "d": ["Deckstats", "webbrowser.open('https://deckstats.net/')"],
    "m": ["Moxfield", "webbrowser.open('https://www.moxfield.com/')"],
    "s": ["Scryfall", "webbrowser.open('https://scryfall.com/')"],
    "e": ["EDHREC", "webbrowser.open('https://edhrec.com/')"],
    "c": ["cedh decklist database", "webbrowser.open('https://cedh-decklist-database.com/')"],
    "6": ["Secret Lair EU", "webbrowser.open('https://secretlair.wizards.com/eu')"],
    "7": ["D&D Beyond", "webbrowser.open('https://dndbeyond.com')"],
    "8": ["BoardGameGeek", "webbrowser.open('https://boardgamegeek.com/')"],
    "9": ["MPCFill", "webbrowser.open('https://mpcfill.com/')"],
    "10": ["MPC", "webbrowser.open('https://www.makeplayingcards.com/')"],

    'b': 'start()',
}

is_root = True
res = ""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def start():
    global is_root
    is_root=True
    create_menu(options)

def welcome_message():
    print(bcolors.OKGREEN+"bg-companion v"+get_version(), bcolors.ENDC)

def about():
    print(bcolors.FAIL+"A tool by slowpokelu"+bcolors.ENDC)

def banner():
    print()
    welcome_message()
    print("   ", end="")
    about()
    print()

def create_header(text):
    print(bcolors.HEADER+"#"*3+" "+text+" "+"#"*3+bcolors.ENDC+"\n")

def create_menu(collection, res=""):
    global is_root
    last = collection
    if collection != options:
        is_root=False
    clear()
    if is_root:
        banner()
    create_header(collection[0])
    if res != "":
        print(bcolors.OKGREEN+res+"\n"+bcolors.ENDC)
    print(bcolors.OKBLUE+"Select Mode:\n"+bcolors.ENDC)
    for key in collection:
        if key != 0 and key != 'b':
            print(bcolors.OKCYAN+f"<{key}> {collection[key][0]}"+bcolors.ENDC)
    print()
    if is_root == False:
        print(bcolors.WARNING+f"<b> Back"+bcolors.ENDC)
        print(bcolors.WARNING+f"<0> Main Menu"+bcolors.ENDC)
    print(bcolors.WARNING+"<q> Exit bg-companion\n"+bcolors.ENDC)
    # print(collection)
    while True:
            try:
                choice = input(">>> ")
                if choice.lower() == "q":
                    exit()
                elif choice.lower() == 'b':
                    exec(collection['b'])
                '''
                else:
                    choice = int(choice)
                if choice > 0:
                    try:
                        exec(collection[choice][1])
                    except KeyError:
                        print("No valid input.")
                    # break
                elif choice == 0:
                    start()
                else:
                    print("No valid input.")
            except ValueError:
                print("No valid input.")
                '''
                
                # this requires keys to be strings
                if choice == "0":
                    start()
                try:
                    exec(collection[choice][1])
                except KeyError:
                    print("No valid input.")
            except ValueError:
                print("Value Error.")
    
def min_max_num():
    global res
    clear()
    min = int(input("Enter min: "))
    clear()
    max = int(input("Enter max: "))
    if min <= max:
        res = f"Random number between {min} and {max}:\n\n>>> "+str(rng.random_number(min, max))+" <<<" # TODO Check for valid input - check min < max
    else:
        res = 0
    choice = create_menu(rng_options, res)

def coinflip():
    global res
    res = " (^-^)/ O\n\n>>> "+str(rng.coinflip())+" <<<"
    choice = create_menu(rng_options, res)

def dice_roller(dice):
    global res
    dicename = "d"+str(dice)
    res = f" (^-^)/ {dicename}\n\n>>> "+str(rng.roll_die(dice))+" <<<"
    choice = create_menu(rng_options, res)

def get_random_deck(mode=0):
    '''
    mode 0 = choose edh + cedh deck
    mode 1 = choose edh
    mode 2 = choose cedh
    '''
    res = []

    edh_file = "src/mtg/collections/edh_decks.txt"
    cedh_file = "src/mtg/collections/cedh_decks.txt"

    edh = open(edh_file)
    cedh = open(cedh_file)

    if mode == 0:
        for deck in edh:
            res.append(deck)
        for deck in cedh:
            res.append(deck)
    elif mode == 1:
        for deck in edh:
            res.append(deck)
    elif mode == 2:
        for deck in cedh:
            res.append(deck)
        
    return rng.choose_random(res).replace('\n', '')

def deck_choose_text(deckname, mode=0):
    deck_choose_all = [
        f"Try {deckname}.",
        f"You shall play {deckname}!",
        f"Great Deck: {deckname} ~",
        f"Consider {deckname}!",
        f"I recommend {deckname} for this round!",
        f"Best Deck EU-West: {deckname} ~",
        f"How about {deckname}?",
        f"You should give {deckname} a spin!",
        f"{deckname} is a good choice!"
    ]
    deck_choose_edh = deck_choose_all + [f"Great Casual Deck: {deckname}."]
    deck_choose_cedh = deck_choose_all + [f"Tryhard mode? Try {deckname}!"]
    if mode == 1: 
        return rng.choose_random(deck_choose_edh)
    if mode == 2:
        return rng.choose_random(deck_choose_cedh)
    return rng.choose_random(deck_choose_all)

def get_version():
    global version
    return version

if __name__ == '__main__':

    start()
