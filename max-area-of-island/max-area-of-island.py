class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        m, n, visited, result = len(grid), len(grid[0]), set([]), 0
        for i in range(m):
            for j in range(n):
                if (i, j) in visited or grid[i][j] == 0:
                    continue
                visited.add((i, j))
                nexts, count = [(i, j)], 0
                while nexts:
                    (px, py), count = nexts.pop(), count + 1
                    for dx, dy in DIRECTIONS:
                        x, y = px + dx, py + dy
                        if not (0 <= x <= m - 1 and 0 <= y <= n - 1):
                            continue
                        if ((x, y) not in visited) and (grid[x][y] == 1):
                            nexts.append((x, y))
                            visited.add((x, y))
                result = max(result, count)
        return result