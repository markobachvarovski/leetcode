class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        lettersTotal = len(ransomNote)

        for letter in ransomNote:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

        for letter in magazine:
            if letter not in letters or letters[letter] == 0:
                continue
            else:
                letters[letter] -= 1
                lettersTotal -= 1

        return lettersTotal <= 0


if __name__ == '__main__':
    testStrings = {
        1: ["a", "b"],
        2: ["aa", "ab"],
        3: ["aa", "aab"],
        4: ["bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"]
    }

    for key in testStrings:
        if Solution().canConstruct(testStrings[key][0], testStrings[key][1]):
            print(f"{testStrings[key][0]} can be constructed from the letters in {testStrings[key][1]}")
        else:
            print(f"{testStrings[key][0]} can not be constructed from the letters in {testStrings[key][1]}")