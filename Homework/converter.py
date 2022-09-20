# coding: utf-8

def main():
    # Input
    number = int(input("Adjon meg egy számot és egy mértékegységet (cm/inch): \n"))
    unit = input("")

    # Convert inch to cm or cm to inch (if none => error message)
    if unit == "inch":
        print(round(2.54 * number, 2), "cm")
    elif unit == "cm":
        print(round(0.393700787 * number, 2), "inch")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    main()