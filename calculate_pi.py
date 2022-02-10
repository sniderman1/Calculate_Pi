import time

print()
print("Chose which equation you would like to calulate pi with")
equationUse = input("0 = Infinite Series and 1 = Nilakantha Series")
print()

num2 = 1
num3 = 1
num4 = 2
estPI = 1
pi = 0

rangeNum = input("How many times would you like to loop equation? ")
print()

if int(equationUse) == 0:
    print("Infinite Series")
    time.sleep(2)
    print("Here we go!")
    time.sleep(1)
    for i in range(0,int(rangeNum)):
        num2 = num2 + 2
        if i%2 == 0:
            # print(estPI, ' - (1/', num2, ')') 
            estPI = (estPI - (1/num2))
            pi = estPI*4
            # print("Pi = ", pi)
        else:
            # print(estPI, ' + (1/', num2, ')') 
            estPI = (estPI + (1/num2))
            pi = estPI*4
            # print("Pi = ", pi)
        print(pi)
if int(equationUse) == 1:
    print("Nilakantha Series")
    time.sleep(2)
    print("Here we go!")
    time.sleep(1)
    estPI = 3
    num2 = 0
    for i in range(0, int(rangeNum)):
        num2 = num2 + 2
        num3 = num3 + 2
        num4 = num4 + 2
        if i%2 == 0:
            estPI = estPI + (4/(num2*num3*num4))
            # print(estPI, " + (4/(", num2, "*", num3, "*", num4,")")
        else:
            estPI = estPI - (4/(num2*num3*num4))
            # print(estPI, " - (4/(", num2, "*", num3, "*", num4,")")
        pi = estPI
        print(pi)
else:
    print(equationUse, " is an invaled input. Please restart program.")