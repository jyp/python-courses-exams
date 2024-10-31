
def load_agenda(file_name):
    result = []
    with open(file_name) as f:
        for l in f:
            start,stop,task = l.split()
            result.append((int(start),int(stop),task))
    return result

def tabulate_agenda(a):
    result = []
    for start,stop,task in a:
        while len(result) <= stop:
            result.append([])
        for i in range(start,stop+1):
            result[i].append(task)
    return result

print(tabulate_agenda(load_agenda("agenda.txt")))
