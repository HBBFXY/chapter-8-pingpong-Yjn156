import random

def ping_pong(prob_a, n_games=1000):
    a_wins = 0
    
    for _ in range(n_games):
        sa, sb = 0, 0
        while not ((sa >= 11 or sb >= 11) and abs(sa - sb) >= 2):
            sa += random.random() < prob_a
            sb += not (sa - 1 == sb) if sa > sb else not (sb - 1 == sa)
        
        a_wins += sa > sb
    
    return f"A胜率: {a_wins/n_games:.2%}, B胜率: {(n_games-a_wins)/n_games:.2%}"

print(ping_pong(0.55, 10000))
