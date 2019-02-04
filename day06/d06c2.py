blocks = []
with open("day06/input.txt") as f:
    for line in f:
        for word in line.split():
            blocks.append(int(word))
f.close()


known = []
while blocks not in known:
    known.append(list(blocks))
    maxValue = max(blocks)
    maxIndex = blocks.index(maxValue)

    blocks[maxIndex] = 0

    index = maxIndex + 1
    while maxValue > 0:
        blocks[index % len(blocks)] += 1
        index += 1
        maxValue -= 1

print(len(known) - known.index(blocks))
