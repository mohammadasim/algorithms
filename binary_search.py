"""
Module to implement functions that uses binary search
"""
from math import floor
from typing import Optional


def binary_search(search_list: list, search_item: int) -> Optional[int]:
    """Function to find the search_item in the search_list and
    return item location, if item not found return None"""
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = floor((low + high) / 2)
        guess = search_list[mid]
        if guess == search_item:
            return mid
        if guess > search_item:
            high = mid - 1
        else:
            low = mid + 1
    return None
