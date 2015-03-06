import numpy

# O(n) solution
def solve_linear(relationships):
    people = relationships.shape[0]
    is_celeb = []
    for i in range(0,people):
        is_celeb.append(True)

    p1 = 0
    p2 = 1

    while p1 < people and p2 < people:
        if not is_celeb[p1]:
            p1 += 1
        elif relationships[p1][p2] == 1:
            is_celeb[p1] = False
            p1 += 1
            p2 += 1
        else:
            is_celeb[p2] = False
            p2 += 1

    celeb = -1
    for i in range(0,people):
        if is_celeb[i]:
            if celeb < 0:
                celeb = i
            else:
                print("ERROR: both %d and %d are marked as celebrities" % (celeb, i))

    is_really_celeb = True
    for i in range(0,people):
        if i != celeb:
            if relationships[celeb][i] == 1 or relationships[i][celeb] != 1:
                is_really_celeb = False
                break

    if is_really_celeb:
        return celeb
    return -1

# O(n^2) solution
def solve_quadratic(relationships):
    people = relationships.shape[0]
    rows = []
    cols = []

    for i in range(0,people):
        rows.append(False)
        cols.append(True)

    for row in range(0,people):
        for col in range(0,people):
            if row != col:
                rows[row] = rows[row] or (relationships[row][col] == 1)
                cols[col] = cols[col] and (relationships[row][col] == 1)

    for i in range(0,people):
        if not rows[i] and cols[i]:
            return i
    return -1
