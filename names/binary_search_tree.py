class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if self.value == None:
        #     node = value
        #     self.value = node
        # else:
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)    
        if value >= self.value:
            if self.right:
                self.right.insert(value)     
            else:
                self.right = BinarySearchTree(value)           
               

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)             
        # if self.left:
        #     if self.value > target:
        #         return self.left.contains(target)
        #     else:
        #         return False    
        # if self.right:        
        #     if self.value <= target:
        #         return self.right.contains(target)
        #     else:
        #         return False     
            


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value
            

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
           self.right.for_each(cb)
        if self.left:
           self.left.for_each(cb)   