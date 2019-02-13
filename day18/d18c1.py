last = None
pc = 0


def value(v):
    try:
        v = int(v)
    except:
        v = reg[v]
    return v


def snd(r):
    global last
    last = reg[r]
    print(str(last) + " " + "♫"*(last // 1000 + 1))


def set(r, v):
    v = value(v)
    reg[r] = v


def add(r, v):
    v = value(v)
    reg[r] += v


def mul(r, v):
    v = value(v)
    reg[r] *= v


def mod(r, v):
    v = value(v)
    reg[r] %= v


def rcv(r):
    global last
    if value(r) is not 0:
        reg[r] = last
        print(last)
        exit()


def jgz(r, y):
    r = value(r)
    y = value(y)
    if r > 0:
        global pc
        pc += y
        pc -= 1


reg = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
       "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
ops = {"snd": snd, "set": set, "add": add,
       "mul": mul, "mod": mod, "rcv": rcv, "jgz": jgz}

with open("day18/input.txt") as f:
    inst = []
    for l in f:
        inst.append(l)

while pc >= 0 and pc < len(inst):
    curinst = inst[pc]
    curinst = curinst.split()
    if len(curinst) is 2:
        ops[curinst[0]](curinst[1])
    else:
        ops[curinst[0]](curinst[1], curinst[2])
    pc += 1
