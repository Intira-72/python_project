from datetime import datetime

class Person:

    def __init__(self, name, height, birthday):
        self.name = name
        self.birthday = birthday
        self.height = height
        self.age = self._get_older()

    def hello_world(self):
        print(f"Hello, I'm {self.name}")

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age} years old\nHeight: {self.height}"

    def _get_older(self):
        cal_age = datetime.now().year - datetime.strptime(self.birthday, "%Y/%m/%d").year
        return cal_age


# Inheritance
class Worker(Person):
    def __init__(self, name, height, birthday, salary):
        super().__init__(name, height, birthday)
        self.salary = salary

    def __str__(self):
        return super(Worker, self).__str__() + f"\nSalary: {self.salary:,}\nSalary Per Year: {self.cals_yearly_salary():,}"

    def cals_yearly_salary(self):
        return self.salary * 12
    
# Operator Overload
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"


if __name__=="__main__":
    worker1 = Worker("Henry", 182, "1980/01/23", 320000)
    yearly_salary = worker1.cals_yearly_salary()

    v1 = Vector(2, 5)
    v2 = Vector(3, 6)
    v3 = v1 + v2
    v4 = v1 - v2

    print(v1)
    print(v2)
    print(v3)
    print(v4)