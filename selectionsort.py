import matplotlib.pyplot as plt
def selectionsort(array):
    n=len(array)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if array[j]<array[min]:
                min=j
        array[i],array[min]=array[min],array[i]
    return array
array=[]
n=int(input("how many element??"))
for i in range(n):
    array.append(int(input("enter %d number:"%i)))
print(f"before swapping:{array}")
array=selectionsort (array)
print(f"after swappoing:{array}")

x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("selection sort time complexity  is O(n/uoob2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
