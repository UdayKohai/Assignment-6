print("Right_Triangle".center(60,'#'))
def right_triangle(n):
    i=1
    for i in range(1,n+1,1):
        print('*'*i)

n=int(input("Enter Size of Triangle : "))
right_triangle(n)