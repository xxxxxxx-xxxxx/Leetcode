class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0                 # Wealth for the richest person(s)
        for money in accounts:          
            total = sum(money)     # Total of the current sum for a person
            if total > wealth:
                wealth = total
        return wealth              # Returm the wealth for the richest person(s)
