class Solution:
    def myAtoi(self, s: str) -> int:
        finalIntegerAsString = ''
        signStrings = ['-', '+']
        hasSeenSign = False
        hasSeenFirstDigit = False
        for i in range(0, len(s)):
            if not hasSeenFirstDigit:
                if s[i].isdigit():
                    finalIntegerAsString += s[i]
                    hasSeenFirstDigit = True
                elif s[i] == '' or (s[i] in signStrings and not hasSeenSign):
                    finalIntegerAsString += s[i]
                    hasSeenSign = True
                elif s[i] == ' ' and not hasSeenSign:
                    continue
                else:
                    break
            else:
                if s[i].isdigit():
                    finalIntegerAsString += s[i]
                else:
                    break


        if finalIntegerAsString in signStrings or finalIntegerAsString == '':
            finalInteger = 0
        else:
            finalInteger = int(finalIntegerAsString)

        if finalInteger > 2**31 - 1:
            finalInteger = 2**31 - 1
        elif finalInteger < (-2)**31:
            finalInteger = (-2)**31

        return finalInteger

if __name__ == '__main__':
    testStrings = {
        1: "123",
        2: "0032",
        3: "  -42",
        4: "4193 with words",
        5: "words and 987",
        6: "3.14159",
        7: "+-12",
        8: "  +0 123",
        9: "  +  413"
    }

    for key in testStrings:
        print(f"The myAtoi output of {testStrings[key]} is: {Solution().myAtoi(testStrings[key])}")
