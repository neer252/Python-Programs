no_of_cases=input("Enter number of cases for the program:")
for i in range(no_of_cases):
    print "Enter Details for Case:",i+1
    number_of_parties=int(input("Enter the number of parties:"))
    hartal_parameters=map(int,raw_input("Emter the hartal parameters for each party in single line having spaces between them:").split(' '))
    no_of_days=int(input("Enter number of days:"))
    wasteddays,dayspassing=0,0
    while(dayspassing<no_of_days):
        if (dayspassing%7)!=5 and (dayspassing%7)!=6:
            for j in range(0,number_of_parties):
                if not((dayspassing+1) % hartal_parameters[j]):
                    wasteddays=wasteddays+1
                    break
        dayspassing=dayspassing+1
    print "CASE:", i+1
    print "Number of Days wasted due to hartals:",wasteddays
    print "\n------------------------------------------\n"
