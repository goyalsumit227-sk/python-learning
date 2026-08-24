n = int(input("Enter a number: "))   #58392
last_digit = n % 10     #2
new_no = n//10          #5839

total = last_digit          #2

while new_no > 0:
    last_digit = new_no % 10                #9
    new_no = new_no // 10                   #583

    total = total + last_digit                 #0+9=9
print("the sum of digits is:", total)