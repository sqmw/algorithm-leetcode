from typing import Set, List


class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        method1:
            这里使用了原字符串反转的一般解，通过数据存储 vowel 的数组下标实现
        T(n): O(n)
        S(n): O(n)
        """
        vowel_set: Set = {'a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U', }
        index_list: List[int] = []
        s_list: List[str] = list(s)
        # 遍历得到 vowel 的下标
        for i in range(len(s_list)):
            if s_list[i] in vowel_set:
                index_list.append(i)
        left = 0
        right = len(index_list) - 1
        while left < right:
            s_list[index_list[left]], s_list[index_list[right]] = s_list[index_list[right]], s_list[index_list[left]]
            left += 1
            right -= 1
        return ''.join(s_list)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels('leetcode'))
