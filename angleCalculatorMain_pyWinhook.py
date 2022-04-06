import pythoncom, pyWinhook #from https://download.lfd.uci.edu/pythonlibs/x6hvwk7i/pyWinhook-1.6.2-cp38-cp38-win_amd64.whl
import numpy as np
from tkinter import *
import time

point = []
top=Tk()
lab=Label(top,text='*', font=('Times','15'), fg='yellow', bg='black')

def onMouseEvent(event):
    point.append(event.Position)
    lab.master.overrideredirect(True)
    lab.master.geometry("8x8+"+str(int(event.Position[0]/1.25))+"+"+str(int(event.Position[1]/1.25)))

    lab.config(text='*')
    
    lab.pack()
    lab.update()
    if len(point)==3 :
        angle = calculateAngle(point)
        print(point)
        print("angle: ", angle)
        point.clear()
        
    return True

def calculateAngle(point):
    
    point1 = point[0]
    point2 = point[1]
    point3 = point[2]
    vector1 = np.array(point1) - np.array(point2)
    vector2 = np.array(point3) - np.array(point2)
    Lx = np.sqrt(vector1.dot(vector1))
    Ly = np.sqrt(vector2.dot(vector2))
    cosAngle = vector1.dot(vector2)/(Lx*Ly)
    angle = np.arccos(cosAngle)*180/np.pi
    # print(angle)
    
    return angle

def main():
    hm = pyWinhook.HookManager()
    hm.HookKeyboard()
    hm.MouseMiddleDown = onMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()

if __name__ == "__main__":
    print("----a tool for angle calculate----")
    print("----copyright huangbiubiu 2020----")
    main()