from typing import Any

class Empty(Exception):
    """Error attempting to access an element from an empty container.
    """
    pass

class LinkedStack: # TODO: fix this... LinkedStack is-a SinglyLinkedList
    """LIFO Stack implementation using a singly linked list as underlying storage
    by inheriting from SinglyLinkedList.
    """
    def __init__(self) -> None:
        pass # TODO: fix this
    
    def push(self, e: Any) -> None:
        pass # TODO: fix this

    def peek(self) -> Any:
        return None # TODO: fix this
    
    def pop(self) -> Any:
        return None # TODO: fix this
    