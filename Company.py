from abc import ABC, abstractmethod
from Collections import * 

class Employee(ABC):
    def __init__(self, name, surname, id, passport_id, age, perf_ind):
        self._name = name
        self._surname = surname
        self._id = id
        self._passport_id = passport_id
        self._age = age
        self._perf_ind = perf_ind
    
    @abstractmethod
    def do_work(self):
        pass
    
    @abstractmethod
    def take_vacation(self):
        pass


    def __gt__(self, other):
        return self._perf_ind  > other._perf_ind

    def __lt__(self, other):
        return self._perf_ind < other._perf_ind

    def __ge__(self, other):
        return self._perf_ind  >= other._perf_ind

    def __le__(self, other):
        return self._perf_ind <= other._perf_ind

    def perf_ind(self):
        return self._perf_ind

class Manager(ABC):
    def __init__(self):
        self._direct_reports = list()
    
    @abstractmethod
    def evaluate_employee(self):
        pass
    
    @abstractmethod
    def review_salary(self):
        pass
    
    def get_direct_reports(self):
        return self._direct_reports
    
    def get_team(self, n=0):
        if n == 0:
            if isinstance(self, Manager) == True:
                for i in self._direct_reports:
                    print(i._name)
                n = n +1
            else:
                print("You don't have employees, who report you")
        else:
            for i in self._direct_reports:
                if isinstance(i, Manager) == True:
                    i.get_team(0)  
            n = 0
        if n == 0:
            return 1
        self.get_team(n)
        
       
    

class SWEngineer(Employee):
    def __init__(self, name, surname, id, passport_id, age, perf_ind, title):
        super().__init__(name, surname, id, passport_id, age, perf_ind)
        self._title = title
        
    def do_work(self):
        print("I design and create computer systems and applications.")
     
    def take_vacation(self):
        print("Twice in a year, I take a vacation.")
    
    def take_lunch(self):
        print("Eat lunch untill to 2pm.")
    

class SWManager(SWEngineer, Manager):
    def __init__(self, name, surname, id, passport_id, age, perf_ind, title):
        SWEngineer.__init__(self, name, surname, id, passport_id, age, perf_ind, title)
        Manager.__init__(self)        
        
    def mentor_employee(self):
        print("Every two month we will do some mentorings.")
    
    def distribute_tasks(self):
        print("Every project will be divided into parts.")
    
    def evaluate_employee(self):
        print("Your every taks will be evaluated and granted")
    
    def review_salary(self):
        print("According to your qualities, you will earn money")
        

class Accountant(Employee):
    def do_work(self):
        print("I prepare and maintain important financial reports.")
    
    def take_vacation(self):
        print("I take 3 vacations in a year.")
        
    def release_salary(self):
        print("I report employees' salaries every month.")
        

class FinanceManager(Accountant, Manager):
    def __init__(self, name, surname, id, passport_id, age, perf_ind):
        Accountant.__init__(self, name, surname, id, passport_id, age, perf_ind)
        Manager.__init__(self)   
        
    def create_company_budget(self):
        print("I will calculate and optimize the budget!")
      
    def evaluate_employee(self):
        pass
        
    def review_salary(self):
        pass
        

class SalesPerson(Employee):
    def __init__(self, name, surname, id, passport_id, age, perf_ind, customer_accounts):
        super().__init__(name, surname, id, passport_id, age, perf_ind)
        self._customer_accounts = customer_accounts
        
    def do_work(self):
        print("I sale products or services to customers, and represent the brand.")
    
    def take_vacation(self):
        print("Twice in a year, I take a vacation.")
    
    def run_product_demo(self):
        print("I also run the product demo")


class Executive(Employee, Manager):
    def __init__(self, name, surname, id, passport_id, age, perf_ind):
        Employee.__init__(self, name, surname, id, passport_id, age, perf_ind)
        Manager.__init__(self)  
        
    def do_work(self):
        print("I direct, plan, and coordinate operational activities")
    
    def take_vacation(self):
        print("Once a year, I go to vacation!")
        
    def confirm_hiring(self, age):
        if age >= 16:
            return True
        else:
            return False
    def confirm_firing(self, Employee):
        pass
    
    def confirm_company_budget(self):
        print("I have counted everything")
    
    def evaluate_employee(self):
        print("I follow jobs and evaluate")
    
    def review_salary(self):
        print("I review salaries")



