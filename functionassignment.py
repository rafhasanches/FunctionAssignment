from math import pi

def main() :

    radius = float(input("Enter the radius of the circle: "))
    money = float(input("Enter the money: "))
    tax = float(input("Enter the tax: "))
    fahrenheit = float(input("Enter the fahrenheit: "))

    result1 = areaCircle(radius)
    print (result1)

    result2 = totalDue(money, tax)
    print (result2)

    result3 = celsius(fahrenheit)
    print(result3)

def areaCircle(radius):
    area = pi * radius ** 2
    return area

def totalDue(money, tax):
    total = money + (money * (tax/100))
    return total

def celsius(fahrenheit):
    degree = (fahrenheit - 32) / 1.8
    return degree
main()
