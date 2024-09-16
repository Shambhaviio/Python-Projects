#Program to identify prime numbers

n = int(input("Enter the number you wish to check."))

flag = False

def prime(n):
    for i in range(2,n):
        if n%i==0:
            flag = False

            break
        else:
            flag = True
        
    if flag == True:
        print("It is a prime.")
    else: 
        print("It is not a prime")


prime(n)

