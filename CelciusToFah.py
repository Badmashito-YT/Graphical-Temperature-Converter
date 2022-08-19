from tkinter import *
root = Tk()

root.title("Animesh Temperature Converter")
root.geometry("400x400")  #width x height

def OnClick():
    fr = value1.get()
    to = value2.get()
    
    inputVal = float(e1.get())
    
    if (fr == "Celcius" and to== "Fah"):
        ans = inputVal*9/5+32
        e1.delete(0,END)
        
    elif (fr == "Fah" and to=="Celcius"):
        ans = (inputVal-32)* (5/9)
        e1.delete(0,END)
        
    elif (fr == "Celcius" and to=="Celcius"):
        ans = inputVal
        e1.delete(0,END)
        
    elif (fr == "Fah" and to=="Fah"):
        ans = inputVal
        e1.delete(0,END)
        
    else:
        Label(root,text="Invaild Input !").place(x=90, y=180)
        e1.delete(0,END)

    Label(root,text=ans).place(x=90, y=180)
    
myList1 = ["Celcius", "Fah"]
myList2 = ["Fah","Celcius"]

value1 = StringVar(root)
value1.set(myList1[0])

opt1 = OptionMenu(root,value1, *myList1)
opt1.config(width=10)
opt1.pack(side="top")

value2 = StringVar(root)
value2.set(myList2[0])

opt2 = OptionMenu(root,value2,  *myList2)
opt2.config(width=10)
opt2.pack(side="top")

#Labeling
Label(root,text="FROM").place(x=10, y=10)
Label(root,text="TO").place(x=10, y=40)
Label(root,text="Temperature").place(x=10, y=80)
Label(root,text="Answer :").place(x=10, y=180)

global e1
e1 = Entry(root,borderwidth=3)
e1.place(x=100,y=80)

myButton = Button(root,text="Calculate", command=OnClick)
myButton.place(x=90 ,y=130)

root.mainloop()
