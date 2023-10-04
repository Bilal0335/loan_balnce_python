#Task OOPS - 2 Salary Calculator

#Basic Information
print("NOTE: Base Salary cannot be less than 50,000")
name = input("Enter name: ").upper()
age = input("Enter your age: ")

#Remember Input is always taken as String so use typecasting
base_sal = float(input("Enter your In-hand Salary: "))

if base_sal <= 50000:
    Home_all = base_sal * .2 #20% Divided by 100 (for Simplicity)
    Med_all = base_sal * .1
    Trans_all = base_sal * .05
    Mob_all = base_sal * 0.03

elif base_sal <= 100000:
    Home_all = base_sal * .2
    Med_all = base_sal * .1
    Trans_all = base_sal * .05
    Mob_all = base_sal * 0.03

elif base_sal <= 150000:
    Home_all = base_sal * .2
    Med_all = base_sal * .1
    Trans_all = base_sal * .05
    Mob_all = base_sal * 0.03

else:
    Home_all = 0
    Med_all = 0
    Trans_all = 0
    Mob_all = 0


total_all = Home_all + Med_all + Trans_all + Mob_all

gross_sal = base_sal + total_all

#Tax Calculation (for Net Salary)

if gross_sal <= 100000:
    net_sal = gross_sal - (gross_sal * 0.13) #13% Divided by 100 (for Simplicity)

elif gross_sal <= 1000000:
    net_sal = gross_sal - (gross_sal * 0.07)

else:
    net_sal = "error"


print("Name:", name)
print("Basic Salary:", base_sal)
print("Total Allowances:", total_all)
print("Salary after Tax:", net_sal)


if net_sal >= 60000:
    print("Congratulations!, You're eligible for the Loan.")