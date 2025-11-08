class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_mapping = {'a':0,'e':0,'i':0,'o':0,'u':0}
        consonant_mapping = {}
        max_vowel = 0
        max_consonant = 0
        for char in s:
            if char in vowel_mapping:
                vowel_mapping[char] = vowel_mapping.get(char) + 1
                max_vowel = max(max_vowel, vowel_mapping[char])
            else:
                consonant_mapping[char] = consonant_mapping.get(char, 0) + 1
                max_consonant = max(max_consonant, consonant_mapping[char])
        return max_vowel + max_consonant