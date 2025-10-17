class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = {}                    #create a list of the letters to look up in
        for l in s:
            if l in n:
                n[l] += 1
            else:
                n[l] = 1
        for x in range(len(s)):
            l = s[x]
            if n[l] == 1:
                return x
        return -1
