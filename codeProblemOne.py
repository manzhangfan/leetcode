'''
1.Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution:
	#Approch One faster
	def twoSum(self,nums:List[int],target:int)->List[int]:
		hashmap={}
		for i in range(len(nums):
			x=nums[i]
			if x in hashmap:
				return [hashmap[x],i]
			else:
				hashpmap[target-x]=i
	#Approch Two 
	def twosum(self,nums:List[int],target:int)->List[int]:
		result=[]
		for i in range(len(nums)-1):
			for j in range(i+1,len(nums)):
				if nums[i]+nums[j]==target:
					result.append(i)
					result.append(j)
		returen result