class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mapping = {}
        if len(s) != len(t):
            return False
        for char in s:
            s_mapping[char] = s_mapping.get(char, 0) + 1
        for c in t:
            if s_mapping.get(c, 0) == 0:
                return False
            else:
                s_mapping[c] = s_mapping[c] - 1
        return True
            