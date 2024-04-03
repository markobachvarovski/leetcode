class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArray = path.split('/')
        finalPath = ""
        popCounter = 0

        while len(pathArray) > 0:
            word = pathArray.pop()

            if word == "." or word == "":
                continue
            elif word == "..":
                popCounter += 1
            else:
                if popCounter > 0:
                    popCounter -= 1
                else:
                    finalPath = word + "/" + finalPath

        return "/" + finalPath[:-1]

if __name__ == '__main__':
    testPaths = {
        1: "/home/",
        2: "/../",
        3: "/home//foo/",
        4: "/a/./b/../../c/",
        5: "/a//b////c/d//././/.."
    }

    for key in testPaths:
        print(f"The canonical path of {testPaths[key]} is: {Solution().simplifyPath(testPaths[key])}")