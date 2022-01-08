def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True

    return arr
print(bubble_sort([12,12,11,23,45,65,76,9]))

def bubble_Sort(arr):
    x=0
    l = len(arr)
    h = l//2
    while x != h +1:
        h=h+1
        for i in range(l):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

print([12,12,11,23,45,65,76,9])
