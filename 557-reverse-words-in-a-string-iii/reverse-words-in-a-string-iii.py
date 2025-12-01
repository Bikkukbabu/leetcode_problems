class Solution:
    def reverseWords(self, s: str) -> str:
        output_string = ''
        temp_string = ''
        for char in s:
            if char == ' ':
                output_string = output_string+temp_string[::-1]+' '
                temp_string = ''
            else:
                temp_string = temp_string+char
        return output_string+temp_string[::-1]