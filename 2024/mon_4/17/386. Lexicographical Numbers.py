from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        method1: 生成之后排序
            T(n): O(nlog(n))
            S(n): O(n)
        """
        nums = list(range(1, n + 1))
        nums.sort(key=lambda num: str(num))
        return nums


if __name__ == "__main__":
    s = Solution()
    print(','.join(map(str, s.lexicalOrder(40))))
