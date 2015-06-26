def deal(cards):
    """Given a stack of cards, deal them into two piles"""

    piles = [[],[]]

    turn = 0 

    for card in cards:
        piles[turn].append(card)
        if turn == 0:
            turn = 1
        else:
            turn = 0

    return piles


    


