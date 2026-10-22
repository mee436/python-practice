employees = [
    (101, "Meet Shastri", 500000),
    (102, "Dhruv", 105000),
    (103, "Ravi Patel", 450000)
]

user_input = int(input("Enter an employee ID"))
found = False

for employee in employees:
    employee_id = employee[0]
    employee_name = employee[1]
    employee_salary = employee[2]

    if employee_id == user_input:
        print("Employee ID: ", employee_id)
        print("Employee Name: ", employee_name)
        print("Employee Salary: ", employee_salary)
        found = True
        break

if found == False:
    print("Employee not found")
