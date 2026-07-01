class Employee:
    def employee_details(self,employee_id,name,salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        return self.employee_id,self.name,self.salary

emp1 = Employee()
emp2 = Employee()

print(emp1.employee_details(1,"Kiran",25000))
print(emp2.employee_details(2,"sunil",35000))
