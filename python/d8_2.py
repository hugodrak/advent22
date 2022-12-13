import numpy as np

def lines_to_mat(lines):
    rows = len(lines)
    cols = len(lines[0])
    mat = np.zeros((rows,cols), dtype=np.int32)
    for ri, r in enumerate(lines):
        for ci, c in enumerate(r):
            mat[ri][ci] = int(c)
    return mat

def visible_than(i, row):
    left, val, right = row[:i], row[i], row[i+1:]
    v_left = 0
    for l in left[::-1]:
        if l >= val:
            v_left += 1
            break
        else:
            v_left += 1


    v_right = 0
    for r in right:
        if r >= val:
            v_right += 1
            break
        else:
            v_right += 1

    return v_left * v_right

def look_through(mat, ref):
    mat_T = mat.copy().T
    for ri, row in enumerate(mat):
        if 0 < ri < len(mat)-1:
            h=0
            for ci, val in enumerate(row):
                if 0 < ci < len(row)-1:
                    r_vis = visible_than(ci, row)
                    c_vis = visible_than(ri, mat_T[ci])
                    visible = r_vis * c_vis
                    ref[ri][ci] = visible
    return ref




if __name__ == "__main__":
    small = open("small", "r").read().splitlines()
    lines = open("input", "r").read().splitlines()
    
    mat = lines_to_mat(lines)
    ref = np.ones(mat.shape, dtype=np.int32)
    look_through(mat, ref)
    print(np.amax(ref))
    h=0

