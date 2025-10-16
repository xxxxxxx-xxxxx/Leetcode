class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        x = [""] * n
        for i in range(n):
            j = indices[i]
            x[j] = s[i]
        return "".join(x)
