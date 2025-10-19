class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for nums in x:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            if counts[ch] > 1:
                return True
            else:
                return False

# Could do it easier using a better loop

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupe_List = set()
        for n in nums:
            if n in dupe_List:
                return True
            dupe_List.add(n)
        return False  
