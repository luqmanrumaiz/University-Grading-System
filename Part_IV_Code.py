 # I declare that my work contains no examples of , such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Date: 2019/11/29

#Initializing Variables
progress=0
trailer=0
retriever=0
exclude=0

#Variables for the index of the test_case list at default
Pass=0
Defer=1
Fail=2

#Variable for the number of students which is also the outcomes that is 10
student_no=10

#List that stores the credits for 10 outcomes
test_cases=[120,0,0,100,20,0,100,0,20,80,20,20,60,40,20,40,40,40,20,40,60,20,20,80,20,0,100,0,0,120]

#function for getting the amount of students for each progression with 3 parameters that used when calling each
#inputs credits 
def progression(p,d,f):
    global progress,trailer,retriever,exclude
    if(p==120):
        progress+=1
    elif(p==100):            
        trailer+=1
    elif(f<=60):
        retriever+=1
    elif(f>=80):
        exclude+=1
#function for creating a histogram 
def histogram():
    print('Progress',progress,':',(progress*'*'))
    print('Trailing',trailer,':',(trailer*'*'))
    print('Retriever',retriever,':',(retriever*'*'))
    print('Excluded',exclude,':',(exclude*'*'))
    print()
    print(student_no,'outcomes in total.\n')

#loop used to call the progression function 10 times where the parameters are increased by one each time to match
#with the index of the test cases
for x in range(10):
    progression(test_cases[Pass+x],test_cases[Defer+x],test_cases[Fail+x])

histogram()
