from typing import List


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        使用栈实现
        每次的 separator 入栈之前都必须保证前面的分隔符都小于他，这点和表达式的计算十分相似
        T(n): O(n)
        S(n): O(n)
        """
        input = '\n' + input
        file_or_dir_path: List[str] = []
        # 用来存储分隔符
        separator_path: List[str] = []
        _max_len: int = 0
        _now_len: int = 0
        _input_list: List[str] = []
        i = 0
        # 得到一个解析之后的 _input_list
        while i < len(input):
            if input[i] == '\n' or input[i] == '\t':
                j = i + 1
                while j < len(input) and (input[j] == '\n' or input[j] == '\t'):
                    j += 1
                _input_list.append(input[i:j])
                i = j
            else:
                j = i + 1
                while j < len(input) and input[j] != '\n' and input[j] != '\t':
                    j += 1
                _input_list.append(input[i:j])
                i = j
        # 使用栈对解析出来的数据进行解析
        _last_index: int = -1
        i = 0
        while i < len(_input_list):
            # 表示是分隔符
            if '\n' in _input_list[i]:
                # 如果 分隔符有不小于(>=)现在这个的，则弹出
                if len(separator_path) > 0 and len(separator_path[-1]) >= len(_input_list[i]):
                    # 除了第一个 root，其他的任何一个都是 一个 分隔符一个文件夹或者文件
                    while len(separator_path) > 0 and len(separator_path[-1]) >= len(_input_list[i]):
                        _file_or_dir = file_or_dir_path.pop()
                        separator_path.pop()
                        _now_len -= len(_file_or_dir)
                        _now_len -= 1
                    separator_path.append(_input_list[i])
                else:
                    separator_path.append(_input_list[i])
            # 表示的是读取到的事 文件 或者 文件夹
            else:
                # 不能文件下面还是文件，可以使用这个方法<或者>在 input 的前面添加 '\n'
                # if len(file_or_dir_path) > 0 and '.' in file_or_dir_path[-1] and '.' in _input_list[i]:
                #     _file_or_dir = file_or_dir_path.pop()
                #     separator_path.pop()
                #     _now_len -= len(_file_or_dir)
                #     _now_len -= 1
                file_or_dir_path.append(_input_list[i])
                _now_len += (1 + len(_input_list[i]))
                # 表示是文件
                if '.' in _input_list[i]:
                    _max_len = max(_now_len, _max_len)
                    print(file_or_dir_path)
            i += 1

        return _max_len - 1 if _max_len > 0 else 0


if __name__ == "__main__":
    s = Solution()
    # 测试用例包含了这个，不讲武德 "file1.txt\nfile2.txt\nlongfile.txt"
    print(s.lengthLongestPath("\nfile1.txt\nfile2.txt\nlongfile.txt"))
