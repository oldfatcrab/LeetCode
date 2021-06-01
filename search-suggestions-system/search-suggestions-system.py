class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        for i in range(1, len(searchWord) + 1):
            target = searchWord[:i]
            products = sorted(list(filter(lambda x: x[:i] == target, products)))
            result.append(products[:3])
        return result