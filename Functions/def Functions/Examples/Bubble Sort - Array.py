# Bubble Sort - Array

def bubbleSort(arr):
    l = len(arr)
    
    for pass_round in range(l):
        for i in range(l - pass_round - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print("Sorted array:", arr)

arr = [17, 28, 25, 1, 32, 3, 40]
bubbleSort(arr)

