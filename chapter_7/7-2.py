"""
7.2 Call Center: Imagine you have a call center with three levels of employees: respondent, manager,
and director. An incoming telephone call must be first allocated to a respondent who is free. If the
respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not
free or not able to handle it, then the call should be escalated to a director. Design the classes and
data structures for this problem. Implement a method dispatchCall() which assigns a call to
the first available employee.
Hints:#363
"""
import time

class Employee:
	def __init__(self):
		self.is_busy = False
		self.call = None

class Manager(Employee):
	def __init__(self):
		super().__init__()

class Respondent(Employee):
	def __init__(self):
		super().__init__()

class Director(Employee):
	def __init__(self):
		super().__init__()

def dispatchCall(employees, call):
	while True:
		for employee in employees:
			if type(employee) == "Respondent" and not employee.is_busy:
				assign_call(employee, call)
				return
		for employee in employees:
			if type(employee) == "Manager" and not employee.is_busy:
				assign_call(employee, call)
				return
		for employee in employees:
			if type(employee) == "Direcotr" and not employee.is_busy:
				assign_call(employee, call)
				return
		time.sleep(1000)

def assign_call(employee, call):
	employee.call = call
	employee.is_busy = True

def remove_call(employee):
	employee.call = None
	employee.is_busy = False
