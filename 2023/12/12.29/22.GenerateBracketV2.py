from typing import List, Union


class Solution:
    # 加入右括号之后是否能找到一个左括号与之成为一对
    brackets = ('(', ')')
    brackets_count_dic = {
        '(': 0,
        ')': 0
    }

    def can_add(self, _s: str) -> bool:
        left = 0
        right = 1  # 因为刚刚要加进来一个
        for i in range(len(_s) - 1, -1, -1):
            if _s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                return True
        return False

    def generateParenthesis(self, n: int) -> List[str]:
        des_str_list = []
        select_arr = [0 for _ in range(2 * n)]
        bracket = self.getParenthesis(select_arr)
        while bracket is not None:
            if bracket != '':
                des_str_list.append(bracket)
            bracket = self.getParenthesis(select_arr)
        return des_str_list

    # 如果返回的是 None 表示已经没有了，就是结束
    def getParenthesis(self, select_arr) -> Union[None, str]:
        if sum(select_arr) == len(select_arr):
            return None
        # 使用 des_str_is_false 标记的部分可以进行优化，但是需要修改递归函数 carry
        des_str_is_false = False
        self.brackets_count_dic['('] = self.brackets_count_dic[')'] = int(len(select_arr) / 2)
        s = ''
        # 取出str
        for i in range(0, len(select_arr)):
            bracket = self.brackets[select_arr[i]]
            if self.brackets_count_dic[bracket] < 1:
                des_str_is_false = True
            else:
                self.brackets_count_dic[bracket] -= 1
            if bracket == ')':
                if not self.can_add(s):
                    des_str_is_false = True
            s += bracket
            # 取完之后需要进位
            if i == len(select_arr) - 1:
                self.carry(select_arr, i)
        # 执行进位
        if des_str_is_false:
            return ''
        else:
            return s

    def carry(self, select_arr, selected):
        if select_arr[selected] == 0:
            select_arr[selected] = 1
        # 需要递归进位
        else:
            select_arr[selected] = 0
            self.carry(select_arr, selected - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
