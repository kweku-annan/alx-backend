#!/usr/bin/env python3
"""Implements a pagination class"""
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """Takes a page and page_size and returns a tuple of index range"""
        start = (page - 1) * page_size
        end = start + page_size
        return start, end

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Paginates dataset and returns result"""
        assert (
            (type(page) is int and page > 0) and
            (type(page_size) is int and page_size > 0)
        )
        start, end = self.index_range(page, page_size)
        dataset = self.dataset()
        if start > len(dataset) or end > len(dataset):
            return []
        list_of_rows = dataset[start:end]
        return list_of_rows
