# 1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. "Two sum"

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
