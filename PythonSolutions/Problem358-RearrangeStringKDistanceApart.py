from collections import Counter, deque
import heapq
class Solution:

    def rearrangeString(self, s: str, k: int) -> str:
        freq_count = Counter(s)
        q = deque([])
        ans = []

        max_heap = [(-freq, char) for char, freq in freq_count.items()]
        heapq.heapify(max_heap)

        while max_heap:
            fq, c = heapq.heappop(max_heap)
            fq = -fq

            ans.append(c)
            q.append((fq - 1, c))

            if len(q) == k:
                wait_fq, wait_c = q.popleft()

                if wait_fq > 0:
                    heapq.heappush(max_heap, (-wait_fq, wait_c))

        if len(ans) != len(s):
            return ""
        return "".join(ans)


if __name__ == '__main__':
    testCases = {
        1: [[8, 2, 13], 3],
        2: [[8, 2, 13], 0],
        3: [[100], 3],
        4: [[10, 10], 5],
        5: [[16, 16, 16], 4]
    }

    for key in testCases:
        print(Solution().getMinPrice(testCases[key][0], testCases[key][1]))