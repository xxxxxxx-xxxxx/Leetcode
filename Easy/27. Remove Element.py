class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        keep = []
        for x in nums:
            if x != val:
                keep.append(x)

        k = len(keep)
        nums[:k] = keep
        return k
