import csv
import openpyxl

with open('employees.csv', newline="") as employeefile:
    employee_dict_reader = csv.DictReader(employeefile)
    employee_dict_data = list(employee_dict_reader)

new_rows = []

for row in employee_dict_data:
    employee_name = row["Name"].strip().capitalize()

    employee_dept = row["Department"].strip()
    if employee_dept == "":
        employee_dept = "Unknown"

    employee_salary = row["Salary"].strip()
    try:
        employee_salary = int(employee_salary)
    except ValueError:
        employee_salary = 0

    new_rows.append({"Name": employee_name, "Department": employee_dept, "Salary": employee_salary})

with open('clean_employees_info.csv',"w", newline="") as newEmployeeFile:
    write = csv.DictWriter(newEmployeeFile, fieldnames=["Name","Department","Salary"])
    write.writeheader()
    write.writerows(new_rows)

wb = openpyxl.Workbook()   
wb.sheetnames  

sheet = wb.active
sheet.title = "Employees"

sheet.append(["Name", "Department","Salary"])

for row in new_rows:
    sheet.append([row["Name"],row["Department"], row["Salary"]])

wb.save("clean_employees_info.xlsx")