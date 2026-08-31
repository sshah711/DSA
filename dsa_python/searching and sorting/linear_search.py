def linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

a = [3, 1, 2, 6, 5, 7]
print(linear(a, 5))
