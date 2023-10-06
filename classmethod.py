class emp:
    com='tcs'
    salary=50000
    location='pune'

    # def changesalary(self,sal):
    #     self.__class__.salary=sal

    @classmethod
    def changesalary(cls,sal):
        cls.salary=sal

ee=emp()
print(ee.salary)
ee.changesalary(100000)
print(ee.salary)
print(emp.salary)

