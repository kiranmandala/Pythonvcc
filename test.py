from cgi import test


print ("test")
x=1
y=2
z=3

def do_addition(x,y,z):
    if x==1:
        print(y)
    else:
        print(z)

do_addition(x, y, z)