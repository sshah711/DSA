# brute force approach
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def intersection_of_2_linkedlist(headA, headB):
    # if not headA or not headB:
    #     return None

    # currentA = headA
    while headA:
        currentB = headB
        while currentB:
            if headA == currentB:
                return headA
            currentB = currentB.next
        headA = headA.next

    return None

# optimized approach using hashing or set
def intersection_of_2_linkedlist1(headA, headB):
    # if not headA or not headB:
    #     return None

    nodes = set()
    # current = headA
    # checking if any node of linked list B is present in linked list A
    while headA:
        nodes.add(headA)
        headA = headA.next

    while headB:
        if headB in nodes:
            return headB
        headB = headB.next

    return None 

headA = Node(4)
headA.next = Node(1)
headA.next.next = Node(8)
headA.next.next.next = Node(4)
headA.next.next.next.next = Node(5)
headB = Node(5)
headB.next = Node(6)
headB.next.next = Node(1)
headB.next.next.next = headA.next.next
headB.next.next.next.next = headA.next.next.next
headB.next.next.next.next.next = headA.next.next.next.next

print(intersection_of_2_linkedlist1(headA, headB).val)
