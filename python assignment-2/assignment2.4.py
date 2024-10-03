# Given an array of size N. The task is to rotate array by D elements towards right

# ---------------------------------- Solution 1 -------------------------------
def rotate(nums, k):
    res = []
    for i in range(len(nums)-k,len(nums)):
        res.append(nums[i])

    for i in range(0,len(nums)-k):
        res.append(nums[i])

    return res


# ---------------------------------- Solution 2-----------------------------------
def rotate2(nums, k):
        n = len(nums)
        k = k%n

        res = [0]*n

        for i in range(n):
            res[(i+k)%n] = nums[i]

        return res

# -------------------------------- Solution 3 ----------------------------------
def func(lst,start,end):
        lst[start:end] = lst[start:end][::-1]

def rotate3(nums, k):
    n = len(nums)
    k = k%n
    func(nums,0,n)
    func(nums,0,k)
    func(nums,k,n)

    return nums


print(rotate([1, 2, 3, 4, 5],2))