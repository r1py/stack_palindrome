# -*- coding: utf-8 -*-
"""
pytest for stack_palindrome.py

requirements : pytest
usage : pytest -v
"""
import random
from copy import deepcopy

import numpy as np
from numpy.testing import assert_array_equal

from stack_palindrome import Stack, main, DTYPE


# Tools functions
# ---------------
def make_filled_stack(max_int=10):
    """Return a stack with random integers in stack_list"""
    stack = Stack()
    stack.stack_list = np.array(
        [random.randint(-999, 999) for i in range(random.randint(1, max_int))],
        dtype=DTYPE)
    return stack


def make_palindrome(max_int=10):
    """Return a Palindrome list of integers"""
    stack_list = [random.randint(-999, 999)
                  for i in range(random.randint(0, max_int/2))]
    stack_list = stack_list + random.choice(
        [[], [random.randint(-999, 999)]]) + stack_list[::-1]
    return np.array(stack_list, dtype=DTYPE)


def make_mixed_palindrome(max_int=10):
    """Return a Mixed Palindrome list of integers"""
    stack_list = make_palindrome(max_int)
    random.shuffle(stack_list)
    return np.array(stack_list, dtype=DTYPE)


# Tests functions
# ---------------
def test_init():
    """Test: Initialization of the Stack"""
    stack = Stack()
    assert_array_equal(stack.stack_list, np.array([]))


def test_push():
    """Test: Add an integer to the end of the stack"""
    stack = Stack()
    stack_before = deepcopy(stack)
    stack.push()
    assert_array_equal(stack_before.stack_list, stack.stack_list[:-1])


def test_pop_empty_stack():
    """Test:  Remove and return an integer from the stack
    with empty stack_list"""
    stack = Stack()
    stack_before = deepcopy(stack)
    poped = stack.pop()
    assert_array_equal(stack_before.stack_list,
                       stack.stack_list, np.array([], dtype=DTYPE))
    assert poped is None


def test_pop_filled_stack():
    """Test:  Remove and return an integer from the stack
    with filled stack_list"""
    stack = make_filled_stack()
    stack_before = deepcopy(stack)
    poped = stack.pop()
    assert_array_equal(stack_before.stack_list[:-1], stack.stack_list)
    assert isinstance(poped, np.int16)


def test_reverse():
    """Test: Reverse the order of self.stack_list"""
    for _ in range(10):
        stack = make_filled_stack()
        stack_list = stack.stack_list
        stack.reverse()
        assert_array_equal(stack_list,
                           np.array([x for x in reversed(stack.stack_list)],
                                    dtype=DTYPE)
                           )
        stack.reverse()
        assert_array_equal(stack_list, stack.stack_list)


def test_shake():
    """Test: Randomly mix the elements of the Stack (self.stack_list)"""
    stack = make_filled_stack(10**5)
    stack_before = deepcopy(stack)
    stack.shake()
    assert tuple(stack_before.stack_list) != tuple(stack.stack_list)
    assert len(tuple(stack_before.stack_list)) == len(tuple(stack.stack_list))
    assert sum(tuple(stack_before.stack_list)) == sum(tuple(stack.stack_list))


def test_is_palindrome():
    """Test: Returns True if the stack (content of self.stack_list)
    is a palindrome"""
    stack = Stack()
    assert stack.is_palindrome()
    stack.push(2)
    assert stack.is_palindrome()
    stack.push(3)
    assert not stack.is_palindrome()
    stack.push(2)
    assert stack.is_palindrome()
    for _ in range(10):
        stack.stack_list = make_palindrome()
        assert stack.is_palindrome()
        stack.push(32767)
        if len(stack.stack_list) > 1:
            assert not stack.is_palindrome()


def test_mixed_can_be_palindrome():
    """Test: returns True if the stack can be mixed to obtain a palindrome"""
    stack = Stack()
    for _ in range(10):
        stack.stack_list = make_mixed_palindrome()
        assert stack.mixed_can_be_palindrome()
        stack.push(32766)
        stack.push(32767)
        assert not stack.mixed_can_be_palindrome()


def test_multiple_occurence():
    """Test Multiple occurences of integers"""
    stack = Stack()
    stack.stack_list = np.array([3, 3, 3], dtype=DTYPE)
    assert stack.mixed_can_be_palindrome()


def test_main():
    """Test: stack_palindrome main function"""
    main()
