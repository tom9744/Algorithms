from typing import List

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= target[char] > 0
            target[char] -= 1

            if missing == 0:
                while left < right and target[s[left]] < 0:
                    target[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right

                target[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]
