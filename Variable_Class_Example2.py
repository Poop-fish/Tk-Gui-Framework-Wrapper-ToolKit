import tkinter as tk
from GTG_imports import *  
from GTG_Widgets import *
from tkinter import ttk



#! String And Boolean Variable Example
def on_string_change(new_value):
    print(f"StringVar changed to: {new_value}")

def on_boolean_change(new_value):
    print(f"BooleanVar changed to: {new_value}")

root = tk.Tk()

#* \\ Create a StringVar with a callback
string_var = GTG.StringVar(value="Hello", callback=on_string_change)
entry = GTG.Entry(root)
string_var.bind_to_widget(entry)  #*  \\ Bind Var to an Entry widget
entry.pack()

#* \\ Create a BooleanVar with a callback \\
boolean_var = GTG.BooleanVar(value=False, callback=on_boolean_change)
checkbutton = GTG.Checkbutton(root, text="Check me")
boolean_var.bind_to_widget(checkbutton)  #* \\ Bind Var to a Checkbutton widget
checkbutton.pack()

root.mainloop() 

#!---------------------------------------------------------------------------------------------------------------

#! \\ List , file , DateTime Variables Example //

def list_changed_callback(new_value):
    print(f"List updated: {new_value}")


def file_changed_callback(new_value):
    print(f"Selected file: {new_value}")


def datetime_changed_callback(new_value):
    print(f"Updated datetime: {new_value}")

root = tk.Tk()
root.title("ListVar Example")

#* \\ Create a ListVar instance
list_var = GTG.ListVar(value=["Apple", "Banana"], callback=list_changed_callback)

#* \\ Label to display the list
label = GTG.Label(root, text="List: ")
label.pack(pady=10)

#* \\ Bind the ListVar to the Label
list_var.bind_to_widget(label)

#* \\ Function to add an item to the list
def add_item():
    item = entry.get()
    if item:
        list_var.append(item)
        entry.delete(0, tk.END)

#* \\ Function to remove an item from the list
def remove_item():
    item = entry.get()
    if item:
        list_var.remove(item)
        entry.delete(0, tk.END)

#* \\ Entry widget for user input
entry = GTG.Entry(root)
entry.pack(pady=10)

#* \\ buttons to add/remove items
add_button = GTG.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=5)

remove_button = GTG.Button(root, text="Remove Item", command=remove_item)
remove_button.pack(pady=5)
file_var = GTG.FileVar(callback=file_changed_callback)

#* \\ Label to display the selected file path
label = GTG.Label(root, text="Selected File: ")
label.pack(pady=10)
file_var.bind_to_widget(label) # \\ Bind the FileVar to the Label

#* \\ Function to open a file dialog and set the selected file path
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        file_var.set_value(file_path)

#* \\ Button to open the file dialog
select_button = GTG.Button(root, text="Select File", command=select_file)
select_button.pack(pady=10)


#* \\ DateTimeVar instance
datetime_var = GTG.DateTimeVar(callback=datetime_changed_callback)

#* \\ Label to display the current date and time
label = GTG.Label(root, text="Current Datetime: ")
label.pack(pady=10)
datetime_var.bind_to_widget(label) #* \\ Bind the DateTimeVar to the Label

#* \\ Function to update the date and time
def update_datetime():
    new_datetime = GTGDateTime.now()
    datetime_var.set_value(new_datetime)

#* \\ Create a Button to update the date and time
update_button = GTG.Button(root, text="Update Datetime", command=update_datetime)
update_button.pack(pady=10)

root.mainloop() 


#!------------------------------------------------------------------------------------------------------------------------------


# !Color pick Variable use case 

#* \\ Callback function to be triggered when the ColorVar changes
def color_changed_callback(new_value):
    print(f"Selected color: {new_value}")

root = tk.Tk()
root.title("ColorVar with CustomColorPicker Example")

color_var = GTG.ColorVar(callback=color_changed_callback)

label = GTG.Label(root, text="Selected Color: ")
label.pack(pady=10)

#* \\ Bind the ColorVar to the Label
color_var.bind_to_widget(label)

#* \\ CustomColorPicker instance
color_picker = CustomColorPicker(color_var.set_value)

def open_color_picker():
    color_picker.open_picker()

select_button = GTG.Button(root, text="Pick Color", command=open_color_picker)
select_button.pack(pady=10)
root.mainloop() 



#!------------------------------------------------------------------------------------------------------------------------------

#! datetime Variable Use Case
if __name__ == "__main__":
    root = tk.Tk()

    # Create a DateTimeVar with the current time
    dt_var = GTG.DateTimeVar()

    # Bind it to a Label
    label = GTG.Label(root, text="Current Date and Time:")
    label.pack()
    dt_var.bind_to_widget(label)

    # Update the value after 1 second
    def update_time():
        dt_var.set_value(GTGDateTime.now())
        root.after(1000, update_time)  # Schedule the next update

    update_time()  # Start the update loop

    root.mainloop()
