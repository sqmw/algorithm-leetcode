from typing import List

"""
1 <= nums.length <= 105
0 <= nums[i] <= 109
"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        下面使用了桶排序，同类使用Python自带的排序，核心就是
        :param nums:
        :return:
        """

        def bucket_sort(_nums):
            # 设置桶的数量
            bucket_cou = max(10, int(len(_nums) / 10))
            buckets: List[List[int]] = [[] for _ in range(bucket_cou)]
            M = max(_nums) + 1
            for item in _nums:
                num_in_bucket_index = (item * bucket_cou) // M
                buckets[num_in_bucket_index].append(item)
            index = 0
            for bucket in buckets:
                bucket.sort()
                for item in bucket:
                    _nums[index] = item
                    index += 1

        if len(nums) < 2:
            return 0

        bucket_sort(nums)
        min_gap = nums[1] - nums[0]
        for i in range(2, len(nums)):
            min_gap = max(min_gap, nums[i] - nums[i - 1])
        return min_gap


if __name__ == "__main__":
    num_arr = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
    print(Solution().maximumGap(num_arr))
