class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord("a")] += 1
            hashmap.setdefault(tuple(cnt), []).append(s)
        return list(hashmap.values())
