import tkinter as tk
from GTG_imports import *  
from GTG_Widgets import *

#! Widget Use Example
root = tk.Tk()
root.title("GTG Widget Dashboard")
root.geometry("700x600")

#* \\ Create a GTG Frame
frame = GTG.Frame(root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

#* \\ Create a GTG Label with description
label_frame = GTG.Frame(frame)
label_frame.pack(pady=5, fill="x")
label = GTG.Label(label_frame, text="Hello, GTG Widgets!", fg="white", bg="black", enable_hover=False, hover_bg="red", hover_fg="lime")
label.pack(side="left", padx=10)
label_desc = GTG.Label(label_frame, text="This is a GTG Label widget. It displays static text.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
label_desc.pack(side="left", padx=10)

#* \\ Create a GTG Button with description
button_frame = GTG.Frame(frame)
button_frame.pack(pady=5, fill="x")
button = GTG.Button(button_frame, text="Click Me", hover_bg="blue", hover_fg="white")
button.pack(side="left", padx=10)
button_desc = GTG.Label(button_frame, text="This is a GTG Button widget. It triggers an action when clicked.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
button_desc.pack(side="left", padx=10)

#* \\ Create a GTG Checkbutton with a callback and description
def on_checkbutton_change(value):
    print(f"Checkbutton value changed to: {value}")

check_frame = GTG.Frame(frame)
check_frame.pack(pady=5, fill="x")
check_var = GTG.BooleanVar(callback=on_checkbutton_change)
checkbutton = GTG.Checkbutton(check_frame, text="Check Me", variable=check_var)
checkbutton.pack(side="left", padx=10)
check_desc = GTG.Label(check_frame, text="This is a GTG Checkbutton widget. It allows toggling a boolean value.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
check_desc.pack(side="left", padx=10)

#* \\ Create a GTG Radiobutton with a callback and description
def on_radiobutton_change(value):
    print(f"Radiobutton value changed to: {value}")

radio_frame = GTG.Frame(frame)
radio_frame.pack(pady=5, fill="x")
radio_var = GTG.StringVar(value="Option1", callback=on_radiobutton_change)
radio1 = GTG.Radiobutton(radio_frame, text="Option 1", variable=radio_var, value="Option1")
radio1.pack(side="left", padx=10)
radio2 = GTG.Radiobutton(radio_frame, text="Option 2", variable=radio_var, value="Option2")
radio2.pack(side="left", padx=10)
radio_desc = GTG.Label(radio_frame, text="This is a GTG Radiobutton widget. It allows selecting one option from a set.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
radio_desc.pack(side="left", padx=10)

#* \\ Create a GTG Entry with a callback and description
def on_entry_change(value):
    print(f"Entry value changed to: {value}")

entry_frame = GTG.Frame(frame)
entry_frame.pack(pady=5, fill="x")
entry_var = GTG.StringVar(callback=on_entry_change)
entry = GTG.Entry(
        entry_frame,
        bg="lightgray",
        fg="black",
        font=("Helvetica", 14),
        borderwidth=3,
        relief="flat",
        insertbackground="red",
        highlightthickness=3,
        highlightbackground="#cccccc",
        highlightcolor="#999999",
        hover_bg="lightgray",
        hover_fg="lime",
        hover_highlightbackground="#666666",
        hover_highlightcolor="#333333",
        enable_hover=True
    )
entry.pack(side="left", padx=10)
entry_desc = GTG.Label(entry_frame, text="This is a GTG Entry widget. It allows single-line text input.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
entry_desc.pack(side="left", padx=10)

#* \\ Create a GTG Listbox with description
listbox_frame = GTG.Frame(frame)
listbox_frame.pack(pady=5, fill="x")
listbox = GTG.Listbox(listbox_frame)
listbox.pack(side="left", padx=10)
listbox.insert(0, "Item 1")
listbox.insert(1, "Item 2")
listbox.insert(2, "Item 3")
listbox_desc = GTG.Label(listbox_frame, text="This is a GTG Listbox widget. It displays a list of items.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
listbox_desc.pack(side="left", padx=10)

#* \\ Create a GTG Textbox with description
textbox_frame = GTG.Frame(frame)
textbox_frame.pack(pady=5, fill="x")
textbox = GTG.Text(textbox_frame, height=5, width=40)
textbox.pack(side="left", padx=10)
textbox_desc = GTG.Label(textbox_frame, text="This is a GTG Textbox widget. It allows multi-line text input.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
textbox_desc.pack(side="left", padx=10)

#* \\ Create a GTG Progressbar with description
progress_frame = GTG.Frame(frame)
progress_frame.pack(pady=5, fill="x")
progress = GTG.Progressbar(progress_frame)
progress.pack(side="left", padx=10)
progress_desc = GTG.Label(progress_frame, text="This is a GTG Progressbar widget. It shows the progress of a task.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
progress_desc.pack(side="left", padx=10)

#* \\ Create a GTG Canvas and draw on it with description
canvas_frame = GTG.Frame(frame)
canvas_frame.pack(pady=5, fill="x")
canvas = GTG.Canvas(canvas_frame)
canvas.pack(side="left", padx=10)
canvas.draw_rectangle(20, 20, 100, 100, fill="red")
canvas_desc = GTG.Label(canvas_frame, text="This is a GTG Canvas widget. It allows drawing shapes and graphics.", fg="black", bg="white", hover_bg="red", hover_fg="lime")
canvas_desc.pack(side="left", padx=10)

root.mainloop()

#!----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#! Example of Messagebox Pop up widget
def show_info():
    GTG.showinfo(root, "Info", "This is an info message.")

def show_error():
    GTG.showerror(root, "Error", "This is an error message.")

def show_warning():
    GTG.showwarning(root, "Warning", "This is a warning message.")

def ask_yes_no():
    result = GTG.askyesno(root, "Confirmation", "Do you want to proceed?")
    print("User clicked:", "Yes" if result else "No")

def ask_ok_cancel():
    result = GTG.askokcancel(root, "Confirmation", "Do you want to continue?")
    print("User clicked:", "OK" if result else "Cancel")

root = tk.Tk()
root.title("MessageBox Example")

#* \\ Buttons to trigger different message boxes
info_button = GTG.Button(root, text="Show Info", command=show_info)
info_button.pack(pady=10)

error_button = GTG.Button(root, text="Show Error", command=show_error)
error_button.pack(pady=10)

warning_button = GTG.Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=10)

yes_no_button = GTG.Button(root, text="Ask Yes/No", command=ask_yes_no)
yes_no_button.pack(pady=10)

ok_cancel_button = GTG.Button(root, text="Ask OK/Cancel", command=ask_ok_cancel)
ok_cancel_button.pack(pady=10)

root.mainloop()

