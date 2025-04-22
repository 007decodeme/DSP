class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self): 
        self.head = None 
    def insertFirst(self, data):
        newnode = Node(data)
        if self.head is None:  
            self.head = newnode  
        else:
            newnode.next = self.head
            self.head = newnode
    def removeFirst(self):
        if self.head is None:  
            print("List is empty.")
        else:
            cur = self.head
            self.head = self.head.next
            print("The deleted item is:", cur.data)
    def search(self, item):
        if self.head is None:  
            print("List is empty.")
            return
        cur = self.head
        found = False
        while cur:
            if cur.data == item:
                found = True
                break
            cur = cur.next
        if found:
            print("The data item is  present in the list.")
        else:
            print("The data item is not present in the list.")
    def display(self):
        if self.head is None:  
            print("List is empty.")
        else:
            cur = self.head
            while cur:
                print(cur.data, end=" ")
                cur = cur.next
            print()  
sll = SinglyLinkedList()
while True:
    choice = int(input("\nEnter your choice 1-insert 2-delete 3-search 4-display 5-exit: "))
    if choice == 1:
        item = input("Enter the element to insert: ")
        sll.insertFirst(item)
    elif choice == 2:
        sll.removeFirst()    
    elif choice == 3:
        item = input("Enter the element to search: ")
        sll.search(item)
    elif choice == 4:
        sll.display()
    elif choice == 5:
        break  
    else:
        print("You have chosen an invalid option. Please enter the correct option.")
