from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        这个方法看起来更加简便，但是实际上和我的之前的思想是一样的
        T(n): O(n)
        S(n): O(1)
        """
        if len(nums) < 3:
            return False

        first_min = second_min = float('inf')

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([1, 2, 3, 4, 5, 6]))
