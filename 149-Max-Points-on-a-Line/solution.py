# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3: return len(points)
        max_count = 2
        for p in points:
            m = {}
            same_p = 0
            same_x = 0
            for q in points:
                if p != q:
                    if p.x == q.x and p.y == q.y: same_p += 1
                    elif p.x == q.x: same_x += 1
                    else:
                        slope = (float)(q.y - p.y) / (float)(q.x - p.x)
                        if slope in m: m[slope] += 1
                        else: m[slope] = 1
            curr_max = max(same_x, 0 if len(m) == 0 else max([m[k] for k in m])) + 1
            max_count = max(max_count, curr_max + same_p)
        return max_count
                        