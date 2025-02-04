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
            T(n): O(n**2)
            S(n): O(n)
        method2: 回溯，时间复杂度很大
        method3: 使用贪心思想，维护一个符合条件的当前最优 arr ，并且不断调整
                 其本质就是判断哟多少个起起落落，起之后必然是落，落下之后必然是起来(因此时间复杂度可以优化为 O(1))[其实就是数学里面的]
                 下面的解法就是使用贪心思想实现的
            T(n): O(n)
            S(n): O(n)
        """

        # 先增
        fix_arr = [nums[0]]
        next_tag = 1
        for i in range(1, len(nums)):
            diff = nums[i] - fix_arr[-1]
            if diff > 0:
                if next_tag == 1:
                    fix_arr.append(nums[i])
                    next_tag = -1
                # -1
                else:
                    # 替换为更加大的
                    fix_arr[-1] = nums[i]
            elif diff < 0:
                if next_tag == -1:
                    fix_arr.append(nums[i])
                    next_tag = 1
                # -1
                else:
                    # 替换为更加大的
                    fix_arr[-1] = nums[i]
        print(fix_arr)
        return len(fix_arr) + 1 if fix_arr[0] < nums[0] else len(fix_arr)


if __name__ == "__main__":
    s = Solution()
    print(s.wiggleMaxLength([0, 0, 0]))
