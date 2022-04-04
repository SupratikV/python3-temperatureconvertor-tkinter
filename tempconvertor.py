#Celcius:
#(0°C × 9/5) + 32 = 32°F
#0°C + 273.15 = 273.15K
#Farenheit:
#(0°F − 32) × 5/9 = -17.78°C
#(0°F − 32) × 5/9 + 273.15 = 255.372K
#Kelvin:
#0K − 273.15 = -273.1°C
#(0K − 273.15) × 9/5 + 32 = -459.7°F
import tkinter as tk
 
OptionList1 = ["Celcius","Kelvin","Farenheit"]
OptionList2 = ["Celcius","Kelvin","Farenheit"]
def conv():
    fr = variable.get()
    to = variable1.get()
    ans = float(e1.get())
    if (fr==to):
        tot=ans
    elif (fr == "Celcius"):
        if to=='Farenheit':
            tot=(ans * 9/5) + 32
        else:
            tot=ans+ 273.15 
    elif (fr =='Farenheit' ):
        if to=="Celcius":
            tot=(ans-32) * 5/9
        else:
            tot=(ans-32) * 5/9 + 273.15
    elif (fr == "Kelvin"):
        if to=='Farenheit':
            tot=(ans-273.15) * 9/5 + 32
        else:
            tot= ans-273.15       
    nsalText.set(tot)
root = tk.Tk()
root.geometry('300x200')
root.title("Temperature Converver System Python")
 
variable = tk.StringVar(root)
variable.set(OptionList1[0])
 
opt = tk.OptionMenu(root, variable, *OptionList1)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side="top")
 
variable1 = tk.StringVar(root)
variable1.set(OptionList2[0])
 
opt = tk.OptionMenu(root, variable1, *OptionList2)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side="top")
 
global e1
global nsalText
nsalText = tk.StringVar()
labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")
 
 
tk.Label(root, text="From").place(x=10, y=10)
tk.Label(root, text="To").place(x=10, y=40)
tk.Label(root, text="Amount").place(x=10, y=80)
 
tk.Label(root, text="RESULT:").place(x=10, y=150)
tk.Label(root, text="", font=('Helvetica', 12), fg='red' , textvariable=nsalText).place(x=100, y=150)
tk.Button(root, text="Convert!", command=conv ,height = 1, width = 7).place(x=100, y=110)
 
e1 = tk.Entry(root)
e1.place(x=80, y=80)
 
root.mainloop()
