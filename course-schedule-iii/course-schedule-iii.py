from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        curr, pq = 0, []
        for duration, lastDay in courses:
            curr += duration
            heappush(pq, -duration)
            if curr > lastDay:
                curr -= -heappop(pq)
        return len(pq)