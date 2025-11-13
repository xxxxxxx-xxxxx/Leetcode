class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        n = columnNumber
        while n > 0:
            n, r = divmod(n - 1, 26)
            res.append(chr(ord('A') + r))
        return ''.join(reversed(res))
