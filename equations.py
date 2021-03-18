def atzeret(n):
    b=1
    for i in range(n):
        b=b*(i+1)
    return b

    
def hezka(x,n):
    b=1
    for i in range(1,1+n):
        b=b*x
    return b

def absu (x):
    if x<0:
        x=x*(-1)
    return x
def Ln(x):
    if x<=0:
        return 0.0
    yn=x-1
    yn1= yn + 2*(x-exponent(yn))/(x+exponent(yn))
    while(absu(yn-yn1)>0.001):
        yn=yn1
        yn1= yn + 2*(x-exponent(yn))/(x+exponent(yn))
    return yn1
         
def exponent(x):
    expo = 1
    for n in range (1,140):
        expo = expo + hezka(x, n)/atzeret(n)
    return expo

def XtimesY(x,y):
    if x<=0 :
       return 0.0
    return exponent(y*Ln(x))

def sqrt(x,y):
    if x==0:
      return 0.0
    return XtimesY(y, 1/x)

def calculate(x):
    return exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    
print (calculate(0))


   

 
#

    
#def XtimesY (x,y):
    
#def calculet ():