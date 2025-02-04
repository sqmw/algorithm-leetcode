from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp: List[int] = []
        # 表示当前需要装入的位置
        index_arr_m = 0
        # 表示 arr1 存放在 arr2 的结束下标，是包含的，-1表示没有
        index_arr_n = 0
        while True:
            if index_arr_m == m:
                while index_arr_n < n:
                    temp.append(nums2[index_arr_n])
                    index_arr_n += 1
                break
            if index_arr_n == n:
                while index_arr_m < m:
                    temp.append(nums1[index_arr_m])
                    index_arr_m += 1
                break
            if nums1[index_arr_m] > nums2[index_arr_n]:
                temp.append(nums2[index_arr_n])
                index_arr_n += 1
            else:
                temp.append(nums1[index_arr_m])
                index_arr_m += 1
        nums1.clear()
        for item in temp:
            nums1.append(item)

if __name__ == '__main__':
    s = Solution()
    num1 = [1]
    num2 = []
    s.merge(num1, 1, num2, 0)
    print(num1)
