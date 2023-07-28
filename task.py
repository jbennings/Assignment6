# author:
# date:
# purpose: Miles Per Gallon

# input

isErrorGallon = True
isErrorMile = True

while isErrorMile:
    try:
        miles = float(input("Please enter miles driven: "))
        if miles >= 0:
            isErrorMile = False
    except:
        isErrorMile = True

while isErrorMile:
    try:
        gallons = float(input("Please enter gallons used: "))
        if gallons >= 0:
            isErrorGallon = False
    except:
        isErrorGallon = True


# calculation
MPG = miles / gallons


# output
print("Miles =", miles, "\nGallons =", gallons, "\nMiles Per Gallon=", MPG)
