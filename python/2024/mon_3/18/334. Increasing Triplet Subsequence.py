import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        method1: greedy
        通过维护一个始终是当前最长目标数组 des_arr
        同时维护一个可能是最长的临时数组 temp_arr,
        并且在 temp_arr 比 des_arr 更加符合要求的时候，将 temp_arr 赋值给 des_arr
        如此迭代下去，如果能够出现 des_arr 的有效长度为 3 的时候，就  return True
        T(n): O(n)
        S(n): O(1)
        """
        # 保证 des_arr 和 temp_arr 都是递增的
        # 用来存储最终的结果
        des_arr: List[int] = [sys.maxsize] * 3
        now_des_len = 0
        temp_len = 0
        # 将出现的可能比 des_arr 更加适合的房子啊 temp_arr 里面
        # 在适当的时候将 des_arr, temp_arr 进行互换
        temp_arr: List[int] = [sys.maxsize] * 3
        for i in range(len(nums)):
            if now_des_len == 0:
                des_arr[now_des_len] = nums[i]
                now_des_len += 1
            elif now_des_len == 1:
                if nums[i] < des_arr[0]:
                    des_arr[0] = nums[i]
                elif nums[i] > des_arr[0]:
                    des_arr[1] = nums[i]
                    now_des_len += 1
            elif now_des_len == 2:
                if nums[i] > des_arr[1]:
                    print(des_arr)
                    return True
                elif des_arr[0] < nums[i] < des_arr[1]:
                    des_arr[1] = nums[i]
                else:
                    if temp_len == 0:
                        temp_arr[0] = nums[i]
                        temp_len += 1
                    if temp_len == 1:
                        if temp_arr[0] < nums[i]:
                            temp_arr[temp_len] = nums[i]
                            temp_len += 1
                            if temp_arr[1] < des_arr[1]:
                                temp_arr, des_arr = des_arr, temp_arr
                                temp_len = 0
                        elif temp_arr[0] > nums[i]:
                            temp_arr[0] = nums[i]
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([1, 5, 0, 4, 1, 3]))
