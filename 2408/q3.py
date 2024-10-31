class Tracker:
    def __init__(self,now):
        self.open = {}
        self.done = []
        self.time = now
    def tick(self,n):
        self.time = self.time + n
    def start(self,task):
        if task in self.open:
            print("Warning: task already started")
        self.open[task] = self.time
    def stop(self,task):
        if task not in self.open:
            print("Warning: task not started")
        else:
            self.done.append((self.open[task],self.time,task))
            self.open.pop(task)
    def stop_all(self):
        for t,start in self.open.items():
            self.done.append((start,self.time,t))
        self.open = {}
    def print_tasks(self):
        if len(self.open) > 0:
            print("Warning: there are currently open tasks")
        for (start,stop,task) in self.done:
            print(start,stop,task)

# from q3 import Tracker
a = Tracker(9)
a.start("exam")
a.tick(3)
a.start("lunch")
a.tick(1)
a.stop("exam")
a.tick(1)
a.stop("lunch")
a.tick(1)
a.start("dance-class")
a.tick(1)
a.tick(1)
a.stop("dance-class")
a.tick(1)
a.start("meet-friends")
a.tick(4)
a.start("exam")
a.tick(1)
a.stop_all()
a.print_tasks()
