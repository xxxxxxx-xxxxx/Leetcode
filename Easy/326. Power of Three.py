class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        # the while loop stops if not divisible by 3
        while n % 3 == 0:
            n //= 3
        return n == 1
