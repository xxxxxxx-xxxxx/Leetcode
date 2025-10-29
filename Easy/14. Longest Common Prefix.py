class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""         # If the str is empty just return ""
        x = strs[0]
        for w in strs[1:]:
            while not w.startswith(x):
                x = x[:-1]    # The -1 removes the last character so like flower -> flowe -> flow -> flo etc..
                if not x:
                    return ""
        return x
