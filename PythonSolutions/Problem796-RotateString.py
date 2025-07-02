class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return s in goal * 2


if __name__ == '__main__':
    testCases = {
        1: ["defdefdefabcabc", "defdefabcabcdef"]
    }

    for key in testCases:
        print(Solution().rotateString(testCases[key][0], testCases[key][1]))
