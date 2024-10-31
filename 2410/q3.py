def score_calculator(A,B):
    return 1/(10**((B-A)/400) + 1)
class EloPool:
    def __init__(self):
        self.elo = {}
        self.retired_elo = {}
    def register_player(self,player_name):
        if player_name in self.elo:
            print("Player already registered")
        elif player_name in self.retired_elo:
            print("Player is retired")
        else:
            self.elo[player_name] = 1000
    def match_players(self,player1_name,player2_name,result):
        if (player1_name in self.elo) and (player2_name in self.elo):
            K = 40
            update = K * (score_calculator(self.elo[player1_name], self.elo[player2_name]) - result)
            self.elo[player1_name] -= update
            self.elo[player2_name] += update
        else:
            print("problem with player names")
    def retire_player(self,player_name):
        if player_name in self.retired_elo:
            print("Already retired")
        elif player_name not in self.elo:
            print("Not registered")
        else:
            pElo = self.elo[player_name]
            points_to_distribute = pElo - 1000
            self.retired_elo[player_name] = pElo
            self.elo.pop(player_name)
            n = len(self.elo)
            d = points_to_distribute/n
            for p in self.elo:
                self.elo[p] += d
    
    def print_players(self):
        data = []
        for p,e in self.elo.items():
            data.append((p,e))
        for p,e in self.retired_elo.items():
            data.append((p,e))
        data.sort()
        for p,e in data:
            print(p,e)

p = EloPool()
p.register_player("Tal")
p.register_player("Reti")
p.register_player("Lasker")
p.print_players()
p.match_players("Tal","Reti",0)
p.match_players("Tal","Reti",1)
p.match_players("Lasker","Reti",1)
p.print_players()

