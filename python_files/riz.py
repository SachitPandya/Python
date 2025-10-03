# str="hello"
# d={}
# for i in range(len(str)):
#     d[i]=str[i]
# print(d)

# str="abcabc"56
# se=set(str)
# print(se)
# se={"sam",2,3,4}
# print(se)


# ls='my name is SaCHit paNDya and my age is 21'
# ls1=ls.encode()
# print(ls1)

# import random
# random_number=random.randint(1,100)
# ctr=0
# f=1
# # n=int(input("enter the number of attempts: "))
# for i in range(100):
#     gues=(input("enter you guess "))
#     if gues==None :
#         print("enter a valid literal")
#     else:
#         guess=int(gues)
#         if guess in range(0,100):
#             if guess>random_number:
#                 print("Too High")
#                 ctr+=1
#             elif guess<random_number: 
#                 print("Too Low")
#                 ctr+=1
#             else:
#                 print("Congratulations!!! You have guessed right ")
#                 print("you have took",ctr+1,"attempts")
#                 f=0
#                 break

# if f==1:
#     print("You failed")


"""4. Write a program that generates a random number between 1 and 100. Allow the user to guess 
 the number. Provide hints such as "Too high" or "Too low" until the user guesses correctly. 
 Include the number of attempts in the output."""

# import random
# random_number=random.randint(1,100)
# ctr=0
# guess=0
# while guess!=random_number :
#     ctr+=1
#     guess=input("enter your guess: ")
#     if guess.isdecimal()!= True:
#         print("enter a valid number")
#     else:
#         guess1=int(guess)
#         if guess1>100:
#             print("enter a number between 0 to 100")
#         else:
#             if guess1>random_number:
#                 print("Too High")
#             elif guess1<random_number: 
#                 print("Too Low")
#             else:
#                 print("Congratulations!!! You have guessed right ")
#                 print("you have took",ctr,"attempts")
#                 break
import os
base_path=os.getcwd()
# file15="file15.txt"
print(base_path)

# file16_name="file17.txt"
# file_p=os.path.join(base_path,"txt_files1")
# if os.path.exists(file_p):
#     file16_path=os.path.join(file_p,file16_name)
# else:
#     folder="txt_files1"
#     dir=os.path.join(base_path,folder)
#     # dir1=os.makedirs(dir)
#     file16_path=os.path.join(base_path,folder,file16_name)
 
# with open(file16_path,"w") as file16:
#     file16.write("hello2")
import os
base_dir=os.getcwd()
print(base_dir)