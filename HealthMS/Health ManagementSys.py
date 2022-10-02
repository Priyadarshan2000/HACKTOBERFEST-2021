list1={1:"Anik",2:"Harry",3:"Hammad"}
list2={1:"Exercise",2:"Food"}
def getdate():
    import datetime
    return datetime.datetime.now()

print(list1)
for key,value in list1.items():
    print("Enter",key,"for",value,"\n",end="")

inp1=int(input())
print("Selected Client:-",list1[inp1])

print("Press 1 for Lock")
print("Press 2 for Retrieve")
inp2=int(input())


if inp2==1:
    for key,option in list2.items():
        print("Enter",key,"for",option,"\n",end="")

    inp3=int(input())
    f1=open(list1[inp1]+"-"+list2[inp3]+".txt","a")
    inp4=input()
    f1.write("["+str(getdate())+"]"+":-"+inp4+"\n")
    f1.close()
elif inp2==2:
    for key,option in list2.items():
        print("Enter",key,"for",option,"\n",end="")

    inp5=int(input())
    f1 = open(list1[inp1] + "-" + list2[inp5] + ".txt")
    contents=f1.read()
    print(contents)
    f1.close()












