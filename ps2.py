class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a
      
    ####### Part a #######
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size
    def select(self, ind):
        left_size = 0 if self.left is None else self.left.size
        if ind == left_size:
            return self
        elif ind < left_size:
            return None if self.left is None else self.left.select(ind)
        else:
            if self.right is None:
               return None
            return self.right.select(ind - left_size - 1)


     def insert(self, key):
        if self.key is None:
           self.key = key
           self.size = 1
        return self

    # increment size along the insertion path
        self.size += 1

        if key < self.key:
            if self.left is None:
               self.left = BinarySearchTree(self.debugger)
               self.left.key = key
            else:
               self.left.insert(key)
        elif key > self.key:
            if self.right is None:
               self.right = BinarySearchTree(self.debugger)
               self.right.key = key
            else:
               self.right.insert(key)

        return self 
       
      def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None

    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):

        # Pick which child we are rotating
        if child_side == "L":
           child = self.left
           if child is None:
              return self
        else:  # "R"
           child = self.right
           if child is None:
               return self

    # left rot
    if direction == "L":
        pivot = child.right
        if pivot is None:
            return self

        # rotation pointers
        child.right = pivot.left
        pivot.left = child

    # right rot
        else:  # direction == "R"
             pivot = child.left
             if pivot is None:
                return self

             # rotation pointers
             child.left = pivot.right
             pivot.right = child

        # Attach pivot back to self
        if child_side == "L":
           self.left = pivot
        else:
           self.right = pivot

    # fix sizes
        def recompute(node):
            if node is None:
               return 0
            node.size = 1
            if node.left:
               node.size += node.left.size
            if node.right:
               node.size += node.right.size
            return node.size

        recompute(child)
        recompute(pivot)
        recompute(self)

        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self

   


