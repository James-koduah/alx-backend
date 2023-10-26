#!/usr/bin/env python3
"""
find range of indexes to return for a search query
"""


def index_range(page, page_size):
    """return range of index to return"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
