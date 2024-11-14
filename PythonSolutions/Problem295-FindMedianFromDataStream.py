from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.lower = [] # max heap to store numbers less than median
        self.upper = [] # min heap to store numbers more than median

    def addNum(self, num: int) -> None:
        heappush(self.lower, -num)

        # If the lower heap has a larger max than the upper heap's min, insert it into the upper heap
        if self.lower and self.upper and -self.lower[0] > self.upper[0]:
            heappush(self.upper, -heappop(self.lower))

        # Balance sizes
        if len(self.lower) > len(self.upper) + 1:
            heappush(self.upper, -heappop(self.lower))
        if len(self.upper) > len(self.lower):
            heappush(self.lower, -heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2