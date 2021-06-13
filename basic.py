#Exercise 2: Given a range of the first 10 numbers, Iterate from the start number to the end number,
# and In each iteration print the sum of the current number and previous number
# print('Printing current and previous number sum in a range(10)')
# for i in range(10):
#     if i==0:
#         print(f'Current number {i} Previous Number {i} Sum: ',i)
#     else:
#         print(f'Current number {i} Previous Number {i-1} Sum: ',i+(i-1))

#def Sumtation(num):
    # previous=0
    # for i in range(num):
    #     print(f'Current number {i} Previous Number {previous} Sum: ',i+previous)
    # previous= i   
    
#Sumtation(10)

#Exercise 3: Given a string, display only those characters which are 
# present at an even index number.

# name_ = input('What is your name: ')
# for i in range(len(name_)):
#     if i%2 != 0:
#         print(name_[i])
# name_l= [name_[i] for i in range(len(input('Name: '))) if i % 2 ==0]
# string1=''
# print(string1.join(name_l))

#Exercise 4: Given a string and an integer number n, remove 
# characters from a string starting from zero up to n and return a new string
# name_='pynative'
# intu= 2
# name_new=[name_[i] for i in range(intu+2,len(name_))]
# print(name_new)
#Given a list of numbers, return True if first and last number of a list is same
# l1=[10, 20, 30, 40, 40]

# if l1[0] == l1[len(l1)-1]:
#     print('True')
# else:
#     print('False')

#Exercise 5: Given a list of numbers, return True if first and last number of a list is same
# def Return_Same(l1):
#     if l1[0] == l1[-1]:
#         # b=True
#         return True
#     else:
#         # b=False
#         return False
#     # print(b)    
# l1=[10, 20, 30, 40, 10]
# l2=[10, 20, 30, 40, 50]

# print('this list is ',Return_Same(l1))
# print('this list is ',Return_Same(l2))

#Exercise 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5
# def inter(m1):
#     print("Given list is ", m1)
#     print("Divisible of 5 in a list")
#     m1_only=[i for i in m1 if i % 5 == 0]
#     print(*m1_only,sep="\n")

# m1=[10, 20, 33, 46, 55]
# inter(m1)

#Exercise 7: Return the count of sub-string “Emma” appears in the given string
# str = "Emma is good developer. Emma is a writer"
# keyword="Emma"

# print(f"{keyword} appears {str.count(keyword)} times.")
# import itertools
# counter = itertools.count(0)
# def Count_key(str,keyword):
#     counterr=0
#     l1=list(str.split(" "))
#     # for i in l1:
#     #     if i == keyword:
#     #         counterr=counterr+1
#     counterr=[++counterr for x in l1 if x == keyword]
#     # counterr=[(next(counter), x) for x in l1 if x == keyword]
#     # counterr=[(i, x) for i, x in enumerate(l1, 1) if i ==keyword]
#     print(f"{keyword} appears {len(counterr)} times in string length")
    
# Count_key(str,keyword)        
# name='Emma'
# str = "Emma is good developer. Emma is a writer"
# count=0
# def Count_Emma(str,name):
#     for i in str:
#         if i == name:
#             count =count+1
# # s= [++i for i in str if i==name]
# print(f'Emma word comes {s}')

#Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
    
#Exercise 9: Reverse a given number and return true if it is the same as the original number
original=102
length=len(original)
for i in range(length):
    num1=original / 10
    rem1=original % 10
    