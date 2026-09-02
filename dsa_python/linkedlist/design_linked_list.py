class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val):
        newnode = Node(val)

        newnode.next = self.head
        self.head = newnode

        self.size += 1

    def addAtTail(self, val):
        newnode = Node(val)

        if(self.head== None):
            self.head=newnode

        else:
            current = self.head

            while current.next != None:
                current=current.next

            # newnode = Node(val)
            current.next=newnode


        self.size += 1

    def addAtIndex(self, index, val):
        newnode= Node(val)

        if(index==0):
            self.addAtHead(val)
            return
        elif(index==self.size):
            self.addAtTail(val)
            return
        else:
            current=self.head

            for i in range(index-1):
                current=current.next

            newnode.next=current.next
            current.next=newnode

        self.size += 1
       

ll = MyLinkedList()

ll.addAtHead(10)
ll.addAtHead(20)
ll.addAtHead(30)
ll.addAtTail(302)
ll.addAtTail(330)
ll.addAtIndex(1,110)
ll.addAtIndex(4,90)

current = ll.head

while current:
    print(current.val, end=" → ")
    current = current.next