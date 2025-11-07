class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1          # last real element in nums1
        j = n - 1          # last element in nums2
        k = m + n - 1      # last position in nums1

# Actually use while loops here instead of for loop as to say simple we dont know for sure how many loops to do
        # nr.1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # nr.2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
