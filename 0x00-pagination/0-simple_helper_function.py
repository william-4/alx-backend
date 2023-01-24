#!/usr/bin/env python3
"""
Module defining a helper function to be used
in pagination
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    returns a tuple of size 2 containing a start index 
    and an end index corresponding to the range of 
    indexes to return in a list for those particular paramters
    """
    end_index = page*page_size
    start_index = end_index - page_size
    range = (start_index, end_index)

    return (range)
