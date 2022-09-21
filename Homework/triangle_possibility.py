# coding: utf-8

def main():
    print("Adja meg a háromszög három oldalát cm-ben: ")
    # Input
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))

    # Output
    if a < b + c and b < a + c and c < a + b:
        print("A(z) {}, {} és {} oldalú háromszög szerkeszthető.".format(a,b,c))
    else:
        print("A(z) {}, {} és {} oldalú háromszög NEM szerkeszthető.".format(a,b,c))

if __name__ == "__main__":
    main()