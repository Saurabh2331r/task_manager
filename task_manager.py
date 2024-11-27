from customtkinter import *
from tkinter import ttk
from tkinter import messagebox
import database

# ------------ FUNCTIONS -----------

def save_task():
    if titleEntry.get()==""  or deadlineEntry.get()=="":
        messagebox.showerror("Error","All Fields Are Required")
    else:
        database.insert(database.sno_count(),titleEntry.get(),categoryBox.get(),priorityBox.get(),deadlineEntry.get(),statusBox.get())
        messagebox.showinfo("Success","Data Is Inserted")
        treeview_data()
        clear()

def treeview_data():
    tasks=database.fetch_tasks()
    tree.delete(*tree.get_children())
    for task in tasks:
        tree.insert("",END,values=task)



def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    titleEntry.delete(0,END)
    categoryBox.set("Project")
    priorityBox.set("High")
    deadlineEntry.delete(0,END)
    statusBox.set("Pending")


def selection(event):
    selected_items=tree.selection()

    # print(selected_items)
    if selected_items:
        row=tree.item(selected_items)['values']
        clear()
        # print(row)
        titleEntry.insert(0,row[1])
        categoryBox.set(row[2])
        priorityBox.set(row[3])
        deadlineEntry.insert(0,row[4])
        statusBox.set(row[5])
    else:
        pass

def update_selection():
    selected_item=tree.selection()
    row=tree.item(selected_item)['values']
    return row[0]

def update():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select Data To Update")
    else:
        database.update(update_selection(),titleEntry.get(),categoryBox.get(),priorityBox.get(),deadlineEntry.get(),statusBox.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data is Updated")


def delete():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Sellect Data To Delete")
    else:
        database.delete(titleEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data is deleted")

def search():
    if searchEntry.get()=="":
        messagebox.showerror("Error","Enter value to search")
    elif searchBox.get()=="Search By":
        messagebox.showerror("Error","Please select an option")
    else:
        search_data=database.search(searchBox.get(),searchEntry.get())
        # print(search_data)
        tree.delete(*tree.get_children())
        for employee in search_data:
            tree.insert("",END,values=employee)

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')




# ------------ GUI -----------

root=CTk()


root.geometry("1000x420+50+50")
root.resizable(0,0)

root.title("Task  Manager")

root.configure(fg_color="#073D70")


# ----------- LEFT FRAME ------------

leftFrame=CTkFrame(root,fg_color="#073D70")
leftFrame.grid(row=1,column=0,padx=10,pady=20)


titleLabel=CTkLabel(leftFrame,text="Title",font=("Arial",18,"bold"))
titleLabel.grid(row=0,column=0,padx=20,pady=15,sticky="w")

titleEntry=CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
titleEntry.grid(row=0,column=1)



categoryLabel=CTkLabel(leftFrame,text="Category",font=("Arial",18,"bold"))
categoryLabel.grid(row=1,column=0,padx=20,pady=15,sticky="w")

category_options=["Project","Tutorial","Assignment","Lecture Notes","Certification"]
categoryBox=CTkComboBox(leftFrame,values=category_options,width=180,font=("Arial",15,"bold"),state="readonly")
categoryBox.grid(row=1,column=1)
categoryBox.set(category_options[0])

priorityLabel=CTkLabel(leftFrame,text="Priority",font=("Arial",18,"bold"))
priorityLabel.grid(row=2,column=0,padx=20,pady=15,sticky="w")

priority_options=["High","Medium","Low"]
priorityBox=CTkComboBox(leftFrame,values=priority_options,width=180,font=("Arial",15,"bold"),state="readonly")
priorityBox.grid(row=2,column=1)
priorityBox.set(priority_options[0])


deadlineLabel=CTkLabel(leftFrame,text="Deadline",font=("Arial",18,"bold"))
deadlineLabel.grid(row=3,column=0,padx=20,pady=15,sticky="w")

deadlineEntry=CTkEntry(leftFrame,font=("Arial",15,"bold"),width=180)
deadlineEntry.grid(row=3,column=1)

statusLabel=CTkLabel(leftFrame,text="Status",font=("Arial",18,"bold"))
statusLabel.grid(row=4,column=0,padx=20,pady=15,sticky="w")

status_options=["Pending","Completed"]
statusBox=CTkComboBox(leftFrame,values=status_options,width=180,font=("Arial",15,"bold"),state="readonly")
statusBox.grid(row=4,column=1)
statusBox.set(status_options[0])


# --------- RIGHT FRAME ------------

rightFrame=CTkFrame(root,fg_color="#073D70")
rightFrame.grid(row=1,column=1,padx=10,pady=10)

search_options=["Title","Category","Priority","Deadline","Status"]
searchBox=CTkComboBox(rightFrame,values=search_options,state="readonly")
searchBox.grid(row=0,column=0)
searchBox.set("Search By")

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text="Search",width=100,command=search,fg_color="#458dd1")
searchButton.grid(row=0,column=2)

showButton=CTkButton(rightFrame,text="Show All",width=100,command=show_all,fg_color="#458dd1")
showButton.grid(row=0,column=3,pady=5)



# ---------- TREE VIEW ---------

style=ttk.Style()
style.configure("Treeview.Heading",font=("Arial",18,"bold"))
style.configure("Treeview",font=("Arial",15,"bold"),rowheight=20,foreground="#000",bordercolor="#fff",borderwidth=2)#,fieldbackground="#000")
style.configure("Custom.Treeview")

tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree["column"]=["S.No.","Title","Category","Priority","Deadline","Status"]

tree.heading("S.No.",text="S.No.")
tree.heading("Title",text="Title")
tree.heading("Category",text="Category")
tree.heading("Priority",text="Priority")
tree.heading("Deadline",text="Deadline")
tree.heading("Status",text="Status")


tree.config(show="headings")

tree.column("S.No.",width=80)
tree.column("Title",width=100)
tree.column("Category",width=100)
tree.column("Priority",width=130)
tree.column("Deadline",width=100)
tree.column("Status",width=100)



# ----------- BUTTON FRAME ----------------

buttonFrame=CTkFrame(root,fg_color="#073D70")
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

refreshButton=CTkButton(buttonFrame,text="Refresh",font=("Arial",15,"bold"),width=160,corner_radius=15,command=lambda: clear(True),fg_color="#458dd1")
refreshButton.grid(row=0,column=0,pady=5,padx=5)

saveButton=CTkButton(buttonFrame,text="Save",font=("Arial",15,"bold"),width=160,corner_radius=15,command=save_task,fg_color="#458dd1")
saveButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text="Update",font=("Arial",15,"bold"),width=160,corner_radius=15,command=update,fg_color="#458dd1")
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text="Delete",font=("Arial",15,"bold"),width=160,corner_radius=15,command=delete,fg_color="#458dd1")
deleteButton.grid(row=0,column=3,pady=5,padx=5)


treeview_data()

tree.bind('<ButtonRelease>',selection)

database.mail_send()

root.mainloop()