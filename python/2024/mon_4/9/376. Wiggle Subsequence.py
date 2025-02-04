from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        :param nums:
        :return:
        都是 last - pre
        method1:
            使用动态规划(正向的[也就是前面决定后面])思想实现
            rec_f: List[List[int]] = [item: List[int]]
            rec_f 的每一个 item[0] 表示包含当前 -1
                          item[1] 表示包含当前 1
            T(n): O(n**2) # 要想在 O(n) 的时间复杂度里面解出来，估计需要利用 0 <= nums[i] <= 1000
            S(n): O(n)
        method2: 回溯，时间复杂度很大
        """
        rec_f: List[List[int]] = [[1, 1] for _ in range(len(nums))]
        # 每次选中一个数字
        for i in range(1, len(nums)):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                if diff < 0:
                    rec_f[i][0] = max(rec_f[i][0], rec_f[j][1] + 1)
                elif diff > 0:
                    rec_f[i][1] = max(rec_f[i][1], rec_f[j][0] + 1)
        des_len = max(max(item[1] for item in rec_f), max(item[0] for item in rec_f))
        return des_len


if __name__ == "__main__":
    s = Solution()
    print(s.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))
