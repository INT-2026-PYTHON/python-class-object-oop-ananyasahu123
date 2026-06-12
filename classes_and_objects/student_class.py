"""
## 3. Student Class with Marks List  *(Medium)*

=================================================
STUDENT CLASS WITH MARKS LIST
=================================================

Problem Statement:
Write a Python CLASS called `Student` that
stores a student's name, roll number, and a
LIST of subject marks. The class should be
able to compute statistics about the marks
and decide a grade.

This problem reinforces:
   - storing a LIST as an instance attribute
   - mutating that list through methods
   - calling one instance method from another
     using `self`

-------------------------------------------------
Instructions:
1. Define a class:
      class Student:
2. Constructor:
      def __init__(self, name, roll, marks=None):
          - if marks is None, set self.marks = []
            (do NOT use marks=[] as a default
             argument — it is a shared mutable
             default)
          - store self.name and self.roll
3. Instance methods:
      - add_mark(self, mark)
            * append a single mark to self.marks
            * reject negative marks or marks > 100
              with a message
      - total(self)          -> sum of marks
      - average(self)        -> total / count,
                                 0 if no marks
      - grade(self)          -> use self.average():
                                  >= 90 -> "A"
                                  >= 75 -> "B"
                                  >= 50 -> "C"
                                  else  -> "F"
      - report(self)         -> return a TUPLE:
              (name, roll, total, average, grade)
4. In the driver code:
      - create AT LEAST TWO students
      - add marks for each student using
        add_mark() in a for loop
      - print each student's report tuple
5. Do NOT use:
   - statistics / numpy modules
   - class attributes for marks (must be on
     each instance)

-------------------------------------------------
Input Example:
s1 = Student("Alice", 101)
for m in [90, 85, 95]:
    s1.add_mark(m)

s2 = Student("Bob", 102)
for m in [40, 55, 60]:
    s2.add_mark(m)

Output Example:
('Alice', 101, 270, 90.0, 'A')
('Bob',   102, 155, 51.666..., 'C')

-------------------------------------------------
Explanation:
- `self.marks` is a SEPARATE list for each
  student object, so Alice's marks do not mix
  with Bob's.
- `grade(self)` calls `self.average()`, which
  shows how one method can use another method
  on the SAME object through `self`.
=================================================

"""
class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age  = int(age)

    def greet(self):
        return f"Hi, I'm {self.name}, age {self.age}"

    @staticmethod
    def is_adult(age):
        return int(age) >= 18

class Employee(Person):
    company   = "Acme Corp"
    bonus_pct = 5

    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = float(salary)

    def work_intro(self):
        return (f"I work at {Employee.company} "
                f"as id {self.emp_id}")

    def apply_bonus(self):
        self.salary += self.salary * Employee.bonus_pct / 100

    @classmethod
    def set_bonus(cls, new_pct):
        cls.bonus_pct = new_pct

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, team=None):
        super().__init__(name, age, emp_id, salary)
        self.team = team if team is not None else []

    def add_member(self, employee):
        self.team.append(employee)

    def team_intro(self):
        return f"I lead a team of {len(self.team)} people."

    def team_total_salary(self):
        total_salary = self.salary
        for member in self.team:
            total_salary += member.salary
        return total_salary

person_name = input("Enter Person's name: ")
person_age = input("Enter Person's age: ")
p = Person(person_name, person_age)
print(p.greet())

emp1_name = input("Enter first Employee's name: ")
emp1_age = input("Enter first Employee's age: ")
emp1_id = input("Enter first Employee's ID: ")
emp1_salary = input("Enter first Employee's salary: ")
e1 = Employee(emp1_name, emp1_age, emp1_id, emp1_salary)

emp2_name = input("Enter second Employee's name: ")
emp2_age = input("Enter second Employee's age: ")
emp2_id = input("Enter second Employee's ID: ")
emp2_salary = input("Enter second Employee's salary: ")
e2 = Employee(emp2_name, emp2_age, emp2_id, emp2_salary)

print(e1.greet())
print(e1.work_intro())
print(e2.greet())
print(e2.work_intro())

manager_name = input("Enter Manager's name: ")
manager_age = input("Enter Manager's age: ")
manager_id = input("Enter Manager's ID: ")
manager_salary = input("Enter Manager's salary: ")
m = Manager(manager_name, manager_age, manager_id, manager_salary)
m.add_member(e1)
m.add_member(e2)

print(m.greet())
print(m.work_intro())
print(m.team_intro())

print(f"{e1.name} salary before bonus: {e1.salary}")
print(f"{e2.name} salary before bonus: {e2.salary}")
print(f"{m.name} salary before bonus: {m.salary}")

e1.apply_bonus()
e2.apply_bonus()
m.apply_bonus()

print(f"{e1.name} salary after first bonus (5%): {e1.salary}")
print(f"{e2.name} salary after first bonus (5%): {e2.salary}")
print(f"{m.name} salary after first bonus (5%): {m.salary}")

new_bonus_pct = input("Enter new bonus percentage: ")
Employee.set_bonus(int(new_bonus_pct))

e1.apply_bonus()
e2.apply_bonus()
m.apply_bonus()

print(f"{e1.name} salary after second bonus ({new_bonus_pct}%): {e1.salary}")
print(f"{e2.name} salary after second bonus ({new_bonus_pct}%): {e2.salary}")
print(f"{m.name} salary after second bonus ({new_bonus_pct}%): {m.salary}")

age_test1 = input("Enter an age to test for adulthood: ")
print(f"is_adult({age_test1}) -> {Person.is_adult(age_test1)}")
age_test2 = input("Enter another age to test for adulthood: ")
print(f"is_adult({age_test2}) -> {Person.is_adult(age_test2)}")

print(f"Team total salary -> {m.team_total_salary()}")