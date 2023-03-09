operand=input("Enter operand")
x=int(input("Enter first no.:"))
y   =int(input("Enter second no.:"))
def add(x,y):
        return x+y
def diff(x,y):
        return x-y
if operand=="+":
    result1=add(x,y)
    print(result1)
else:
    result2=diff(x,y)
    print(result2)
