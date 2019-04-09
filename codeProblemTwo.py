'''
167. Two Sum II
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(numbers)):
            x=numbers[i]
            if x in hashmap:
                return [hashmap[x],i+1]
            else:
                hashmap[target-x]=i+1