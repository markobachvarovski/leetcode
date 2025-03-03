from typing import List
from collections import deque
class Solution:
    def compress(self, chars: List[str]) -> int:
        beginningSequenceIndex = 0
        writeIndex = 0

        while beginningSequenceIndex < len(chars):
            endSequenceIndex = beginningSequenceIndex

            while endSequenceIndex < len(chars) and chars[beginningSequenceIndex] == chars[endSequenceIndex]:
                endSequenceIndex += 1

            numDuplicates = endSequenceIndex - beginningSequenceIndex

            chars[writeIndex] = chars[beginningSequenceIndex]
            writeIndex += 1

            if numDuplicates > 1:
                for digit in str(numDuplicates):
                    chars[writeIndex] = digit
                    writeIndex += 1

            beginningSequenceIndex = endSequenceIndex

        return writeIndex




if __name__ == '__main__':
    testCases = {
        1: ["a","a","b","b","c","c","c"],
        2: ["a"],
        3: ["a", "b", "c", "c", "d", "d", "d", "e", "f"],
        4: ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    }

    for key in testCases:
        print(Solution().compress(testCases[key]))