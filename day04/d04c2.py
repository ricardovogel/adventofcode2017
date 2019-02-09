def isPalindrome(a, b):
    a = sorted(a)
    b = sorted(b)

    return a == b


res = 0
with open("day04/input.txt") as f:
    for line in f:
        a = []
        for word in line.split():
            if word in a:
                res -= 1
                break
            stopIt = False
            for knownWord in a:
                if isPalindrome(word, knownWord):
                    res -= 1
                    stopIt = True
                    break
            if stopIt:
                break
            a.append(word)
        res += 1

print(res)
