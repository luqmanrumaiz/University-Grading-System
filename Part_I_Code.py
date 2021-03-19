# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Date: 2019/11/29


#initializing variables with boolean values False
pass_entered=False      
defer_entered=False     
fail_entered=False


#function to see if the entered credit is out of range 
def range_error(grade):
    if(grade%20!=0 or grade>120):   
        print('Range Error!\n')
        credit_input()

#function to see if the total of the credits is not equals to 120
def total_check():
    global pass_entered,defer_entered,fail_entered,total
    if(total!=120):
        print('Incorrect Total!\n')
        #entered credits variables are resetted so that the user can retry the program when the
        #total is incorrect
        pass_entered=False                 
        defer_entered=False
        fail_entered=False
        credit_input()
#function that checks the progression outcome based on the credits entered
def show_progression():
    print('\nProgression Outcome :',end=' ')
    if(Pass==120):
       print('Progress')
    elif(Pass==100):
        print('Progress – module trailer')        
    elif(Fail<=60):                                                     
        print('Do not Progress – module retriever')
    elif(Fail>60):
        print('Exclude')

#function for obtaining user input while checking if any errors occur       
def credit_input():                                                 
    global Pass,Defer,Fail,pass_entered,defer_entered,fail_entered,total
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
            print('Integers Required !')
            credit_input()
    #checking the total of the inputs 
    total=Pass+Defer+Fail
    total_check()
    return

credit_input()
show_progression()
