from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        O(t) = n
        :param nums:
        :return:
        """
        # 用来表示多余的数量
        dup_count = 0
        i = 0
        while i < len(nums) - dup_count:
            one_same_count = 1
            for j in range(i + 1, len(nums) - dup_count):
                if nums[j] == nums[i]:
                    one_same_count += 1
                else:
                    break
            if one_same_count == 1 or one_same_count == 2:
                i += one_same_count
            else:
                # 移位
                for k in range(i + one_same_count - 2, len(nums) - dup_count):
                    nums[k - (one_same_count - 2)] = nums[k]
                dup_count += (one_same_count - 2)
                i += 2
        print(nums)
        print(dup_count)
        return len(nums) - dup_count


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1, 1]))
