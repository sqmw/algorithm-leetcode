from typing import List


class Solution:
    bracketCountDic = {
        '(': 0,
        ')': 0
    }

    def generateParenthesis(self, n: int) -> List[str]:
        # 第一个只能是左括号
        brackets = ('(', ')')
        # 表示对应的位置选择的是'('还是')'
        select_arr = [0]
        for i in range(1, n * 2):
            select_arr.append(0)
        des_list = []
        # 枚举
        while True:
            bracket_str = '('
            self.bracketCountDic['('] = n - 1
            self.bracketCountDic[')'] = n
            for i in range(1, n * 2):
                added_bracket = brackets[select_arr[i]]
                # 这里表示的是 index == i 的括号的数量不够了或者，这里也是需要进位的->这种情况下行不通
                if self.bracketCountDic[added_bracket] < 1:
                    if select_arr[i] == 1:
                        self.carry(select_arr, i)
                    else:
                        select_arr[i] = 1
                    self.carry(select_arr, i)
                    break
                elif added_bracket == ')' and not can_add(bracket_str, ')'):
                    pass
                else:
                    self.bracketCountDic[added_bracket] -= 1
                bracket_str += added_bracket
                if i == 2 * n - 1:
                    if select_arr[i] == 1:
                        if can_add(bracket_str, ')'):
                            des_list.append(bracket_str)
                        if sum(select_arr) == len(select_arr) - 1:
                            return des_list
                        self.carry(select_arr, i)
                    else:
                        select_arr[i] = 1

    def carry(self, select_arr, selected):
        if selected > 0:
            if select_arr[selected - 1] == 0:
                select_arr[selected - 1] = 1
            else:
                select_arr[selected] = 0
                self.carry(select_arr, selected - 1)


# 加入右括号之后是否能找到一个左括号与之成为一对
def can_add(s: str, bracket: str) -> bool:
    left = 0
    right = 1  # 因为刚刚要加进来一个
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return True
    return False


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(2))
