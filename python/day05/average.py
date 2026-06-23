nums = [10, 20, 30, 40, 50]

total=0
count=0


for  i in nums:
    total += i
    
avg = total/len(nums)

for i in nums:
    if i>avg:
        count += 1
print(count)    
print(avg)