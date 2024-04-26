print("Counter".center(60,'#'))
def counter(S):
    S=(S.lower()).strip()
    c1={}
    for i in S:
        if i in c1:
            c1[i]+=1
        else:
            c1[i]=1
    for ch in c1:
        print(ch,'->',c1[ch])
    return c1
s=str(input("Enter a string : "))
x=counter(s)
print(x)
print('#'*60)