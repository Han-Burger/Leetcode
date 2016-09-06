class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return self.mapWith2Ptrs(s, t)
        
    def mapWith2Ptrs(self, s, t):
        if not t or len(s) < len(t): return ""
        
        w_count = {}
        for c in t:
            if c in w_count: w_count[c] += 1
            else: w_count[c] = 1
        
        head, tail, count = 0, 0, len(t)
        min_start, min_len = 0, len(s) + 1
        while tail < len(s):
            if s[tail] in w_count:
                if w_count[s[tail]] > 0:
                    count -= 1
                w_count[s[tail]] -= 1
            tail += 1
            while count == 0:
                l = tail - head
                if l < min_len:
                    min_start = head
                    min_len = l
                if s[head] in w_count:
                    w_count[s[head]] += 1
                    if w_count[s[head]] > 0:
                        count += 1
                head += 1
        return "" if min_len > len(s) else s[min_start: min_start + min_len]
        
    def mapWithQueue(self, s, t):
        from collections import deque
        
        if not t or len(s) < len(t): return ""
        
        #w_count counts the frequency of char in t
        w_count = {}
        for c in t:
            if c in w_count: w_count[c] += 1
            else: w_count[c] = 1
        m = {}
        min_str = s
        min_pos = -1
        
        for i in xrange(len(s)):
            c = s[i]
            if c in w_count:
                if w_count[c] == 1: w_count.pop(c)
                else: w_count[c] -= 1
                
                if c not in m: m[c] = deque()
                m[c].append(i)
                # first time we see all chars in t
                if len(w_count) == 0:
                    min_pos = min([m[k][0] for k in m])
                    min_str = s[min_pos: i + 1]
                    print min_str
            elif c in m:
                if w_count:
                    m[c].append(i)
                    m[c].popleft()
                else:  
                    m[c].append(i)
                    pos = m[c].popleft()
                    if pos == min_pos:
                        min_pos = min([m[k][0] for k in m])
                        if i - min_pos + 1 < len(min_str):
                            min_str = s[min_pos: i + 1]
        return "" if len(w_count) > 0 else min_str
                
             