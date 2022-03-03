class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_linked_list(l1: LinkedNode, l2: LinkedNode) -> LinkedNode:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    prehead = LinkedNode(0)
    traverse = prehead
    while l1 and l2:
        if l1.data <= l2.data:
            traverse.next = l1
            l1 = l1.next
        else:
            traverse.next = l2
            l2 = l2.next
        traverse = traverse.next