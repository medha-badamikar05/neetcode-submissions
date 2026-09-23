"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        n = len(intervals)
        minRooms = 0
        s,e = 0, 0
        count = 0
        while s < n:
            if start[s] < end[e]:
                count += 1
            else:
                e += 1
            minRooms = max(minRooms, count)
            s += 1
        return minRooms