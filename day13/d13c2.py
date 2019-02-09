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
    def __init__(self, delay=0):
        self.position = 0
        self.severity = 0
        self.scanned = False
        self.done = False
        self.delay = delay

    def movePacket(self):
        if p.done:
            return

        if self.position >= layerCount:
            self.done = True
            return

        if len(layers[self.position]) is not 0:
            if layers[self.position][0]:
                self.severity += self.position * len(layers[self.position])
                self.scanned = True

        self.position += 1


layerCount = 89
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

packets = []
stop = False

delay = 0
while not stop:
    packets.append(Packet(delay))
    delay += 1
    for p in packets:
        if p.done:
            if not p.scanned:
                print(p.delay)
                stop = True
            packets.remove(p)
        else:
            p.movePacket()
    moveScanners()
