import math
class Grid:
    def __init__(self):
        self.visited = [(0,0)]
        self.head = Node('Head', 0, 0)
        self.tail = Node('Tail', 0, 0)

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
            self.move_tail()

    def move_tail(self):
        hx, hy = self.head.x, self.head.y
        tx, ty = self.tail.x, self.tail.y
        sqdistX = abs(hx-tx)**2
        sqdistY = abs(hy-ty)**2
        sqdist = sqdistX+sqdistY
    
        if sqdist > 2:
            if sqdistX == 1 and sqdistY == 4:
                self.tail.x
                if hy < ty:
                    self.tail.x = hx
                    self.tail.y -= 1
                else:
                    self.tail.x = hx
                    self.tail.y += 1
            elif sqdistX == 4 and sqdistY == 1:
                if hx < tx:
                    self.tail.y = hy
                    self.tail.x -= 1
                else:
                    self.tail.y = hy
                    self.tail.x += 1
            elif sqdistX == 4 and sqdistY == 0:
                if hx < tx:
                    self.tail.x -= 1
                else:
                    self.tail.x += 1
            elif sqdistX == 0 and sqdistY == 4:
                if hy < ty:
                    self.tail.y -= 1
                else:
                    self.tail.y += 1
            else:
                raise ValueError(f"Vrong pos. sqdist {sqdist} {sqdistX} {sqdistY}")

            pos = (self.tail.x,self.tail.y)
            if pos not in self.visited:
                self.visited.append(pos)

        

    def read_instructions(self, lines):
       for line in lines:
        direction, steps = line.split(" ")
        steps = int(steps)
        self.move(direction, steps)

class Node:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y


if __name__ == "__main__":
    small = open("small", "r").read().splitlines()
    lines = open("input", "r").read().splitlines()
    grid = Grid()
    grid.read_instructions(lines)
    print(len(grid.visited))