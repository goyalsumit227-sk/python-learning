n = int(input("Enter a number: "))
i=2

if n <= 1:
    print(n,"is not a prime number")
        
while n > 2 and i <n :
    if n%i == 0:

        print(n,"is not a prime number")
        i+=1
      
      

else:
    print(n,"is a prime number")