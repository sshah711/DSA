def max_consecutive_ones(a):
    c = 0
    cmax = 0
    for i in range(0, len(a), 1):
        if a[i] == 1:
            c += 1
        else:
            cmax = max(cmax, c)
            c = 0
    return max(cmax, c)


a = [1, 1, 1, 0, 2, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1]
print(max_consecutive_ones(a))
