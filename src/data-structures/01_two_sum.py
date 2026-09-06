"""
Author: Harshul Raina
Problem: Two Sum
Leet Code: 01-Two Sum
Topic: Arrays / Hash Map
Difficulty: Easy

This module contains an O(n) average-time solution to the Two Sum
problem using a hash map.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Return the indices of two numbers whose sum equals target.

    Args:
        nums: A list of integers.
        target: The required sum of two elements.

    Returns:
        A list containing the indices of the two matching numbers.

    Raises:
        ValueError: If no valid pair exists.
    """
    seen: dict[int, int] = {}

    for index, number in enumerate(nums):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    raise ValueError("No valid solution exists.")


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum(nums, target))
