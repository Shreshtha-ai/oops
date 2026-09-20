class Employee:
    def __init__(self, name, salary):
        self.__salary = salary
        self.name = name

    def get_salary(self):
        return self.__salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.bonus


m = Manager("Sarah", 80000, 10000)

print(m.get_salary())