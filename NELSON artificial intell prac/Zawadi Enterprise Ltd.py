#Capture  the employee details
payroll_number = input("Enter payroll number: ")
name = input("Enter employee name: ")
gender = input("Enter gender: ")
department = input("Enter department: ")
basic_salary = float(input("Enter basic salary (Ksh): "))

#Calculate their allowances and gross pay
house_allowance = 6500
medical_allowance = 5500

gross_pay = basic_salary + house_allowance + medical_allowance

# 3. Calculate P.A.Y.E
if gross_pay >= 40000 and gross_pay <= 49000:
    paye = gross_pay * 0.06
elif gross_pay >= 31000 and gross_pay <= 39000:
    paye = gross_pay * 0.05
elif gross_pay >= 20000 and gross_pay <= 30000:
    paye = gross_pay * 0.04
elif gross_pay >= 0 and gross_pay <= 19000:
    paye = 0

#Calculate N.H.I.F and N.S.S.F
nhif = gross_pay * 0.02
nssf = gross_pay * 0.03

# Calculate total deductions and net pay
total_deductions = paye + nhif + nssf
net_pay = gross_pay - total_deductions

# Display employee details and salary calculations
print("\n EMPLOYEE PAY SLIP ")
print("Name of employee:", name)
print("Payroll number:", payroll_number)
print("Gender:", gender)
print("Department:", department)
print("Basic Pay: Ksh", basic_salary)
print("House Allowance: Ksh", house_allowance)
print("Medical Allowance: Ksh", medical_allowance)
print("Gross Pay: Ksh", gross_pay)
print("P.A.Y.E: Ksh", paye)
print("N.H.I.F: Ksh", nhif)
print("N.S.S.F: Ksh", nssf)
print("Total Deductions: Ksh", total_deductions)
print("NET PAY: Ksh", net_pay)
