#!/usr/bin/python3
""" 
MRUCache module that inherits from BaseCaching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A caching system using MRU - Most Recently Used
    Methods: put
             get
    """
    def __init__(self):
        """
        Initializes cache data
        """
        super().__init__()
        self.age = list(self.cache_data.keys())

    def put(self, key, item):
        """
        Add key value data to the cache_data
        """
        if key is None or item is None:
            pass

        self.cache_data[key] = item

        if len(self.cache_data) > super().MAX_ITEMS:
            popped = self.age[-1]
            print("Discard: {}".format(popped))
            del self.cache_data[popped]
            self.age.remove(popped)

        if key in self.frequency:
            self.age.remove(key)
            self.age.append(key)
        else:
            self.age.append(key)

    def get(self, key):
        """
        Retrieves key's value from cache_data
        """
        if key is None or key not in self.cache_data.keys():
            return None
        self.age.remove(key)
        self.age.append(key)
        return self.cache_data[key]
