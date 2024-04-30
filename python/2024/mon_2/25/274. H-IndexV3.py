from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        [3,0,6,1,5]
        T(n): O(n)
        S(n): O(n)
        """
        cite_count_arr: List[int] = [0] * (len(citations) + 1)
        for times in citations:
            cite_count_arr[min(len(citations), times)] += 1
        count = 0
        for i in range(len(citations), -1, -1):
            count += cite_count_arr[i]
            if count >= i:
                return i

        # 意思是上面的 else 没有执行，上面的每一个数字都通过了题目条件
        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([1, 3, 3, 1]))
