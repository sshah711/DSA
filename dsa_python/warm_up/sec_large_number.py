def sec_large_num(Ar):
    if len(Ar) < 2:
        return "null"
    l = Ar[0]
    sl = Ar[0]
    for i in range(len(Ar)):
        if Ar[i] > l:
            sl = l
            l = Ar[i]
        elif Ar[i] > sl and Ar[i] != l:
            sl = Ar[i]
    # Ar.sort()
    # return Ar[-2]
    return sl


a = [-1, -2, -5, -31, 3, 3,3,7,7,7]
aa = [1]
aaa = []
print(sec_large_num(a))
print(sec_large_num(aa))
print(sec_large_num(aaa))
