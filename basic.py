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
name_='pynative'
intu= 2
name_new=[name_[i] for i in range(intu+2,len(name_))]
print(name_new)