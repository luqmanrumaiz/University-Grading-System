# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Date: 2019/11/29

#initializing variables required to count different progression outcomes
progress=0
trailer=0
retriever=0
exclude=0
student_no=0

#function to see if the entered credit is out of range 
def range_error(grade):
    if(grade%20!=0 or grade>120):
          print('Range Error!\n')
          credit_input()
#function to see if the total of the credits is not equals to 120
def total_check():
    global pass_entered,defer_entered,fail_entered
    if(total!=120):
        print('Incorrect Total!\n')
        #entered credits variables are resetted so that the user can retry the program when the
        #total is incorrect
        pass_entered=False
        defer_entered=False
        fail_entered=False
        credit_input()
#function that checks the progression outcome based on the credits entered and
#counts the number of students for each progression outcome
def show_progression():
    global progress,trailer,retriever,exclude
    if(Pass==120):
        progress+=1
        print('\nProgression Outcome : Progress')
    elif(Pass==100):            
        print('\nProgression Outcome : Progress – module trailer')
        trailer+=1
    elif(Fail<=60):
        print('\nProgression Outcome : Do not progress – module retriever')                
        retriever+=1
    elif(Fail>=80):
        print('\nProgression Outcome : Exclude')
        exclude+=1
#function that displays the histogram for the progression outcomes
def histogram():
    print('Progress',progress,':',(progress*'*'))
    print('Trailing',trailer,':',(trailer*'*'))
    print('Retriever',retriever,':',(retriever*'*'))
    print('Excluded',exclude,':',(exclude*'*'))
    print()
    print(student_no,'outcomes in total.\n')

#function for obtaining user input while checking if any errors occur   
def credit_input():
    global Pass,Defer,Fail,pass_entered,defer_entered,fail_entered,total,student_no
    #error handling for the credit inputs 
    try:
    #multiple if conditions are used for each input to identify if it has been already given to prevent the user
    #from entering the previous input when the input function is called again if an error is made
        if(pass_entered==False):
            Pass=int(input('Insert your Credits for Passed Exams : '))
            range_error(Pass)
            pass_entered=True

        if(defer_entered==False):    
            Defer=int(input('Insert your Credits you recieved from Deferred exams : '))
            range_error(Defer)
            defer_entered=True

        if(fail_entered==False):
            Fail=int(input('Insert your Credits for Failed Exams : '))
            range_error(Fail)
            fail_entered=True
        
    #exception if the input type is not an integar
    except ValueError:
        print('Integers Required !\n')
        credit_input()
    #checking the total of the inputs 
    total=Pass+Defer+Fail
    total_check()
    return 

#while loop that allows the user to retry the program any number of times for different students
while True:
    #resetting the variables that see if the input has been entered for a student
    pass_entered=False
    defer_entered=False
    fail_entered=False
    #counting each student and displaying which students' (by number) progression outcome is being calculated
    student_no+=1
    print('Predicting Progression Outcome for Student',student_no,'\n')
    credit_input()
    show_progression()
    #Identifying if the user wishes to exit the program and display the histogram or to get the progression
    #outcome of another studen
    Quit=input('\nInput q to Quit else any other key to Continue  : ')
    if(Quit=='q'):
        histogram()
        break



