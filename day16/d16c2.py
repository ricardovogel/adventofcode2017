def exchange(a, b):
    positions[a], positions[b] = positions[b], positions[a]


def partner(a, b):
    a = positions.index(a)
    b = positions.index(b)
    exchange(a, b)


def spin(a):
    global positions
    part_a = positions[len(positions) - a:]
    part_b = positions[0: len(positions) - a]
    positions = part_a + part_b


positions = "a b c d e f g h i j k l m n o p".split()
known = []

with open("day16/input.txt") as f:
    for l in f:
        for i in range(0, 1000000000):
            if positions in known:
                jumps = i
                break

            known.append(positions.copy())
            for s in l.split(","):
                type = s[0]
                if type is "s":
                    spin(int(s[1:]))
                elif type is "x":
                    s1 = s[1:].split("/")
                    exchange(int(s1[0]), int(s1[1]))
                else:
                    s1 = s[1:].split("/")
                    partner(s1[0], s1[1])

with open("day16/input.txt") as f:
    for l in f:
        for i in range(0, (1000000000 % jumps)):
            for s in l.split(","):
                type = s[0]
                if type is "s":
                    spin(int(s[1:]))
                elif type is "x":
                    s1 = s[1:].split("/")
                    exchange(int(s1[0]), int(s1[1]))
                else:
                    s1 = s[1:].split("/")
                    partner(s1[0], s1[1])

for c in positions:
    print(c, end="")
