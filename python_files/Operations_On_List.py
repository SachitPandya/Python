Rizwan=["Yess is a 2","Ji humne batting me momentum unhe dediya","bowling me unhone momentum  humse leliya"]
# # print("Lst->",List)
Virat=["Shamm tk khelenge",976,True]
# # print(len(List))
# # print(List[0:2])
# # print(Virat[:2])
# # print()
# # print()
# # if "Yss" in List:
# #     print("jii Definately")
# # else:
# #     print("Jii Dekhiye Planning to thi hamare pass bss exeute nhi ho payi ")
# # print()
Rohit=["koi bhi garden me nhi ghumega","Bhagg pujji Bhagg","Kya bolu yr me ab","ye bhi achi h isme bhi koi kammi nhi h"]
# Rohit[1:4]=["Ro-hitman sharma","Vha humne vo kra tha na isiliyee"]
# # print(Rohit)
# Virat.insert(1,"ye Hari Patti pr fekk bss")
# # print(Virat)
# Virat.insert(1,"ye Hari Patti pr fekk bss")
# Rizwan.append("ye aagya range me")
# # print(Rizwan)

Rohit.extend(Virat)
# print(Rohit)
# Virat.remove("ye Hari Patti pr fekk bss")
# Virat.remove(9876)
# print(Virat)
# Virat.pop(2)
# print(Virat)
 


# a=[1,2,43,5,6,75]
# b=[2.43,6,5,6]
# c = [*a, *b]
# print(c)
# a.reverse()
# print(a)

# for item in b:
#     if item in a:
#         a.remove(item)

# print(a)


# list=[2,3,45,6,8]
# mus=1
# for item in list:
#     mus = mus * item
# print(mus)


#max item
list23=[2,3,45,6,8]
# mus=list[0]
# for item in range(0,len(list)):
#     if list[item]>mus :
#         mus=list[item]
# print(mus)

# a=max(list)
# print(a)
# list=[1,2,3,(4,5),6]

# print(type(list[3]))
# print(list[3][1])
# a=list[3][1]

# list[1]=998
# print(list)

# list[3][1]=300
# print(list)


#minimum item
# mini=list[0]
# for i in range(0,len(list)):
#     if mini>list[i]:
#         mini=list[i]

# print(mini)


#list items start and end with same char
# los=["aba","car","aba"]
# ctr=0
# for word in los:
#     if len(word) > 1 and word[0]==word[-1]:
#         ctr+=1
# print(ctr)

#remove duplicates
# 
# for i in range (len(listu)-1):
#     for j in range(0,i):
#         if listu[j]^listu[i]==0:
#             listu.pop(i)

            
# print(listu)
# listu1 = set(listu)
# listu=list(listu1)
# print(listu,type(listu))

#find strings larger than len of n

rishab=["spider man","27 cr","car accident","come on ash...come on ash"]
# ris=[]
# n=int(input("enter value of len of string:"))
# for item in rishab:
#     if len(item)>n:
#         ris.append(item)
# print(ris)
    

# a=[]
# if len(a)==0:
#     print("list is empty")
# a=rishab
# print(a)


#common elements in 2 lists
lis1=[2,3,4,5,6,8]
lis2=[3,4,8,7]
# f=0
# lis3=[]
# for i in lis1:
#     for j in lis2:
#         if i==j:
#             lis3.append(i)
#         else:
#             f=0

# print(lis3)

#Deleting items from specific indexes
# list3=list(input("Enter the indexes you want to be deleted from list : "))

# for i in range(len(lis1)):
#     for j in range(len(list3)):
#         if i == j:
#             lis1.pop(i)
#         else:
#             pass
# print(lis1)

#removing even numbers 
# lis1=[2,3,4,5,6,8]
# for i in range(len(lis1)-1,-1,-1):
#     if lis1[i]%2==0:
#         lis1.pop(i)
# print(lis1)


#print first 5 last 5 of a squared list
# sq_list=[]
# square=1
# for sq in range(1,31):
#     if sq < 6 or sq > 25:
#         square=sq*sq
#         sq_list.append(square)

# print(sq_list)
    

#if all numbers are prime in a list
# lis1=[1,3,5,7]
# for p in lis1:
#     if p<2:
#         f=0
#     else:
#         for i in range(2,p):
#             if p%i==0:
#                 f=1
#                 break
#             else:
#                 f=0

# if f==0:
#     print("True")
# else:
#     print("False")

# from random import shuffle
# shuffle(Rizwan)
# print(Rizwan)


# str1=str(lis1)
# print(type(str1),str1)


lis1=[2,3,4,5,6,8]
lis2=[3,4,8,7]
lis3=[]
for l1 in range(len(lis1)):
    for l2 in range(len(lis2)):
        if lis1[l1] != lis2[l2]:
            lis3.append(lis1[l1])
            
lis3=set(lis3)
lis3=list(lis3)
print(lis3)

l3=lis3.index(2)
print(l3)

list=[1,2,3,4]
for i in list:
    del i
    print(i)



a=[1,2,3,4,4,5,6,7,1,5]
print(a)
d={}
for i in a :
    for j in a:
        if i==j:
            mini=i-j
            d[a[i]]=mini



sa=[x for x in a if x%2==0]
print(sa)



a=1
b=2
a==b


lst=["Virat","Rohit","Shubhman"]
for i,name in enumerate(lst):
    print(i,name)