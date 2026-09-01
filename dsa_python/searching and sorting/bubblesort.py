def bubblesort(arr):
    for i in range(len(arr) - 1):
        isSwapped=False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                isSwapped=True
        if(not isSwapped):
           break
    return arr


arr = [6, 4, 8, 2, 5, 1]
arr = [1,2,3]
print(bubblesort(arr))
