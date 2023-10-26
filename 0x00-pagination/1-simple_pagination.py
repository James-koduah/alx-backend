#!/usr/bin/env python3
"""
ssssssssssssssssssssssssssssssssssssssssssssss
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return range of index to return"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get items for requested page"""
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        start_range, end_range = index_range(page, page_size)
        if self.__dataset is None:
            self.dataset()
        ans = []
        try:
            for i in range(start_range, end_range):
                ans.append(self.__dataset[i])
        except Exception as e:
            pass
        return ans
