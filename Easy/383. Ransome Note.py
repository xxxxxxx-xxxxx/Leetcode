class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      x = {}

      for ch in magazine:
        x[ch] = x.get(ch, 0) + 1

      for ch in ransomNote:
        if x.get(ch, 0) == 0:
          return False
        x[ch] -= 1
      return True


# Could do a better which I havent seen done nor knew at the time of the function "all" or a import function

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = Counter(ransomNote)
        have = Counter(magazine)
        return all(have[c] >= need[c] for c in need)
