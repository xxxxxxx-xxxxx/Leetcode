class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = set(nums2)      # number check
        y = []
        z = set()           # to keep the result unique (optional if you iterate set(nums1))
        for a in nums1:
            if a in x and a not in z:
                y.append(a)
                z.add(a)
        return y

  # Simpler method, requires pree info tho.
  class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
