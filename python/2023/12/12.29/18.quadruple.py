from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        _nums = []
        same_count = 0
        current_same = nums[0]
        for i in nums:
            if i == current_same:
                if same_count >= 4:
                    continue
                else:
                    _nums.append(i)
                    same_count += 1
            # 表示来了一个新的数字
            else:
                _nums.append(i)
                current_same = i
                same_count = 1
        nums = _nums
        if len(nums) < 4 or (target > 4 * nums[len(nums) - 1] > 0) or (target < 4 * nums[0] < 0):
            return []
        des_list = []
        select_arr = [0, 1, 2, 3]
        while True:
            sum_list = [0] * 4
            select = 0  # 表示当前选中的是下标为 select 的数字
            # 取前三个数
            for i in range(0, 3):
                sum_list[i] = nums[select_arr[select]]
                select = (select + 1) % len(nums)
            # 取第三个数
            for i in range(select_arr[2] + 1, len(nums)):
                sum_list[3] = nums[i]
                if sum(sum_list) == target:
                    des_list.append(sum_list[:])
                if i == len(nums) - 1:
                    select_arr[3] = len(nums) - 1
                    self.carry(select_arr, 3, nums)
                    if select_arr[2] == i - 1 and select_arr[1] == i - 2 and select_arr[0] == i - 3:
                        sum_list = [nums[select_arr[0]], nums[select_arr[1]], nums[select_arr[2]],
                                    nums[select_arr[3]]]
                        if sum(sum_list) == target:
                            des_list.append(sum_list)
                        return [list(item) for item in set(tuple(row) for row in des_list)]

    def carry(self, select_arr, select, nums):
        if select > 0:
            if select_arr[select - 1] < select_arr[select] - 1:
                select_arr[select - 1] += 1
                for i in range(select, len(select_arr)):
                    select_arr[i] = select_arr[i - 1] + 1
            elif select_arr[select - 1] == select_arr[select] - 1:
                self.carry(select_arr, select - 1, nums)


if __name__ == '__main__':
    s = Solution()
    arr = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
    print(s.fourSum(arr, 200))
    print(len(arr), len(set(arr)))
