# select the minimum element and move this min element to right position
def selectionsort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:   #agar ye condition nhi rkhege to swapping wala code jyada time run hoga , isko avoid krne ke liye ye conditon rkhi
            arr[i], arr[min] = arr[min], arr[i]
    return arr


arr = [2, -5, 1, 6, 8, 3]
print(selectionsort(arr))
