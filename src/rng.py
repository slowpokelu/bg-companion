#!/usr/bin/env python

import random as r

def random_number(min, max):
    return r.randint(min, max)

def roll_die(sides):
    return r.randint(1, sides)

def coinflip():
    return r.choice(["Heads", "Tails"])

def coinflip_num():
    return r.randint(0, 1)

def choose_random(list):
    return list[r.randint(0, len(list)-1)]