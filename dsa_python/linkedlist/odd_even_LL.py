class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

# All nodes at odd positions come first.
# Then all nodes at even positions come after them.
# Position means index in the list (1st, 2nd, 3rd...), not the node value
def odd_even(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while odd.next and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head
    return head

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(12)
head.next.next.next.next.next = Node(11)

print_list(head)
head = odd_even(head)
print_list(head)
