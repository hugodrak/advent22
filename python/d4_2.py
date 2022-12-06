

if __name__ == "__main__":
    lines = open("d4/data/input", "r").read().splitlines()
    c = 0
    for line in lines:
        range1, range2 = [range(int(x.split("-")[0]),int(x.split("-")[1])+1) for x in line.split(",")] 
        if sum(e in range2 for e in range1) > 0 or sum(f in range1 for f in range2) > 0:
            c += 1

    print(c)