from typing import List, Set

"""
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        middle_set: Set[str] = set()

        hash_set: Set[str] = set()
        for i in range(0, len(s) - 10 + 1):
            if s[i:i + 10] in hash_set:
                middle_set.add(s[i:i + 10])
            else:
                hash_set.add(s[i:i + 10])

        return list(middle_set)


if __name__ == "__main__":
    print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))
