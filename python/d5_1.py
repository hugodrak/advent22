import re

comman_match = re.compile(r"move (\d+) from (\d+) to (\d+)")
crate_pattern = re.compile(r"\[(\w+)\]|\s{4}")

def create_stacks(first_lines):
    stacks = [[] for x in range(0, int(first_lines[-1].split(" ")[-2]))]

    for line in first_lines[:-1][::-1]:
        #crates = [s[i] for i in range(1, len(s), 4)]
        crates = crate_pattern.findall(line)
        for i, crate in enumerate(crates):
            if crate != "":
                stacks[i].append(crate)

    return stacks

def move(commands, stacks):
    for command in commands:
        ammount = command[0]
        from_ = command[1]-1
        to_ = command[2]-1
        for _ in range(ammount):
            taken = stacks[from_].pop()
            stacks[to_].append(taken)
    return stacks


if __name__ == "__main__":
    lines = open("d5/data/input", "r").read().splitlines()
    first_lines = []
    first_lines_found = False
    stacks = []
    commands = []
    for line in lines:
        if line == "":
            first_lines_found = True
            stacks = create_stacks(first_lines)
        else:
            if not first_lines_found:
                first_lines.append(line)
            else:
                ma = comman_match.findall(line)
                if ma:
                    res = [int(x) for x in ma[0]]
                    commands.append(res)
            
    stack_done = move(commands, stacks)

    tops = [x[-1] for x in stack_done]
    print("".join(tops))
        
        

