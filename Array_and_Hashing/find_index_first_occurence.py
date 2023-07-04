'''
28. Find the Index of the First Occurrence in a String - Easy/Hard

Easy - O(N^2) or O(MN)

Hard - O(M+N) : KMP

Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

#Easy : O(n)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)
    
#Easy 2 : O(n^2)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)):
            for j in range(i,len(haystack)):
                print(haystack[i:j+1])
                if(haystack[i:j+1]==needle):
                    return(i)

        return -1
    
#Easy 3 : O(n*m)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        i ,j =0, len(needle)
        while j <= len(haystack):
            currentNeedle = haystack[i:j]
            if currentNeedle == needle:
                return i
            i += 1
            j += 1
        return -1
    
#Hard : O(m+n)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        fn = len
        if needle == "":
            return 0
        lps = [0] * fn(needle)

        prevLPS, i = 0, 1
        while i < fn(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0 
        j = 0  
        while i < fn(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == fn(needle):
                return i - fn(needle)
        return -1