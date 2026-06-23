sales = {
    "Jan": 100,
    "Feb": 150,
    "Mar": 200,
    "Apr": 250
}
count=0
for i in sales:
    if sales[i]>150:
        count += 1
print(count)