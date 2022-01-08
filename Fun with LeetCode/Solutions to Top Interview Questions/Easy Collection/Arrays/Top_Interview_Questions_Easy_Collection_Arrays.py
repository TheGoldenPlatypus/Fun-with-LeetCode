### Contains Duplicate ###

class Solution(object):
    def containsDuplicate(self, nums):
        no_duplicate_nums = list(set(nums))
        nums_len = len(nums)
        no_dup_nums_len = len(no_duplicate_nums)
        if (nums_len - no_dup_nums_len) > 0:
            return True
        return False
        
 ########################################

 
### Single Number ###

class Solution(object):
    def singleNumber(self, nums):
        x = 0
        for i in range(len(nums)):
            x = nums.count(nums[i])    
            if x == 1:
                return nums[i]
        
 #########################################


 ### Intersection of Two Arrays II ###

class Solution(object):
    def intersect(self, nums1, nums2):
        res = []
        len1 = len(nums1)
        len2 = len(nums2)
        max_len = max(len1,len2)
        if len1 == max_len:
            non_iter_arr = nums1
            iterate_arr = nums2
        else:
            non_iter_arr = nums2
            iterate_arr = nums1
            
        for i in range(len(iterate_arr)):
         
            if iterate_arr[i] in non_iter_arr:
                res.append(iterate_arr[i])
                non_iter_arr.remove(iterate_arr[i])
                
        
        return res
        
 #########################################


 ### Plus One ###

class Solution(object):
    def plusOne(self, digits):
        digits.reverse()
        for i in range(len(digits)):
            if digits[i] != 9:
                digits[i] += 1
                return list(reversed(digits))
            
            if digits[i] == 9:
                digits[i] = 0
                if i == len(digits)-1:
                    digits.insert(0,1)    
                    return (digits)
        
 #########################################


### Move Zeroes ###

class Solution(object):
    def moveZeroes(self, nums):
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter+=1
                
                
        while counter > 0:
            nums.remove(0)
            nums.append(0)
            counter-=1
        
 #########################################


### Two Sum ###

class Solution(object):
    def twoSum(self, nums, target):
        res = {}
        for i,j in enumerate(nums):
            remnant = target - j
            if remnant in res:
                return [res[remnant],i]
            res[j] = i
        
 #########################################