def reverse_num(n):
    copyn = n
    rev = 0
    # last digit (reminder) n%10
    # remove last digit n/10
    if n == 0:  # corner case
        return 0
    n = abs(n)  # corner case

    while n > 0:
        rem = n % 10
        rev = 10 * rev + rem
        n = n // 10

    return -rev if copyn < 0 else rev

    # if(copyn<0):
    #     return -rev
    # else:
    #     return rev


n = -143

print(reverse_num(n))


def rev(n):
    s = str(n)
    return s[::-1]


print(rev(-127210))
