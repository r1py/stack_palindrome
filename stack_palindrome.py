# -*- coding: utf-8 -*-

""" Integer Stack manager and palindrome checker in Python

"""
from __future__ import print_function
import random

import numpy as np


# DTYPE can be
#   - 'int16' (-32768 to 32767)
#   - 'int32' (-2 147 483 648 to 2 147 483 647)
DTYPE = 'int16'


class Stack:
    """Integer Stack manager and palindrome checker"""

    def __init__(self):
        """Initialize the Stack with an empty list"""
        self.stack_list = np.array([], dtype=DTYPE)

    def push(self, integer=None):
        """Add an integer to the end of the stack.

        Args:
            integer: int - optional argument,
                     if no given generates a random number between -999 and 999
        """
        if not integer:
            integer = random.randint(-999, 999)
        self.stack_list = np.append(self.stack_list,
                                    np.array(integer, dtype=DTYPE))

    def pop(self, index=-1):
        """Remove and return an integer from the stack at the index (default last)

        Args:
            index : int - optional argument, default -1

        Returns:
            int : if index is in list range
            None : if self.stack_list is empty, or index is out of range
        """
        if self.stack_list.size and self.stack_list.size >= abs(index):
            integer = self.stack_list[index]
            self.stack_list = np.delete(self.stack_list, index)
            return integer
        return None

    def print(self):
        """Display the contents of the stack (self.stack_list)"""
        print(self.stack_list)

    def reverse(self):
        """Reverse the order of self.stack_list"""
        self.stack_list = self.stack_list[::-1]

    def shake(self):
        """Randomly mix the elements of the Stack (self.stack_list)"""
        random.shuffle(self.stack_list)

    def is_palindrome(self):
        """Returns True if the stack (content of self.stack_list) is a palindrome

        Returns:
            True : if self.stack_list is a palindrome
            False : if self.stack_list is NOT a palindrome
        """
        return np.array_equal(self.stack_list, self.stack_list[::-1])

    def mixed_can_be_palindrome(self):
        """Returns True if the stack (content of self.stack_list) can be mixed
        to obtain a palindrome

        Returns:
            True : if self.stack_list can be mixed to obtain palindrome
            False : if self.stack_list can't be mixed to obtain palindrome
        """
        if self.stack_list.size <= 1:
            return True
        # If there is more than one Integer with odd counts,
        # it can't be a palindrome

        # _ countains uniques numbers and counts coutains the number
        # of their occurences
        _, counts = np.unique(self.stack_list, return_counts=True)
        # we just have to modulo 2 the values, and sum them
        # No more than one distinct value to obtain a palindrome
        return np.sum(counts % 2) <= 1


def main():
    """ Main function """
    stack = Stack()
    stack.push()
    stack.pop()
    stack.pop()
    stack.push(2)
    stack.push(2)
    stack.print()
    stack.reverse()
    stack.shake()
    if stack.is_palindrome():
        print('Palindrome')
    if stack.mixed_can_be_palindrome():
        print('Mixed can be a Palindrome')
    stack.pop()
    stack.print()
    stack.mixed_can_be_palindrome()


if __name__ == '__main__':
    main()
