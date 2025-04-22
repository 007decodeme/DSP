import time
import matplotlib.pyplot as plt
def linearsearch(a,key):
    n=len(a)
    for i in range(n):
        if a[i]==key:
            return i;
    return-1
a=[13,24,35,46,57,68,79]
start=time.time()
print(f" the array elemaents are:{a}")
k=int(input("enter the key element to search:"))
result=linearsearch(a,k)
if result==-1:
    print("search Unsuccessful")
else:
    print("search successful key found at% d location:",result)
end=time.time()
print("Runtime of the program is",end-start)
x=list(range(1,10000))
plt.plot(x,[y for y in x])
plt.title("linear search-time complexity is O(n)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
                










                      
