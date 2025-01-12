class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs:
            while s.startswith(prefix) == False:
                # shrink the prefix from the end till we pass for all strings
                prefix = prefix[:-1]
        
        return prefix
