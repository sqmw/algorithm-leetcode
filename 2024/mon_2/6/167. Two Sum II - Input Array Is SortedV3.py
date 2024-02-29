from typing import List, Optional


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        大前提：一定有存在这两个数 并且是 有序的数组
        :param numbers:
        :param target:
        :return:
        """
        left: int = 0
        right: int = len(numbers) - 1
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] == target:
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

        return [left + 1, right + 1]


if __name__ == '__main__':
    print(Solution().twoSum(
        [3, 3, 5, 8, 18, 21, 22, 22, 22, 24, 26, 28, 29, 31, 31, 34, 37, 37, 40, 43, 43, 43, 44, 47, 48, 51, 51, 51, 52,
         54, 55, 56, 59, 59, 60, 74, 74, 76, 76, 81, 82, 82, 82, 85, 89, 91, 91, 94, ], 101))
