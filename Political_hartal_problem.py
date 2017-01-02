no_of_cases=input("Enter number of cases for the program:")
for i in range(no_of_cases):
    print "                    CASE:", i+1
    print "               -:Enter Details:-          "
    number_of_parties,hartal_parameters,no_of_days=int(input("Enter the number of parties:")),map(int,raw_input("Emter the hartal parameters for each party in single line having spaces between them:").split(' ')),int(input("Enter number of days:"))
    hartal_parameters.append(0)
    while(no_of_days):
        if ((no_of_days-1)%7)!=5 and ((no_of_days-1)%7)!=6:
            for j in range(0,number_of_parties):
                if (no_of_days % hartal_parameters[j])==0:
                    hartal_parameters[number_of_parties]+=1
                    break
        no_of_days-=1
    print "Number of Days wasted due to hartals: ",hartal_parameters[number_of_parties], "Days"
    print "\n------------------------------------------\n"
