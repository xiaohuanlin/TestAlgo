# File: solution
# Problem: Insert Delete GetRandom O(1)
# Status: Wrong Answer
# Language: python3
# Submit Time: 2025-07-01 20:19:56
# Runtime: N/A
# Memory: N/A

from random import randint

class RandomizedSet:

    def __init__(self):
        self.l = []
        self.m = {}

    def insert(self, val: int) -> bool:
        if val in self.m:
            return False
        self.l.append(val)
        self.m[val] = len(self.l) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.m:
            return False
        idx = self.m[val]
        last_idx = len(self.m)-1
        last_val = self.l[last_idx]

        del self.m[val]
        self.l[idx], self.l[last_idx] = self.l[last_idx], self.l[idx]
        return True

    def getRandom(self) -> int:
        i = randint(0, len(self.m) - 1)
        return self.l[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()