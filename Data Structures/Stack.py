class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None 
        return self.items.pop()
    
    def peek(self):
        return self.items[-1] if self.is_empty() is False else None
    
    def length(self):
        return len(self.items)