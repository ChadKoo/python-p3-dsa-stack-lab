class Stack:

    def __init__(self, items = [], limit = 100):
        self.stack = []
        self.limit = limit
        self.items = []  # keep this to match tests!

        if items:
            for char in items:
                self.stack.append(char)
                self.items.append(char)  # sync items

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        if len(self.stack) < self.limit:
            self.stack.append(item)
            self.items.append(item)  # sync items

    def pop(self):
        if not self.isEmpty():
            popped = self.stack.pop()
            self.items.pop()  # sync items
            return popped

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def full(self):
        return len(self.stack) == self.limit

    def search(self, target):
        if target in self.stack:
            index_from_bottom = self.stack.index(target)
            index_from_top = len(self.stack) - index_from_bottom - 1
            return index_from_top
        else:
            return -1
