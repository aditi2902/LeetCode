from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        f1=Counter(nums1)
        f2=Counter(nums2)
        res=[]
        for x in f1:
            if x in f2:
                y=f1[x]
                z=f2[x]
                j=min(y,z)
                for i in range(0,j):
                    res.append(x)
        return res
                    
                


        