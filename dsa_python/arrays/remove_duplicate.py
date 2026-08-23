def remove_duplicate(a):
    # using 2 pointer
    p1 = 0
    for i in range(len(a)):
        if a[i] > a[p1]:
            p1 = p1 + 1
            a[p1] = a[i]
    return len(a) - (p1 + 1), (p1 + 1),a
    # total duplicate element no, total unique element nums, modified array


aa = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5]
print(remove_duplicate(aa))
