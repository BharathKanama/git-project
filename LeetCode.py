class Solution:
    def twoSum(self, nums, target):
        res=[]
        for i in nums:
             a,b=i,i+1
             x=a+b
             if x==target:
                 res.append(a,b)
        return res

nums=[2,7,11,15]
target=[9]
output= Solution
r= output.twoSum(nums,target)
print(r)
