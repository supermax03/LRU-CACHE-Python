class LRUCache:

    def __init__(self, maxcapacity):
        import collections
        self.items = collections.OrderedDict()
        self.maxcapacity = maxcapacity

    def put(self, key, value):
        if len(self.items.keys()) == self.maxcapacity:
            del self.items[self.items.keys()[0]]
        self.items[key] = value

    def get(self, key):
        try:
            value = None
            if (cmp(self.items.keys()[0], key) == 0):
                value = self.items[key]
                del self.items[key]
                self.items[key] = value
            value = self.items[key]
        finally:
            return value


