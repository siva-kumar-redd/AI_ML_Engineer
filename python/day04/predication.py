def prediction(marks):
    if marks>=40:
        return "pass"
    else:
        return "fail"

print(prediction(75))
print(prediction(20))