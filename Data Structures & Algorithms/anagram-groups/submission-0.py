class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            # hashmap.setdefault(s_sorted, []).append(s)
            value = hashmap.get(s_sorted)
            if value:
                value.append(s)
                hashmap[s_sorted] = value
            else:
                hashmap[s_sorted] = [s]
        return list(hashmap.values())
