
health = input("What is your problem?  ")
problem = input("have you had this problem befor?(yes or no) ")

def problem_out(problem):
    if problem == "yes":
        print('you have it again')
    elif(problem == "no"):
        print("you have it now")
    else:
        print("ENTER EITHER YES OR NO")
        problem = input("have you had this problem befor?(yes or no) ")
        problem_out(problem)


problem_out(problem)
