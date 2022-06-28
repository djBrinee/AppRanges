from KataRangePack import RangeClass
import os

def Menu():
    print("\t\tApp Menu options:")
    print("1. EndPoints")
    print("2. AllPoints")
    print("3. Equals")
    print("4. OverLaps\n\n")


def Main():
    Choice = input("insert the number to which option you choose: ")
    if(Choice == '1'):
        Range = input("Select your range to know its endpoints: ")
        Range = RangeClass(Range)
        if(Range.range_validation() == True):
            print("\nThe endpoints are: " + Range.endpoints())
        else:
            print("\nThe range is not valid, verify it.")

    elif(Choice == '2'):
        Range = input("Select your range to know all the points of it: ")
        Range = RangeClass(Range)
        if(Range.range_validation() == True):
            print("\n All the points are: " + Range.allPoints())
        else:
            print("\nThe range is not valid, verify it.")

    elif(Choice == '3'):
        Range1 = input("Select the first range: ")
        Range1 = RangeClass(Range1)
        Range2 = input("Select the second range: ")
        Range2 = RangeClass(Range2)

        if(Range1.range_validation() == True and Range2.range_validation() == True):
            if(Range1.Equals(Range2)):
                print("\nThese ranges are equal.")
            else:
                print("\nThese ranges are not equal")
        else:
            print("\nOne or both ranges are invalid, verify it.")

    elif(Choice == '4'):
        Range1 = input("Select the first range: ")
        Range1 = RangeClass(Range1)
        Range2 = input("Select the second range: ")
        Range2 = RangeClass(Range2)

        if(Range1.range_validation() == True and Range2.range_validation() == True):
            if(Range1.overlapsRange(Range2)):
                print("\nThese ranges overlap.")
            else:
                print("\nThese ranges don't overlap.")
        else:
            print("\nOne or both ranges are invalid, verify it.")

    else:
        print("Error, please choose one of the options (1,2,3, or 4):\t")


while True:
    print(Menu())
    print(Main())
    dec = input("\n\nDo you want to keep using the application? (y/n): ")
    if(dec == 'y'):
        os.system('CLS')
        print(Menu())
        print(Main())
    else:
        break