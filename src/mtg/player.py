#!/usr/bin/env python

class Player():
    playerlist=[]
    def __init__(self,
                 playername="",
                 startinglife=40,
                 is_eliminated=False,
                 is_monarch=False):
        self.name = playername
        self.hp = startinglife
        # Counters and Mana are stored in dict to allow any type of both for different games (mana is a coutertype?)
        self.counters = {}
        self.mana = {
            "c": 0,
            "w": 0,
            "u": 0,
            "b": 0,
            "r": 0,
            "g": 0,
        }
        self.is_eliminated = is_eliminated
        self.is_monarch = is_monarch

        # Add instance to class array
        self.playerlist.append(self)

    # debug print function - probably not used in repl
    def print_playerinfo(self):
        print(self.name)
        if len(self.counters) != 0:
            for v, k in self.counters.items():
                print(f"{k} {v}", end=" - ")
            print()
        if len(self.mana) != 0:
            print("Mana:", end=" ")
            for v, k in self.mana.items():
                if k == 0:
                    continue
                print(f"{k}{v.upper()}", end=" ")
            print()
    
    def print_hp(self):
        print(f"{self.name} is at {self.hp} HP.")
        # no return

    def decrease_hp(self, amount=1):
        self.hp -= amount
        if self.hp <= 0:
            self.is_eliminated = True

    def increase_hp(self, amount=1):
        self.hp += amount

    def set_hp(self, new_hp):
        self.hp = new_hp

    def add_counter(self, countertype, amount=1):
        if not countertype in self.counters.keys():
            self.counters[countertype] = amount
        else:
            self.counters[countertype] += amount

    # Remove X counters (counters can be negative, but must exist)
    def remove_counter(self, countertype, amount=1):
        if countertype in self.counters.keys():
            self.counters[countertype] -= amount
        else:
            print("No such counters on player")

    def add_mana(self, manatype, amount=1):
        if not manatype.lower() in self.mana.keys():
            print("Invalid mana type - please use c w u b r g")
        else:
            self.mana[manatype.lower()] += amount

    def remove_mana(self, manatype, amount=1):
        if not manatype.lower() in self.mana.keys():
            print("Invalid mana type - please use c w u b r g")
        else:
            self.mana[manatype.lower()] -= amount

    def clear_mana(self):
        self.mana = {
            "c": 0,
            "w": 0,
            "u": 0,
            "b": 0,
            "r": 0,
            "g": 0,
        }

if __name__ == '__main__':
    pass
