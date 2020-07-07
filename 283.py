nums = [0,0,0,1,0,1,0,1]

i = 0
count = 0
nums.append(None)
while nums[i] is not None:
    if nums[i] == 0:
        del nums[i:i+1]
        nums.append(0)
    else:
        i += 1
nums.remove(None)
print(nums)