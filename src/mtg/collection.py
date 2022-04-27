#!/usr/bin/env python

# This only works for collection text file with format "X CARDNAME" where X is the amount. ALl cards must be on different lines

import re
from collections import defaultdict
import scrython
from os import system, name
import sys
from sys import platform

collection_file = "collections/collection.txt"
collection_advanced = "collections/collection_advanced.txt"
collection_csv = "collections/collection.csv"

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def load_collection(collectionfile):

    collection_dict = defaultdict(int) #{}

    lines = open(collectionfile, 'r')

    for card in lines:
        amount = int(card.split(" ", 1)[0])
        card = card.split(" ", 1)[1][:-1]

        collection_dict[card] += amount


    return collection_dict

def search(query, collection):
    for card, amount in collection.items():
        if re.search(query.lower(), card.lower()):
            print(amount, card)

def show_collection(collection):
    for card, amount in collection.items():
        print("{} {}".format(amount, card))

def interactive_search(prefix="src/mtg/"):
    global collection_file
    
    clear()

    collection = prefix+collection_file

    collection = load_collection(collection)

    continue_loop = True

    while (continue_loop):
        
        print("\nSearch for a card:")
        query = input()
        if query == "" or query.lower() == 'q':
            continue_loop = False
            break
        clear()
        print("+" * 20)
        search(query, collection)
        print("+" * 20)
        print("\nEnter 'q' to quit.")
        

if __name__ == "__main__":

    if (os.path.isfile(collection_file)):
        collection = load_collection(collection_file)
        print("Collection Loaded!")
    else:
        try:
            collection = load_collection(sys.argv[1])
        except (FileNotFoundError):
            print("FIle NOt FOUnd")
            print("Exiting...")
            raise
        except (IndexError):
            print("Please give the collection path as an argument to this script")
            print("Exiting...")
            raise
        

    continue_loop = True

    while (continue_loop):
        print("\nSearch for a card:")
        query = input()
        if query == "":
            continue_loop = False
            break

        clear()

        print("+" * 20)
        search(query, collection)
        print("+" * 20)
   
