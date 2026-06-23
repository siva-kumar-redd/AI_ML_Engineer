marks = [78, 92, 45, 88, 67]

largest=marks[0]
lowest=marks[0]

total=0

for i in marks:
    if i>largest:
        largest=i
    else:
        lowest=i

for i in marks:
    total += i


print(largest)
print(lowest)
print(total/len(marks))