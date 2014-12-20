class Employee:
	'Common base class for all employees'
	empCount =0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount +=1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee (self):
		print "Name:", self.name, " Salary:", self.salary

"This would create first object of employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total employee %d" % Employee.empCount 
emp1.age = 7
setattr(emp1, 'age', 8)
print"%d" % emp1.age