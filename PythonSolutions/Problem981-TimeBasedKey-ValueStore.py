from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        for i in range(len(self.cache[key]) - 1, -1, -1):
            val, timestamp_prev = self.cache[key][i]

            if timestamp_prev <= timestamp:
                return val

        return ""


if __name__ == '__main__':
    timemap = TimeMap()
    print(timemap.set("foo", "bar", 1))
    print(timemap.get("foo", 1))
    print(timemap.get("foo", 3))
    print(timemap.set("foo", "bar2", 4))
    print(timemap.get("foo", 4))
    print(timemap.get("foo", 5))
