class Employee():
    def show_details(self,**kwargs):
        print("Employee",kwargs)

class Developer(Employee):
    def show_details(self,**kwargs):
        print("Developer: ",kwargs)

        kwargs["role"]="Developer"
        super().show_details(**kwargs) #super passes onto next on mro

class Tester(Employee):
    def show_details(self,**kwargs):
        print("Tester",kwargs)

        kwargs['testing'] = 'Manual'
        super().show_details(**kwargs)


class TeamLead(Developer,Tester):
    def show_details(self,**kwargs):
        print("TeamLead",kwargs)

        kwargs["manage"] = "Team"
        super().show_details(**kwargs)


obj = TeamLead()
obj.show_details(name = "shreshtha",experience = 10,) #here 9 is not a keyword argument. It is pos




