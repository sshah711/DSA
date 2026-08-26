def single_num(n):
    x = 0
    for i in range(len(n)):
        x = x ^ n[i]
        # print(x)
    return x


n = [1, 1, 2, 3, 3, 4, 4, 5, 5]
print(single_num(n))
