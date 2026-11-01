from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        f=Counter(s)
        n=len(s)
        for ch in range(n):
            if f[s[ch]]==1:
                return ch
        return -1