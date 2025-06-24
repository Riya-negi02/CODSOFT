from tkinter import*
window= Tk()
window.title("Simple calculator")
window.geometry('800x200')

def calculate():
    try:
        num1= float(entry1.get())
        num2= float(entry2.get())
        operation= operation_var.get()
        result= 0
        if operation=="+":
            result= num1+num2
        elif operation=="-":
            result= num1-num2
        elif operation=="*":
            result= num1*num2 
        elif operation=="/":
            if num2!=0:
                result= num1/num2
            else:
                result_label.config(text='cannot be divided by zero')
                return

        result_label.config(text=f"Result:{result}")
    except ValueError:
        result_label.config(text=f"Result:INVALID INPUT. Enter numbers")

label1= Label(window, text="NUMBER 1:", background='lavender')
label1.config(font=("microsoft himalaya",20, "bold"))
label1.grid(row=0, column=0, padx=30, pady=15)
entry1= Entry(window)
entry1.grid(row=0, column=1, padx=30, pady=15)

label2= Label(window, text="NUMBER 2:", background='lavender')
label2.config(font=("microsoft himalaya",20, "bold"))
label2.grid(row=1, column=0, padx=30, pady=15)
entry2= Entry(window)
entry2.grid(row=1, column=1, padx=30, pady=15)


operation_var= StringVar()
operation_var.set("+")

label3= Label(window, text="Operation:", background='lavender')
label3.config(font=("microsoft himalaya",20, "bold"))
label3.grid(row=2, column=0, padx=30, pady=15)

operations_frame= Frame(window)
operations_frame.grid(row=2, column=1, padx=30, pady=15)


def set_operation(op):
    operation_var.set(op)

button_add= Button(operations_frame, text='+', command= lambda: set_operation("+"), background='cyan')
button_add.pack(side=LEFT, padx=10)

button_sub= Button(operations_frame, text='-', command= lambda: set_operation("-"),background='cyan')
button_sub.pack(side=LEFT, padx=10)

button_mul= Button(operations_frame, text='*', command= lambda: set_operation("*"),background='cyan')
button_mul.pack(side=LEFT, padx=10)

button_div= Button(operations_frame, text='/', command= lambda: set_operation("/"),background='cyan')
button_div.pack(side=LEFT, padx=10)


submit_button= Button(window, text='CALCULATE',command= calculate, background='lavender')
submit_button.config(font=("microsoft himalaya",20, "bold"))
submit_button.grid(row=3, column=0, columnspan=1, pady=30)

result_label= Label(window, text="Result:",background='lavender')
result_label.config(font=("microsoft himalaya",20, "bold"))
result_label.grid(row=4, column=0, columnspan=1, pady=30)


window.mainloop()



      
        
        
