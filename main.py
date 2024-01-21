class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dups = []
        for i in range(len(nums)-1):
            if nums[i] == nums [i+1]:
                dups.append(i)

        for idx, i in enumerate(dups):
            del nums[i-idx]
            
        return len(nums)