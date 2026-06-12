f = open("employee.txt", "w")

name = input("Enter employee name:")
salary = input("Enter employee salary:")
emp_Id = input("Enter employee id:")

f.write("employee name:" + name + "\n")
f.write("emloyee salary:" + salary + "\n")
f.write("employee id:" + emp_Id + "\n")

print("Data saved successfully")