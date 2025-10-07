class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        y = x // 2        
        while y > x // y:
            y = (y+x // y) // 2
        return y

#Used the Netwon formula which is = (1/2) * (y+(x/y)) for simplicity
