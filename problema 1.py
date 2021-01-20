with open ("input.txt","r") as f:
    a=list(eval(f.readline()))
print(a)
x=sorted(a)
print(x)
x.sort(reverse=True)
print(x)
print(len(a))
print(max(a))
print(min(a))
print(a+[111])
a[2]=222
print(a)
with open('output.txt',"w") as f:
    f.write(str(a))
 

    