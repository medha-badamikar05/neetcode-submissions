"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        n = len(intervals)
    
        i = 1
        while i < n:
            if intervals[i].start < intervals[i-1].end:
                return False
            i += 1
        return True

