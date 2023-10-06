class ro:
    def hey(self):
        print("say hey")
        
class ar(ro):
    def morning(self):
        print("say morning")

    def hey(self):
        super().hey()
        print("say goodbay")

class rda(ar):
    def night(self):
        print("say night")

    def hey(self):
        super().morning()
        super().hey()
        print("say i am happy")

a=rda()
a.hey()
a.morning()
a.night()