class Solution:
    def isPalindrome(self, s: str) -> bool:
        x, y = 0, len(s) - 1
        while x < y:
            while x < y and not s[x].isalnum():
                x += 1
            while x < y and not s[y].isalnum():
                y -= 1
            if s[x].lower() != s[y].lower():
                return False
            x += 1
            y -= 1
        return True


# Can also do a cleaner way with
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]

# The "" means the a, b, c is abc, if it was "-" would be a-b-c etc
