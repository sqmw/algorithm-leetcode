from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path_list: List[List[int]] = []
        path: List[int] = []

        path_index_arr: List[int] = []

        def traceback():
            if len(path) == len(nums):
                path_list.append(path[:])
            else:
                last_val = nums[0] - 1
                for i in range(len(nums)):
                    if i not in path_index_arr:
                        if nums[i] != last_val:
                            last_val = nums[i]
                        else:
                            continue
                        path_index_arr.append(i)
                        path.append(nums[i])
                        traceback()
                        path.pop()
                        path_index_arr.pop()

        traceback()
        return path_list


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 3, 4]))
