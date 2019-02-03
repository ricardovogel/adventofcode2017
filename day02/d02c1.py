res = 0
with open("day02/input.txt") as f:
    for line in f:
        small = 999999999
        big = 0
        for word in line.split():
            if int(word) > big:
                big = int(word)
            if int(word) < small:
                small = int(word)
        res += (big - small)
print(res)
