from GTG_Widgets import GTG
from GTG_DateTime_Module import *
from GTG_imports import *
from GTG_Extended_Widgets import FileDialog , SidePanel , Tooltip


# #!------------ || Hover Tooltip Widget Example ||----------------------
# root = tk.Tk()
# root.title("Tooltip Example")
# root.geometry("300x200")

# button = GTG.Button(root, text="Hover over me!")
# button.pack(pady=20)

# # \\ Attach a tooltip to the button
# tooltip = GT.Tooltip(
#     button,
#     text="This is a tooltip!",
#     delay=500,  # \\ Tooltip appears after 500ms
#     bg="#ffffe0",  # \\ Light yellow background
#     fg="black",  # \\ Black text
#     font=("Arial", 10),  # \\ Font style and size
#     borderwidth=1,  # \\ Border width
#     relief="solid"  # \\ Border style
# )

# entry = GTG.Entry(root)
# entry.pack(pady=20)

# # \\ Attach a tooltip to the entry widget
# entry_tooltip = GT.Tooltip(
#     entry,
#     text="Enter some text here.",
#     bg="lightblue",
#     fg="white",
#     font=("Arial", 12, "bold")
# )

# root.mainloop() 


#!------------ || Side Panel Widget Example ||----------------------

# root = tk.Tk()
# root.title("Side Panel Example")
# root.geometry("800x600")

# side_panel = SidePanel(root, width=200, height=500,bg="lightgray", open_state=True ,)
# side_panel._build()  #* \\ Build the side panel and its toggle button 


# #* \\ Example: Add a GTG.label to the side panel
# label = GTG.Label(side_panel.panel, text="This is a side panel", bg="lightgray")
# label.pack(pady=100)

# #* \\ Example: Create and Add GTG.Listbox widget to side panel
# listbox = GTG.Listbox(side_panel.panel)
# listbox.pack(pady=5)
# listbox.insert(0, "Item 1")
# listbox.insert(1, "Item 2")
# listbox.insert(2, "Item 3")


# #* \\ Example: Add a button to the side panel
# button = GTG.Button(side_panel.panel, text="Click Me", bg="white")
# button.pack(pady=10) 

# root.mainloop() 


# #!------------ || Paned Window Widget Example ||----------------------

# root = tk.Tk()
# root.geometry("400x300")

# #* \\ Example: Create and Pack PanedWindow to a tkinter window
# paned_window = GTG.PanedWindow(root, sash_color="blue", hover_sash_color="red", orientation="vertical")
# paned_window.pack(fill=tk.BOTH, expand=True)

# #* \\ Example: Add panes
# frame1 = GTG.Frame(paned_window, bg="lightblue")
# frame2 = GTG.Frame(paned_window, bg="lightgreen")
# frame3 = GTG.Frame(paned_window, bg="lightcoral")
# #* \\ Build function for panes
# paned_window.add_pane(frame1)
# paned_window.add_pane(frame2)
# paned_window.add_pane(frame3)

# #* \\ Example: Add some widgets to the frames
# label1 = GTG.Label(frame1, text="Test Text 1", font=("Arial", 14))
# label1.pack(pady=20)

# label2 = GTG.Label(frame2, text="Test Text 2", font=("Arial", 14))
# label2.pack(pady=20)

# label3 = GTG.Label(frame3, text="Test Text 3", font=("Arial", 14))
# label3.pack(pady=20)

# root.mainloop() 

#!-------------------------------------------------------------------------------------------------

#! CustomFile Dialog example 
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

def open_file_dialog():
    # Open the CustomFileDialog when the button is clicked
    dialog = FileDialog(root)
    root.wait_window(dialog)  # Wait until the dialog is closed before proceeding
    
    file_path = dialog.get_file_path()
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")

# Create a button in the main window to open the file dialog
open_button = tk.Button(root, text="Open File Dialog", command=open_file_dialog)
open_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
