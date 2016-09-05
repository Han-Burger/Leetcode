class Solution(object):
    def minWindow(self, s, t):
        from collections import deque
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or len(s) < len(t): return ""
        
        #w_count counts the frequency of char in t
        w_count = {}
        for c in t:
            if c in w_count: w_count[c] += 1
            else: w_count[c] = 1
        print w_count
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
                
             