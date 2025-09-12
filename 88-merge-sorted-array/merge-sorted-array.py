class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #find the last index in nums1
        #length of nums1 is n + m - 1
        l = n + m - 1
        #iterate until you reach end of either list
        while n > 0 and m > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[l] = nums2[n - 1]
                n -= 1
            elif nums1[m - 1] >= nums2[n - 1]:
                nums1[l] = nums1[m - 1]
                m -= 1
            l -= 1
        #case if all elements in list1 are processed
        while n > 0:
            nums1[l] = nums2[n - 1]
            l -= 1
            n -= 1
        return
        