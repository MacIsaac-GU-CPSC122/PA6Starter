from linked_stack import LinkedStack
from copy import deepcopy

# for PA5 BONUS
class PostfixEvaluationError(Exception):
    """Error when evaluating postfix expression.
    """
    pass

def check_operator_on_stack_precedence(operator_on_stack: str, current_operator: str) -> bool:
    return False # TODO: copy your PA5 solution here

class Calculator:
    def __init__(self, symbol_table:dict = None) -> None:
        if symbol_table is None:
            symbol_table = {}
        self.symbol_table = symbol_table
        self.stack = LinkedStack()

    def set_symbol_table(self, new_symbol_table: dict) -> None:
        self.symbol_table = deepcopy(new_symbol_table)

    def convert_infix_to_postfix(self, infix: str) -> str:
        return "" # TODO: copy your PA5 solution here

    def evaluate_postfix(self, postfix: str) -> str:
        return "" # TODO: copy your PA5 solution here
