class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words, l, result = [(set(word), len(word)) for word in words], len(words), 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not words[i][0].intersection(words[j][0]):
                    result = max(result, words[i][1] * words[j][1])
        return result