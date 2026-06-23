predictions = [1, 0, 1, 1, 0, 0, 1, 1]

fraud_count=0
genuine_count=0

for i in predictions:
    if i==1:
        fraud_count+=1
    if i==0:
        genuine_count+=1

fraud_percentage = fraud_count/len(predictions) * 100

print(fraud_count)
print(genuine_count)
print(fraud_percentage)