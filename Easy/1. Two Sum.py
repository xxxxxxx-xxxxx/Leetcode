class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        index_of = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in index_of:
                return [index_of[need], i]
            index_of[x] = i
        return []


## A better solution with a faster runtime

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
