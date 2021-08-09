class Node:
    def __init__(self, char=''):
        self.char = char
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node.count += 1
            node = node.children[char]
        
    def get_unique_prefix(self, word):
        prefix = ""
        node = self.root
        for char in word:
            if node.count == 1:
                return prefix
            prefix += char
            node = node.children[char]
        return prefix
    
    
def solve(words):
    trie = Trie()
    for word in words:
        trie.insert_word(word)
    return [trie.get_unique_prefix(word) for word in words]