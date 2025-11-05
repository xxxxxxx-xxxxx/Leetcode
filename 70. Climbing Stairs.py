# Problem might look hard, I started with some weird loops
# However its actually simple, as it is the Fibonacci sequence
# That is 1.1.2.3.5.8 etc..

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
# To solve it first you make for the case if n = 1 or 2 above
        x = 1
        y = 2
# Here x and y is the inputs or the steps you can take
        for whatever in range(3, n + 1):
            z = x + y
            x = y
            y = z
        return y
# Lastly the 3, is because if the number is larger than 2 its then
# that you start counting, so the 3 is the start position
# You basically take what you got say to find out for 5
# You take the number from if it was 3 and 4 then sum together
