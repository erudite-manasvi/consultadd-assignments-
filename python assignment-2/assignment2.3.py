# Given an array of N integers and an integer K, find the number of pairs of elements in the array whose sum is equal to K.

def twoSum(nums, target):
        d = {}
        c = 0

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in d:
                c+=1
        
            d[nums[i]] = i

        return c

print(twoSum([1, 4, 45, 6, 10, 8],16))



