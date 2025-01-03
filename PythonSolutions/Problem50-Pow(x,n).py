from collections import defaultdict
from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_product = x

        while n > 0:
            if n % 2 == 1:
                result *= current_product
            current_product *= current_product
            n //= 2
        return result


if __name__ == '__main__':
    testCases = {
        1: [2.0, 10],
        2: [2.1, 3],
        3: [2.0, -2]
    }

    for key in testCases:
        print(Solution().myPow(testCases[key][0], testCases[key][1]))
