import math
print("Hii, This Is The Standard Calculator")

while True:
    print("1.Addition       (+)\n2.Subtraction    (-)\n3.Multiplication (×)\n4.Division       (÷)\n5.Modulo         (%)\n6.Square         (x²)\n7.Square Root    (√x)\n8.Close The Program")
    num = int(input("Enter Choice : "))
    match num:
        case 1:
            n1 = int(input("Enter First Number : "))
            n2 = int(input("Enter Second Number : "))
            sum1 = n1 + n2
            print(f"Addition Of {n1} And {n2} Is :", sum1)

        case 2:
            n1 = int(input("Enter First Number : "))
            n2 = int(input("Enter Second Number : "))
            sub1 = n1 - n2
            print(f"Subtraction Of {n1} And {n2} Is :", sub1)

        case 3:
            n1 = int(input("Enter First Number : "))
            n2 = int(input("Enter Second Number : "))
            mul1 = n1 * n2
            print(f"Multiplication Of {n1} And {n2} Is :", mul1)

        case 4:
            n1 = int(input("Enter First Number : "))
            n2 = int(input("Enter Second Number : "))
            if n2 != 0:
                div1 = n1 / n2
                print(f"Division Of {n1} And {n2} Is :", div1)
            else:
                print("Error! Division By Zero Is Not Allowed")

        case 5:
            n1 = int(input("Enter First Number : "))
            n2 = int(input("Enter Second Number : "))
            if n2 != 0:
                mod1 = n1 % n2
                print(f"Modulo Of {n1} And {n2} Is :", mod1)
            else:
                print("Error! Division By Zero Is Not Allowed")

        case 6:
            n1 = int(input("Enter Number : "))
            power1 = n1 ** 2
            print(f"Square Of {n1} Is :", power1)

        case 7:
            n1 = int(input("Enter Number : "))
            sqrt1 = math.sqrt(n1)
            print(f"Square Root Of {n1} Is :", sqrt1)

        case 8:
            print("Thank You For Using Calculator")
            break
