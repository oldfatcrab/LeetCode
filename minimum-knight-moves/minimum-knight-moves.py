class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0):
            return 0
        (x, y) = (abs(x), abs(y))
        DIRECTIONS = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        moves, nexts = {(0, 0): 0}, [(0, 0, 0) ]
        while nexts:
            cx, cy, d = nexts.pop(0)
            for dx, dy in DIRECTIONS:
                if (cx + dx, cy + dy) == (x, y):
                    return d + 1
                if cx + dx < -1 or cy + dy < -1:
                    continue
                if (cx + dx, cy + dy) in moves:
                    continue
                moves[(cx + dx, cy + dy)] = d + 1
                nexts.append((cx + dx, cy + dy, d + 1))
        return -1