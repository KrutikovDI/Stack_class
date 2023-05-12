class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    d = Stack()
    print(d.is_empty())
    d.push('and')
    d.push(56)
    d.push('f')
    # print(d.peek())
    # print(d.size())
    # print(d.pop())
    # print(d.size())
    print(d.items())