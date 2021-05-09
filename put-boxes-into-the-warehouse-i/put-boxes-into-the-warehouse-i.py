class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        tempHeight = float('inf')
        for i in range(len(warehouse)):
            tempHeight = min(warehouse[i], tempHeight)
            warehouse[i] = tempHeight

        count = 0
        for box in sorted(boxes):
            while warehouse:
                if box <= warehouse[-1]:
                    break
                warehouse.pop()
            if not warehouse:    
                break
            count += 1
            warehouse.pop()
            
        return count