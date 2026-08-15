class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        """
        stack=[]
        maxAr=0
        for i,h in enumerate(heights):
            start=i #store the start index
            while stack and stack[-1][1]>h:
                index,ht=stack.pop()
                maxAr=max(maxAr,ht*(i-index))
                start=index
            stack.append([start,h])
        for i,h in stack:
            maxAr=max(maxAr,(len(heights)-i)*h)
        return maxAr