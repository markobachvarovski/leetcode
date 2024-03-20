class Solution:
    def convert(self, s: str, numRows: int) -> str:
        substringsByRow = {}
        iterateUpwards = False
        currentRow = 1
        finalString = ''

        for i in range(0, len(s)):
            if currentRow not in substringsByRow:
                substringsByRow[currentRow] = ''

            if currentRow == 1 or currentRow == numRows:
                iterateUpwards = not iterateUpwards

            substringsByRow[currentRow] += s[i]

            if iterateUpwards:
                currentRow += 1
            else:
                currentRow -= 1

        for key in substringsByRow:
            finalString += substringsByRow[key]

        return finalString

if __name__ == '__main__':
    testStrings = {
        1: ["PAYPALISHIRING", 3],
        2: ["PAYPALISHIRING", 4]
    }

    for key in testStrings:
        print(f"The zigzag conversion of {testStrings[key][0]} with {testStrings[key][1]} rows is: {Solution().convert(testStrings[key][0], testStrings[key][1])}")

