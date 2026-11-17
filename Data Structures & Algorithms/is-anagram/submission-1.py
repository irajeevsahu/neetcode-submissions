class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for a, b in zip(s, t):
            cnt1[ord(a) - ord("a")] += 1
            cnt2[ord(b) - ord("a")] += 1
        for c1, c2 in zip(cnt1, cnt2):
            if c1 != c2:
                return False
        return True
