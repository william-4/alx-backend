#!/usr/bin/env python3
"""
Module for a basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Simple caching that adds and returns an item from our dict
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
