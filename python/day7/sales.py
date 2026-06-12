sales = (120, 150, 180, 220, 300)


total=0
largest=sales[0]
smallest=sales[0]

for i in sales:
    total += i
    if i>largest:
        largest = i
    else:
        smallest = i
print(total)
print(largest)
print(smallest)
print(total/len(sales))