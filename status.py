from enum import Enum


class ItemStatus(Enum):
    CART = 0
    ORDER = 1
    PROCESSING = 2
    DELIVERED = 3
