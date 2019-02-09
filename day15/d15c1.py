a = 634
b = 301
c = 0
mask = (1 << 16) - 1

for i in range(0, 40000000):
    a *= 16807
    a %= 2147483647
    b *= 48271
    b %= 2147483647

    a_mask = a & mask
    b_mask = b & mask

    if a_mask == b_mask:
        c += 1

print(c)
