res = 0
with open("day04/input.txt") as f:
    for line in f:
        a = []
        for word in line.split():
            if word in a:
                res -= 1
                break
            else:
                a.append(word)
        res += 1

print(res)
