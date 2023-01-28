#!/usr/bin/python3
""" LRUCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching system using LRU - Least Recently Used.
    """
    def __init__(self):
        """Initializes cache data.
        """
        super().__init__()
        self.age = []

    def put(self, key, item):
        """Add key value data to the cache.
        """
        if key is None or item is None:
            pass

        self.cache_data[key] = item
        if key in self.age:
            self.age.remove(key)
            self.age.append(key)
        else:
            self.age.append(key)

        if len(self.cache_data) >= super().MAX_ITEMS:
            popped = self.age[0]
            print("Discard: {}".format(popped))
            del self.age[0]
            del self.cache_data[popped]

    def get(self, key):
        """ Retrieves key's value.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.age:
            self.age.remove(key)
            self.age.append(key)
        else:
            if len(self.age) >= super().MAX_ITEMS:
                del self.age[0]
            self.age.append(key)
        return self.cache_data[key]
