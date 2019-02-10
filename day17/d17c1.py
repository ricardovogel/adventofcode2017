def spinlock(jumpsize):
    position = 1
    pointer = 0
    buffer = [0]

    while position <= 2017:
        pointer += jumpsize
        pointer %= len(buffer)
        pointer += 1
        buffer.insert(pointer, position)
        position += 1

    return buffer[(pointer + 1) % len(buffer)]


assert spinlock(3) == 638
print(spinlock(359))
