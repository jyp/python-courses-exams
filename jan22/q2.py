
def read_letter(fname, keywords):
    # assumption: the file always contains at least one word.
    found = []
    with open(fname) as f:
        for line in f:
            for w in line.split():
                last_word = w
                if w in keywords:
                    found.append(w)
    return (last_word, found)


print(read_letter("letter_alex.txt", ["doll","car","crayon"]))
