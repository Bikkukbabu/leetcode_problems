class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_mapping = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in string_mapping:
                string_mapping[sorted_string].extend([string])
            else:
                string_mapping[sorted_string] = [string]
        result = []
        for _, value in string_mapping.items():
            result.append(value)
        return result