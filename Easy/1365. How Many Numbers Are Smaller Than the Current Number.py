# First solution

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x = []
        for a in nums:
            c = 0
            for b in nums:
                if b < a:
                    c += 1
            x.append(c)
        return x



# Second with faster processing

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        first_pos = {}
        for i, v in enumerate(sorted_nums):
            if v not in first_pos:
                first_pos[v] = i
        return [first_pos[a] for a in nums]



class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s_nums = sorted(nums)
        first_pos = {}
        for x, y in enumerate(s_nums):
            if y not in first_pos:
                first_pos[y] = x
        return [first_pos[a] for a in nums]
