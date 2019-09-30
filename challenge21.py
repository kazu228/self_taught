# 1
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) -1
        return self.items[last]

    def size(self):
        return len(self.items)
        
string = "yesterday"
reverse = ""
stack = Stack()

for c in string:
    stack.push(c)

# print(stack.items)

while stack.size():
    reverse += stack.pop()

print(reverse)
print(stack.items)

list_a = [1,2,3,4,5]
list_b = []

stack = Stack()

for i in list_a:
    stack.push(i)

while stack.size():
    list_b.append(stack.pop())

print(list_b)
print(stack.items)