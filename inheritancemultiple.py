class emp:
    com='google'

class teacher:
    com='dypcet'
    score=5
    def sky(self):
        self.score=self.score+1
        print(self.score)

class student(emp,teacher):
    name='rohan'

kl=student()
kl.sky()
print(kl.com)