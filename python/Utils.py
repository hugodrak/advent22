import re
def load_grid(lines, pattern, convert_type=False):
    patt = re.compile(pattern)
    out = []
    cols = 0
    for line in lines:
        match = patt.findall(line)
        if match:
            if cols == 0:
                cols = len(match)
            if len(match) != cols:
                raise ValueError("Grid is irregular in size")   
            out.append(match)
    print('Size:', f"{len(out)}x{cols}")
    return out




if __name__ == "__main__":
    lines = """    [Q]         [N]             [N]
[H]     [B] [D]             [S] [M]
[C]     [Q] [J]         [V] [Q] [D]
[T]     [S] [Z] [F]     [J] [J] [W]
[N] [G] [T] [S] [V]     [B] [C] [C]
[S] [B] [R] [W] [D] [J] [Q] [R] [Q]
[V] [D] [W] [G] [P] [W] [N] [T] [S]
[B] [W] [F] [L] [M] [F] [L] [G] [J]"""
    print(load_grid(lines.split("\n"), r"\[(\w+)\]|\s{4}"))

