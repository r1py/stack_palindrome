# -*- coding: utf-8 -*-
"""
pytest for stack_palindrome.py

requirements : pytest
usage : pytest -v
"""
import random
from copy import deepcopy

from stack_palindrome import Stack


# Tools functions
# ---------------
def make_filled_stack(max_int=10):
    """Return a stack with random integers in stack_list"""
    stack = Stack()
    stack.stack_list = [random.randint(-999, 999)
                        for i in range(random.randint(1, max_int))]
    return stack


def make_palindrome(max_int=10):
    """Return a Palindrome list of integers"""
    stack_list = [random.randint(-999, 999)
                  for i in range(random.randint(0, max_int/2))]
    stack_list = stack_list + random.choice(
        [[], [random.randint(-999, 999)]]) + stack_list[::-1]
    return stack_list


def make_mixed_palindrome(max_int=10):
    """Return a Mixed Palindrome list of integers"""
    stack_list = make_palindrome(max_int)
    random.shuffle(stack_list)
    return stack_list


# Tests functions
# ---------------
def test_init():
    """Test: Initialization of the Stack"""
    stack = Stack()
    assert stack.stack_list == []


def test_push():
    """Test: Add an integer to the end of the stack"""
    stack = Stack()
    stack_before = deepcopy(stack)
    stack.push()
    assert stack_before.stack_list == stack.stack_list[:-1]
    assert isinstance(stack.stack_list[-1], int)


def test_pop_empty_stack():
    """Test:  Remove and return an integer from the stack
    with empty stack_list"""
    stack = Stack()
    stack_before = deepcopy(stack)
    poped = stack.pop()
    assert stack_before.stack_list == stack.stack_list == []
    assert poped is None


def test_pop_filled_stack():
    """Test:  Remove and return an integer from the stack
    with filled stack_list"""
    stack = make_filled_stack()
    stack_before = deepcopy(stack)
    poped = stack.pop()
    assert stack_before.stack_list[:-1] == stack.stack_list
    assert isinstance(poped, int)


def test_reversed():
    """Test: Return the stack_list reversed"""
    for _ in range(10):
        stack = make_filled_stack()
        assert [x for x in reversed(stack.stack_list)] == stack._reversed()


def test_reverse():
    """Test: Reverse the order of self.stack_list"""
    for _ in range(10):
        stack = make_filled_stack()
        stack_list = stack.stack_list
        stack.reverse()
        stack.reverse()
        assert stack_list == stack.stack_list


def test_shake():
    """Test: Randomly mix the elements of the Stack (self.stack_list)"""
    stack = make_filled_stack(10**5)
    stack_before = deepcopy(stack)
    stack.shake()
    assert stack_before.stack_list != stack.stack_list
    assert len(stack_before.stack_list) == len(stack.stack_list)
    assert sum(stack_before.stack_list) == sum(stack.stack_list)


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
        stack.push(10**6)
        if len(stack.stack_list) > 1:
            assert not stack.is_palindrome()


def test_mixed_can_be_palindrome():
    """Test: returns True if the stack can be mixed to obtain a palindrome"""
    stack = Stack()
    for _ in range(10):
        stack.stack_list = make_mixed_palindrome()
        assert stack.mixed_can_be_palindrome()
        stack.push(10**6)
        stack.push(10**6 + 1)
        if len(stack.stack_list) > 1:
            assert not stack.mixed_can_be_palindrome()
