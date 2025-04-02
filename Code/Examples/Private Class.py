#use __variable to make it private
class Employee:
    __salary =1000
def get_salary(self):
    return self.__salary
    
e = Employee()
print(e.get__salary())