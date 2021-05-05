class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.word = True  # 완성된 문자열임을 표시한다.

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # 문자가 node.children 내부에 없으면 False 값을 반환한다.
            if char not in node.children:
                return False
            node = node.children[char]

        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        # 주어진 prefix 부분에 대해서만 search()를 수행한다.
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
