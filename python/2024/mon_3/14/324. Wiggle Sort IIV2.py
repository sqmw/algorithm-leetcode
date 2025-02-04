from random import randint, seed
from typing import List


class Helper:
    @staticmethod
    def quickSelect(arr: List, l: int, r: int, index: int) -> int:
        q = Helper.randomPartition(arr, l, r)
        if q == index:
            return arr[q]
        if q < index:
            return Helper.quickSelect(arr, q + 1, r, index)
        return Helper.quickSelect(arr, l, q - 1, index)

    @staticmethod
    def randomPartition(nums: List, l: int, r: int) -> int:
        i = randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return Helper.partition(nums, l, r)

    @staticmethod
    def partition(nums: List, l: int, r: int) -> int:
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        x = (n + 1) // 2
        seed(None)
        target = Helper.quickSelect(nums, 0, n - 1, x - 1)

        transAddress = lambda i: (2 * n - 2 * i - 1) % (n | 1)
        k, i, j = 0, 0, n - 1
        while k <= j:
            tk = transAddress(k)
            if nums[tk] > target:
                while j > k and nums[transAddress(j)] > target:
                    j -= 1
                tj = transAddress(j)
                nums[tk], nums[tj] = nums[tj], nums[tk]
                j -= 1
            if nums[tk] < target:
                ti = transAddress(i)
                nums[tk], nums[ti] = nums[ti], nums[tk]
                i += 1
            k += 1


if __name__ == "__main__":
    s = Solution()
    nums = [1, 5, 1, 1, 6, 4]
    s.wiggleSort(nums)
    print(nums)
