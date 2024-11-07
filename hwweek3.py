a= int(input("Give me a start number "))
b=int(input("Give me an endpoint "))
c=int(input("Give me a step number "))


if a<b:
    for i in range(a, b + 1, c):
        print(i, end=" ")
elif a>b:
    for i in range(a, b - 1, -c):
        print(i, end=" ")