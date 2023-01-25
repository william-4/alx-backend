#!/usr/bin/env python3
"""
Module for a basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):

  def __init__(self):
    """
        Initialize BasicCache using parent class __init__ method
        """
    super().__init__()
    self.counter = 0
    self.list = []

  def put(self, key, item):
    """
        Adds an item to our dict from cache_data
        """
    if key is None and item is None:
      pass
    else:
      self.counter++
      if (self.counter > self.MAX_ITEMS):
        index = self.counter % 4
        print("DISCARD: {}".format(self.list[index]))
        del self.cache_data[self.list[index]]
        self.list[index] = key
      else:
        self.list[self.counter] = key
        self.cache_data[key] = item

  def get(self, key):
    """
        Retrieves an item from our dict cache_data
        """
    if key is None or key not in self.cache_data.keys():
      pass
    else:
      return (self.cache_data[key])
