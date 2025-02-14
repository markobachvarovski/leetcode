from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonzero[i] = num

    def dotProduct(self, vec) -> int:
        result = 0

        if len(self.nonzero) > len(vec.nonzero):
            self.nonzero, vec.nonzero = vec.nonzero, self.nonzero

        for i, val in self.nonzero.items():
            if i in vec.nonzero:
                result += val * vec.nonzero[i]
        return result
