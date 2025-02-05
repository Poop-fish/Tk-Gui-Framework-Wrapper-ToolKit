from GTG_Widgets import GTG 
from GTG_DateTime_Module import *
from GTG_imports import *
from GTG_Extended_Widgets import SidePanel 
from GTG_iterables import GTG_range , GTG_string


#! ----------------------- Text Editor Example -----------------------------------------------------

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("GTG NotePad")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        # \\ Create the notebook for tabbed interface
        self.notebook = GTG.Notebook(root, enable_hover=True, hover_background="red", 
                            default_background="gray", foreground="black", font=("Arial", 12))
        self.notebook.pack(expand=True, fill="both")

        # \\ Add a default tab
        self.add_tab("Untitled")

        # \\ Create the menu bar
        self.menu_bar = GTG.Menu(root)
        self.root.configure(menu=self.menu_bar)

        # \\ File menu
        file_menu = GTG.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # \\ Edit menu
        edit_menu = GTG.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Clear", command=self.clear_text)

        # \\ Format menu
        format_menu = GTG.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Bold", command=self.toggle_bold)
        format_menu.add_command(label="Font Size", command=self.change_font_size)

    def add_tab(self, title):
        """Add a new tab to the notebook."""
        frame = GTG.Frame(self.notebook , bg="lime",  relief="groove")
        text_area = GTG.Text(frame,insertbackground="yellow", fg="lime", bg="black",wrap="word", font=("Arial", 12) , highlightbackground="pink", highlightcolor="pink", highlightthickness=20)
        text_area.pack(fill=tk.BOTH, expand=True)
        self.notebook.add(frame, text=title)
        self.notebook.select(frame)  # \\ Focus on the new tab

    def get_current_tab(self):
        """Get the current tab's text area and frame."""
        current_tab = self.notebook.select()
        if current_tab:
            frame = self.notebook.nametowidget(current_tab)
            text_area = frame.winfo_children()[0]  # \\  Text area is the first child
            return text_area, frame
        return None, None

    def new_file(self):
        """Create a new file in a new tab."""
        self.add_tab("Untitled")

    def open_file(self):
        """Open a text file and load its content into a new tab."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                tab_title = file_path.split("/")[-1]  # \\ Use the file name as the tab title
                self.add_tab(tab_title)
                text_area, _ = self.get_current_tab()
                text_area.insert(tk.END, content)
            except Exception as e:
                GTG.showerror(self.root, "Error", f"Failed to open file: {e}")

    def save_file(self):
        """Save the current tab's content to the associated file."""
        text_area, frame = self.get_current_tab()
        if not text_area:
            return

        tab_title = self.notebook.tab(self.notebook.select(), "text")
        if tab_title == "Untitled":
            self.save_file_as()
        else:
            self._save_to_file(tab_title, text_area.get(1.0, tk.END))

    def save_file_as(self):
        """Save the current tab's content to a new file."""
        text_area, frame = self.get_current_tab()
        if not text_area:
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self._save_to_file(file_path, text_area.get(1.0, tk.END))
            tab_title = file_path.split("/")[-1]
            self.notebook.tab(frame, text=tab_title)

    def _save_to_file(self, file_path, content):
        """Helper method to save text to a file."""
        try:
            with open(file_path, "w") as file:
                file.write(content)
            GTG.showinfo(self.root, "Success", f"File saved: {file_path}")
        except Exception as e:
            GTG.showerror(self.root, "Error", f"Failed to save file: {e}")

    def clear_text(self):
        """Clear the current tab's text area."""
        text_area, _ = self.get_current_tab()
        if text_area:
            text_area.delete(1.0, tk.END)

    def toggle_bold(self):
        """Toggle bold formatting for selected text in the current tab."""
        text_area, _ = self.get_current_tab()
        if text_area:
            try:
                current_tags = text_area.tag_names("sel.first")
                if "bold" in current_tags:
                    text_area.tag_remove("bold", "sel.first", "sel.last")
                else:
                    text_area.tag_add("bold", "sel.first", "sel.last")
                    text_area.tag_configure("bold", font=("Arial", 12, "bold"))
            except tk.TclError:
                GTG.showwarning(self.root, title="No Selection", message="Please select text to apply bold formatting.")

    def change_font_size(self):
        """Open a pop-up to change the font size of the text in the current tab."""
        text_area, _ = self.get_current_tab()
        if not text_area:
            return
        popup = GTG.Toplevel(self.root , default_bg="lime" ,relief="groove")
        popup.title("Font Size")
        popup.geometry("300x250")
        label_font_size = GTG.Label(popup, text="Enter font size (8-72):")
        label_font_size.pack(pady=10)
        entry_font_size = GTG.Entry(popup, bg="black" , fg="lime")
        entry_font_size.pack(pady=10)

        # \\ Function to apply the font size
        def apply_font_size():
            try:
                new_size = int(entry_font_size.get())
                if 8 <= new_size <= 72:
                    text_area.configure(font=("Arial", new_size))
                    popup.destroy()  
                else:
                    GTG.showerror(popup,title="Invalid Size", message="Font size must be between 8 and 72.")
            except ValueError:
                GTG.showerror(popup,title="Invalid Input", message="Please enter a valid integer.")

        apply_button = GTG.Button(popup, text="Apply", command=apply_font_size)
        apply_button.pack(pady=10)

