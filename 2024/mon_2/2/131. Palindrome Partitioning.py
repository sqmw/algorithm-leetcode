from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        des_str_list: List[List[str]] = []
        def is_palindrome(start_index, end_index):
            """
            [start, end)
            :param start_index:
            :param end_index:
            :return:
            """
            for i in range(start_index, int((end_index - start_index - 1) / 2) + 1):
                if s[i] != s[end_index - 1 - i]:
                    return False
            return True
        return des_str_list
