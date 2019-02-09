a = 634
b = 301
c = 0
mask = (1 << 16) - 1

for i in range(0, 5000000):
    while True:
        a *= 16807
        a %= 2147483647
        if a % 4 is 0:
            break

    while True:
        b *= 48271
        b %= 2147483647
        if b % 8 is 0:
            break

    a_mask = a & mask
    b_mask = b & mask

    if a_mask == b_mask:
        c += 1

print(c)
