class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for s in strs:
            while result != s[:len(result)]:    
                result = result[:-1]

        return result


