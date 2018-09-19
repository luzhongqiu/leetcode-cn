from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        value = self.cache[key]
        self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache.keys()) == self.capacity:
                self.cache.popitem(last=False)

            self.cache[key] = value