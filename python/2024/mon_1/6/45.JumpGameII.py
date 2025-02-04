from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = []
        now_index = 0
        if len(nums) == 1:
            return 0
        else:
            fit_index = 0
            while now_index + nums[now_index] < len(nums) - 1:
                max_for = -1
                # 每次筛选出一条最适合的路
                for i in range(1, nums[now_index] + 1):
                    if max_for < i + nums[now_index + i]:
                        max_for = i + nums[now_index + i]
                        fit_index = now_index + i
                now_index = fit_index
                steps.append(now_index)
        return len(steps) + 1


if __name__ == '__main__':
    s = Solution()
    print(s.jump(
        [2, 1, 9, 5, 9, 7, 6, 4, 8, 3, 2, 2, 2, 1, 9, 1, 7, 9, 7, 0, 7, 5, 8, 2, 1, 3, 2, 4, 1, 9, 5, 4, 0, 6, 1, 1]))
