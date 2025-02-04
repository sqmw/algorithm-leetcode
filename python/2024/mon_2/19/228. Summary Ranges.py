from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        T(n): O(n)
        S(n): O(n)
        """
        des_str_list: List[str] = []
        i = 0
        while i < len(nums):
            # j 是没有包含的
            j = i + 1
            while j < len(nums) and nums[j] == nums[j - 1] + 1:
                j += 1
            if j == i + 1:
                des_str_list.append(str(nums[i]))
            else:
                des_str_list.append(f'{nums[i]}->{nums[j - 1]}')

            i = j

        return des_str_list


if __name__ == "__main__":
    s = Solution()
    nums = [0, 2, 3, 4, 6, 8, 9]
    print(s.summaryRanges(nums))
