res = 0
prev = "a"
with open("day01/input.txt") as f:
    for line in f:
        size = len(line)
        for i in range(size):
            if line[i] is line[int(i - size / 2)]:
                res += int(line[i])

print(res)
