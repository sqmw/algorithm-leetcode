from typing import List, Optional, Dict


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        大前提：一定有存在这两个数 并且是 有序的数组
        因为是两个数字，因此可以使用 hash_map 的 kv 实现
        题目说了答案唯一，那么两个数相加的时候等于 target 并且 两个相等此时数组里面只能是出现一次这个两个数
        :param numbers:
        :param target:
        :return:
        """
        num_dic: Dict[int, List[int]] = {}
        for i in range(len(numbers)):
            if numbers[i] in num_dic:
                num_dic[numbers[i]].append(i)
            else:
                num_dic[numbers[i]] = [i]
        for k, v in num_dic.items():
            if target - k in num_dic:
                if target != 2 * k:
                    return [num_dic[k][0] + 1, num_dic[target - k][0] + 1]
                else:
                    if len(num_dic[k]) > 1:
                        return [min(num_dic[k]) + 1, max(num_dic[k]) + 1]


if __name__ == '__main__':
    print(Solution().twoSum(
        [0, 0, 3, 4], 0))
