max1=-1
max2=-1
idi1=-1
idi2=-1
n=int(input("enter no of students"))
if n<2:
    print("please enter no greater than one")
else:
    for i in range (1,n+1):
        idi: int(input("enter id no."))
        aver: float(input("enter avrage"))
        if aver > max1:
            idi2=idi1
            max2=max1
            max1=aver
            idi1=idi
        else:
            if aver>max2:
                max2=aver
                idi2=idi
    print("max2=",max2,"\t", "idi2=", idi2)
             
            
        
