class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        while True:
            if value < self.value:
                if self.left == None:
                    self.left = BinarySearchTree(value)
                    break
                else:
                    return self.left.insert(value)
            else:
                if self.right == None:
                    self.right = BinarySearchTree(value)
                    break
                else:
                    return self.right.insert(value)

    def contains(self, target):
        while True:
            if target == self.value:
                return True
            if target < self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
            if target > self.value:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
