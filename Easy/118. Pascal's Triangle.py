# This one is interesting

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x = []      # Triangle
        y = []      # Previous
        for _ in range(numRows):
            if not y:
                n = [1]
            else:
                n = [1]
                for z in range(1, len(y)):
                    n.append( y[z-1] + y[z] )
                n.append(1)
            x.append(n)
            y = n
        return x

# Its better to visualise not a sa triangle such as this
# row 1: [1]
# row 2: [1, 1]
# row 3: [1, 2, 1]        (2 = 1+1)
# row 4: [1, 3, 3, 1]     (3 = 1+2, 3 = 2+1)
# row 5: [1, 4, 6, 4, 1]  (4 = 1+3, 6 = 3+3, 4 = 3+1)
