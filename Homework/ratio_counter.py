# coding: utf-8

def main():

     infinity = True # Make the cicle run forever

     while infinity == True:
         # Input
         a = int(input("Enter 'a' value: "))
         b = int(input("Enter 'b' value: "))

        # Output
         try:
             c = a / b
             print(c)
         except ZeroDivisionError: # ZeroDivisionError
             print("Division by zero not allowed.")
         # Cicle end message
         print("Out of try except blocks")

if __name__ == "__main__":
    main()