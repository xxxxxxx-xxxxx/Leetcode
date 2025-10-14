# First clear

class Solution:
    def defangIPaddr(self, address: str) -> str:
        out = []
        for ch in address:
            out.append("[.]" if ch == "." else ch)
        return "".join(out)


# Second, only asked for one so the for loop was unnessecary

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
