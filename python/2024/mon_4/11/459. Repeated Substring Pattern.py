import collections
from typing import List, Dict


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        method1: 使用字来存储，充分必要条件，倒推，现在的这个用例有问题
            T(n): O(n)
            S(n): O(n)
        """
        char_index_arr_dic: Dict[str, List[int]] = collections.defaultdict(list)
        # T(n): O(n)
        for i in range(len(s)):
            char_index_arr_dic[s[i]].append(i)
        print(char_index_arr_dic)
        first_index_arr = char_index_arr_dic[s[0]]
        if len(first_index_arr) < 2:
            return False
        diff = first_index_arr[1] - first_index_arr[0]
        # O(n)
        for each_index_arr in char_index_arr_dic.values():
            if len(each_index_arr) != len(first_index_arr):
                return False
            for j in range(1, len(first_index_arr)):
                if each_index_arr[j] - each_index_arr[j - 1] != diff:
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    #  {'a': [0, 2, 3, 5, 7, 8], 'b': [1, 4, 6, 9]}
    # abaab
    print(s.repeatedSubstringPattern("abaab abaab"))
