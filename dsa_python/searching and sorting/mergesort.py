def mergesort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        mergesort(arr, l, mid)
        mergesort(arr, mid + 1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    leftarr = arr[l : mid + 1]
    rightarr = arr[mid + 1 : r + 1]

    i = 0
    j = 0
    k=l
    while i < len(leftarr) and j < len(rightarr):
        if leftarr[i] <= rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
        else:
                arr[k] = rightarr[j]
                j += 1
        k += 1

    while i < len(leftarr):
        arr[k] = leftarr[i]
        i += 1
        k += 1

    # Copy remaining elements of right array
    while j < len(rightarr):
        arr[k] = rightarr[j]
        j += 1
        k += 1

arr = [2, 5, 1, 4, 8, -1, 3]
mergesort(arr, 0, len(arr) - 1)
print(arr)
