from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_freq = max(count.values())

        if max_freq > (len(s) + 1) // 2:
            return ""

        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        result = []
        prev_char = None
        prev_freq = 0

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            prev_char = char
            prev_freq = freq + 1

        return ''.join(result)


if __name__ == '__main__':
    testCases = {
        1: [10,15,20],
        2: [1,100,1,1,1,100,1,1,100,1]
    }

    for key in testCases:
        print(f"{Solution().minCostClimbingStairs(testCases[key])}")
