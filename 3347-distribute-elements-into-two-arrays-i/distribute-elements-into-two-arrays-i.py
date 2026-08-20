class Solution(object):
    def resultArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1=[len(nums)]
        arr2=[len(nums)]
        arr1[0]=nums[0]
        arr2[0]=nums[1]//1
        for i in range(2,len(nums)):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        nums=arr1+arr2
        return nums

        


        