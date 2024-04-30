from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path_list: List[List[int]] = []
        path: List[int] = []

        def traceback():
            if len(path) == len(nums):
                path_list.append(path[:])
            else:
                for i in nums:
                    if i not in path:
                        path.append(i)
                        traceback()
                        path.pop()

        traceback()
        return path_list


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3, 4]))
