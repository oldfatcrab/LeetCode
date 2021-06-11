class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if self.right:
                return self.right.insert(node)
            self.right = node
            return True
        if node.end <= self.start:
            if self.left:
                return self.left.insert(node)
            self.left = node
            return True
        return False

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)