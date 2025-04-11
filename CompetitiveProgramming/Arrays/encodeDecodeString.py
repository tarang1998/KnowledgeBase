class Solution:

    # Time Complexity : O(n)
    def encode(self, strs: List[str]) -> str:

        result = ""
        for string in strs:
            stringLength = len(string)
            result += str(stringLength) + "#" + string

        return result


    def decode(self, s: str) -> List[str]:
        
        count = ""

        index = 0 
        result = []

        while(index<len(s)):
            c = s[index]
            if c.isdigit():
                count += c
                index += 1 
            if c == "#":
                index += 1
                result.append(s[index:index+int(count)])
                index += int(count)
                count = ""

        return result

