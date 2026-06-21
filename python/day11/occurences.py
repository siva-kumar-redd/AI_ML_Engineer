with open("occurences.txt","r")  as file:
    count = 0

    for line in file:
        if line.strip() == "positive":
            count += 1
    print(count)