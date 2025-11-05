# this code is given
possible_moves = ["R", "P", "S"]
def corresponding_move(move, result):
    return possible_moves[(possible_moves.index(move) - result) % 3]

# task 3a

# using count dict (alt 1)
def most_common_move(moves):
    count = {}
    for k in possible_moves:
        count[k] = moves.count(k)
    most_common = 'R'
    for m in count:
        if count[m] > count[most_common]:
            most_common = m
    return most_common

# using nested ifs (alt 2)
def most_common_move_2(moves):
    count_r = moves.count("R")
    count_p = moves.count("P")
    count_s = moves.count("S")
    if count_r > count_p:
        if count_r > count_s: return "R"
        else: return "S"
    else:
        if count_p > count_s: return "P"
        else: return "S"

# task 3b

class Player:
    def __init__(self):
        self.previous_games = {}
        self.current_opponent = None

    def start_game(self, opponent: str) -> str:
        if self.current_opponent != None:
            raise ValueError
        self.current_opponent = opponent
        moves = self.previous_games.setdefault(opponent, [])
        self.my_move = corresponding_move(most_common_move(moves), -1)
        return self.my_move

    def end_game(self, result: int):
        if self.current_opponent == None:
            raise IndexError
        self.previous_games[self.current_opponent].append(corresponding_move(self.my_move, result))
        self.current_opponent = None


p = Player()
for i in range(3):
    print(p.start_game("X"))
    p.end_game(1)

print(p.start_game("Y"))
p.end_game(0)
print(p.start_game("Y"))
p.end_game(1)
print(p.start_game("Y"))
p.end_game(1)
print(p.start_game("Y"))
p.end_game(1)

print(p.start_game("X"))
p.end_game(-1)


print(p.previous_games)
