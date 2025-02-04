from typing import List


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        有点类似直接构造二叉树的题目，下面的解法是错误的
        """
        now_index: int = 0
        path: List[str] = []
        _max_len: int = 0
        _input_list: List[str] = []
        i = 0
        # 得到一个解析之后的 _input_list
        while i < len(input):
            if input[i] == '\n' or input[i] == '\t':
                _input_list.append(input[i])
                i += 1
            else:
                j = i + 1
                while j < len(input) and input[j] != '\n' and input[j] != '\t':
                    j += 1
                _input_list.append(input[i:j])
                i = j
        _last_index: int = -1

        def traceback(_start_index: int):
            """
            其实这里使用递归和栈都是可以实现的，毕竟递归就是通过栈实现的
            """
            nonlocal path, _input_list, _max_len, _last_index
            if _start_index >= len(_input_list):
                return
            # 表示是 \n 或者 tab
            if _input_list[_start_index] == '\n' or _input_list[_start_index] == '\t':
                j = _start_index + 1
                while j < len(_input_list) and (_input_list[j] == '\n' or _input_list[j] == '\t'):
                    j += 1
                traceback(j)

            # 表示是 . 文件(因为文件都是包含 . 这个符号的)
            elif '.' in _input_list[_start_index]:
                path.append(_input_list[_start_index])
                _max_len = max(_max_len, sum([len(item) for item in path]) + len(path) - 1)
                _last_index = max(_last_index, _start_index)
                return
            # 表示是文件夹
            # 这里是代码的核心
            else:
                _last_index = max(_last_index, _start_index)
                path.append(_input_list[_start_index])
                traceback(_start_index + 1)
                path.pop()

                while -1 < _last_index < len(_input_list):
                    traceback(_last_index + 1)

        traceback(0)
        return _max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthLongestPath(
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
