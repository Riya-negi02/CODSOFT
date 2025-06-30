import tkinter
from tkinter import messagebox

tasks={}
task_id_calculator= 0

def add_task():
    global task_id_calculator
    task_string= task_entry.get()
    if task_string:
        tasks[task_id_calculator]= {"text": task_string, "crossed": False}
        task_id_calculator+=1
        update_task_list()
        task_entry.delete(0, tkinter.END)
    else:
        messagebox.showwarning("Input Error","Please enter a task")

def update_task_list():
    task_listbox.delete(0, tkinter.END)
    for task_id, task_info in tasks.items():
        task_text= task_info["text"]
        if task_info["crossed"]:
            display_text= "✅" + task_text
            task_listbox.insert(tkinter.END, display_text)
        else:
            display_text=task_text
            task_listbox.insert(tkinter.END, display_text)

def get_selected_task_id():
    try:
        selected_index= task_listbox.curselection()[0]
        selected_task_display= task_listbox.get(selected_index)
        original_task_text = selected_task_display.replace("✅","")
        for task_id, task_info in tasks.items():
            if task_info["text"]== original_task_text:
                return task_id
        return None
    except IndexError:
        return None
    
def delete_task():
    task_to_delete_id = get_selected_task_id()
    if task_to_delete_id is not None:
       del tasks[task_to_delete_id]
       update_task_list()
    else:
       messagebox.showwarning("Selection Error", "Please select a task to delete")

def check_task():
    task_to_check_id= get_selected_task_id()
    if task_to_check_id is not None:
        tasks[task_to_check_id]["crossed"] = True
        update_task_list()
    else:
        messagebox.showwarning("warning","Could not find selected task")
    
def uncheck_task():
    task_to_uncheck_id = get_selected_task_id()
    if task_to_uncheck_id is not None:
        tasks[task_to_uncheck_id]["crossed"] = False
        update_task_list()
    else:
        messagebox.showwarning("warning","Could not find selected task")
    

window= tkinter.Tk()
window.title("List")
window.configure(bg='beige')


label= tkinter.Label(window,text="TO-DO LIST", font=('Microdoft Himalaya',18,'bold'), bg='Lavender').pack(pady=10)
window.geometry('400x400')

input_frame= tkinter.Frame(window,bg='beige')
input_frame.pack(pady=10)

task_entry= tkinter.Entry(input_frame, width= 40, font=('Microdoft Himalaya',14),bg='lavender')
task_entry.pack(side=tkinter.TOP, pady=10)

button_frame= tkinter.Frame(window,bg='beige')
button_frame.pack(pady=10)

add_button = tkinter.Button(button_frame, text="Add Task", command=add_task, bg='cyan')
add_button.pack(side=tkinter.LEFT, padx=5)

delete_button = tkinter.Button(button_frame, text="Delete Task", command=delete_task, bg='cyan')
delete_button.pack(side=tkinter.LEFT, padx=5)

check_button = tkinter.Button(button_frame, text="cross Task", command=check_task, bg='cyan')
check_button.pack(side=tkinter.LEFT, padx=5)

uncheck_button = tkinter.Button(button_frame, text="uncross Task", command=uncheck_task, bg='cyan')
uncheck_button.pack(side=tkinter.LEFT, padx=10)

task_listbox= tkinter.Listbox(window, selectmode= tkinter.SINGLE, bg='lavender', width= 40, height= 40)
task_listbox.pack(pady=10)

window.mainloop()
