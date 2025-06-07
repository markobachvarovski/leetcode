
class Solution:
    def robotWithString(self, s: str) -> str:
        # Precompute the minimum character from each index to the end
        n = len(s)
        min_suffix = [''] * n
        min_suffix[n - 1] = s[n - 1]

        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        t = []  # stack
        result = []
        i = 0

        while i < n or t:
            # Pop from stack if it's empty OR current char in s OR
            # top of stack <= min remaining in s
            while t and (i >= n or t[-1] <= min_suffix[i]):
                result.append(t.pop())

            # If we still have characters in s, move to stack
            if i < n:
                t.append(s[i])
                i += 1

        return ''.join(result)


if __name__ == '__main__':
    testCases = {
        1: "zza",
        2: "bac",
        3: "bdda",
        4: "bydizfve"
    }

    for key in testCases:
        print(Solution().robotWithString(testCases[key]))
