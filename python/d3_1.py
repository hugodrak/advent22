def non_uniq(comp1, comp2):
    nu = ""
    for a in comp1:
        for b in comp2:
            if a == b:
                return a

def convert(cha):
    if (o := ord(cha)) > 90:
        return o - 96
    else:
        return o - 38


if __name__ == "__main__":
    lines = open("d3/data/input", "r").read().splitlines()
    tot = 0
    for line in lines:
        ll = len(line)//2
        first,second = line[:ll], line[ll:]
        nu = non_uniq(first, second)
        tot += convert(nu)
    print(tot)

