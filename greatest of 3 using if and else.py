a =int(input("a is "))
b = int(input("b is "))
c = int(input("c is "))
if a==b:
    if a==c:
        print("all are equal")
if a==b and a!=c:
    print("a and b are equal")
if a==c and a!=b:
    print("a and c are equal")
if b==c and b!=a:
    print("b and c are euqal")               
if a>b:
    if a>c:
        print("a is max")
    else:
        print("c is max")
if b>a:
    if b>=c:
        print("b is max")
if c>b:
    if c>a:
        print("c is max")               