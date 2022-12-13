class Register:
    def __init__(self, start):
        self.val = start

    def add(self, val):
        self.val += val


def check_val(cycle, X):
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
    small = open("small", "r").read().splitlines()
    lines = open("input", "r").read().splitlines()
    cycle = 0
    X = Register(1)
    tot = 0
    for line in lines:
        sp = line.split(" ")
        match sp[0]:
            case "noop":
                cycle += 1
                tot += check_val(cycle, X)
            case "addx":
                cycle += 1
                tot += check_val(cycle, X)
                cycle += 1
                tot += check_val(cycle, X)
                X.add(int(sp[1]))
    print('tot:',tot)

