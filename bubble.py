import time
import matplotlib.pyplot as plt
def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
a=[55,66,12,8,7,36,28,96,101,200]
start=time.time()
print("Before sorting:",a)
bubblesort(a)
print("After sorting:",a)
end=time.time()
print("runtime of the program is",end-start)
x=list(range(1,10000))

plt.plot(x,[y*y for y in x])
plt.title("Bubble sort Time complexity is")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
