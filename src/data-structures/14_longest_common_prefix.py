"""
Author: Harshul Raina
Problem: Longest Common Prefix
Leet Code: 14-Longest Common Prefix
Topic: Strings / Arrays
Difficulty: Easy
"""


def longest_common_prefix(strs: list[str]) -> str:
    """
    Return the longest prefix shared by all strings.

    Args:
        strs: A list of strings.

    Returns:
        The longest common prefix, or an empty string if none exists.
    """
    first_string = strs[0]

    for index, character in enumerate(first_string):
        for string in strs[1:]:
            if index >= len(string) or string[index] != character:
                return first_string[:index]

    return first_string


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]

    print(longest_common_prefix(strs))
