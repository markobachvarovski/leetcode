from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Solution 1
        letterLogs = []
        digitLogs = []

        for log in logs:
            spaceIdx = log.index(" ")
            if log[spaceIdx + 1].isdigit():
                digitLogs.append(log)
            else:
                identifier = log[0:spaceIdx]
                content = log[spaceIdx + 1:]
                letterLogs.append((content,identifier))

        letterLogs = sorted(letterLogs)

        ans = []
        for log in letterLogs:
            ans.append(log[1] + " " + log[0])
        ans.extend(digitLogs)

        return ans

        # Solution 2
        # def sorting_key(log):
        #     spaceIdx = log.index(" ")
        #     identifier, content = log[:spaceIdx], log[spaceIdx + 1:]
        #     return (0, content, identifier) if content[0].isalpha() else (1,)
        #
        # return sorted(logs, key=sorting_key)

if __name__ == '__main__':
    testCases = {
        1: ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
        2: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    }

    for key in testCases:
        print(Solution().reorderLogFiles(testCases[key]))
