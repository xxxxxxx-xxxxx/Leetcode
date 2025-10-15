class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


# Could do
class Solution:
    def reverseString(self, s: List[str]) -> None:
      s.reverse()


# Possible to do this as well, nothing much to run int faster tbh
class Solution:
    def reverseString(self, s: List[str]) -> None:
      s[:] = s[::-1]
