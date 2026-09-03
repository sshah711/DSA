class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def Middle_of_the_Linked_List(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(50)

middle = Middle_of_the_Linked_List(head)

print(middle.val)
