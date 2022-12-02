t=0
print("**********Products**********")
print("1.tomato  2.potato  3.onion")
print("4.pepper  5.lettuce 4.lemon")
print("****************************")
print("Press - to finish procces")
f=open("receipt.txt","w")
f.write("PRODUCT     KG     PRİCE     COST"+"\n")
while True:
    x=input("Enter kg: ")
    if(x=="-"):
        break
    y=int(input("Enter price: "))
    z=int(input("Choice a product: "))
    if(z==1):
        b="TOMATO"
    elif(z==2):
        b="POTATO"
    elif(z==3):
        b="ONION"
    elif(z==4):
        b="PEPPER"
    elif(z==5):
        b="LETTUCE"
    elif(z==6):
        b="LEMON"
    else:
        print("WRONG KEY")
        continue
    f.write(b)
    c=" "*(12-len(b))
    f.write(c)
    f.write(x)
    d=" "*(7-len(str(x)))
    f.write(d)
    f.write(str(y))
    e=" "*(10-len(str(y)))
    f.write(e)       
    f.write(str(int(x)*y)+"\n")
    t=t+(int(x)*int(y))
f.write("TOTAL AMOUNT:"+str(t))
f.close()

f=open("receipt.txt","r")
for line in f:
    print(line)
f.close()
    
        
    
