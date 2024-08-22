
class WordDict:
    # instance attributes:
    # d: dictionary from word to meanings
    # r:  dictionary  from meaning to words
    def __init__(self):
        self.d = dict()
        self.r = dict()
    def addWord(self, word, meanings):
        # adds a new word with the specified list of
        # meanings. If some of the meanings already exist, they are not added again.
        if word not in self.d:
            self.d[word] = []
        for m in meanings:
            if m not in self.d[word]:
                self.d[word].append(m)
            if m not in self.r:
                self.r[m] = []
            self.r[m].append(word)
        
    def getMeanings(self, word):
        # returns the list of meanings for that word.
        return self.d[word]
    def getWords(self, meaning):
        # returns the list of words with the given meaning.
        return self.r[meaning]

wdict = WordDict()
wdict.addWord("apple", ["fruit","tree"])
wdict.addWord("strawberry", ["fruit","plant"])
wdict.addWord("plum", ["fruit"])
wdict.addWord("plum", ["tree"]) # a second meaning is added
wdict.addWord("plum", ["fruit"]) # this line does nothing
wdict.addWord("birch", ["tree"])
print(wdict.getMeanings("plum"))
# ["fruit","tree"]
print(wdict.getWords("tree"))
# ["apple","plum","birch"]
