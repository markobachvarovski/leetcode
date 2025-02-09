from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        currWordIndex = 0

        while currWordIndex < len(words):
            currLine = []
            currLineLength = 0

            while (currWordIndex < len(words) and
                   currLineLength + len(words[currWordIndex]) + len(currLine) <= maxWidth):
                currLine.append(words[currWordIndex])
                currLineLength += len(words[currWordIndex])
                currWordIndex += 1

            if currWordIndex == len(words) or len(currLine) == 1:
                line = ' '.join(currLine)
                line += ' ' * (maxWidth - len(line))
                ans.append(line)
                continue

            totalSpaces = maxWidth - currLineLength
            gaps = len(currLine) - 1
            spacesPerGap = totalSpaces // gaps
            extraSpaces = totalSpaces % gaps

            line = ''
            for i in range(len(currLine) - 1):
                line += currLine[i]
                spaces = spacesPerGap + (1 if i < extraSpaces else 0)
                line += ' ' * spaces

            line += currLine[-1]
            ans.append(line)

        return ans


if __name__ == '__main__':
    testCases = {
        1: [["This", "is", "an", "example", "of", "text", "justification."], 16]
    }

    for key in testCases:
        print(f"{Solution().fullJustify(testCases[key][0], testCases[key][1])}")
