class rohan:
    com='cognizant'
    salary=50000
    salrybonus=1000

    @property
    def totalsalary(self):
        return self.salary+self.salrybonus
    
rr=rohan()
print(rr.totalsalary)