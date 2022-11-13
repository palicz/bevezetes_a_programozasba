def isPalindrome(s):
    if s == s[::-1]:
        print("Palidrome")
    else:
        print("Not palidrome")

s = input("Type in your word, words or sentence: ")
ans = isPalindrome(s)