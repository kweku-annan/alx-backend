#!/usr/bin/env python3
"""A simple helper function that returns index range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Takes a page and page_size and returns a tuple of index range"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
