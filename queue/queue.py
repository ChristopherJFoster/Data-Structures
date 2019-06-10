class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
  
    def dequeue(self):
        if self.len() > 0:
            return self.storage.pop(0)
        else:
            return None

    def len(self):
        return len(self.storage)
