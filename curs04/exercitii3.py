s = input("Scrie un string ")
n = input("Scrie un numar ")

if n.isdigit() and (n := int(n)) and n <= len(s):
    s = s[n:]
    print(s)



