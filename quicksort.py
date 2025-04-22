import time
import matplotlib.pyplot as plt

def partition(array, start, end):
    pivot = array[start]  
    low = start + 1
    high = end

    while True:
        while low <= high and array[low] < pivot:
            low += 1
        while low <= high and array[high] >= pivot:
            high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def quicksort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quicksort(array, start, p - 1) 
    quicksort(array, p + 1, end)


array = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    array.append(int(input(f"Enter the {i + 1} number: ")))


print("Before sorting: the list items are:", array)


start_time = time.time()
quicksort(array, 0, len(array) - 1)
end_time = time.time()


print("After sorting: the list items are:", array)
print("Time taken for QuickSort:", end_time - start_time)


x=list(range(1,10000))
plt.plot(x,[y for y in x])
plt.title("quicksort")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
