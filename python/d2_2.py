win_mat = [[3,4,8],
           [1,5,9],
           [2,6,7]]
def win(elf, me):
   elf_index = ord(elf) - 65
   me_index = ord(me) - 88
   return win_mat[elf_index][me_index]

if __name__ == "__main__":
    lines = open("d2/data/input", "r").read().splitlines()
    tot = 0
    c = 0
    for row in lines:
        
        elf, me = row.split(" ")
        score = win(elf, me)
        print(score)
        tot += score
        c+=1
    print(tot)