def Convert_Int_To_List(n):
    lst=[]
    for i in range(n):
        a=int(input("enter the element for list at "))
        lst.append(a)
    print(lst)

n=int(input("enter the size for the list:"))
Convert_Int_To_List(n)



# number = 153
# # initialize required variable
# sum = 0
# temp = number
# n = len(str(number))

# while temp > 0:
#   val = temp % 10
#   sum += val ** n
#   temp //= 10

# print("Number is: ", number)
# print("Sum is: ", sum)

# if number == sum:
#   print("{} is an Armstrong number".format(number))
# else:
#   print("{} is not an Armstrong number".format(number))

