def exec_op(op, old):
    sp = op.split(" ")
    first_val = sp[2]
    operator = sp[3]
    second_val = sp[4]

    if first_val == "old":
        first_val = old
    else:
        first_val = int(first_val)

    if second_val == "old":
        second_val = old
    else:
        second_val = int(second_val)
    
    match operator:
        case '+':
            return first_val + second_val
        case '-':
            return first_val - second_val
        case '*':
            return first_val * second_val
        case '/':
            return int(first_val / second_val)


class Monkey:
    def __init__(self, number, starting_items, operation, test, test_cases):
        self.number = number
        self.items = starting_items
        self.operation = operation
        self.test_raw = test
        self.test_true = test_cases[0]
        self.test_false = test_cases[1]
        self.times_inspected = 0

    def operate(self, worry):
        res =  exec_op(self.operation, worry)
        return res

    def test(self, worry):
        div = int(self.test_raw.split(" ")[2])
        if worry % div == 0:
            return self.test_true
        else:
            return self.test_false

    def inspect(self):
        self.times_inspected += 1
        worry = self.items.pop(0)
        operated_worry = self.operate(worry)
        regulated_worry = operated_worry # no regulation
        #regulated_worry = int(operated_worry / 3)
        next_monky = self.test(regulated_worry)
        return next_monky, regulated_worry

    def has_items(self):
        return len(self.items) > 0 


class Player:
    def __init__(self):
        self.worry = 0

    def after_inspect(self):
        self.worry = int(self.worry / 3)
        return self.worry

class Round:
    def __init__(self, monkies):
        self.monkies = monkies

    def run(self):
        for monky in monkies:
            while monky.has_items():
                next_monky, worry = monky.inspect()
                monkies[next_monky].items.append(worry)

if __name__ == "__main__":
    small = open("small", "r").read().splitlines()
    lines = open("input", "r").read().splitlines()
    monkies = []
    monk_build = False
    mdict = {'id': '', 'items': [], 'op': "", 'test': '', 'IT': '', 'IF': ''}
    for line in small:
        sp = line.split(" ")
        if line[:6] == "Monkey":
            monk_build = True
            mdict['id'] = int(sp[1][:1])
        elif line[:17] == "  Starting items:":
            mdict['items'] = [int(x.rstrip(',')) for x in sp[4:]]
        elif line[:12] == "  Operation:":
            mdict['op'] = line[13:]
        elif line[:7] == "  Test:":
            mdict['test'] = line[8:]
        elif line[:12] == "    If true:":
            mdict['IT'] = int(line[29:])
        elif line[:13] == "    If false:":
            mdict['IF'] = int(line[30:])
        else:
            if monk_build:
                M = Monkey(mdict['id'], mdict['items'], mdict['op'], mdict['test'], (mdict['IT'], mdict['IF']))
                monkies.append(M)
                monk_build = False
    if monk_build:
                M = Monkey(mdict['id'], mdict['items'], mdict['op'], mdict['test'], (mdict['IT'], mdict['IF']))
                monkies.append(M)
                monk_build = False

    # --------- run round --------
    R = Round(monkies)  
    for i in range(1, 10_00+1): # prev 20
        R.run()
        if i % 200 == 0:
            print(f"== After round {i} ==")
            for m in monkies:
                print(f"Monkey {m.number} inspected items {m.times_inspected} times.")
    
    stats = [(m.number, m.times_inspected) for m in monkies]
    stats.sort(key=lambda x: x[1], reverse=True)
    print(stats[:2])
    print("ans:", stats[0][1]*stats[1][1])

    h=0

