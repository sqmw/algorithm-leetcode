class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        greedy: 这里的做法是取长度为 len(num) - k  的数字，但是按照体育约束，去除数字比保留数字效果好
        :return:
        """

        smallest = min(list(num))

        if len(num) <= k:
            return '0'
        res_list = ['9'] * (len(num) - k)
        res_index = 0

        num_index = 0
        while res_index < len(res_list):
            if num[num_index] == smallest:
                res_index += 1
                num_index += 1
                continue

            res_list[res_index] = num[num_index]
            next_smaller_index = self.findFirstSmallerIndex(num, num[num_index], num_index + 1)
            # 找到下一个不大的数字的时候长度不够或者刚刚好
            if next_smaller_index == -1 or (len(num) - next_smaller_index <= len(num) - k - res_index - 1):
                # 此时 res 定了一个 digit
                res_index += 1
                num_index += 1
                continue
            else:
                res_list[res_index] = num[next_smaller_index]
                num_index = next_smaller_index
        res_str = ''.join(res_list).lstrip('0')
        return res_str if res_str else '0'

    def findFirstSmallerIndex(self, num: str, val: str, start: int) -> int:
        """
        return -1: error
        """
        for i in range(start, len(num)):
            if num[i] < val:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits(num="112", k=1))
