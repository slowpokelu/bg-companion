#TODO - Lifetracker for up to 4 players

from src.mtg.player import Player
# from player import Player

players = {}
    
def init_players():
    print("Enter number of players to track (1-4)")
    no_players = input("--> ")
    if no_players == "":
        no_players = 1
    no_players = int(no_players)
    if no_players > 4 or no_players < 1:
        print("Please enter a number between 2 and 4")
        no_players = 1
    
    print("Enter starting Hit Points")
    starting_life = input("--> ")
    if starting_life == "":
        starting_life = 40
    starting_life = int(starting_life)
    if starting_life < 0:
        print("Starting HP cannot be below 0")
        starting_life=40

    for i in range(0, no_players):
        players[i+1] = Player(playername=f"Player {i+1}", startinglife=starting_life)

def tracking_repl():
    # TODO - maybe as menu in main.py??
    pass

def start_tracking():
    init_players()

def showhp():
    res = ""
    for k, v in players.items():
        res+=f'##### {v.name}: {v.hp}HP #####\n'
    return res
       

def modify_hp(mode="+"):
    '''
    mode "+" is heal
    mode "-" is damage
    '''
    maxplayer = len(players)
    print(f"Choose player: (1-{maxplayer})")
    selected_player = input("--> ")
    if selected_player == "":
        selected_player = 1
    selected_player = int(selected_player)
    if selected_player < 1 or selected_player > maxplayer:
        print("Not a valid player")
    else:
        print("How Much Health? (default: 1)")
        amount = input("--> ")
        if amount == "":
            amount = 1
        amount = int(amount)
        if amount >= 0:
            if mode == "+":
                players[selected_player].increase_hp(amount)
            elif mode == "-":
                players[selected_player].increase_hp(-amount)

if __name__ == "__main__":
    pass