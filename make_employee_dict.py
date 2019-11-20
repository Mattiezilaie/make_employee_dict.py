# Author: Mahtab Zilaie
# Date: November 19 2019
# Description: class named Employee that has data members for an employee's name,
# ID_number, salary, and email_address.function named make_employee_dict that
# takes as parameters a list of names, a list of ID numbers, a list of salaries
# and a list of email addresses. function takes the first value of each list
# and use them to create an Employee object. As it creates these objects, it adds
# them to a dictionary, where the key is the ID number and the value for that key
# is the whole Employee object.

class Employee:

    def __init__(self, name, ID_number, salary, email_address):
        """Represents the employee's name, id number, salary, and email address"""
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address
    def __repr__(self):
        return str(self.name) + ", " + str(self.ID_number) + ", " + str(self.salary) + ", " + str(self.email_address)

def make_employee_dict(names, ID_numbers, salaries, emails):
    """ takes the first value of each list and use them to create an Employee object."""
    employee_dict = dict()
    for i in range(len(names)):
        employee = Employee(names[i], ID_numbers[i], salaries[i], emails[i])
        employee_dict[ID_numbers[i]] = employee
    return employee_dict
