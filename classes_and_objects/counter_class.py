"""
## 4. Counter Class with Class vs Instance Attributes  *(Medium)*

=================================================
COUNTER WITH CLASS VS INSTANCE ATTRIBUTES
=================================================

Problem Statement:
Write a Python CLASS called `Counter` that
maintains:
   - an INSTANCE counter for the current
     object (its own count)
   - a CLASS counter shared across ALL objects
     (the total count across the program)

The goal of this problem is to understand the
difference between:
   - INSTANCE attributes  (one per object,
     stored on `self`)
   - CLASS attributes     (one for the whole
     class, stored on the class itself)

-------------------------------------------------
Instructions:
1. Define the class:
      class Counter:
          total = 0       # CLASS attribute

          def __init__(self, name):
              self.name  = name
              self.count = 0   # INSTANCE attribute
2. Instance methods:
      - increment(self, step=1)
            * self.count  += step
            * Counter.total += step
        (note: use Counter.total, NOT self.total,
         when UPDATING the class attribute)
      - reset(self)
            * sets self.count back to 0
            * does NOT touch Counter.total
      - __str__(self)
            * "<name>: count=<count>"
3. Class method (regular method that touches
   class attribute):
      - show_total() can be a @staticmethod or
        a regular function inside the class
        that returns Counter.total
4. In the driver code:
      - create at least THREE Counter objects
      - call increment() a different number of
        times on each
      - reset ONE of them
      - print each object using print(c)
      - print the overall Counter.total
5. Do NOT use:
   - the global keyword
   - any external library

-------------------------------------------------
Input Example:
c1 = Counter("clicks")
c2 = Counter("views")
c3 = Counter("downloads")

for _ in range(3):
    c1.increment()
for _ in range(5):
    c2.increment()
c3.increment(10)
c1.reset()

Output Example:
clicks:    count=0
views:     count=5
downloads: count=10
Total across all counters: 18

-------------------------------------------------
Explanation:
- `c1.count`, `c2.count`, and `c3.count` are
  three SEPARATE numbers, because each lives
  on its own object.
- `Counter.total` is a SINGLE number shared by
  the whole class. Every increment() call adds
  to it, including the ones that were later
  reset on the instance.
- This is why c1 shows 0 but the class total
  is still 18 (3 + 5 + 10).
=================================================

"""
class Employee:
    company    = "Acme Corp"
    raise_pct  = 5

    def __init__(self, name, salary):
        self.name   = name
        self.salary = float(salary)

    def apply_raise(self):
        self.salary *= (1 + self.raise_pct / 100)

    @classmethod
    def set_raise_percentage(cls, new_pct):
        cls.raise_pct = new_pct

    @classmethod
    def from_string(cls, csv_line):
        name, salary = csv_line.split(',')
        return cls(name.strip(), float(salary.strip()))

    @staticmethod
    def is_valid_salary(amount):
        return (isinstance(amount, (int, float)) and amount > 0)

emp1_name = input("Enter first employee's name: ")
emp1_salary = input("Enter first employee's salary: ")
e1 = Employee(emp1_name, emp1_salary)

emp2_name = input("Enter second employee's name: ")
emp2_salary = input("Enter second employee's salary: ")
e2 = Employee(emp2_name, emp2_salary)

emp3_str = input("Enter third employee data: ")
e3 = Employee.from_string(emp3_str)

e1.apply_raise()
e2.apply_raise()
e3.apply_raise()

new_raise_percentage = int(input("Enter new global raise percentage: "))
Employee.set_raise_percentage(new_raise_percentage)

e1.apply_raise()
e2.apply_raise()
e3.apply_raise()

print(f"{e1.name} -> {e1.salary}")
print(f"{e2.name} -> {e2.salary}")
print(f"{e3.name} -> {e3.salary}")

salary_test1 = float(input("Enter a salary to test: "))
print(f"is_valid_salary({salary_test1})  -> {Employee.is_valid_salary(salary_test1)}")

salary_test2 = float(input("Enter another salary to test: "))
print(f"is_valid_salary({salary_test2})   -> {Employee.is_valid_salary(salary_test2)}")

salary_test3 = input("Enter a non-numeric value to test: ")
print(f"is_valid_salary('{salary_test3}')  -> {Employee.is_valid_salary(salary_test3)}")