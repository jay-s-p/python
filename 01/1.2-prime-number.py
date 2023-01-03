a = int(input("Enter no. : "))
if a <= 0:
    print("Invalid input")
    exit(1)
if a == 1:
    print("1 is not Prime")
    exit(0)

isPrime = True

i = 2
while i < a:
    if a % i == 0:
        isPrime = False
        break
    i += 1

if isPrime:
    print(a, "is prime.")
else:
    print(a, " is not prime.")
