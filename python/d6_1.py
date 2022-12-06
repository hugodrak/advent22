# In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.
def check_chars(chars):
    check = set(chars)
    checklen = 0
    for c in check:
        if c != "":
            checklen += 1
    return checklen == len(chars)

if __name__ == "__main__":
    small = open("small", "r").read()
    lines = open("input", "r").read()
    # last_four = ["", "", "", ""]
    # i = 0
    # index = 0
    # for char in lines:
    #     last_four[i] = char
    #     if check_chars(last_four):
    #         print(index+1, lines[index], lines[:index+1], )
    #         break
    #     i += 1
    #     i %= 4
    #     index += 1
    for i in range(len(small)):
        if check_chars(small[i:i+4]):
            print(i+4,small[i:i+4])
            break

