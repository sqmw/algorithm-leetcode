from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        动态规划的思想，这里直接给出了递推关系
        :param numRows:
        :return:
        """
        if numRows == 0:
            return []
        # 表示的是第一行
        before_nums: List[int] = [1]
        now_nums: List[int] = [1]
        des_nums_arr: List[List[int]] = [now_nums[:]]
        for i in range(2, numRows + 1):
            for j in range(len(before_nums)):
                # 先把最后一个加上去
                if j > 0:
                    now_nums[j] = before_nums[j - 1] + before_nums[j]
                else:
                    now_nums[j] = before_nums[j]
            now_nums.append(before_nums[len(before_nums) - 1])
            before_nums = now_nums[:]
            des_nums_arr.append(now_nums[:])
        return des_nums_arr


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
