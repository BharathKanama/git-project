# "if loop" Operators

# house_price = 100000
# good_credit= True
# if good_credit:
#     down_payment= 0.1 * house_price
#     print('put down 10%')
#
# else:
#     down_payment = 0.2 * house_price
#     print("put down 20%")
#
# print(f"down payment {down_payment}")




# LOGICAL OPERATORS

# has_high_income = True
# has_good_credit = True
# has_criminal_record = False
# if has_high_income and not has_good_credit:
#     print("eligible for loan")



#COMPARSION OPERATORS

# name = input("enter your name here: ")
# if len(name)<3:
#     print("name must be at least 3 characters")
# elif len(name)>10:
#     print("name can be maximum of 10 characters")
# else:
#     print("name looks good!")


# WEIGHT CONVERTER

# weight =int(input("enter your weight here: "))
# status = input(" (L)bs or (K)gs: ")
# if status.lower()=='l':
#     convert= int(weight * 0.45)
#     print(f"your are {convert} kgs")
# elif status.lower()=='k':
#     convert = int (weight * 2.204)
#     print(f"your are {convert} pounds")
# else:
#     print("enter a valid letter")



# WHILE LOOPS

# i=1
# while i<=5:
#     print('* ' * i)
#     i +=1
# print('done')


#GUEESING GAME

# secret_number =9
# guess_count =0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count +=1
#     if guess == secret_number:
#         print("You win!")
#         exit()
# print("try again")



#CAR GAME

help ='''
start - to start the car
stop - to stop the car
quit - to quit'''
start = False
stop = True
cmd = ""

while cmd.lower() !='quit':
    cmd = input("> ")
    if cmd.lower()=='help':
        print(help)

    elif cmd.lower()=='start':
        if start==False:
            start=True
            stop=False
            print("car started... ready to go")

        else:
            print("car already started.. lets go")
    elif cmd.lower()=='stop':
        if stop==False:
            stop=True
            start=False
            print("car stopped..")
        else:
            print("car isn't moving..")
    elif cmd.lower()=='quit':
        print("game over")
        exit()
    else:
        print("enter a valid cmd")
