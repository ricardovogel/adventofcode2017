def spinlock(jumpsize):
    position = 1
    pointer = 0

    while position <= 50000000:
        pointer += jumpsize
        pointer %= position
        pointer += 1
        if pointer is 1:
            res = position
        position += 1

    return res


print(spinlock(359))
