class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linkedlist(head):
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    # head=prev
    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(50)

print("Before reversing the linked list:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next

head = reverse_linkedlist(head)
print("\nAfter reversing the linked list:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
