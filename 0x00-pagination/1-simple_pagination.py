#!/usr/bin/env python3
"""
Simple Pagination
"""


import csv
import math


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


class Server:
    """Server class to paginate a database of
    popular baby names"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes our private variable
        """
        self.__dataset = None

    def dataset(self) -> list:
        """Cached dataset - opens the file and reads every row
        into our private class variable"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]

            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1,
                 page_size: int = 10) -> list:
        """ gets the required rows from the data set and
        returns them"""

        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        range = index_range(page, page_size)
        try:
            data = dataset[range[0]:range[1]]
        except IndexError:
            data = []
        return data
