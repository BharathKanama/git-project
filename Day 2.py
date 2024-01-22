
# IF LOOP OPERATORS

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

# help ='''
# start - to start the car
# stop - to stop the car
# quit - to quit'''
# start = False
# stop = True
# cmd = ""
#
# while cmd.lower() !='quit':
#     cmd = input("> ")
#     if cmd.lower()=='help':
#         print(help)
#
#     elif cmd.lower()=='start':
#         if start==False:
#             start=True
#             stop=False
#             print("car started... ready to go")
#
#         else:
#             print("car already started.. lets go")
#     elif cmd.lower()=='stop':
#         if stop==False:
#             stop=True
#             start=False
#             print("car stopped..")
#         else:
#             print("car isn't moving..")
#     elif cmd.lower()=='quit':
#         print("game over")
#         exit()
#     else:
#         print("enter a valid cmd")




# REVISION

# help='''
# start =  to start the car
# stop= to stop the car
# quit = to quit tHE GAME
# '''
# start=False
# stop= True
# cmd =""
# while cmd.lower() != quit:
#     cmd= input("> ").lower()
#     if cmd=="help":
#         print(help)
#     elif cmd =="start":
#         if start==False:
#             start=True
#             stop=False
#             print("car started.. ready to go now")
#         else:
#             print("car already started")
#     elif cmd == "stop":
#         if stop== False:
#             stop=True
#             start=False
#             print("car stoppped")
#         else:
#             print("car already stopped")
#     elif cmd == "quit":
#         print("game over!...Thanks for playing my Game!!")
#         break
#     else:
#         print("cmd invalid... try again")




#   FOR LOOOPS

# total =0
# prices= [10,20,30]
# for price in prices:
#     total += price
# print(f" Total: {total}")



#  NESTED LOOPS

# for x in range(3):
#     for y in range(4):
#         print(f"( {x} , {y} )")


# numbers =[5,2,5,2,2]
# x='x'
# for i in numbers:
#     for y in x:
#         print(y * i)


# numbers=[2,2,2,2,7]
# for i in numbers:
#     result=''
#     for y in range(i):
#         result += 'x'
#     print(result)




#   LISTS

# numbers = [ 1,2,31,4,51,6,7,8,9]
# max = numbers[0]
# for i in numbers:
#     if i > max:
#         max =i
# print(max)



#  2D LISTS

# matrix =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for i in row:
#         print(i)



#    LIST METHODS

# numbers= [1,2,33,4]
# numbers.append(20)  --- add's item at ens of the list
# numbers.insert(4,9) --- insert item at given location
# numbers.insert(1,10)
# numbers.remove(9)   --- removes given item in list
# numbers.clear()   -- removes all items in list
# numbers.pop()  --- removes last item in list
# print(numbers.index(33)) --- provides the index value of given item
# print(numbers.count(2))

# numbers=[1,1,21,2,3,43,4,55,55,2,3,4,99]
# output=[]
# for i in numbers:
#     if i not in output:
#         output.append(i)
# output.sort()
# output.reverse()
# max = numbers[0]
# for i in numbers:
#     if i >max:
#         max =i
# print(max)
# print(output)



#  TUPLES

# you cant modify a tuple
# numbers= (1,2,3)



#  UNPACKING
# unpacking means extracting items and assigning it to a variable
# coordinates = (1,2,3)
# x,y,z= coordinates
# print(x,y)



#   DICTIONARY

# customer={
#     "name":"john",
#     "age" : 30,
#     "is verified" : True
# }
# customer["sex"]="male"
# print(customer.get('body type', 'muscular'))
# for x,y in customer.items():
#     print(f"[{x}] , [{y}]")



# numbers={
#     '1':'one',
#     '2':'two',
#     '3':'three',
#     '4':'four'
# }
# cmd = input("> ")
# output=''
# for i in cmd:
#     output += numbers.get(i, '!') + " "
#
# print(output)




#   EMOJI CONVERTER

message =input("> ")
words = message.split(" ")
emojis = {

    ':)' : '😊',
    '(:' : '😢',
    ';)' : '🤣'
}
output=''
for i in words:
    output += emojis.get(i, i) + " "

print(output)