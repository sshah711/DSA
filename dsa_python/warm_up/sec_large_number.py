def sec_large_num(Ar):
    l = Ar[0]
    sl = Ar[0]
    for i in range(len(Ar)):
        if Ar[i] > l:
            sl = l
            l = Ar[i]
        elif Ar[i] > sl:
            sl = Ar[i]
    # Ar.sort()
    # return Ar[-2]
    return sl


a = [-1, -2, -5, -31, 3, 1]
print(sec_large_num(a))
