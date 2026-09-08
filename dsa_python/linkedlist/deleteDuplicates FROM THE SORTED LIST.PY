class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    curr=head
    while curr and curr.next:
        if curr.val==curr.next.val:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head



def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

print_list(head)
head = deleteDuplicates(head)
print_list(head)
