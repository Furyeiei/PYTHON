import sys

while True:
     pwd=input("input password  ")
     if pwd !="skw":
         print("Incorrect password try again pls: ")
     else:
        print("Correct Password Ready to Execute \n")
        while True:
            volt = float(input("enter volt  "))
            amp = float(input("enter amp  "))
            watt = volt * amp
            print(watt)
            chk=input("Press E to Exit or Enter to continue:  ")
            if((chk=='E') or (chk=='e')):
             sys.exit()
