nums = [10, 20, 30, 40, 50]
largest_element=nums[0]
smallest_element=nums[0]
total=0
for i in nums:
    if i>largest_element:
        largest_element=i
    else:
        smallest_element=i


for i in range(len(nums)):
    total += nums[i]
print(total)
print(largest_element)
print(smallest_element)