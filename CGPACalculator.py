import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
main = tk.Tk()
main.title("SGPA Calculator")
sep = tk.Frame(main, height = 10)
sep.grid(sticky = 'n')
window = tk.Frame(main)
window.grid()

#Inputting the number of subjects
tk.Label(window, text = "Enter the number of subjects : ", font = ("Georgia 10 bold"), justify = "left").grid(row = 0, column = 0, sticky = 'e')
num_subjects = Combobox(window)
num_subjects['values'] = (1,2,3,4,5,6,7,8)
num_subjects.current(0)
num_subjects.grid(row = 0, column = 1)

#Inputting the number of Labs
tk.Label(window, text = "Enter the number of labs : ", font = ("Georgia 10 bold")).grid(row = 1, column = 0, sticky = 'e')
num_labs = Combobox(window)
num_labs['values'] = (0,1,2,3,4)
num_labs.current(0)
num_labs.grid(row = 1, column = 1)

#Function to clear window 
def clear_window(event):
    window.grid_remove()
    credits = []
    grades = []
    subjects = []
    labs = []
    window1 = tk.Frame(main)
    window1.grid()
    
    tk.Label(window1, text = "Courses", font = ("Georgia 10 bold")).grid(row = 0, column = 0)
    tk.Label(window1, text = "Credits", font = ("Georgia 10 bold")).grid(row = 0, column = 1)
    tk.Label(window1, text = "Grades", font = ("Georgia 10 bold")).grid(row = 0, column = 2)
    
    for i in range(int(num_subjects.get())):
        lbl = tk.Label(window1, text = "Subject_" + str(i + 1), font = ("Georgia 8 italic"))
        crdt = Combobox(window1)
        crdt['values'] = (0,1,2,3,4,5)
        crdt.current(0)
        grd = Combobox(window1)
        grd['values'] = (0,1,2,3,4,5,6,7,8,9,10)
        grd.current(0)    
        
        lbl.grid(row = i+1, column = 0)
        crdt.grid(row = i+1, column = 1)
        grd.grid(row = i+1, column = 2)
        
        subjects.append(lbl)
        credits.append(crdt)
        grades.append(grd)
        
    for i in range(int(num_subjects.get())+1,int(num_labs.get())+int(num_subjects.get())+1,1):
        lbl = tk.Label(window1, text = "      Lab_" + str(i-int(num_subjects.get())), font = ("Georgia 8 italic"))
        crdt = Combobox(window1)
        crdt['values'] = (1,2)
        crdt.current(0)
        grd = Combobox(window1)
        grd['values'] = (0,1,2,3,4,5,6,7,8,9,10)
        grd.current(0)
        
        lbl.grid(row = i, column = 0)
        crdt.grid(row = i, column = 1)
        grd.grid(row = i, column = 2)
        
        labs.append(lbl)
        credits.append(crdt)
        grades.append(grd)
        
    def get_values(event):
        credit = [int(i.get()) for i in credits]
        grade = [int(i.get()) for i in grades]
        credit = np.array(credit)
        grade = np.array(grade)
        sgpa = Calculate(credit, grade)
        messagebox.showinfo(title="Result", message="Your SGPA for this\nsememester is : " + str(round(sgpa,4)))
          
        
    cal = tk.Button(window1, text = "Calculate", font = ("Georgia 10 bold"))
    cal.bind("<Button-1>", get_values)
    cal.grid(row = int(num_labs.get())+int(num_subjects.get())+3, column = 1, sticky = 'e')

    
    
def Calculate(credit, grade):
    weighted_sum = sum(credit*grade)
    credit_sum = sum(credit)
    sgpa = weighted_sum/credit_sum
    return(sgpa)
    

#Next Button
nxt = tk.Button(window, text = "Next >>")
nxt.bind("<Button-1>", clear_window)
nxt.grid(row = 3, column = 1, sticky = 'e')
main.mainloop()
