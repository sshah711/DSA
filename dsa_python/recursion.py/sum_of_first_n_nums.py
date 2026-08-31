def sum_of_first_n_nums(n):
    if n < 1:
        return 0
    return n + sum_of_first_n_nums(n - 1)


print(sum_of_first_n_nums(5))


def fect(n):
    if n < 1:
        return 1
    return n * fect(n - 1)


print(fect(4))


def fibo(n):
    if n == 1 or n == 0:
        return 1
    return n + fibo(n - 1)


print(fibo(4))
