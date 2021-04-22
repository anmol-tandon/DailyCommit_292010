# 21/04/2021
print("hello"=="hello")  # Boolean, here it returns True
print("Ani">"Andy")  # True as A-A compared first then n-n and now i>d, therefore Ani>Andy

# Lists
number=3
things=["string",0,[1,2,number],4.56]  # can include several different types in Lists
print(things[1])  # 0
print(things[2])  # [1,2,3]
print(things[2][2])  # 3

# 2D lists
m=[[1,2,3],[4,5,6]]
print(m[1][1])  #gives 5 as output

# Functions there in lists
n=[1,2,3]
n.append(4)
print(len(n))
print(n.index(1))
print(max(n))
n.reverse()
print(n)

# While loop
x=1
while x<10:
    if x%2==0:
        print(str(x)+ "is even")
    else:
        print(str(x)+"is odd")
    x+=1

# for loop and range
for i in range(2,11,2):
    print("Even numbers are"+str(i))


