from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        T(n): O(n)
        S(n): O(1)
        使用 floyd 方法
        """
        # num[index] == index + 1
        slow = 0
        fast = 0
        while True:

            # if slow == nums[slow] # 这个判定不需要，显然，当第一个 index == 0
            # 就出现这个问题是不行的，然后就是在 非 index == 0 出现原地踏步，此时必然有一个值满足
            #                              num[j] == num[index_now] and index_now != j
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == "__main__":
    s = Solution()
    nums = [3, 1, 3, 4, 2]
    print(s.findDuplicate(nums))