class Company:
    def __init__(self, name):
        self._name = name
        self._director = None
        self._employees = list()
        self._id = 1
        self.mentors = HashMap()

    def getEmployee(self, name, surname):
         for i in self._employees:
             if name == i._name and surname == i._surname:
                 return(i)
     
    def getEmployees(self):
        return(self._employees)
    
    def enableMentorship(self, mentor: Employee, mentee: Employee):
        self.index = self.mentors.hash(mentor)
        self.current = self.mentors._hash_table[self.index]
        while self.current:
            if self.current._key == mentor:
                if self.current._value._length < 3:
                    temp = self.current._value._first
                    while temp:
                        if temp._data == mentee:
                            return False
                        temp = temp._next
                    self.current._value.addLast(mentee)
                    self.mentors.put(mentor, self.current._value)
                    return True
                else:
                    return False
            self.current = self.current._next
            
        self.menteeList = LinkedList()
        self.menteeList.addLast(mentee)
        self.mentors.put(mentor, self.menteeList)
        return True
        
    def getMentor(self, mentee: Employee) -> Employee:
        j = list(self.mentors.keySet())

        for i in j:
            self.index = self.mentors.hash(i)
            current = self.mentors._hash_table[self.index]
            while current:
                temp = current._value._first
                while temp:
                    if temp._data == mentee:
                        return current._key
                    temp = temp._next
                current = current._next
        return False
    
        
        
    def hireDirector(self, name, surname, passport_id, age, perf_ind):
        d = Executive(name, surname, self._id, passport_id, age, perf_ind)
        self._employees.append(d)
        self._id +=1
        self._director = d
    
    def print_enableMentorship(self):
        for i in range(len(self.mentors._hash_table)):
            if self.mentors._hash_table[i] != None:
                current = self.mentors._hash_table[i] 
                mentees = list()
                while current:
                    temp = current._value._first
                    while temp:
                        mentees.append(temp._data._name)
                        temp = temp._next
                    print(f"{current._key._name} : {mentees}")
                    current = current._next
            else:
                print(None)
    
    def hireEmployee(self, name, surname, passport_id, age, perf_ind, type, title= None,  Manager = None, customer_accounts= None):
        if self._director != None:
            if Executive.confirm_hiring(Employee, age) == True:
                if type == "SWEngineer":
                    e = SWEngineer(name, surname, self._id, passport_id, age, perf_ind, title)
                    self._id +=1
                    self._employees.append(e)
                    
                    #checking
                    
                    if Manager == None:
                        for i in self._employees:
                            if (str(i.__class__) == "<class 'Company.Executive'>"):
                                i._direct_reports.append(e)
                    else:
                        Manager._direct_reports.append(e)      
                    
                        
                elif type == "SWManager":
                    e = SWManager(name, surname, self._id, passport_id, age, perf_ind, title)
                    self._id +=1
                    self._employees.append(e)
                    
                    #checking
                    
                    if Manager == None:
                        for i in self._employees:
                            if (str(i.__class__) == "<class 'Company.Executive'>"):
                                i._direct_reports.append(e)
                    else:
                        Manager._direct_reports.append(e)      
                    
                    
                elif type == "Accountant":
                    e = Accountant(name, surname, self._id, passport_id, age, perf_ind)
                    self._id +=1
                    self._employees.append(e)
                    
                    #checking
                    
                    if Manager == None:
                        for i in self._employees:
                            if (str(i.__class__) == "<class 'Company.Executive'>"):
                                i._direct_reports.append(e)
                    else:
                        Manager._direct_reports.append(e)      
                    
                
                elif type == "FinanceManager":
                    e = FinanceManager(name, surname,self._id, passport_id, age, perf_ind)
                    self._id +=1
                    self._employees.append(e)
                    
                    #checking
                    
                    if Manager == None:
                        for i in self._employees:
                            if (str(i.__class__) == "<class 'Company.Executive'>"):
                                i._direct_reports.append(e)
                    else:
                        Manager._direct_reports.append(e)      
                    
                    
                elif type == "SalesPerson":
                    e = SalesPerson(name, surname, self._id, passport_id, age, perf_ind, customer_accounts)
                    self._id +=1
                    self._employees.append(e)
                    
                    
                    #checking
                    
                    if Manager == None:
                        for i in self._employees:
                            if (str(i.__class__) == "<class 'Company.Executive'>"):
                                i._direct_reports.append(e)
                    else:
                        Manager._direct_reports.append(e)      
                    

                elif type == "Executive":
                    e = Executive(name, surname, self._id, passport_id, age, perf_ind)
                    self._id +=1
                    self._employees.append(e)
                    
                    
                    #checking
                    
                    if Manager == None:
                        for i in self._employees:
                            if (str(i.__class__) == "<class 'Company.Executive'>"):
                                i._direct_reports.append(e)
                    else:
                        Manager._direct_reports.append(e)      
                    
            else:
                print(name + " You cannot work in the company." + " You are still " + str(age) + ".\n")
        else:
            print("The company does not have a director, you can't hire anyone.")
        
       

        
        
        
        
        
        
        
        
        
        