# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        if not intervals:
            return [newInterval]
        
        #find head index
        i, j = -1, len(intervals)
        while j - i > 1:
            mid = i + (j - i) / 2
            if intervals[mid].end < newInterval.start:
                i = mid
            else:
                j = mid
        startIdx = j
        
        #find tail index
        i, j = -1, len(intervals)
        while j - i > 1:
            mid = i + (j - i) / 2
            if intervals[mid].start <= newInterval.end:
                i = mid
            else:
                j = mid
        endIdx = i
        
        if startIdx == len(intervals):
            intervals.append(newInterval)
        elif endIdx == -1:
            intervals.insert(0, newInterval)
        elif startIdx > endIdx:
            intervals.insert(startIdx, newInterval)
        else:
            toAddInterval = Interval(min(intervals[startIdx].start, newInterval.start),
                                     max(intervals[endIdx].end, newInterval.end))
            for i in xrange(startIdx, endIdx + 1):
                intervals.pop(startIdx)
            intervals.insert(startIdx, toAddInterval)
        
        return intervals
            
        
        
        