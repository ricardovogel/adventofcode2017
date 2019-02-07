class Program:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.disc = []

    def add(self, other):
        self.disc.append(other)


drive = []
with open("day07/input.txt") as f:
    for line in f:
        split = line.split()
        p = Program(split[0], split[1][1:-1])
        for u in split[3:]:
            p.add(u.replace(",", ""))
        drive.append(p)

drivecopy = drive.copy()
for p0 in drive:
    for p1 in drive:
        if p0.name in p1.disc:
            drivecopy.remove(p0)

print(drivecopy[0].name)
