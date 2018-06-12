print("Jonathan's calculator")
data = int
x = int(input("Enter a number: "))
op = input(":")
y = int(input("Enter a number: "))
if(op == "+"):
	z = x + y

if(op == "-"):
	z = x - y

if(op == "*"):
	z = x * y

if(op == "/"):
	z = x / y

print(z)