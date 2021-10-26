import datetime
def getdate1():
    date=input(datetime.date)
    return(date)

print("Welcome to Anik's Daily Directory")
list1={1:"Academic Activities",2:"Food Consumed",3:"Procrastinating"}
inp7=getdate1()
print("Date:-",inp7)

def getdate():
    import datetime
    return datetime.datetime.now()

print("Press 1 to Lock")
print("Press 2 to retrieve")
inp1=int(input())


if inp1==1:
    for key,value in list1.items():
        print("Enter",key,"for",value)

    inp2=int(input())
    f1=open("Anik-"+list1[inp2]+".txt","a")
    print("Enter your data:-")
    inp3=input()
    f1.write("Day-"+str(inp7)+"\n"+"["+str(getdate())+"]"+"-"+inp3+"\n")
    f1.close()

elif inp1==2:
    for key,value in list1.items():
        print("Enter",key,"for",value,"\n")

    inp4=int(input())
    f2=open("Anik-"+list1[inp4]+".txt")
    contents=f2.read()
    print(contents)
    f2.close()








