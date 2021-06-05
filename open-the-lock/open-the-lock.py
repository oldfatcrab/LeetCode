class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        changes = {
            '0': ['1', '9'],
            '1': ['2', '0'],
            '2': ['3', '1'],
            '3': ['4', '2'],
            '4': ['5', '3'],
            '5': ['6', '4'],
            '6': ['7', '5'],
            '7': ['8', '6'],
            '8': ['9', '7'],
            '9': ['0', '8'],
        }
        nexts = ['0000']
        records = {'0000': 0}
        for d in deadends:
            records[d] = 0
        while nexts:
            s = nexts.pop(0)
            for i in range(len(s)):
                for alt in changes[s[i]]:
                    t = s[:i] + alt + s[i + 1:]
                    if t not in records and t not in deadends:
                        records[t] = records[s] + 1
                        if t == target:
                            return records[t]
                        nexts.append(t)
        return -1