'''
MEDIUM
 
Description

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original 
list of strings.

Please implement encode and decode

Example 1:

Input: ["lint","code","love","you"]

Output: ["lint","code","love","you"]

Explanation:
One possible encode method is: "lint:;code:;love:;you"

'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: s: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, s):
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res