class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        while True:
            if value < self.value:
                # print('less')
                if self.left == None:
                    self.left = BinarySearchTree(value)
                    break
                else:
                    return self.left.insert(value)
            else:
                # print('more')
                if self.right == None:
                    self.right = BinarySearchTree(value)
                    break
                else:
                    return self.right.insert(value)

    def contains(self, target):
        pass

    def get_max(self):
        pass

    def for_each(self, cb):
        pass
