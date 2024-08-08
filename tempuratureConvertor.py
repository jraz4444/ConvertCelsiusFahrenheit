#Ask the user to select C or F to determine what you want to convert
convert= input("Would you like to convert Fahrenheit(F) or Celsius(C)?")
if convert == "C":
    tempurature = int(input("What tempurature is it in Fahrenheit"))
    Celsius= (tempurature - 32) / 1.8
    print("The tempurature outside is: " +  str(Celsius) + " in Celsius")
elif convert == "F":
    tempurature = int(input("What tempurature is it in Celsius?"))
    Fahrenheit=(1.8 * tempurature) + 32
    print("The tempurature is " + str(Fahrenheit) + " in Fahrenheit ")
elif convert == "c":
    tempurature = int(input("What tempurature is it?"))
    Celsius= (tempurature - 32) / 1.8
    print("The tempurature outside is: " +  str(Celsius) + " in Celsius")
elif convert == "f":
    tempurature = int(input("What tempurature is it?"))
    Fahrenheit=(1.8 * tempurature) + 32
    print("The tempurature is " + str(Fahrenheit) + " in Fahrenheit")
else:
    convert= input("Would you like to convert Fahrenheit(F) or Celsius(C)?")
