# 1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. "Two sum"

# Print The Two sum int given array that matches the target Value.

a = list(map(int,input("Enter a List: ").split()))
target = int(input("Enter a Target Value: "))
first_index = a[0]
length = len(a)
for i in range(0, length):
    for j in range(i + 1 , length):
        if(a[i] + a[j] == target):
            print([i , j])
            break;
    first_index = a[i]

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

