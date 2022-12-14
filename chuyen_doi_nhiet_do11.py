from tkinter import *

def f_sang_c():
    fahrenheit = entry_do_f.get()
    celsius=5/9*(float(fahrenheit)-32) 
    label_result_celsius['text']=f"{round(celsius, 2)} \N{DEGREE CELSIUS}"
    
def c_sang_f():
    celsius=entry_celsius.get()
    fahrenheit= 9/5 * float(celsius)  + 32 
    label_result_fahrenheit["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"
    
window = Tk()    
window.title("  chuyendoi nhiet do ")
entry_do_f = Entry(master=window,width=10)
entry_do_f.grid(row=0,column=0)
label_do_f= Label(master=window, text="\N{DEGREE FAHRENHEIT}")
label_do_f.grid(row=0, column=1)
button_do_f = Button(master=window,text="\N{RIGHTWARDS BLACK ARROW}",command=f_sang_c)
button_do_f.grid(row=0, column=2)
label_result_celsius = Label(master=window, text="\N{DEGREE CELSIUS}")
label_result_celsius.grid(row=0, column=3)




entry_celsius=Entry(master=window,width=10 )
entry_celsius.grid(row=1,column=0)
label_celsius=Label(master=window ,text="\N{DEGREE CELSIUS}")
label_celsius.grid(row=1, column=1)

button_celsius= Button(master=window,text="\N{RIGHTWARDS BLACK ARROW}",command=c_sang_f)
button_celsius.grid(row=1, column=2)
label_result_fahrenheit = Label(master=window, text="\N{DEGREE FAHRENHEIT}")
label_result_fahrenheit.grid(row=1, column=3)



window.mainloop()



