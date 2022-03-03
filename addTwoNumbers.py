# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
        self.numOfNodes = 0
        self.head = None

    def insertAtBegin(self, value):
        self.numOfNodes += 1
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def traverse(self):
        if self.head is None:
            print("the linked list is empty!")
        traverse_node = self.head
        while traverse_node:
            print(traverse_node.val)
            traverse_node = traverse_node.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        array1, array2 = [], []
        while l1 is not None:
            array1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            array2.append(l2.val)
            l2 = l2.next

        num1, num2 = 0, 0
        for i in range(len(array1)):
            add1 = 10 ** (i) * array1[i]
            num1 += add1
        for j in range(len(array2)):
            add2 = 10 ** (j) * array2[j]
            num2 += add2
        total = num1 + num2
        answer_linkedlist = LinkedList()
        for each in str(total):
            answer_linkedlist.insertAtBegin(int(each))
        answer_linkedlist.traverse()
        answers = []
        for i in range(len(str(total))):
            value = int(str(total)[-i - 1])
            answers.append(value)
        print(answers)


