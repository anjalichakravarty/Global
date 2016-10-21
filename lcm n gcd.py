#funct declaration
def lcm_gcd(x,y):
    i=1
    while i<=x and i<=y:
        if x%i==0 and y%i==0:
            gcd=i
            i=i+1
    product=x*y
    lcm=product/gcd
    print("first num:",x)
    print("sec num:",y)
    print("lcm:", lcm)
    print("gcd:",gcd)
    return
#lcm and gcd
n1=int(input("Enter a num:"))
n2=int(input("Enter a num:"))
lcm_gcd(n1,n2)
    
