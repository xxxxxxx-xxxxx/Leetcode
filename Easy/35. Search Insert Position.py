class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            m_val = nums[m]
            if m_val == target:
                return m
            elif m_val < target:
                l = m + 1
            else:
                r = m - 1
        return l
