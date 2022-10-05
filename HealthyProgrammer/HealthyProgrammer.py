from pygame import mixer
from datetime import datetime
from time import time
print("--------------WELCOME TO HEALTHIFY ME---------------")
now=datetime.now()
date=now.strftime("%d/%m/%y")
time_now=now.strftime("%H:%M:%S")


def log(name):
    with open(f"{name}log.txt","a")as f:
        f.write(f"["+date+time_now+"]:-"+"NOTED\n")
def music(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        i=input()
        if i==stopper:
            mixer.music.stop()
            break
if __name__ == '__main__':
    dict = {1: "START", 2: "VIEW LOGS"}
    for key, value in dict.items():
        print("PRESS", key, "to", value)
    i = int(input())
    if(i==1):
        init_water=time()
        init_eye=time()
        init_exercise=time()
        w=25*60
        e=40*60
        ex=60*60
        while True:
            if time()-init_water>w:
                print("DRINK WATER\n"
                      "Type 'drank' to stop remainder")
                music('water.mp3','drank')
                log("water")
                init_water=time()
                time_now = now.strftime("%H:%M:%S")
            if time()-init_eye>e:
                print("DO EYE EXERCISE\n"
                      "Type 'done' to stop remainder")
                music('eyes.mp3','done')
                log("eyes")
                init_eye=time()
                time_now = now.strftime("%H:%M:%S")
            if time()-init_exercise>ex:
                print("DO EXERCISE\n"
                      "Type done to stop remainder")
                music('Exercise.mp3','done')
                log("exercise")
                init_exercise=time()
                time_now = now.strftime("%H:%M:%S")

    if(i==2):
        dict1={1:"WATER LOG",2:"EYE LOG",3:"EXERCISE LOG"}
        for keys,values in dict1.items():
            print("Press",keys,"to open",values)
        inp_log=int(input())
        if(inp_log==1):
            f=open("Waterlog.txt")
            contents=f.read()
            print(contents)
        if(inp_log==2):
            f=open("eyeslog.txt")
            contents=f.read()
            print(contents)
        if(inp_log==3):
            f=open("exerciselog.txt")
            contents=f.read()
            print(contents)


