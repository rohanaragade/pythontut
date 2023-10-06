class Employee:
    compony='TCS'

ro=Employee()
ar=Employee()
print(ro.compony)
print(ar.compony)

Employee.compony='GOOGLE'
print(ro.compony)