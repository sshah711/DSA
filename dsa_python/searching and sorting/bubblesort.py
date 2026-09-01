# after the first iteration largest number is bubble up at the end of arr

def bubblesort(arr):
    for i in range(len(arr) - 1):
        isSwapped = False  # check for is swapped or not bcoz if the array is already sorted at that time also this whole loop runs, so avoiding these we can make boolean function that checks wethear swapped or not
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                isSwapped = True
        if not isSwapped:
            break
    return arr


arr = [6, 4, 8, 2, 5, 1]
arr = [1, 2, 3]
print(bubblesort(arr))
