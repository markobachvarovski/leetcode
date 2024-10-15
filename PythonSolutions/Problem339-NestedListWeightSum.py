from typing import List

class NestedInteger:
    def __init__(self, value=None):
        """If value is not specified, initializes an empty list. Otherwise initializes a single integer."""
        if value is None:
            self._list = []
            self._integer = None
        elif isinstance(value, int):
            self._list = None
            self._integer = value
        else:
            raise TypeError("Invalid type for value")

    def isInteger(self) -> bool:
        """Return True if this NestedInteger holds a single integer, otherwise False."""
        return self._integer is not None

    def getInteger(self) -> int:
        """Return the single integer that this NestedInteger holds, if it holds a single integer.
        Return None if this NestedInteger holds a nested list."""
        return self._integer

    def getList(self) -> ['NestedInteger']:
        """Return the nested list that this NestedInteger holds, if it holds a nested list.
        Return None if this NestedInteger holds a single integer."""
        return self._list

    def setInteger(self, value: int):
        """Set this NestedInteger to hold a single integer."""
        self._integer = value
        self._list = None

    def add(self, ni: 'NestedInteger'):
        """Add a NestedInteger to this NestedInteger, treating it as a list."""
        if self._list is None:
            self._list = []
        self._list.append(ni)

    def __repr__(self):
        if self.isInteger():
            return str(self._integer)
        else:
            return str(self._list)

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def helper(lst, depth):
            sum = 0
            for i in lst:
                if i.isInteger():
                    sum += i.getInteger() * depth
                else:
                    sum += helper(i.getList(), depth + 1)
            return sum

        return helper(nestedList, 1)


if __name__ == '__main__':
    ni1 = NestedInteger()
    ni1.add(NestedInteger(1))
    ni1.add(NestedInteger(1))

    ni2 = NestedInteger(2)

    ni3 = NestedInteger()
    ni3.add(NestedInteger(1))
    ni3.add(NestedInteger(1))

    ni4 = NestedInteger(1)

    ni5 = NestedInteger()
    ni5.add(NestedInteger(4))

    ni6 = NestedInteger()
    ni6.add(NestedInteger(6))

    ni5.add(ni6)

    testCases = {
        1: [ni1, ni2, ni3],
        2: [ni4, ni5],
    }

    for key in testCases:
        print(Solution().depthSum(testCases[key]))