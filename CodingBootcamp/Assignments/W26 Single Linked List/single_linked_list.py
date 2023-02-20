class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Sll:
    def __init__(self):
        self.head = None

    def front(self):
        if (self.head == None):
            return self
        return self.head.value
    
    def addFront(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return self
        new_node.next = self.head
        self.head = new_node
        return self 
    
    def removeFront(self):
        if (self.head == None):
            return self.head
        # removed_node = self.head
        # self.head = removed_node.next
        # removed_node.next = None
        self.head = self.head.next
        return self.head
    
    def add_back(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            print(runner.value)
            runner = runner.next
        runner.next = new_node
        print(runner.next.value)
        return self
    
mySLL = Sll()
mySLL.addFront(17)
mySLL.addFront(15)
mySLL.addFront(13)
print(mySLL.head.value)
mySLL.removeFront()
print(mySLL.head.value)
print(mySLL)
