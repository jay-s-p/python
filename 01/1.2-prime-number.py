a = int(input("Enter no. : "))
if a <= 0:
    exit("Invalid input")
if a == 1:
    exit("1 is not Prime")

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
    print(a, "is not prime.")
