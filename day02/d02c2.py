res = 0
with open("day02/input.txt") as f:
    for line in f:
        sp = line.split()
        for i in range(0, len(sp)):
            for j in range(i + 1, len(sp)):
                if sp[i] is sp[j]:
                    break

                high = max(int(sp[i]), int(sp[j]))
                low = min(int(sp[i]), int(sp[j]))

                if high % low is 0:
                    print(high / low)
                    res += high // low
                    break

print(res)
