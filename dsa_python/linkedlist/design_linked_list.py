class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            # print(-1)
            return -1

        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        newnode = Node(val)
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def addAtTail(self, val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newnode

        self.size += 1

    def addAtIndex(self, index, val):
        newnode = Node(val)

        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        elif index == self.size:
            self.addAtTail(val)
            return
        else:
            current = self.head

            for i in range(index - 1):
                current = current.next

            newnode.next = current.next
            current.next = newnode

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1


ll = MyLinkedList()

ll.addAtHead(10)
ll.addAtHead(20)
ll.addAtHead(30)
ll.addAtTail(302)
ll.addAtTail(330)
ll.addAtIndex(1, 110)
ll.addAtIndex(4, 90)
ll.get(4)
ll.deleteAtIndex(0)
ll.deleteAtIndex(1)
ll.get(40)
ll.get(2)
ll.addAtIndex(4, 900)

current = ll.head

while current:
    print(current.val, end=" → ")
    current = current.next
