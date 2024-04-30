class Trie:

    def __init__(self):
        # 使用树形结构的字典进行存储
        self.trie = dict()

    def insert(self, word: str) -> None:
        trie_dic = self.trie
        for i in range(len(word)):
            if word[i] not in trie_dic:
                trie_dic[word[i]] = dict()
            trie_dic = trie_dic[word[i]]
            if i == len(word) - 1:
                trie_dic['#'] = None

    def search(self, word: str) -> bool:
        trie_dic = self.trie
        for i in range(len(word)):
            if word[i] in trie_dic:
                trie_dic = trie_dic[word[i]]
            else:
                return False
            if i == len(word) - 1:
                if '#' in trie_dic:
                    return True
                else:
                    return False

    def startsWith(self, prefix: str) -> bool:
        trie_dic = self.trie
        for letter in prefix:
            if letter in trie_dic:
                trie_dic = trie_dic[letter]
            else:
                return False
        return True


if __name__ == "__main__":
    trie = Trie()

    res = []
    res.append(trie.insert("hello"))
    res.append(trie.search("helloa"))  # return True
    res.append(trie.search("app"))  # return False
    res.append(trie.startsWith("app"))  # return True
    res.append(trie.insert("app"))  #
    res.append(trie.search("app"))  # return True
    print(res)
