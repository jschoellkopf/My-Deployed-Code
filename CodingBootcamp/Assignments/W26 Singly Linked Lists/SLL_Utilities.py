class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
    
    def addFront(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return self
        new_node.next = self.head
        self.head = new_node
        return self
    

    def contains(self, value):
        runner = self.head
        is_found = False
        while runner.value:
            if (runner.value == value):
                is_found = True
                return is_found
            runner = runner.next
        return is_found
    
    def length(self):
        if not self.head:
            print("This SLL is currently empty, try adding a node with addFront()")
            return self
        counter = 0
        runner = self.head
        while runner:
            counter += 1
            runner = runner.next
            # print(counter)
        return counter

    def display_values(self):
        if not self.head:
            print("This SLL is currently empty, try adding a node with add_front()")
            return self
        values = ""
        runner = self.head
        while runner:
            values += (str(runner.value) + "/")
            # print(values)
            runner = runner.next
        return values
    
    def min_to_front(self):
        if not self.head:
            print("This SLL is currently empty, try adding a node with add_front()")
            return self
        min = self.head.value
        runner = self.head
        # to find the min
        while runner:
            if (runner.value < min):
                min = runner.value
            print(min)
            runner = runner.next
        
        # to make min go to front, we need to skip it
        runner = self.head
        while runner.next:
            # in case the min is the head
            if (runner.value == min): 
                return self
            # if the min is last
            if (runner.next.value == min and runner.next.next == None):
                runner.next = None
                mySLL.addFront(min)
                return self
            # if the min is somewhere in the middle
            if (runner.next.value == min):
                if (runner.next.next):
                    runner.next = runner.next.next
                # runner.next = None Why not working?
            runner = runner.next

        mySLL.addFront(min)
        return self

mySLL = Sll()    
mySLL.addFront(7)
mySLL.addFront(11)
mySLL.addFront(13)
mySLL.addFront(12)
mySLL.addFront(10)
# print(mySLL.contains(17))
# print(mySLL.length())
print(mySLL.display_values())
mySLL.min_to_front()
print(mySLL.display_values())
