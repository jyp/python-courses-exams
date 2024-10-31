# Assumption: every line contains a student name

def print_students(list):
  for s in list:
      print(s)
      
def print_report():
 with open("students.txt") as f:
    passed = []
    yet_to_be_graded = []
    failed = []
    for line in f:
        fields = line.split()
        student = fields[0]
        grades = fields[1:]
        if len(grades) < 1:
            yet_to_be_graded.append(student)
        elif grades[0] == 'U':
            failed.append(student)
        elif len(grades) < 2:
            yet_to_be_graded.append(student)
        elif grades[0] == 'G' and grades[1] == 'G':
            passed.append(student)
        else:
            failed.append(student)
 print(",*** Students who passed ***")
 print_students(passed)
 print(",*** Students who failed ***")
 print_students(failed)
 print(",*** Students to be graded ***")
 print_students(yet_to_be_graded)

print_report()
