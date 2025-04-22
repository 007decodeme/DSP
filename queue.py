class Queue:
    def __init__(self):
        self.queue = []

    def Enqueue(self):
        element = int(input("Enter the element: "))
        self.queue.append(element)
        print(self.queue)

    def Dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            a = self.queue.pop(0)
            print("Dequeued element is", a)

    def size(self):
        print("Size of queue is", len(self.queue))

    def peek(self):
        if not self.queue:
            print("Queue is empty")
        else:
            c = self.queue[0]
            print("Peek value is", c)

queue = Queue()
while True:
    choice = int(input("\nEnter your choice 1-Enqueue 2-Dequeue 3-size 4-peek 5-exit: "))
    if choice == 1:
        queue.Enqueue()
    elif choice == 2:
        queue.Dequeue()
    elif choice == 3:
        queue.size()
    elif choice == 4:
        queue.peek()
    elif choice == 5:
        break
    else:
        print("You have chosen an invalid option. Please enter the correct option.")
