
class Player():
    def __init__(self): # 3 points
       self.offside = False
       self.x = 0
       self.team = []
    def move(self,dx): # 10 points
        if self.offside and dx > 0: print("Foul") # 1 point
        self.x += dx # 1 point
        if self.offside:
            # making this player onside (4 points)
            for p in self.team:
                if p.x > self.x and not p.offside:
                    self.offside = False
        else:
            # making other players onside (4 points)
            for p in self.team:
                if self.x > p.x:
                    p.offside = False
    def tackling_or_kick(self): #5 points
        if self.offside: print("Foul") #1 points
        for p in self.team: # making players offside (4 points)
            if self.x < p.x:
                p.offside = True
    def catch_ball(self): # 2 points
        if self.offside: print("Foul")

def initialise_team(n): # 5 points
    team = []
    for _ in range(n):
        team.append(Player())
    for p in team:
            p.team = team
    return team

players = initialise_team(2)
players[0].move(5) # player 0 is now in front
players[1].tackling_or_kick() # the other player is tackled
players[0].move(-5) # player 0 keeps moving forward: this is a foul.

