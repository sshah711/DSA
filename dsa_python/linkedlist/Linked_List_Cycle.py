class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


# using set to store the nodes and check if we have already seen the node before
# tc- o(n) sc- o(n)
def has_Cycle(head):
    seennodes = set()
    curr = head
    while curr:
        if curr in seennodes:
            return True
        seennodes.add(curr)
        curr = curr.next

    return False


# better solution using two pointer approach - floyd's cycle detection algorithm
# if cycle exists then the fast pointer will eventually meet the slow pointer
# tc- o(n) sc- o(1)
def has_Cycle1(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head = Node(1)

node2 = Node(2)
head.next = node2

n2 = Node(3)
head.next.next = n2
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Connect 5 back to the existing node 2
head.next.next.next.next.next = node2

# print(has_Cycle(head))
print(has_Cycle1(head))
