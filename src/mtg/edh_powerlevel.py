# Formula: 2/A + ((D / 2 + T + R / 2) / 2) + I / 20 = P
# A = Avg CMC
# D = Draw that lets you see 3+ cards, or continuous draw
# T = Tutors CMC <= 4
# R = Ramp CMC <= 2
# I = Interaction (single target removal, wrath spells, counterspells and even stax)
# Commander counts as 2 in the respective category
#
# This formula is not suitable for determining the powerlevel of commander centric decks, for example krenko
#
# Yoinked from https://discipleofthevault.com/2020/11/18/my-edh-power-level-formula/

def old_powerlevel(A, D, T, R, I):
    powerlevel = 2/A + (((D / 2) + T + (R / 2)) / 2) + I / 20

    return round(powerlevel, 2)

def new_powerlevel(A, D, T, R, I): #,E, modifier=0):
    '''
    Modifier 0 (default): the commander is not counting towards any category.
    Modifier 1: the commander has synergy with Evergreen Cards (Doubles Evergreen Cards)
    Modifier 2: the commander has synergy with Interaction (Doubles Interaction Cards)
    '''
    '''
    if (modifier == 1):
        E = E*2
    elif (modifier == 2):
        I = I*2
    '''

    powerlevel = 2/A + ((D/2 + T/2 + R/2)/2) + I/20 # + E/20

    return round(powerlevel, 2)

def var_input():
    print("Enter CMC: ", end='')
    A = float(input())
    print("Enter Draw: ", end='')
    D = float(input())
    print("Enter Tutors: ", end='')
    T = float(input())
    print("Enter Ramp: ", end='')
    R = float(input())
    print("Enter Interaction: ", end='')
    I = float(input())
    '''
    print("Enter Evergreen: ", end='')
    E = float(input())
    print("Enter Modifier (0=None, 1=Evergreen, 2=Interaction): ", end='')
    '''

    return [A, D, T, R, I]#, E, M]

def get_powerlevel():
    v = var_input()
    # print("Powerlevel:", new_powerlevel(v[0], v[1], v[2], v[3], v[4], v[5], v[6]))
    return new_powerlevel(v[0], v[1], v[2], v[3], v[4]) #, v[5], v[6])

if __name__ == "__main__":
    print(f"Powerlevel: {get_powerlevel()}")
    