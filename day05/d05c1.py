maze = []
with open("day05/input.txt") as f:
    for line in f:
        maze.append(int(line))

length = len(maze)
jumps = 0
i = 0
while i >= 0 and i < length:
    this = maze[i]
    temp = i
    i = i + this
    maze[temp] += 1
    jumps += 1

print(jumps)
