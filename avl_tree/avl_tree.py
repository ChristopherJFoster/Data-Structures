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
        if self.node.left:
            if self.node.right:
                self.balance = self.node.left.height - self.node.right.height
            else:
                self.balance = self.node.left.height + 1
        elif self.node.right:
            self.balance = -1 - self.node.right.height
        else:
            self.balance = 0

    """
    Perform a left rotation, making the right child of this node the parent and making the old parent the left child of the new parent.
    """

    def left_rotate(self):
        if self.node.right == None:
            temp = self.node.left
            self.node.left = self.node.left.node.right
            self.node.left.node.left = temp
        else:
            temp_node = Node(self.node.key)
            temp_node.left = self.node.left
            temp_node.right = self.node.right
            if self.node.right.node.left:
                temp_node.right = self.node.right.node.left
            self.node = self.node.right.node
            self.node.left = AVLTree(temp_node)
        # self.rebalance()

    """
    Perform a right rotation, making the left child of this node the parent and making the old parent the right child of the new parent.
    """

    def right_rotate(self):
        if self.node.left == None:
            temp = self.node.right
            self.node.right = self.node.right.node.left
            self.node.right.node.right = temp
        else:
            temp_node = Node(self.node.key)
            temp_node.left = self.node.left
            temp_node.right = self.node.right
            if self.node.left.node.right:
                temp_node.left = self.node.left.node.right
            self.node = self.node.left.node
            self.node.right = AVLTree(temp_node)
        # self.rebalance()

    """
    Sets in motion the rebalancing logic to ensure the tree is balanced such that the balance factor is 1 or -1
    """

    def rebalance(self):
        self.update_height()
        self.update_balance()
        if self.balance > 1:
            if self.node.left.node.left == None:
                self.left_rotate()
            else:
                self.right_rotate()
        elif self.balance < -1:
            if self.node.right.node.right == None:
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


# test = AVLTree()
# print('-')
# test.insert(0)
# print('0')
# test.insert(1)
# print('1')
# test.insert(2)
# print('2')
# test.insert(3)
# test.insert(4)
# test.insert(5)
# test.insert(6)

# print(test.display())
