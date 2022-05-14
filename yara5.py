bin_num=[]
inp=int(input("Enter the number :"))
y=inp
while y != 0 :
    x=y%2
    bin_num.append(x)
    y=y//2
bin_num.reverse()
w=" "
for i  in bin_num:
    w=w +str(1)
print(w)
