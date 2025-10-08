class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        y = x // 2        
        while y > x // y:
            y = (y+x // y) // 2
        return y

#Used the Netwon formula which is = (1/2) * (y+(x/y)) for simplicity


# A better solution with a faster runtime

from typing import List

class Solution:
    __slots__ = ()
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        y = 1 << ((x.bit_length() + 1) // 2)
        while y * y > x:
            y = (y + x // y) // 2
        return y

