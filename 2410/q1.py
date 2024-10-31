def score_calculator(A,B):
    return 1/(10**((B-A)/400) + 1)

def guess_winner(white_rating, black_rating):
    A = white_rating
    B = black_rating
    e = score_calculator(B, A)
    if e < 0.45:
        print("White is expected to win")
    elif e > 0.55:
        print("Black is expected to win")
    else:
        print("A draw is expected")

guess_winner(1700,1200)
guess_winner(1220,1200)
