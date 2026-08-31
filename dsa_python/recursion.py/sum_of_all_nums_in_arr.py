def sum_of_all_nums_in_arr(n):
    if n == 0:
        return a[n]
    return a[n] + sum_of_all_nums_in_arr(n - 1)


a = [1, 4, 3, 2, 7, 8]
print(sum_of_all_nums_in_arr(len(a) - 1))


def sum_of_all_odd_nums(n):
        if n == 0:
            if a[n] % 2 == 0:
                return 0
            else:
                return a[n]
            
        if a[n] % 2 == 0:
            return 0 + sum_of_all_odd_nums(n-1)
        else:
            return a[n] + sum_of_all_odd_nums(n - 1)


a = [1, 4, 3, 2, 7, 8]
print(sum_of_all_odd_nums(len(a) - 1))
