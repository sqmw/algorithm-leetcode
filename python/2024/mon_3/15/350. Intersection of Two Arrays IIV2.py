from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        method2: 这里的方法其实和第一个完全一样的，只是这里使用了 Python 的内置函数
        """
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)

        intersection = counts1 & counts2
        return list(intersection.elements())


if __name__ == "__main__":
    s = Solution()
    # 示例：
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(s.intersect(nums1, nums2))  # 输出应为 [2, 2]
