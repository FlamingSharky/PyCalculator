from time import sleep
from playsound import playsound
playsound('slamjam.wav', False)

print("Possible Types of Calculators Include: ",'\033[1m' + 'ARITHMETIC, FINANCIAL,' + '\033[0m' + " and",'\033[1m' + 'SCIENTIFIC' + '\033[0m')
calculator = input("Choose your calculator! Calculator: ")

while calculator == "ARITHMETIC":
    print("\n")
    
    number1 = float(input("Calculator: Choose your fighter! Number: "))
    
    print("\n")

    print("Possible Arithmetic Stages Include: ", '\033[1m' + 'ADDITION' + '\033[0m' + ", " '\033[1m' + 'SUBTRACTION' + '\033[0m'+ ", " '\033[1m' + 'MULTIPLICATION' + '\033[0m'+ " and " '\033[1m' + 'DIVISION' + '\033[0m')
    
    arithmetic = input("Calculator: Choose your stage! (All Uppercase for it to work) Arithmetic: ")

    print("\n")

    number2 = float(input("Calculator: Choose your foe! Number: "))

    if arithmetic == "ADDITION":
        result = number1 + number2

    elif arithmetic == "SUBTRACTION":
        result = number1 - number2

    elif arithmetic == "MULTIPLICATION":
        result = number1 * number2

    elif arithmetic == "DIVISION":
        result = number1 + number2

    elif arithmetic != "DIVISION":
        print("Not a valid stage.")
        break
    
    print("\n")

    print("3...")
    sleep(1)
    print("2...")
    sleep(1)
    print("1...")
    sleep(1)
    print("Fight!!!")
    print("\n")
    sleep (5)
    print(f"Right from the get go Fighter {number1} gets control of the stage as he knocks Fighter {number2} off into the ledge!")
    sleep(3)
    print(f"Fighter {number2} got the perfect recovery and...")
    sleep(2)
    print(f"HE GOT THE COUNTER!!!")
    sleep(3)
    print(f"Can Fighter {number1} even make the comeback??? Nobody knows!!!")
    sleep(5)
    print(f"He did it!!! Fighter {number1} got the comeback and it seems like...")
    sleep(8)
    print(f"HE DID IT, FIGHTER {number1} GOT THE VICTORY!!!")

    print("\n")

    print("AND THE TRUE WINNER IS...")
    sleep(3)

    print(f"{result}!!!!! (That is your answer)")

    print("\n")

    stop = input("Continue?", '\033[1m' + 'Y or N' + '\033[0m')
    
    if stop == "N":
        break
