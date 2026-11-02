class Empty(Exception):
    """Error attempting to access an element from an empty container.
    """
    pass

class _Node:
    """Lightweight, nonpublic class for storing a singly linked node
    """
    def __init__(self, item: object, next: object = None):
        self._item = item
        self._next = next

class SinglyLinkedList:
    """
    """
    def __init__(self):
        self._head = None

    def __str__(self) -> str:
        return "" # TODO: fix this
    
    def __len__(self) -> int:
        return 0 # TODO: fix this
    
    def is_empty(self) -> bool:
        return True # TODO: fix this
    
    def clear(self) -> None:
        pass # TODO: finish this
    
    def add_to_front(self, new_item: object) -> None:
        pass # TODO: finish this

    def delete_at_front(self) -> object:
        return None # TODO: fix this

    def add_to_back(self, new_item: object) -> None:
        pass # TODO: finish this

    def delete_at_back(self) -> object:
        return None # TODO: fix this

    def delete(self, target_item: object) -> None:
        return None # TODO: fix this
    
    def search(self, item: object) -> bool:
        return False # TODO: fix this
    
    def get_item_at_index(self, index: int) -> object | None:
        return None # TODO: fix this

    def reverse(self) -> None:
        pass # TODO: finish this

    # BONUS: this method is for the BONUS task
    def insert_in_order(self, new_item: object) -> None:
        pass # TODO: fix this