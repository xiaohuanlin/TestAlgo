# File: solution
# Problem: Insert Delete GetRandom O(1)
# Status: Wrong Answer
# Language: python3
# Submit Time: 2025-07-01 20:31:33
# Runtime: N/A
# Memory: N/A

from random import randint

class RandomizedSet:

    def __init__(self):
        self.l = []
        self.m = {}
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        if self.size < len(self.l):
            self.l[self.size] = val
        else:
            self.l.append(val)
        self.m[val] = len(self.m)
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        idx = self.m[val]
        last_val = self.l[self.size - 1]

        del self.m[val]
        self.m[last_val] = idx
        self.l[idx], self.l[self.size-1] = self.l[self.size-1], self.l[idx]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        i = randint(0, len(self.m) - 1)
        return self.l[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()