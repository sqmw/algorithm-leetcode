from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        有点类似动态规划的思想
        :param rowIndex:
        :return:
        """
        before_nums: List[int] = [1]
        now_nums: List[int] = [1]
        for _ in range(rowIndex):
            for j in range(len(before_nums)):
                if j > 0:
                    now_nums[j] = before_nums[j - 1] + before_nums[j]
                else:
                    now_nums[j] = before_nums[j]
            now_nums.append(before_nums[len(before_nums) - 1])
            before_nums = now_nums[:]
        return now_nums


if __name__ == "__main__":
    print(Solution().getRow(3))
