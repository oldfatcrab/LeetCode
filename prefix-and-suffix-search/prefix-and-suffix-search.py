class TrieNode:
    def __init__(self):
        self.nexts = {}
        self.index = -1
        
    def addWord(self, word, index):
        if not word:
            self.index = max(self.index, index)
            return
        letter = word[0]
        if letter not in self.nexts.keys():
            self.nexts[letter] = TrieNode()
        self.nexts[letter].addWord(word[1:], index)
        
    # helper to fetch all indices as a set
    def traverseNode(self) -> Set[int]:
        result = {self.index}
        for letter, nextNode in self.nexts.items():
            nextResult = nextNode.traverseNode()
            result.update(nextResult)
        return result
        
    # find all indices with prefix
    def findPrefix(self, word) -> Set[int]:
        if not word:
            return self.traverseNode()
        letter = word[0]
        if letter not in self.nexts.keys():
            return {-1}
        return self.nexts[letter].findPrefix(word[1:])
        
class WordFilter:
    def __init__(self, words: List[str]):
        # create two tries, one straight order, one reverse order
        self.root = TrieNode()
        self.reversedRoot = TrieNode()
        for i, word in enumerate(words):
            self.root.addWord(word, i)
            self.reversedRoot.addWord(word[::-1], i)
        
    def f(self, prefix: str, suffix: str) -> int:
        # search prefix and suffix in two tries
        result = self.root.findPrefix(prefix)
        reversedResult = self.reversedRoot.findPrefix(suffix[::-1])
        
        # find common one (with both prefix and suffix) and return max
        return max(result.intersection(reversedResult))
