class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        seenCharacters = {}
        sCounter = 0
        pCounter = 0

        while sCounter < len(s) and pCounter < len(p):
            seenCharacters[s[sCounter]] = '1'

            currCharS = s[sCounter]
            currCharP = p[pCounter]
            if s[sCounter] != p[pCounter]:
                if p[pCounter] == '*':
                    previousCharacter = p[pCounter-1]

                    if previousCharacter == '.':
                        pCounter +=1
                        sCounter += 1
                        continue

                    sCounterAdjusted = False
                    while sCounter < len(s):
                        if s[sCounter] != previousCharacter:
                            sCounter -= 1
                            sCounterAdjusted = True
                            break
                        else:
                            sCounter += 1

                    if not sCounterAdjusted:
                        sCounter -= 1

                elif p[pCounter] != '.':
                    if pCounter + 1 < len(p) and p[pCounter + 1] != '*':
                        return False

            pCounter += 1
            sCounter += 1

        return sCounter == len(s) and pCounter == len(p)

if __name__ == '__main__':
    testStrings = {
        1: ["aa", "a"],
        2: ["aa", "a*"],
        3: ["ab", ".*"],
        4: ["aab", "c*a*b"],
        5: ["mississippi", "mis*is*ip*."],
        6: ["mississippi", "mis*is*p*."]
    }
    key=4
    Solution().isMatch(testStrings[key][0], testStrings[key][1])

    for key in testStrings:
        if Solution().isMatch(testStrings[key][0], testStrings[key][1]):
            print(f"{testStrings[key][1]} is a regex match of {testStrings[key][0]}")
        else:
            print(f"{testStrings[key][1]} is not a regex match of {testStrings[key][0]}")