class Program:
    def __init__(self, line):
        s = line.split()
        self.id = s[0]
        self.neighbors = []

        for n in s[2:]:
            self.neighbors.append(n.replace(",", ""))

    def countNeighbors(self, drive, known=[]):
        if self in known:
            return 0
        known.append(self)
        res = 1
        for n in self.neighbors:
            res += drive[int(n)].countNeighbors(drive, known)
        return res


drive = []
with open("day12/input.txt") as f:
    for l in f:
        drive.append(Program(l))

print(drive[0].countNeighbors(drive))
