#******************Functions*************************************
#Write a function to find the no. of digits in a number
print("*********Number of digits in a number***********")

def digits(n):
    return len(str(n))

print(f"digits(123456):{digits(123456)}")
print("\n")


#******************************************************************
# Write a function to find the no. of words in a sentence
print("*********Number of words in a sentence************")

def words(string):
    string2 = string.replace('.','').split(" ")
    return len(string2)


sentence = "Eesha loves chocolates. Her passion is to become a chocolatier"
print(sentence)
print(f"No. of words in the above sentence is {words(sentence)}")
print("\n")



#*********************************************************************
# Write a function to find the biggest of 2 numbers
print("********Biggest of 2 numbers**********************")

def big(x,y):
    "Find the biggest of 2 numbers x, y"
    if x>y:
        return x
    else:
        return y

print(f"big(6,7): {big(6,7)}")
print('\n')



#************************************************************************
# Write a function to find the biggest of 3 numbers
print("***********Biggest of 3 numbers****************")

def large(a,b,c):
    "Find the largest of 3 numbers"
    if a>b:
        if a>c:
            return a
        else:
            return c
    elif b>c:
         return b
    else:
        return c
    
print(f"largest among 23,-4,37 :{ large(23,-4,37) }")
print('\n')


#*************************************************************************
# Write a function to print a table using for loop
print("**********Table*************")

def tables(n):
    for i in range(1,n+1):
        row = []

        for j in range(1,n+1):
            q = f"{str(i*j):3}"
            row.append(q)

        print(" ".join(row)) #join all the elements in row using space and print row
        
tables(5)
print('\n')



#***************************************************************************
""""Write a function fizzbizz that takes a number n as input using for and if loops.
    It should print numbers from 1 to n with the following rules.
    1. if it's a multiple of 3, it should print fizz

    2.if its's a multiple of 5, it should print bizz

    3.if its a multiple of 15, it should print fizzbizz

    4.Otherwise it should just print the number"""

print("********FizzBizz**********")

def fizzbizz(n):
    for i in range(1,n+1):
        if i%15==0: 
            print("fizzbizz")
        elif i%5==0:
            print("bizz")
        elif i%3==0:
            print("fizz")
        else:
            print(i)


fizzbizz(30)
print("\n\n")



#***********************************************************************
""""Write a program biggest which will return the largest among 
    a list of numbers.
    e.g. biggest2([1,5,9,20,7,-5,23,4,12]) will return 23"""
print("*************Largest among a list of numbers*******************")

def biggest(l):
    temp = l[0]
    for i in l[1: ]:
        if i > temp:
            temp = i

    return temp

print(f"biggest([1,5,9,20,7,-5,23,4,12]):{biggest([1,5,9,20,7,-5,23,4,12])}")
print("\n")



#*************************************************************************
"""Write a function called "freq" which will take a string 's' as input and return a
   dictionary that contains the number of times each letter occurs in s""" 

print("*********Count of occurances of each letters in a string********** ")

def freq(string):
    string = string.lower().replace(" ", '')
    count = {}
    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
    "Method1 - Using count.items"
    for key, value in count.items():    # Either use 'for loop' having 'count.items()' or use 'count', to print dictionary (keys and values)
        print(key, ':', value)
        
    print("\n\n")

    "Method2 - Using count"
    for key in count:
        print(key, ':', count[key])
             

freq("Peter piper picked a peck of pickled pepper")
