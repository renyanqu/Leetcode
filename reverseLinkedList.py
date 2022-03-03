class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
##############################################################
class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def reverse(self):
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def insertAtBegining(self, val):
        new_node = LinkedNode(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

