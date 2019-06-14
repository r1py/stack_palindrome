# -*- coding: utf-8 -*-

""" Integer Stack manager and palindrome checker in Python

"""
from __future__ import print_function
import random


class Stack:
    """Integer Stack manager and palindrome checker"""

    def __init__(self):
        """Initialize the Stack with an empty list"""
        self.stack_list = []

    def push(self, integer=None):
        """Add an integer to the end of the stack.

        Args:
            integer: int - optional argument,
                     if no given generates a random number between -999 and 999
        """
        if not integer:
            integer = random.randint(-999, 999)
        self.stack_list.append(integer)

    def pop(self, index=-1):
        """Remove and return an integer from the stack at the index (default last)

        Args:
            index : int - optional argument, default -1

        Returns:
            int : if index is in list range
            None : if self.stack_list is empty, or index is out of range
        """
        if self.stack_list and len(self.stack_list) >= abs(index):
            return self.stack_list.pop(index)
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
        for i in range(len(self.stack_list) // 2):
            if self.stack_list[i] != self.stack_list[-i - 1]:
                return False
        return True

    def mixed_can_be_palindrome(self):
        """Returns True if the stack (content of self.stack_list) can be mixed
        to obtain a palindrome

        Returns:
            True : if self.stack_list can be mixed to obtain palindrome
            False : if self.stack_list can't be mixed to obtain palindrome
        """
        if len(self.stack_list) <= 1:
            return True
        # If there is more than one Integer with odd counts,
        # it can't be a palindrome

        # Put odd values elements in a list
        odd_values = [x for x in self.stack_list
                      if self.stack_list.count(x) % 2]

        # No more than one distinct value to obtain a palindrome
        return len(set(odd_values)) <= 1


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
