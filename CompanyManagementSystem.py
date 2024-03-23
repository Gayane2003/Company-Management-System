from Company import * 

def main():
    c1 = Company("DISCO")
    c1.hireDirector("Lili", "Brown", "6262763", 40, 5)
    lili = c1.getEmployee("Lili", "Brown")
    
    c1.hireEmployee("Ann", "White", "2787937", 39, 4, "SWManager", "senior")
    ann = c1.getEmployee("Ann", "White")
    
    c1.hireEmployee("Gayane", "Ohanjanyan", "978743", 19, 5, "SWManager", "senior", ann)
    gayane = c1.getEmployee("Gayane", "Ohanjanyan")
    
    c1.hireEmployee("Jack", "Green", "7163876", 26, 1, "FinanceManager")
    fm1 = c1.getEmployee("Jack", "Green")
    
    c1.hireEmployee("Ann", "Stepanyan", "73618726", 39, 3, "Accountant", "", fm1)
    ann2 = c1.getEmployee("Ann", "Stepanyan")
    
    c1.hireEmployee("Iren", "Sahakyan", "324798237", 20, 2, "Accountant", "", fm1)
    iren = c1.getEmployee("Iren", "Sahakyan")
    
    c1.hireEmployee("Jane", "Scott", "678123862", 25, 1, "SWEngineer", "middle", ann)
    jane = c1.getEmployee("Jane", "Scott")
    
    c1.hireEmployee("Nare", "Ohanjanyan", "6337874", 17, 3, "SWEngineer", "junior", ann)
    nare = c1.getEmployee("Nare", "Ohanjanyan")
    
    c1.hireEmployee("Gurgen", "Matevosyan", "128739", 39, 2, "SWEngineer", "junior", ann)
    gurgen = c1.getEmployee("Gurgen", "Matevosyan")
    
    c1.hireEmployee("Mariana", "Ananyan", "38949328", 28, 0, "SWEngineer", "middle", ann)
    mariana = c1.getEmployee("Mariana", "Ananyan")
    
    
    c1.hireEmployee("Rustam", "Hakobyan", "128739", 39, 4, "SWEngineer", "senior", gayane)
    rustam = c1.getEmployee("Rustam", "Hakobyan")

    c1.hireEmployee("Diana", "Rustamyan", "88173719", 45, 0, "SWEngineer", "middle", gayane)
    diana = c1.getEmployee("Diana", "Rustamyan")
    
    c1.hireEmployee("Tom", "Mask", "1786434", 14, 5, "SalesPerson", "63623874jkda")
    
    for i in c1.getEmployees():
        print("ID: " + str(i._id) + ", Name: " + i._name + ",  Surname: " + i._surname + "\n")
    
    ann.get_team()



    print("\n______________HOMEWORK 4_______________")
    
    print("\nDisplaying the result via Print\n")
    c1.enableMentorship(ann, gayane)
    c1.enableMentorship(ann, jane)
    c1.enableMentorship(ann, nare)
    c1.enableMentorship(ann, gurgen)

    
    c1.enableMentorship(fm1, ann2)
    c1.enableMentorship(fm1, iren)
    c1.enableMentorship(fm1, iren)
    
    c1.enableMentorship(lili, ann)
    c1.enableMentorship(lili, fm1)
    
    #I created this method for myself, to make sure the method is working properly. 
    c1.print_enableMentorship()
    
    mentor = c1.getMentor(ann2)
    
    print("\nThe mentor of", ann2._name, "is", mentor._name, "\n")


    print("\n______________HOMEWORK 6_______________")
    workers = c1._employees
    workers.pop()
    workers.pop()

    hp = MinPriorityQueue()


    for i in workers:
        hp.enqueue(i)

    print("Number of employees with given performance indicator: ", hp.getNumberOfEmployeesPerformingAt(5), "\n")

    print("Level Order Traversal")
    hp.print()

    print("\nIn Order Traversal\n")
    hp_iter = iter(hp)

    while True:
        try:
            k = next(hp_iter)
            print("Name :", k._name, ",", "Perf. indicator :", k._perf_ind)
        except StopIteration:
            break

    print("\nRemoving elements from heap one by one\n")
    print("1st removed: ", hp.deque()._perf_ind)
    print("2nd removed: ", hp.deque()._perf_ind)
    print("3rd removed: ", hp.deque()._perf_ind)
    print("4th removed: ", hp.deque()._perf_ind)
    print("5th removed: ", hp.deque()._perf_ind)
    print("6th removed: ", hp.deque()._perf_ind)
    print("7th removed: ", hp.deque()._perf_ind)
    print("8th removed: ", hp.deque()._perf_ind)
    print("9th removed: ", hp.deque()._perf_ind)
    print("10th removed: ", hp.deque()._perf_ind)


    
if __name__ == "__main__":
    main()
    
    
    