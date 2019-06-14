class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        if comparator:
            self.comparator = comparator
        else:
            self.comparator = lambda x, y: x >= y

    def insert(self, value):
        self.storage.insert(len(self.storage), value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        s = self.storage
        s[0], s[len(s) - 1] = s[len(s) - 1], s[0]
        max = s.pop(len(s) - 1)
        self._sift_down(0)
        return max

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        s, c, i, p = self.storage, self.comparator, index, (index - 1) // 2
        if p >= 0:
            if c(s[i], s[p]):
                s[i], s[p] = s[p], s[i]
                self._bubble_up(p)
            else:
                return
        else:
            return

    def _sift_down(self, index):
        s, c, i, l, r = self.storage, self.comparator, index, 2 * index + 1, 2 * index + 2
        if l > len(s) - 1:
            return
        elif r > len(s) - 1 or c(s[l], s[r]):
            if not c(s[i], s[l]):
                s[i], s[l] = s[l], s[i]
                self._sift_down(l)
            else:
                return
        else:
            if not c(s[i], s[r]):
                s[i], s[r] = s[r], s[i]
                self._sift_down(r)
            else:
                return
