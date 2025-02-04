"""
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
        考察数学几何思维
        T(n): O(1)
        S(n): O(1)
        """
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        have_coincide: bool = True
        # 使用 area1 作为参照物
        if ax2 <= bx1 or ax1 >= bx2 or \
                by1 >= ay2 or ay1 >= by2:
            have_coincide = False
        # 表示相离
        if have_coincide is False:
            return area1 + area2
        # 表示相交
        else:
            a = min(ax2, bx2) - max(ax1, bx1)
            b = min(ay2, by2) - max(ay1, by1)
            return area1 + area2 - a * b


if __name__ == "__main__":
    s = Solution()
    print(s.computeArea(ax1=0, ay1=0, ax2=1, ay2=1, bx1=0, by1=0, bx2=1, by2=2))
