class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initiate blocks
        blocks = []
        for i in range(n):
            blocks.append({i})
            
        # update blocks using edge
        for edge in edges:
            [start, end] = edge
            if blocks[start] is blocks[end]:
                continue
            if len(blocks[end]) > len(blocks[start]):
                start, end = end, start
            blocks[start].update(blocks[end])
            for i in blocks[end]:
                blocks[i] = blocks[start]
                
        # count different blocks and return
        count = 0
        for node in blocks:
            count += (len(node) > 0)
            node.clear()
        return count