print("Multiplication_Table".center(60,'#'))
def multiplication_table(n):
    for i in range(1,11,1):
        print(n,"\tX\t",i,'\t=\t',n*i)

var=int(input("Enter a Number : "))
multiplication_table(var)
print('#'*60)