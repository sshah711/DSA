def insertsort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > cur:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = cur
    return arr

arr = [2, 5, 1, 4, 8, -1, 3]
print(insertsort(arr))