# \\ Build and root app to tk window 
def NotePad_Example():
    
    root = tk.Tk()
    
    app = TextEditor(root)
    
    root.mainloop() 

if __name__ == "__main__":
    NotePad_Example()

#! ----------------------- End of Text Editor Example -----------------------------------------------------






#! ----------------------- To Do list App -----------------------------------------------------
# class TodoList(GTG.Frame):
#     def __init__(self, parent, **kwargs):
#         super().__init__(parent, **kwargs)
#         self.tasks = []
#         #* \\ Entry for adding tasks
#         self.task_entry = GTG.Entry(self, enable_hover=True)
#         self.task_entry.pack(pady=10)

#         #* \\ Button to add tasks
#         self.add_button = GTG.Button(self, text="Add Task", command=self.add_task)
#         self.add_button.pack(pady=5)

#         #* \\ Listbox to display tasks
#         self.task_listbox = GTG.Listbox(self, enable_hover=True, bg="white", fg="black")
#         self.task_listbox.pack(fill="both", expand=True, pady=10)

#         #* \\ Button to remove selected task
#         self.remove_button = GTG.Button(self, text="Remove Task", command=self.remove_task)
#         self.remove_button.pack(pady=5)

#         #* \\ Button to edit selected task
#         self.edit_button = GTG.Button(self, text="Edit Task", command=self.edit_task)
#         self.edit_button.pack(pady=5)

#     def add_task(self):
#         """Add a task to the listbox."""
#         task = self.task_entry.get()
#         if task:
#             self.tasks.append(task)
#             self.task_listbox.insert(tk.END, task)
#             self.task_entry.delete(0, tk.END)
#             GTG.showinfo(self, "Success", "Task added successfully!")
#         else:
#             GTG.showerror(self, "Empty Task", "Please enter a task.")

#     def remove_task(self):
#         """Remove the selected task from the listbox."""
#         try:
#             selected_task_index = self.task_listbox.curselection()[0]
#             self.task_listbox.delete(selected_task_index)
#             self.tasks.pop(selected_task_index)
#             GTG.showinfo(self, "Success", "Task removed successfully!")
#         except IndexError:
#             GTG.showwarning(self, "No Selection", "Please select a task to remove.")

#     def edit_task(self):
#         """Edit the selected task in the listbox."""
#         try:
#             selected_task_index = self.task_listbox.curselection()[0]
#             selected_task = self.task_listbox.get(selected_task_index)

#             #* \\ Create a new window for editing using GTG
#             edit_window = GTG.Toplevel(self)
#             edit_window.title("Edit Task")

#             #* \\  Entry widget to edit the task
#             edit_entry = GTG.Entry(edit_window, enable_hover=True)
#             edit_entry.insert(0, selected_task)
#             edit_entry.pack(pady=10)

#             #* \\ Button to save the edited task
#             save_button = GTG.Button(
#                 edit_window,
#                 text="Save",
#                 command=lambda: self.save_task(selected_task_index, edit_entry.get(), edit_window)
#             )
#             save_button.pack(pady=5)

# #* \\ Adding GTG custom message box pop ups
#         except IndexError:
#             GTG.showwarning(self, "No Selection", "Please select a task to edit.")

#     def save_task(self, index, new_task, window):
#         """Save the edited task and close the edit window."""
#         if new_task:
#             self.tasks[index] = new_task
#             self.task_listbox.delete(index)
#             self.task_listbox.insert(index, new_task)
#             window.destroy()
#             GTG.showinfo(self, "Success", "Task updated successfully!")
#         else:
#             GTG.showerror(self, "Empty Task", "Task cannot be empty.")


# #* \\ Adding the to do list to a tkinter window 
# root = tk.Tk()
# root.title("Main Window")

# todo_list = TodoList(root, bg="#2b2b2b")
# todo_list.pack(fill="both", expand=True)

# root.mainloop()

#! ----------------------- END of To Do List App -----------------------------------------------------



#! ----------------------- Stop Watch App -----------------------------------------------------

# class Stopwatch(GTG.Frame):
#     def __init__(self, parent, **kwargs):
#         super().__init__(parent, **kwargs)

#         #* \\ Variables to track time
#         self.running = False
#         self.start_time = None
#         self.elapsed_time = GTGDateTime(0, 1, 1, 0, 0, 0)  #* \\ Initialize elapsed time to 00:00:00
       
#         #* \\ Frame to hold the buttons
#         self.button_frame = GTG.Frame(self)
#         self.button_frame.pack(pady=5)
        
#         #* \\ Label to display the time
#         self.time_label = GTG.Label(self, text="00:00:00", font=("Arial", 24), bg="#2b2b2b", fg="white")
#         self.time_label.pack(pady=10)

#         self.start_button = GTG.Button(self.button_frame, text="Start", command=self.start)
#         self.start_button.pack(side=tk.LEFT, padx=5)  #* \\ Place the Start button on the left

