#!/usr/bin/env python

class Player():
    players = []
    def __init__(self,
                 playername="",
                 startinglife=40,
                 counters={},
                 mana={},
                 is_eliminated=False,
                 is_monarch=False):

        self.name = playername
        self.life = startinglife
        # Counters and Mana are stored in dict to allow any type of both for different games
        self.counters = counters
        self.mana = mana
        self.is_eliminated = is_eliminated
        self.is_monarch = is_monarch

        # Add instance to class array
        self.players.append(self)

    def take_damage(self, amount):
        self.life -= amount
        if self.life <= 0:
            self.is_eliminated = True
    def heal(self, amount):
        self.life += amount
    def get_counter(self, countertype, amount=1):
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


if __name__ == '__main__':
    pass
