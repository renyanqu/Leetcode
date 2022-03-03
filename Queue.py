### FIFO : first item inserted is the first to be taken out

class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            print("the queue is empty!")
        data = dequeue[0]
        del dequeue[0]
        return data
