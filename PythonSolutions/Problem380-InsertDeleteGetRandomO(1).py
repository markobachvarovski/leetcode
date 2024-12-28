from random import randint


class RandomizedSet:

    def __init__(self):
        self.cache = {}
        self.valueList = []

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False

        self.valueList.append(val)
        self.cache[val] = len(self.valueList) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False

        self.cache[self.valueList[-1]] = self.cache[val]
        self.valueList[-1], self.valueList[self.cache[val]] = self.valueList[self.cache[val]], self.valueList[-1]

        self.valueList.pop()
        del self.cache[val]

        return True

    def getRandom(self) -> int:
        return self.valueList[randint(0, len(self.valueList) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
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