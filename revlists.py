
class Node:
    def __init__(self,inp):
        self.inp = inp
        self.next = None

class Revlists:
    def __init__(self):
        self.head = None
        self.next_node = None

   # print("This is a Linked List.\n ")
    # n = int(input("Enter the number of nodes in the Linked List"))
     #We can use any word instead of append here but just use the same  when declaring the function below to add data
    def append(self, inp): 
        if self.next_node is None:            
            self.head = Node(inp)
            self.next_node = self.head
        else:
            self.next_node.next = Node(inp)
            self.next_node = self.next_node.next

    def reverse(self):
        while self.next_node is not None:
            prev = self.next_node
            self.head = self.next_node
            self.next_node = self.next_node.next
            print(prev)

REV = Revlists()
n = int(input("Enter the number of nodes for the linked lists: "))
for i in range(n):
    inp = int(input("Enter the data for the system:"))
    REV.append(inp)
print("The reversed form of the linklist you applied is\n")
REV.reverse()


    
