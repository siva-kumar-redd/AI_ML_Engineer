marks = [65, 78, 92, 35, 40, 88, 21, 95]

total=0
highest=marks[0]
lowest=marks[0]
pass_count=0
fail_count=0
for i in marks:
    total += i
    if i>highest:
        highest=i
    else:
        lowest=i
    if i>=35:
        pass_count += 1
    else:
        fail_count += 1
print(total)
print(total/len(marks))
print(highest)
print(lowest)
print(pass_count)
print(fail_count)