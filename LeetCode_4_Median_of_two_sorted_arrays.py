class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        l,r=0,0
        res=[]
        while l<len(nums1) and r<len(nums2):
            if nums1[l]<=nums2[r]:
                res.append(nums1[l])
                l+=1
            else:
                res.append(nums2[r])
                r+=1
        while l<len(nums1):
            res.append(nums1[l])
            l+=1
        while r<len(nums2):
            res.append(nums2[r])
            r+=1
        length = len(nums1)+len(nums2)
        
        if length%2 != 0:
            return res[length//2]
        return (res[length//2-1] + res[length//2])/2
            