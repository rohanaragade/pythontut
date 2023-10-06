class brand:
    com="bmw"
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
        print("bmw is luxury brand")

    def getdetails(self):
        print(f"name of compony is {self.name}")
        print(f"model of compony   is {self.model}")
        print(f"year of compony is {self.year}")

    def suv(self):
        print(f"{self.com} is king of suv")

toyota=brand('mahindra','thar',2021)
# toyota.name='Fortuner'
toyota.suv()
toyota.getdetails()

        