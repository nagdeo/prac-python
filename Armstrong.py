sum = 0
num = int(input("Enter the number:"))
act_no=num
while (num > 0):
    rem = num % 10
    sum = sum + (rem*rem*rem)
    num= num // 10
if act_no==sum:
    print("Armstrong")


