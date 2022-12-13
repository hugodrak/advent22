import math
class Grid:
    def __init__(self):
        self.visited = [(0,0)]
        self.head = Node('H', 0, 0)
        self.knots = []
        for i in range(1,10):
            self.knots.append(Node(f"{i}",0,0))
        #self.tail = Node('Tail', 0, 0)

    def move(self, direction, steps):
        for i in range(steps):
            match direction:
                case 'U':
                    self.head.y += 1
                case 'L':
                    self.head.x -= 1
                case 'D':
                    self.head.y -= 1
                case 'R':
                    self.head.x += 1

            for i in range(len(self.knots)):
                if i == 0:
                    self.move_knot(self.head, self.knots[0])
                else:
                    self.move_knot(self.knots[i-1], self.knots[i])
                if i == 8:
                    pos = (self.knots[8].x, self.knots[8].y)
                    if pos not in self.visited:
                        self.visited.append(pos)

    def move_knot(self, a, b):
        hx, hy = a.x, a.y
        tx, ty = b.x, b.y
        sqdistX = abs(hx-tx)**2
        sqdistY = abs(hy-ty)**2
        sqdist = sqdistX+sqdistY
    
        if sqdist > 2:
            if sqdistX == 1 and sqdistY == 4:
                if hy < ty:
                    b.x = hx
                    b.y -= 1
                else:
                    b.x = hx
                    b.y += 1
            elif sqdistX == 4 and sqdistY == 1:
                if hx < tx:
                    b.y = hy
                    b.x -= 1
                else:
                    b.y = hy
                    b.x += 1
            elif sqdistX == 4 and sqdistY == 0:
                if hx < tx:
                    b.x -= 1
                else:
                    b.x += 1
            elif sqdistX == 0 and sqdistY == 4:
                if hy < ty:
                    b.y -= 1
                else:
                    b.y += 1
            elif sqdistX == 4 and sqdistY == 4:
                if hy < ty:
                    b.y -= 1
                else:
                    b.y += 1

                if hx < tx:
                    b.x -= 1
                else:
                    b.x += 1
                
            else:
                raise ValueError(f"Vrong pos. sqdist {sqdist} {sqdistX} {sqdistY}")


    def read_instructions(self, lines):
        for line in lines:
            direction, steps = line.split(" ")
            steps = int(steps)
            self.move(direction, steps)
            #print(self.head.name, self.head.x, self.head.y)
            # for knot in self.knots:
            #     print(knot.name, knot.x, knot.y)
            # print("---------")

class Node:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.name}, ({self.x},{self.y})"


if __name__ == "__main__":
    small = open("small", "r").read().splitlines()
    lines = open("input", "r").read().splitlines()
    grid = Grid()
    grid.read_instructions(lines)
    print(len(grid.visited))