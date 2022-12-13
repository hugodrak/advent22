import numpy as np
class Register:
    def __init__(self, start):
        self.val = start

    def add(self, val):
        self.val += val

class Monitor:
    def __init__(self, widht, height):
        self.mat = np.zeros((height, widht), dtype=np.int16)

    def add(self,x,y):
        self.mat[y][x] = 1

    def print(self):
        for row in self.mat:
            prow = []
            for c in row:
                if c == 0:
                    prow.append(".")
                elif c == 1:
                    prow.append("#")
            print("".join(prow))



def check_val(cycle, X, mon):
    #      0 ##..##..##..##..##..##..##..##..##..##..
    #     41 ###...###...###...###...###...###...###. 80
    if cycle == 8:
            h=0
    if (X.val-1) <= cycle%40-1 <= (X.val+1):
        mon.add(cycle%40-1, cycle//40)
    #print(cycle, X.val, X.val*cycle)
    if cycle == 20:
        print(cycle, X.val, X.val*cycle)
        return X.val*cycle
    elif (cycle+20) % 40 == 0:
        print(cycle, X.val, X.val*cycle)
        return X.val*cycle
    else:
        return 0



if __name__ == "__main__":
    # 40 wide and 6 high    
    small = open("small", "r").read().splitlines()
    lines = open("input", "r").read().splitlines()
    cycle = 0
    X = Register(1)
    mon = Monitor(40, 6)
    mon.print()
    tot = 0
    for line in lines:
        sp = line.split(" ")
        match sp[0]:
            case "noop":
                cycle += 1
                tot += check_val(cycle, X, mon)
            case "addx":
                cycle += 1
                tot += check_val(cycle, X, mon)
                cycle += 1
                tot += check_val(cycle, X, mon)
                X.add(int(sp[1]))
                #tot += check_val(cycle, X, mon)
    mon.print()
    print('tot:',tot)

