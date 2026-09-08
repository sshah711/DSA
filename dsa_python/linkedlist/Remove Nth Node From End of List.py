class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 2pass solution - first pass is to calculate the length of the linked list and second pass is to remove the nth node from the end of the list
def Remove_Nth_Node_From_End_of_List(head, n):
    sentinel = ListNode()
    sentinel.next = head

    length = 0
    while head:
        head = head.next
        length += 1

    prevpos = length - n
    prev = sentinel
    for _ in range(prevpos):
        prev = prev.next
    prev.next = prev.next.next
    return sentinel.next

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
head.next.next.next.next.next = ListNode(8)

print_list(head)
head = Remove_Nth_Node_From_End_of_List(head, 2)
print_list(head)
