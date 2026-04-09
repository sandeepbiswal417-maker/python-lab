num = int(input("Enter a number: "))

fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial =", fact)


n = int(input("Enter a number: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)


num = int(input("Enter a number: "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number =", rev)


num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
