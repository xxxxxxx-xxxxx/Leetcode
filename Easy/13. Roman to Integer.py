class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
    
        t = 0
        p = 0

        for c in reversed (s):
            v = r[c]

        # choose either +/-
            if v < p:
                t -= v
            else:
                t += v
            p = v

        return t   
