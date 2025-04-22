import time
import matplotlib.pyplot as plt 


def mergesort(list1):
    if len(list1) > 1:  
        mid = len(list1) // 2  
        left = list1[:mid]
        right = list1[mid:]

        mergesort(left) 
        mergesort(right) 

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k += 1

       
        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1

    return list1



list1 = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    list1.append(int(input(f"Enter the {i + 1} number: ")))

print("Before merge sorting: the list items are", list1)


start = time.time()
list1 = mergesort(list1)
end = time.time()

print("After Merge sorting: The list items are", list1)
print("Time taken for merge sorting: ", end - start)

x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("mergesort")
plt.xlabel("input") 
plt.ylabel("time")
plt.show()
