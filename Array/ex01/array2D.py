def slice_me(fam: list, start: int, end: int) -> list:
    if (type(fam) is not list or start >= len(fam) or end >= len(fam)):
        print("Error : out of range.")
        return
    col = len(fam)
    row = len(fam[0])
    for f in fam:
        if len(f) != row:
            print("Error : lists not all of same size.")
            return
    print("My shape is : (", col, ",", row, ")")
    if (start < 0):
        start = len(fam) + start
    if (end < 0):
        end = len(fam) + end
    print("My new shape is : (", end - start, ",", row, ")")
    ret = []
    for i in range(start, end):
        ret.append(fam[i])
    return ret
