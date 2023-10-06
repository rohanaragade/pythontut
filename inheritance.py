class employee:
    compony='google'

    def showdetails(self):
        print(f'employee working in {self.compony}')

    def salary(salary):
        print("salary is 100K")
    
class progammer(employee):
    language='python'
    compony='tcs'
    
    def showcode(self):
        print(f"programmers are using language {self.language}")

    # def showdetails(self):
    #     print(f'employee working in')

e=employee()
p=progammer()
e.showdetails()
e.salary()
p.showcode()
p.showdetails()
p.salary()
print(p.compony)