import matplotlib.pyplot as plt
def insertionsort(array):
    n=len(array)
    for step in range(1,n):
        item=array[step]
        j=step-1
        while j>=0 and item<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]
    return array

array=[]
n=int(input("how many element??:"))
for i in range(n):
    array.append(int(input("emter %d number:"%i)))
print(f"before swapping:{array}")
array=insertionsort(array)    
print(f"after swapping:{array}")
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.plot("insertion sort time complexing is o(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()