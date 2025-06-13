class Crochet:
    def __init__(self):
        self.stitch_count = 0
        self.prev_row = []
        self.current_row = []
        self.links = []

    def new_stitch(self):
        self.stitch_count += 1
        n = self.stitch_count
        self.current_row.append(n)
        return n

    def new_link(self, prev, curr):
        self.links.append((prev,curr))

    def chain(self):
        self.new_stitch()

    def single(self):
        if not self.prev_row:
            raise ValueError("Trying to single crochet, but no stitches left in previous row")
        else:
            n = self.new_stitch()
            p = self.prev_row.pop()
            self.new_link(p,n)

    def inc(self):
        if not self.prev_row:
            raise ValueError("Trying to increase, but no stitches left in previous row")
        else:
            n1 = self.new_stitch()
            n2 = self.new_stitch()
            p = self.prev_row.pop()
            self.new_link(p,n1)
            self.new_link(p,n2)

    def dec(self):
        if len(self.prev_row) < 2:
            raise ValueError("Trying to decrease, but <2 stitches left in previous row")
        else:
            n = self.new_stitch()
            p1 = self.prev_row.pop()
            p2 = self.prev_row.pop()
            self.new_link(p1,n)
            self.new_link(p2,n)

    def next_row(self):
        self.prev_row = self.current_row
        self.current_row = []

    def print_crochet(self):
        print(self.links)


## Test
c = Crochet()
c.chain()       # Stitch 1
c.chain()       # Stitch 2
c.chain()       # Stitch 3
c.chain()       # Stitch 4
c.next_row()
c.single()      # Stitch 5, link (4,5)
c.dec()         # Stitch 6, links (3,6) and (2,6)
c.single()      # Stitch 7, link (1,7)
c.chain()       # Stitch 8
c.next_row()
c.single()      # Stitch 9, link (8,9)
c.inc()         # Stitches 10 and 11, links (7,10) and (7,11)
c.single()      # Stitch 12, link (6,12)

if __name__ == "__main__":
    c.print_crochet()
