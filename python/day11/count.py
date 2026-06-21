with open("count.txt","r") as file:
    count = 0
    for line in file:
       if line.strip():
           count += 1
    print(count)