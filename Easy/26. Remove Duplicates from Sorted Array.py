class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return "n.a."      # In case nothings there
        x = 1                  # Running count in the list of numbers
        for n in range(1, len(nums)):
            if nums[n] != nums[x - 1]:
                nums[x] = nums[n]
                x += 1
        return x
