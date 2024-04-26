def ispalandrome():
    st = str(input("Enter a string : "))
    st = st.lower()
    temp = st[-1::-1]
    if st==temp:
        return True
    else:
        return False
o=ispalandrome()
print(o)
print('#'*60)