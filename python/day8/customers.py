customer_ids = [
    101, 102, 101, 103, 104,
    102, 105, 106, 106, 107
]
unique_record = len(set(customer_ids))
duplicate_record = len(customer_ids) - unique_record
unique_record_percentage = unique_record/len(customer_ids) * 100
duplicate_record_percentage = duplicate_record/len(customer_ids) * 100
print("total customers:",len(customer_ids))
print("unique records:",len(set(customer_ids)))
print("duplicate records:",len(customer_ids)-len(set(customer_ids)))
print("unique record percentage:",unique_record_percentage)
print("duplicate record percentage:",duplicate_record_percentage)