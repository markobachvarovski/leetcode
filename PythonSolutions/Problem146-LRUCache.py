# Definition for a Node.
from typing import Optional


class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.most_recent = ListNode(-1, -1)
        self.least_recent = ListNode(-1, -1)

        self.most_recent.next = self.least_recent
        self.least_recent.prev = self.most_recent

    def insert(self, node: ListNode):
        node.next = self.most_recent.next
        node.prev = self.most_recent

        self.most_recent.next.prev = node
        self.most_recent.next = node

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def evict(self, node: ListNode):
        self.remove(node)
        del self.cache[node.key]
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = ListNode(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            self.evict(self.least_recent.prev)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    testLists = {
        1: [ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2],
        2: [ListNode(0, ListNode(1, ListNode(2))), 4],
        3: [ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 123456],
    }

    for key in testLists:
        head = Solution().rotateRight(testLists[key][0], testLists[key][1])
        print(f"Key = {key}")
        while head is not None:
            print(head.val)
            head = head.next