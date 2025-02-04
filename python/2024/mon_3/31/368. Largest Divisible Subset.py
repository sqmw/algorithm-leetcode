from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        method_1(本来想回溯的，但是时间复杂度好像是阶乘级别的):
            先排序，然后使用动态规划
        T(n): O(n**2)
        S(n): O(n**2)
        """
        nums.sort()
        row_max_len = 0
        # matrix[i] 表示的是 看到直到 index == 1 的时候包含 nums[i] 的最长的符合题目要求的 sub_nums
        matrix: List[List[int]] = []
        # 每次选择一个数字
        for i in range(len(nums)):
            # 每次都遍历之前处理好的 nums
            now_max_row = []
            for j in range(i):
                if nums[i] % matrix[j][-1] == 0:
                    if len(now_max_row) < len(matrix[j]):
                        now_max_row = matrix[j]
            in_row = now_max_row.copy()
            in_row.append(nums[i])
            matrix.append(in_row)
            row_max_len = max(row_max_len, len(in_row))
        for row in matrix:
            if len(row) == row_max_len:
                return row
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.largestDivisibleSubset([1, 2, 4, 8]))
