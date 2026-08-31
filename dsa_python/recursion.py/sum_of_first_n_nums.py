def sum_of_first_n_nums(n):
    if n < 1:
        return 0
    return n + sum_of_first_n_nums(n - 1)


print(sum_of_first_n_nums(5))


def fect(n):
    if n == 1:
        return 1
    return n * fect(n - 1)


print(fect(5))


def fibo(n):
    if n == 1 or n == 0:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(4))
