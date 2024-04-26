print("Calculator".center(60,"#"))
def cal(num1,num2,str1):
    str1= str1.lower()
    str1=str1.strip()
    if str1=='add'or str1=='1':
        temp1= num1+num2
        return temp1
    elif str1=='substract'or str1=='2':
        temp2 = num1-num2
        return temp2
    elif str1=='multiply'or str1=='3':
        temp3 = num1*num2
        return temp3
    elif str1=='divide'or str1=='4':
        temp4 = num1/num2
        return temp4
    else:
        print("Error: choose from the given option.\n")
        
n1= int(input("Enter num 1 : "))
n2= int(input("Enter num 2 : "))
print("Write what you want to perform\n1.Add\t\t2.Substract\n3.Multiply\t4.Divide.")
st= str(input("Write Your choice : "))
op=cal(n1,n2,st)
print("Result : ",op)
print('#'*60)