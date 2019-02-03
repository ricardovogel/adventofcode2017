res = 0
prev = "a"
with open("day01/input.txt") as f:
    for line in f:
        first = line[0]
        last = line[-1]
        for char in line:
            if char is prev:
                res += int(char)
            prev = char
        if first is last:
            res += int(first)
print(res)
