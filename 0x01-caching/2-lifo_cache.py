#!/usr/bin/env python3
"""
Module for a basic dictionary
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Caching using FIFO
    Methods: put
             get
    """

    def __init__(self):
        """
        Initialize BasicCache using parent class __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to our dict from cache_data
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if (len(self.cache_data) > super().MAX_ITEMS):
                popped = list(self.cache_data.keys())[super().MAX_ITEMS - 1]
                print("DISCARD: {}".format(popped))
                del self.cache_data[popped]

    def get(self, key):
        """
        Retrieves an item from our dict cache_data
        """
        if key is None or key not in self.cache_data.keys():
            pass
        else:
            return (self.cache_data[key])
