class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_pay(self):
        return self.salary * 12
    
    def __repr__(self):
        return f"{self.name} {self.yearly_pay()}"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def yearly_pay(self):
        base_pay = super().yearly_pay()
        return base_pay + self.bonus

# Main
sara = Employee("Sara", 80000)
omar = Manager("Omar", 150000, 200000)

staff = [sara, omar]

for person in staff:
    # Polymorphism: same method yearly_pay() different behavior
    print(person.name, person.yearly_pay())

print(isinstance(omar, Employee))