class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A power of two must be positive
        if n <= 0:
            return False
            
        # Real code for when its doable
        return (n & (n - 1)) == 0
