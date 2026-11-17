class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [c.lower() for c in s if c.isalnum()]
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True
