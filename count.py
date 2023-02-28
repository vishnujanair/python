x=int(input("enter your mark"))
if x>24:
    print("You have passed")
    if x>90:
        print("You have an A+")
    elif x>80 and x<90:
        print("You have an A")
    elif x>70 and x<80:
        print("You have a B")
else:
     print("Failed")
