from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_num = nums[0] - 1
        # len == valid_index + 1
        valid_index = -1
        for i in range(0, len(nums)):
            if nums[i] != last_num:
                if valid_index != i:
                    nums[valid_index + 1] = nums[i]
                last_num = nums[i]
                valid_index += 1
        return valid_index + 1


if __name__ == '__main__':
    s = Solution()
    a = [1, 1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 5, 5, 6]
    a = [1, 1, 1]
    b = set(a)
    print(s.removeDuplicates(a), a)
    print(b)
