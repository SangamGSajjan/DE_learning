x = int(input("enter x"))
y = int(input("enter y"))
z = int(input("enter z"))

# if(x>y):
#     if(x>z):
#         print("x is grater")
#     else:
#         print("z is grater")
# elif(y>z):
#      print("y is grater")
# else:
#     print("z is grater")



if(x>y & x>z):
    print("x is grater")
elif(y>z & y>x):
     print("y is grater")
else:
    print("z is grater")