# In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.
def check_chars(chars):
    check = set(chars)
    checklen = 0
    for c in check:
        if c != "":
            checklen += 1
    return checklen == len(chars)

if __name__ == "__main__":
    small = open("small", "r").read().splitlines()
    small_list = [x.split(":")[0] for x in small]
    lines = open("input", "r").read()
    for small in small_list:
        for i in range(len(small)):
            if check_chars(small[i:i+14]):
                print(i+14,small[i:i+14])
                break
    
    for i in range(len(lines)):
        if check_chars(lines[i:i+14]):
            print(i+14,lines[i:i+14])
            break