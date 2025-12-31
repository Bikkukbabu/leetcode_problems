class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = {}
        for index in range(len(magazine)):
            char = magazine[index]
            magazine_map[char] = magazine_map.get(char, 0) + 1
        for index in range(len(ransomNote)):
            char = ransomNote[index]
            if magazine_map.get(char, 0) == 0:
                return False
            else:
                magazine_map[char] = magazine_map.get(char) - 1
        return True