class Team:
    def __init__(self, pitch, bench):
        self.pitch = pitch
        self.bench = bench
        self.minutes = dict()
        for p in pitch+bench:
            self.minutes[p] = 0
    def tick(self):
        for p in self.pitch:
            self.minutes[p] += 1
    def swap(self,p1,p2):
        self.pitch.remove(p1)
        self.pitch.append(p2)
        self.bench.remove(p2)
        self.bench.append(p1)
    def print_stats(self):
        for p in self.minutes:
            print(p,"played",self.minutes[p],"minutes")


t = Team(["Alana","Chelsea","Georgia"],["Iritana","Kate"])
t.tick()
t.tick()
t.tick()
t.swap("Alana","Iritana")
t.tick()
t.tick()
t.tick()
t.tick()
t.print_stats()
