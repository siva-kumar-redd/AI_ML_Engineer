text = "banana"
b_count=0
a_count=0
n_count=0
for i in text:
    if i=="b":
        b_count += 1
    if i=="a":
        a_count += 1
    if i=="n":
        n_count += 1

print("b","->",b_count)
print("a","->",a_count)
print("n","->",n_count)
