"""
Node class to keep track of the data internal to individual nodes
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


"""
A tree class to keep track of things like the balance factor and the rebalancing logic
"""


class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """

    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print('-' * level * 2, pref, self.node.key,
                  f'[{self.height}:{self.balance}]',
                  'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are in the tree
    """

    def update_height(self):
        if self.node.left and self.node.right:
            self.height = max(self.node.left.update_height(),
                              self.node.right.update_height()) + 1
            return self.height
        elif self.node.left and not self.node.right:
            self.height = self.node.left.update_height() + 1
            return self.height
        elif self.node.right and not self.node.left:
            self.height = self.node.right.update_height() + 1
            return self.height
        else:
            self.height = 0
            return self.height

    """
    Updates the balance factor on the AVLTree class
    """

    def update_balance(self):
        if self.node.left and self.node.right:
            self.balance = self.node.left.update_height() - self.node.right.update_height()
            return self.balance
        elif self.node.left and not self.node.right:
            self.balance = self.node.left.update_height() + 1
            return self.balance
        elif self.node.right and not self.node.left:
            self.balance = -1 - self.node.right.update_height()
            return self.balance
        else:
            self.balance = 0
            return self.balance

    """
    Perform a left rotation, making the right child of this node the parent and making the old parent the left child of the new parent.
    """

    def left_rotate(self):
        if self.balance > 1:
            temp_node = Node(self.node.left.node.key)
            temp_node.left = self.node.left.node.left
            temp_node.right = self.node.left.node.right.node.left
            self.node.left = self.node.left.node.right
            self.node.left.node.left = AVLTree(temp_node)
            self.rebalance()
        else:
            temp_node = Node(self.node.key)
            temp_node.left = self.node.left
            temp_node.right = self.node.right.node.left
            self.node = self.node.right.node
            self.node.left = AVLTree(temp_node)
            self.rebalance()

    """
    Perform a right rotation, making the left child of this node the parent and making the old parent the right child of the new parent.
    """

    def right_rotate(self):
        if self.balance < -1:
            temp_node = Node(self.node.right.node.key)
            temp_node.left = self.node.right.node.left.node.right
            temp_node.right = self.node.right.node.right
            self.node.right = self.node.right.node.left
            self.node.right.node.right = AVLTree(temp_node)
            self.rebalance()
        else:
            temp_node = Node(self.node.key)
            temp_node.left = self.node.left.node.right
            temp_node.right = self.node.right
            self.node = self.node.left.node
            self.node.right = AVLTree(temp_node)
            self.rebalance()

    """
    Sets in motion the rebalancing logic to ensure the tree is balanced such that the balance factor is 1 or -1
    """

    def rebalance(self):
        self.update_height()
        self.update_balance()
        if self.balance > 1:
            if self.node.left.update_balance() == -1:
                self.left_rotate()
            else:
                self.right_rotate()
        elif self.balance < -1:
            if self.node.right.update_balance() == 1:
                self.right_rotate()
            else:
                self.left_rotate()

    """
    Uses the same insertion logic as a binary search tree. After the value is inserted, we need to check to see if we need to rebalance
    """

    def insert(self, key):
        if self.node == None:
            self.node = Node(key)
        elif key < self.node.key:
            if self.node.left == None:
                self.node.left = AVLTree(Node(key))
            else:
                self.node.left.insert(key)
        else:
            if self.node.right == None:
                self.node.right = AVLTree(Node(key))
            else:
                self.node.right.insert(key)
        self.rebalance()
