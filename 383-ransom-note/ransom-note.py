class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomnote_map = {}
        magazine_map = {}
        for index in range(len(ransomNote)):
            char = ransomNote[index]
            ransomnote_map[char] = ransomnote_map.get(char, 0) + 1
        for index in range(len(magazine)):
            char = magazine[index]
            magazine_map[char] = magazine_map.get(char, 0) + 1
        for key, value in ransomnote_map.items():
            if magazine_map.get(key, 0) == 0:
                return False
            if magazine_map.get(key) < value:
                return False
        return True