print("1. for simple interest")
print("2. for compound interest")

ch = input("enter choice")

if ch == "1":
    p = input('The principal')
    t = input('The time period')
    r = input('The rate of interest')

    si = p*(1+(r*t))

    print('The Simple Interest is', si)

elif ch == "2":
    p = input('The principal')
    t = input('The time period')
    r = input('The rate of interest')
    Amount = p * (pow((1 + r / 100), ))
    CI = Amount - p
    print("Compound interest is", CI)

else:
    print("Wrong Choice!")
