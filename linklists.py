class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def add(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def display(self):
        current = self.head
        while current is not None:
            print(current.data," ->", end = '')
            current = current.next
    
    def Search(self,target):
        current = self.head
        print("The value being searhed : ",(target))
        while current != None:
            if current.data == target:
                return "Element is present"
            current = current.next
        return "Element is not present"

    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): # the number will be swapped until the last element becomes fast and so on
            next = current.next
           # print(next.data)
           # print("current:",current.data)
            current.next = prev 
           # print(current.next.data)
            #print(prev.data)
            prev = current 
           # print("prevdata",prev.data)
            #print("current.data",current.data)
            current = next
            #while (current is not None):
            print(current.data)
                #current = current.next
            #print("final current",current.data)
            #print("The reversed Link List")    
            
        # self.head = prev 
        # temp = self.head
        # while (temp is not None):
        #     print(temp.data)
        #     temp= temp.next
        
Linklist = LinkedList()
n = int(input('How many elements would you like to add? '))
for i in range(n):
    data = int(input('Enter data item: '))
    Linklist.add(data)
print('The linked list: ', end = '')
print("\nChoose an option to do one thing:\n1:Display\n2:Search\n3:Reverse")
opt = int(input("Enter the option : "))
if opt == 1:
    Linklist.display()
elif opt == 2:
    target = int(input("Enter the number to search :"))
    print(Linklist.Search(target))
elif opt == 3:
    Linklist.reverse()
else:
    print("That option is not available")
