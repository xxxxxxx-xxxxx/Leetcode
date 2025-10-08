class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
        index_of = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in index_of:
                return [index_of[need], i]
            index_of[x] = i
        return []
