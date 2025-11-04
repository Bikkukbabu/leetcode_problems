class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_mapping = {}
        result = []
        for string in strs:
            map_string = "".join(sorted(string))
            if map_string in string_mapping:
                string_mapping[map_string].append(string)
            else:
                string_mapping[map_string] = [string]
        for _, value in string_mapping.items():
            result.append(value)
        return result