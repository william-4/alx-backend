#!/usr/bin/env python3
"""
Module for a basic dictionary
"""
'''from base_caching import BaseCaching'''


class BaseCaching():
    """
    BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """
        Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data[key]))

    def put(self, key, item):
        """
        Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your \
        cache class")

    def get(self, key):
        """
        Get an item by key
        """
        raise NotImplementedError("get must be implemented in your \
        cache class")

        
class BasicCache(BaseCaching):

    def __init__(self):
        """
        Initialize BasicCache using parent class __init__ method
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to our dict from cache_data
        """
        if key is None and item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from our dict cache_data
        """
        if key is None or key not in self.cache_data.keys():
            pass
        else:
            return (self.cache_data[key])
