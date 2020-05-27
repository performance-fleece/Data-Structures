"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = self
        while current:
            if current.value > value:
                if current.left is None:
                    current.left = BSTNode(value)
                    return
                current = current.left
            elif current.value <= value:
                if current.right is None:
                    current.right = BSTNode(value)
                    return
                current = current.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
       
        
        while current:
            if current.value == target:
                return True
            elif current.value > target:
                if current.left is None:
                    return False
                current = current.left
            elif current.value < target:
                if current.right is None:
                    return False
                current = current.right
                
                    




    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        max_value = self.value

        while current:
            if current.right is None:
                max_value = current.value
                return max_value
            current = current.right

        
        return max_value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# bst = BSTNode(5)

# bst.insert(5)
# bst.insert(2)
# bst.insert(6)
# print(bst.get_max())