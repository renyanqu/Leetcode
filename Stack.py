### stack LIFO structure: last inserted in is the first to be taken out

class Stack:

    def __init__(self):
        self.stack = []

    def pop_stack(self):
        if len(self.stack) == 0:
            print("the stack is empty!")
        val = self.stack[-1]
        del self.stack[-1]

        return val

    def push_stack(self, val):
        self.stack.append(val)

    def peek(self):
        if len(self.stack) == 0:
            print("the stack is empty")
        print(self.stack[-1])







