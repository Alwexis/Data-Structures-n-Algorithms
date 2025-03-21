class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)
    
    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items) if len(self.items) > 0 else None
