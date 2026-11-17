class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans = ans + str(len(s)) + "è" + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = s.find("è", i)
            length = int(s[i:j])
            ans.append(s[j + 1 : j + 1 + length])
            i = j + length + 1
        return ans
