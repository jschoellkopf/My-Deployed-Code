class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Bst():
    def __init__(self):
        self.root = None

    def add(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return self
        monkey = self.root
        while monkey:
            if new_node.value >= monkey.value:
                if monkey.right != None:
                    monkey = monkey.right
                else:
                    monkey.right = new_node
                    return self
            else:
                if monkey.left != None:
                    monkey = monkey.left
                else:
                    monkey.left = new_node
                    return self
                
    def contains(self, val):
        exists_in_tree = False
        monkey = self.root
        while monkey:
            if monkey.value == val:
                exists_in_tree = True
                return exists_in_tree
            if val >= monkey.value:
                monkey = monkey.right
            else:
                monkey = monkey.left
        return exists_in_tree
    
    def min_val(self):
        if self.root == None:
            print("empty tree")
            return self
        monkey = self.root
        min = self.root.value
        while monkey.left:
            if monkey.left.value < min:
                min = monkey.left.value
            monkey = monkey.left
        return min
    
    def max_val(self):
        if self.root == None:
            print("empty tree")
            return self
        monkey = self.root
        max = self.root.value
        while monkey.right:
            if monkey.right.value > max:
                max = monkey.right.value
            monkey = monkey.right
        return max
    
    def get_size(self):
        if self.root == None:
            return "empty tree"
        def monkey_size(monkey):
            if monkey == None:
                return 0
            return 1 + monkey_size(monkey.left) + monkey_size(monkey.right)
        return monkey_size(self.root)
    
    def is_empty(self):
        if self.root == None:
            return True
        return False


my_bst = Bst()
my_bst.add(5)
# print(my_bst.root.value)
my_bst.add(17)
# print(my_bst.root.right.value)
my_bst.add(10)
# print(my_bst.root.right.left.value)
my_bst.add(12)
# print(my_bst.root.right.left.right.value)
my_bst.add(18)
# print(my_bst.root.right.right.value)
my_bst.add(14)
print(my_bst.contains(12))
print(my_bst.contains(5))
print(my_bst.contains(15))
print(my_bst.contains(20))
print(my_bst.contains(10))
print(my_bst.min_val())
print(my_bst.max_val())
print(my_bst.get_size())
print(my_bst.is_empty())