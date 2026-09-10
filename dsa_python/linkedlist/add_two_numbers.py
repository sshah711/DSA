class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:

        total = carry

        if l1:
            total += l1.val
            l1 = l1.next

        if l2:
            total += l2.val
            l2 = l2.next

        carry = total // 10
        digit = total % 10

        curr.next = Node(digit)
        curr = curr.next

    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# l1 = [2,4,3]
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

# l2 = [5,6,4]
l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

result = add_two_numbers(l1, l2)

print_list(result)
