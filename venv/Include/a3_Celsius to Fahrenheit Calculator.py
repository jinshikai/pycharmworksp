#Celsius to Fahrenheit Calculator:
flag=True
while flag:
    celsius_Start=int(input("Celsius Start:"))
    celsius_End=int(input("Celsius End :"))
    if(celsius_Start>celsius_End):
        print("Error: end value must be bigger than start value!")
    else:
        step_size=int(input("step size:"))
        if step_size<0:
            print("Error: step size cannot be negative!")
        else:
            print("------------------------")
            print("Celsius       Fahrenheit")
            times=int((celsius_End-celsius_Start)/step_size)
            for i in range(times):
                j=i
                celsius=j*step_size
                fahrenheit=celsius*(9/5)+32
                print("{:.1f}".format(celsius),end="      ")
                print("{:.1f}".format(fahrenheit))

            flag=False
            print("------------------------")