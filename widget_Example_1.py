import tkinter as tk
from GTG_imports import *  
from GTG_Widgets import *

#! 
# root = tk.Tk()
# root.title("GTG Widget Example")
# root.geometry("500x500")

# #* \\ Create a GTG Frame
# frame = GTG.Frame(root)
# frame.pack(pady=10, padx=10, fill="both", expand=True)

# #* \\ Create a GTG Label
# label = GTG.Label(frame, text="Hello, GTG Widgets!", fg="white", bg="black", enable_hover=False)
# label.pack(pady=5)

# #* \\ Create a GTG Button
# button = GTG.Button(frame, text="Click Me", hover_bg="blue", hover_fg="white")
# button.pack(pady=5)

# #* \\ Create a GTG Checkbutton with a callback
# def on_checkbutton_change(value):
#     print(f"Checkbutton value changed to: {value}")

# check_var = GTG.BooleanVar(callback=on_checkbutton_change)
# checkbutton = GTG.Checkbutton(frame, text="Check Me", variable=check_var)
# checkbutton.pack(pady=5)

# #* \\ Create a GTG Radiobutton with a callback
# def on_radiobutton_change(value):
#     print(f"Radiobutton value changed to: {value}")

# radio_var = GTG.StringVar(value="Option1", callback=on_radiobutton_change)
# radio1 = GTG.Radiobutton(frame, text="Option 1", variable=radio_var, value="Option1")
# radio2 = GTG.Radiobutton(frame, text="Option 2", variable=radio_var, value="Option2")
# radio1.pack(pady=2)
# radio2.pack(pady=2)

# #* \\ Create a GTG Entry with a callback
# def on_entry_change(value):
#     print(f"Entry value changed to: {value}")

# entry_var = GTG.StringVar(callback=on_entry_change)
# entry = GTG.Entry(frame, textvariable=entry_var)
# entry.pack(pady=5)

# #* \\ Create a GTG Listbox
# listbox = GTG.Listbox(frame)
# listbox.pack(pady=5)
# listbox.insert(0, "Item 1")
# listbox.insert(1, "Item 2")
# listbox.insert(2, "Item 3")

# #* \\ Create a GTG Textbox
# textbox = GTG.Text(frame, height=5, width=40)
# textbox.pack(pady=5)

# #* \\ Create a GTG Progressbar
# progress = GTG.Progressbar(frame)
# progress.pack(pady=5)

# #* \\ Create a GTG Canvas and draw on it
# canvas = GTG.Canvas(frame)
# canvas.pack(pady=5)
# canvas.draw_rectangle(20, 20, 100, 100, fill="red")

# root.mainloop() 





# #! Example Message Pop ups widget
# def show_info():
#     GTG.showinfo(root, "Info", "This is an info message.")

# def show_error():
#     GTG.showerror(root, "Error", "This is an error message.")

# def show_warning():
#     GTG.showwarning(root, "Warning", "This is a warning message.")

# def ask_yes_no():
#     result = GTG.askyesno(root, "Confirmation", "Do you want to proceed?")
#     print("User clicked:", "Yes" if result else "No")

# def ask_ok_cancel():
#     result = GTG.askokcancel(root, "Confirmation", "Do you want to continue?")
#     print("User clicked:", "OK" if result else "Cancel")

# root = tk.Tk()
# root.title("MessageBox Example")

# #* \\ Buttons to trigger different message boxes
# info_button = GTG.Button(root, text="Show Info", command=show_info)
# info_button.pack(pady=10)

# error_button = GTG.Button(root, text="Show Error", command=show_error)
# error_button.pack(pady=10)

# warning_button = GTG.Button(root, text="Show Warning", command=show_warning)
# warning_button.pack(pady=10)

# yes_no_button = GTG.Button(root, text="Ask Yes/No", command=ask_yes_no)
# yes_no_button.pack(pady=10)

# ok_cancel_button = GTG.Button(root, text="Ask OK/Cancel", command=ask_ok_cancel)
# ok_cancel_button.pack(pady=10)

# root.mainloop()
