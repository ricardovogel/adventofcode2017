def moveScanners():
    for i in range(0, len(layers)):
        l = layers[i]
        if l is not [] and True in l:
            scanner = l.index(True)

            if scanner is 0:
                movingDown[i] = True

            if scanner is len(l) - 1:
                movingDown[i] = False

            if movingDown[i]:
                l[scanner] = False
                l[scanner + 1] = True

            elif not movingDown[i]:
                l[scanner] = False
                l[scanner - 1] = True


class Packet:
    def __init__(self):
        self.position = 0
        self.severity = 0
        self.scanned = False

    def movePacket(self):
        if len(layers[self.position]) is not 0:
            if layers[self.position][0]:
                self.severity += self.position * len(layers[self.position])
                self.scanned = True

        self.position += 1


layerCount = 90
layers = []
for i in range(0, layerCount):
    layers.append([])

with open("day13/input.txt") as f:
    for l in f:
        s = l.split()
        i = int(s[0][:-1])
        for j in range(0, int(s[1])):
            layers[i].append(False)
        layers[i][0] = True

movingDown = []
for i in range(0, layerCount):
    movingDown.append(True)

p = Packet()

for i in range(0, layerCount):
    p.movePacket()
    moveScanners()

print(p.severity)
