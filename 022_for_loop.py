start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("Even numbers between", start, "and", end, "are:")
for number in range(start, end + 1):
    if number % 2 ==0:
        print(number)
