import operator

ops = {"==": operator.eq, "<": operator.lt,
       ">": operator.gt, "<=": operator.le, ">=": operator.ge, "!=": operator.ne}
incdec = {"inc": operator.add, "dec": operator.sub}


file = "day08/input.txt"
registers = {}
m = -999999

with open(file) as f:
    for l in f:
        s = l.split()
        registers[s[0]] = 0

with open(file) as f:
    for l in f:
        s = l.split()
        register = s[0]
        action = s[1]
        value = int(s[2])
        conditionalRegister = s[4]
        conditionalAction = s[5]
        conditionalValue = int(s[6])

        if ops[conditionalAction](registers[conditionalRegister], conditionalValue):
            registers[register] = incdec[action](registers[register], value)

        m = max(m, max(registers.values()))

print("Challenge 1: %s\nChallenge 2: %s" % (max(registers.values()), m))
