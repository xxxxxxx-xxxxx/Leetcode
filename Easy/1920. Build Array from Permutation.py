class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        x = len(nums)
        y = []
        for z in range(x):
            v = nums[nums[z]]
            y.append(v)
        return y
