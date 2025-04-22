
class Stack:
    def __init__(self):
        self.stack = []

    def push(self):
        element = int(input("Enter the element: "))
        self.stack.append(element)
        print(self.stack)

    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            a = self.stack.pop()
            print("Popped element is", a)

    def size(self):
        print("Size of stack is", len(self.stack))

    def peek(self):
        if not self.stack:
            print("Stack is empty")
        else:
            c = self.stack[-1]
            print("Peek value is", c)

stack = Stack()
while True:
        choice = int(input("\nEnter your choice 1-push 2-pop 3-size 4-peek 5-exit: "))
        if choice == 1:
            stack.push()
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.size()
        elif choice == 4:
            stack.peek()
        elif choice == 5:
            break
        else:
            print("You have chosen an invalid option. Please enter the correct option.")
