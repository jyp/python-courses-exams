import random

class Ur:
    def __init__(self):
        self.board = [None,None]
        self.board[0] = [None] * 15
        self.board[1] = [None] * 15
        self.unused = [7,7]
        self.home = [0,0]
        self.cur_player = 0
        self.rolled = None
    def roll(self):
        self.rolled = 0
        for i in range(0,4):
            self.rolled += random.randint(0,1)
        print("player",self.cur_player,"rolled:", self.rolled)
    def pass_action(self):
        self.cur_player = 1 - self.cur_player
    def move(self,loc):
        # compute target location
        p = self.cur_player
        target_loc = loc+self.rolled
        # is the target valid?
        if target_loc > 14 or target_loc == 0:
            print("cannot move there")
            return
        # is the target free?
        if self.board[p][target_loc] != None:
            print("own piece in target")
            return
        # remove the piece
        if loc==0:
            if self.unused[p] == 0:
                print("no free piece left")
                return
            self.unused[p] -= 1
        else:
            if self.board[p][loc] == None:
                print("no piece in desired location")
                return
            self.board[p][loc] = None
        # put the piece in target
        if target_loc == 14:
            print("arrived home")
            self.home[p] += 1
        else:
            self.board[p][target_loc] = "x"
        # handle "combat"
        if 5 <= target_loc <= 12 and self.board[1-p][target_loc] != None:
            print("other player piece taken")
            self.board[1-p][target_loc] = None
            self.unused[1-p] += 1
        # winning test
        if self.home[p] == 7:
            print("You won!")
        else:
            self.pass_action()

