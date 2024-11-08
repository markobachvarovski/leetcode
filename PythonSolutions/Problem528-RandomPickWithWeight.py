from bisect import bisect
from random import randint
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.cumulativeSum = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.cumulativeSum.append(curr_sum)

    def pickIndex(self) -> int:
        pick = randint(1, self.cumulativeSum[-1])

        index = bisect.bisect_left(self.cumulativeSum,pick)
        return index

