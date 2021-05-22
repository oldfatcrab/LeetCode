class Solution:
    def isPattern(self, word: str, pattern: str) -> bool:
        if len(word) != len(pattern):
            return False
        patternDict, wordDict = {}, {}
        for i in range(len(word)):
            cond1, cond2 = word[i] in patternDict, pattern[i] in wordDict
            if cond1 != cond2:
                return False
            if not cond1:
                wordDict[pattern[i]], patternDict[word[i]] = word[i], pattern[i]
                continue
            if patternDict[word[i]] != pattern[i] or wordDict[pattern[i]] != word[i]:
                return False
        return True
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return list(filter(lambda w: self.isPattern(w, pattern), words))