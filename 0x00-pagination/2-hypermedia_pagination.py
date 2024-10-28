#!/usr/bin/env python3
"""Creates a server class"""
from typing import Tuple, List, Dict, Union
import csv


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

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Union[int, List[List], None]]:
        """Returns the Hypermedia metadate"""
        hypermedia_data = {}
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        next_page = page + 1
        prev_page = page - 1
        total_pages = ((len(dataset)) + (page_size - 1)) // page_size

        if next_page > len(dataset):
            next_page = None
        if prev_page < 1:
            prev_page = None

        hypermedia_data["page_size"] = page_size
        hypermedia_data["page"] = page
        hypermedia_data["data"] = data
        hypermedia_data["next_page"] = next_page
        hypermedia_data["prev_page"] = prev_page
        hypermedia_data["total_pages"] = total_pages

        return hypermedia_data
