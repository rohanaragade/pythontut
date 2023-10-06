class mk:
    run=100
    def skip(self,aka):
        print(f"the runmachine {self.name} scored {self.run} AKA {aka}")

    @staticmethod
    def century():
            print("he scored 76 century till now")

ind=mk()
ind.name='virat'
print(ind.name)
ind.skip('king')
ind.century()
