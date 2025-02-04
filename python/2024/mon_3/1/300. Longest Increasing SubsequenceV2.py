from typing import List

"""
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the length of the longest strictly increasing subsequence
        method1: 回溯法
            估计要超时，因为时间复杂度大于 O(n**2)
        method2： 动态规划
            T(n): O(n**2)
            S(n): O(n)
        method3： 贪心 + 二分法
            T(n): << O(nlog(n))
            S(n): O(n)
            思路：维护一个数组 tails，其中 tails[k] 的值代表长度为 k+1 的所有递增子序列中尾部元素的最小值
                 遇到一个新的数字大于 tails[-1]就加进去，遇到一个更小的，就二分找到一个适合的位置替换掉

        """
        if not nums:
            return 0
        des_arr: List[int] = []
        for num in nums:
            # 直接加入
            if len(des_arr) == 0 or des_arr[-1] < num:
                des_arr.append(num)
            elif num == des_arr[-1]:
                continue
            # 插入，使用二分查找(类似夹逼准则)
            else:
                # [0,1,3] , target = 2
                left: int = 0
                right: int = len(des_arr) - 1
                while left <= right:
                    mid: int = (left + right) // 2
                    if des_arr[mid] == num:
                        # 因为下面有一个 des_arr[left]，因此要修正 left
                        left = mid
                        break
                    elif des_arr[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                des_arr[left] = num
        return len(des_arr)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))
