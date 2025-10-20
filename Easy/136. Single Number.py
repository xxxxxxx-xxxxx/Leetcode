# Sort of like the previous one

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        for x in nums:
            if count[x] == 1:
                return x
