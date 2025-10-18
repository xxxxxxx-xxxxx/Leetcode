class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for l in s:
            letters[l] = letters.get(l, 0) + 1

        for l in t:
            if l not in letters:
                return False
            letters[l] -= 1
            if letters[l] < 0:
                return False

        for total in letters.values():
            if total != 0:
                return False
        return True



# Shortening the last step can be done as
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for l in s:
            letters[l] = letters.get(l, 0) + 1

        for l in t:
            if l not in letters:
                return False
            letters[l] -= 1
            if letters[l] < 0:
                return False

        return all(v == 0 for v in letters.values())
