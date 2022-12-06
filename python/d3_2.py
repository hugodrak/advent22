def find_common(a,b,c):
    au = set(a)
    bu = set(b)
    cu = set(c)
    comm = au & bu & cu
    return comm.pop()

def convert(cha):
    if (o := ord(cha)) > 90:
        return o - 96
    else:
        return o - 38


if __name__ == "__main__":
    lines = open("d3/data/input", "r").read().splitlines()
    tot = 0
    for lg in [lines[i:i+3] for i in range(0, len(lines), 3)]:
        A, B, C = lg
        nu = find_common(A, B, C)
        tot += convert(nu)
    print(tot)

