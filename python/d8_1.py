import numpy as np

def lines_to_mat(lines):
    rows = len(lines)
    cols = len(lines[0])
    mat = np.zeros((rows,cols), dtype=np.int8)
    for ri, r in enumerate(lines):
        for ci, c in enumerate(r):
            mat[ri][ci] = int(c)
    return mat

def visible_than(i, row):
    left, val, right = row[:i], row[i], row[i+1:]
    v_left = all([True if val > x else False for x in left])
    v_right = all([True if val > x else False for x in right])
    return v_left or v_right

def look_through(mat, ref):
    mat_T = mat.copy().T
    for ri, row in enumerate(mat):
        if 0 < ri < len(mat)-1:
            h=0
            for ci, val in enumerate(row):
                if 0 < ci < len(row)-1:
                    r_vis = visible_than(ci, row)
                    c_vis = visible_than(ri, mat_T[ci])
                    visible = r_vis or c_vis
                    ref[ri][ci] = 1 if visible else 0
    return ref




if __name__ == "__main__":
    small = open("small", "r").read().splitlines()
    lines = open("input", "r").read().splitlines()
    
    mat = lines_to_mat(lines)
    ref = np.ones(mat.shape, dtype=np.int8)
    look_through(mat, ref)
    print(np.count_nonzero(ref))
    h=0

