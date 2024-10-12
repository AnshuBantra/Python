# For this lab, imagine you are an IT Specialist at a medium-sized company.
# The Human Resources Department at your company wants you to find out how many
# people are in each department.
# You need to write a Python script that reads a CSV file containing a list of
# the employees in the organization, counts how many people are in each department,
# and then generates a report using this information. The output of this script
# will be a plain text file. We will guide you through each step of the lab.
# %%
import csv
dept = {}
with open('employees.csv') as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    for row in reader:
        if row['Department'] not in dept:
            dept[row['Department']] = 1
        else:
            dept[row['Department']] += 1

print(dept)
# %%

import csv

def read_employees(csv_file):
  with open(csv_file) as file:
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    reader = csv.DictReader(file, dialect='empDialect')

    employee_list = []
    for row in reader:
        employee_list.append(row)

  return employee_list

employee_list = read_employees('employees.csv')
print(employee_list)
# %%
#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

  employee_list = []
  for data in employee_file:
    employee_list.append(dict(data))

  return employee_list

employee_list = read_employees('employees.csv')
print(employee_list)
# %%


#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')

    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))

    return employee_list

employee_list = read_employees('/home/student/data/employees.csv')

def process_data(employee_list):

    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

dictionary = process_data(employee_list)


def write_report(dictionary, report_file):

    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
        f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()

write_report(dictionary, 'report.txt')