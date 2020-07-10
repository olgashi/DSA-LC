nums = [-2,1,-3,4,-1,2,1,-5,4]

p_slow = 0
p_fast = 1
temp_sum = nums[p_slow]
max_sum = nums[p_slow]

while p_fast < len(nums):
    if p_slow == len(nums)-1:
        break
    if p_slow == p_fast - 1 and p_fast < len(nums):
        p_fast += 1
    if (temp_sum + nums[p_fast]) > max_sum:
        max_sum = temp_sum + nums[p_fast]
        temp_sum += temp_sum + nums[p_fast]
        p_fast += 1
    else:
        temp_sum = nums[p_slow]
        p_slow += 1


