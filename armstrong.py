//Enter the number
num = int(input('Enter the number:'))
sum=0
temp=num
//loop
while temp>0:
    digit = temp%10
    sum = sum + digit**3
    temp = temp//10
if num == sum:
    print(num,'is an armstrong number')
else :
    print(num,'is not an armstrong number')
