if __name__ == "__main__":
    lines = open("d1/data/input", "r").read().splitlines()
    highest = []
    sub = 0
    c  = 0
    for row in lines:
        if row == "":
            highest.append(sub)
            sub = 0
               
        else:
            sub += int(row)
       

    print(sum(sorted(highest, reverse=True)[:3]))