from typing import Dict


# letters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

class WordDictionary:
    def __init__(self):
        self.word_dict = dict()

    def addWord(self, word: str) -> None:
        now_dict = self.word_dict
        for i in range(len(word)):
            if word[i] not in now_dict:
                now_dict[word[i]] = dict()
            now_dict = now_dict[word[i]]
            if i == len(word) - 1:
                now_dict['#'] = None

    # 这里应该使用回溯法
    def search(self, word: str) -> bool:
        def depth_first_search(_now_dic: Dict, _i: int):
            nonlocal can_find
            if _i == len(word) and '#' in _now_dic:
                can_find = True
                return
            elif can_find is True or _i >= len(word):
                return
            # dot 使用深度优先遍历
            if word[_i] == '.':
                for letter in _now_dic.keys():
                    if letter != '#':
                        depth_first_search(_now_dic[letter], _i + 1)
            else:
                if word[_i] in _now_dic:
                    depth_first_search(_now_dic[word[_i]], _i + 1)

        can_find = False
        depth_first_search(self.word_dict, 0)
        return can_find


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("aad")
    print(wordDictionary.search(".ad"))
    print(wordDictionary.search("aad"))
    print(wordDictionary.search("..."))