#         self.stop_button = GTG.Button(self.button_frame, text="Stop", command=self.stop)
#         self.stop_button.pack(side=tk.LEFT, padx=5)  #* \\ Place the Stop button next to the Start button

#         self.reset_button = GTG.Button(self.button_frame, text="Reset", command=self.reset)
#         self.reset_button.pack(side=tk.LEFT, padx=5) #* \\ Place the reset button next to the Stop button
    
#     def start(self):
#         """Start the stopwatch."""
#         if not self.running:
#             self.running = True
#             self.start_time = GTGDateTime.now()  #* \\ Use GTGDateTime.now() to get the current time
#             self.update_time()

#     def stop(self):
#         """Stop the stopwatch."""
#         if self.running:
#             self.running = False
#             current_time = GTGDateTime.now()
#             elapsed_seconds = self.calculate_elapsed_seconds(self.start_time, current_time)
#             self.elapsed_time = self.add_seconds_to_time(self.elapsed_time, elapsed_seconds)

#     def reset(self):
#         """Reset the stopwatch."""
#         self.running = False
#         self.elapsed_time = GTGDateTime(0, 1, 1, 0, 0, 0)  #* \\ Reset elapsed time to 00:00:00
#         self.time_label.config(text="00:00:00")

#     def update_time(self):
#         """Update the displayed time."""
#         if self.running:
#             current_time = GTGDateTime.now()
#             elapsed_seconds = self.calculate_elapsed_seconds(self.start_time, current_time)
#             total_time = self.add_seconds_to_time(self.elapsed_time, elapsed_seconds)
#             self.time_label.config(text=f"{total_time.time.hour:02}:{total_time.time.minute:02}:{total_time.time.second:02}")
#             self.after(1000, self.update_time)  #* \\ Update every second

#     def calculate_elapsed_seconds(self, start_time, end_time):
#         """Calculate the elapsed time in seconds between two GTGDateTime objects."""
#         start_seconds = (
#             start_time.time.hour * 3600
#             + start_time.time.minute * 60
#             + start_time.time.second
#         )
#         end_seconds = (
#             end_time.time.hour * 3600
#             + end_time.time.minute * 60
#             + end_time.time.second
#         )
#         return end_seconds - start_seconds

#     def add_seconds_to_time(self, time_obj, seconds):
#         """Add seconds to a GTGDateTime object and return a new GTGDateTime object."""
#         total_seconds = (
#             time_obj.time.hour * 3600
#             + time_obj.time.minute * 60
#             + time_obj.time.second
#             + seconds
#         )
#         hours = total_seconds // 3600
#         minutes = (total_seconds % 3600) // 60
#         seconds = total_seconds % 60
#         return GTGDateTime(0, 1, 1, hours, minutes, seconds)  #* \\ Date part is irrelevant for stopwatch 


# #* \\ Adding the stop watch to a tkinter window 
# root = tk.Tk()
# root.title("Stopwatch")

# #* \\ Create an instance of the Stopwatch class and add it to the window
# stopwatch = Stopwatch(root)
# stopwatch.pack()

# root.mainloop()

# # #! ----------------------- END of Stop Watch Example -----------------------------------------------------


# class Calculator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Calculator")
#         self.root.geometry("300x400")
#         self.root.resizable(False, False)

#         # \\ Variable to store the current input
#         self.input_var = GTG.StringVar(value="")

#         # \\ Create the display
#         self.display = GTG.Entry(root, font=("Arial", 18), justify="right")
#         self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
#         self.input_var.bind_to_widget(self.display) 

#         buttons = [
#             ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
#             ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
#             ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
#             ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
#             ("C", 5, 0, 1, 4)  
#         ]

#         # \\ Create a frame for the buttons
#         button_frame = GTG.Frame(root)
#         button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

#         # \\ Add buttons to the frame
#         for button in buttons:
#             text, row, col = button[0], button[1], button[2]
#             colspan = button[3] if len(button) > 3 else 1
#             rowspan = button[4] if len(button) > 4 else 1

#             btn = GTG.Button(
#                 button_frame,
#                 text=text,
#                 bg="red" if text == "C" else "#f0f0f0",
#                 fg="black",
#                 font=("Arial", 14),
#                 command=lambda t=text: self.on_button_click(t)
#             )
#             btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky="nsew", padx=5, pady=5)

#         # \\ Configure grid weights using GTG_range
#         for i in GTG_range(0, 6):  
#             button_frame.grid_rowconfigure(i, weight=1)
#         for j in GTG_range(0, 4):  
#             button_frame.grid_columnconfigure(j, weight=1)

#     def on_button_click(self, text):
#         """Handle button clicks."""
#         current_input = self.input_var.get()

#         if text == "C":
#             self.input_var.set("")   
#         elif text == "=":
#             try:
#                 result = str(eval(current_input))  
#                 self.input_var.set(result)
#             except Exception as e:
#                 self.input_var.set("Error")   
#         else:
#             self.input_var.set(current_input + text) 

# #! Example adding to a tk window 
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Calculator(root)
#     root.mainloop()



