class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        前置条件 len(s1) + len(s2) = len(s3)
        这里使用的是动态规划
            - 时间复杂度 O(n^2)
            - 空间复杂度 O(n^2)
                - 通过有效的利用，可以将空间复杂度减少到 O(n)
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        if len(s1) + len(s2) < len(s3):
            return False
        if s1 == '' or s2 == '':
            if(s1 + s2).find(s3) != -1:
                if len(s1) + len(s2) == len(s3):
                    return True
                else:
                    return False
        # f[x][y]: 表示取出 s1[:x + 1] s2[:y + 1]
        f = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        f[0][0] = True
        # 表示取出 s3
        for i in range(1, len(s3) + 1):
            # 表示取出 s1
            for j in range(max(0, i - len(s2)), len(s1) + 1):
                # 上 左
                if i - j > -1:
                    if (j - 1 > -1) and f[j - 1][i - j] is True and s1[j - 1] == s3[i - 1]:
                        f[j][i - j] = True
                    elif (i - j > -1) and f[j][i - j - 1] is True and s2[i - j - 1] == s3[i - 1]:
                        f[j][i - j] = True

        return f[len(s1)][len(s2)]


if __name__ == '__main__':
    s = Solution()
    s1 = "bbaabacacbabcbaa"
    s2 = "abccccbaccaca"
    s3 = "bbccccababaaccacaccbaababcbaa"
    print(s.isInterleave(s1, s2, s3))
