class Department():
    parentAttr = 100
    def __init__(self, Dept):
        self.Dept=Dept
        parentAttr = 100
class Employee(Department):
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary, Age,Dept):
      self.name = name
      self.salary = salary
      self.Age= Age
      self.Dept=Dept
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary, 'Age :',self.Age,'Department:',self.Dept)

emp1 = Employee("Zara", 2000,32,10)
emp2 = Employee("samba", 3000,44,11)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
emp1.Age=27 # modify age to 27
emp1.displayEmployee()

print(hasattr(emp1, 'Age') )# returns true or flase
print(getattr(emp1, 'Age')) # returns value o age of emp1
print(Department.parentAttr) # inheritance useds calling with parent class



