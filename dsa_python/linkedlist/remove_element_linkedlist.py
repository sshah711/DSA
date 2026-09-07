class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_element_linkedlist(head, val):
    sentinel = ListNode()
    sentinel.next = head
    prev = sentinel
    # use sentinel node(kind of dummy node that add to front) to handle the case when the head node needs to be removed
    while prev and prev.next:
        if prev.next.val == val:
            prev.next = prev.next.next
        else:
            prev = prev.next
    return sentinel.next

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(2)
node6 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print_list(node1)
head = remove_element_linkedlist(node1, 3)
print_list(head)
