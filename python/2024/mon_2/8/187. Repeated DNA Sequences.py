from typing import List, Set

"""
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        des_str_list: List[str] = []
        temp_set: Set[str] = set()
        for i in range(0, len(s) - 10):
            if s.find(s[i:i + 10], i + 1) != -1:
                temp_set.add(s[i:i + 10])

        des_str_list = list(temp_set)
        return des_str_list


if __name__ == "__main__":
    print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
