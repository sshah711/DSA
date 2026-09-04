class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def palindrome_linkedlist(head):

    # finding middle of the linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #  reversing the second half of the linked list
    prev = None
    curr = slow
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    # checking if the first half and the second half are equal
    first = head
    second = prev
    while second:
        if first.val == second.val:
            first = first.next
            second = second.next
        else:
            return False
    return True

head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(2)
# head.next.next.next.next.next = Node(1)

print(palindrome_linkedlist(head))
