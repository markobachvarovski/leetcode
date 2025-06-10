import heapq

class Solution:
    def clearStars(self, s: str) -> str:

        heap = []
        result = [''] * len(s)  # Pre-allocate result array

        for i, char in enumerate(s):
            if char == '*':
                if heap:
                    _, neg_idx = heapq.heappop(heap)
                    actual_idx = -neg_idx
                    result[actual_idx] = ''  # Mark for removal
            else:
                heapq.heappush(heap, (char, -i))
                result[i] = char

        return ''.join(char for char in result if char)

if __name__ == '__main__':
    testCases = {
        1: "aaba*",
        2: 'abc',
        3: "abc*def*ghi**",
        4: "abc*aef*ahi**"
    }

    for key in testCases:
        print(Solution().clearStars(testCases[key]))
