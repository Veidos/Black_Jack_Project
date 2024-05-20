# SCRIPTS AND FUNTIONS FOR BLACK JACK GAME

def card_one_eleven(player):
    for i in player.hand:
        if i.number == "one":
            return True
    return False

def results(player, valuep, croupier,valuec):
       
       # Board
    print(f"\n\nPlayer Hand:")
    for i in player.hand:
        print(i)
    print(f"Player Count: {valuep}")
    print(f"\nCroupier Hand:")
    for i in croupier.hand:
        print(i)
    print(f"Croupier Count: {valuec}\n\n") 