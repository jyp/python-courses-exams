# Assumption: the method addStudent is never called twice with the same arguments.
def list_to_str(xs):
    result = ""
    for x in xs:
        result = result + " " + str(x)
    return result

class ListMerger:
    # instance attribute:
    # attended: dictionary mapping student name to the *list* of their attended lectures.
    def __init__(self):
        self.attended = dict()
        
    def addStudent(self,name,lecture):
        # add lecture to attended[name]
        if name not in self.attended:
            self.attended[name] = []
        self.attended[name].append(lecture)
        
    def getNrOfLectures(self,name):
        return len(self.attended[name])
    
    def printList(self):
        for student in self.attended:
            print(student,list_to_str(sorted(self.attended[student])))

#################################
# Test code
merger = ListMerger()
merger.addStudent("Erik", 1)
merger.addStudent("Eva", 1)
merger.addStudent("Gustav", 2)
merger.addStudent("Mark", 2)
merger.addStudent("Mary", 1)
merger.addStudent("Erik", 2)
merger.addStudent("Mark", 1)
merger.printList()

# Erik 1 2
# Eva 1
# Gustav 2
# Mark 1 2
# Mary 1

    
