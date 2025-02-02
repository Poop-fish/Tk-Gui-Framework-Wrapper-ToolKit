from GTG_Widgets import GTG , SidePanel
from GTG_DateTime_Module import *
from GTG_imports import *

#! ----------------------- To Do list App -----------------------------------------------------
class TodoList(GTG.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.tasks = []
        #* \\ Entry for adding tasks
        self.task_entry = GTG.Entry(self, enable_hover=True)
        self.task_entry.pack(pady=10)

        # Button to add tasks
        self.add_button = GTG.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        #* \\ Listbox to display tasks
        self.task_listbox = GTG.Listbox(self, enable_hover=True, bg="white", fg="black")
        self.task_listbox.pack(fill="both", expand=True, pady=10)

        #* \\ Button to remove selected task
        self.remove_button = GTG.Button(self, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        #* \\ Button to edit selected task
        self.edit_button = GTG.Button(self, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

    def add_task(self):
        """Add a task to the listbox."""
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            GTG.showinfo(self, "Success", "Task added successfully!")
        else:
            GTG.showerror(self, "Empty Task", "Please enter a task.")

    def remove_task(self):
        """Remove the selected task from the listbox."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
            GTG.showinfo(self, "Success", "Task removed successfully!")
        except IndexError:
            GTG.showwarning(self, "No Selection", "Please select a task to remove.")

    def edit_task(self):
        """Edit the selected task in the listbox."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_task_index)

            #* \\ Create a new window for editing using GTG
            edit_window = GTG.Toplevel(self)
            edit_window.title("Edit Task")

            #* \\  Entry widget to edit the task
            edit_entry = GTG.Entry(edit_window, enable_hover=True)
            edit_entry.insert(0, selected_task)
            edit_entry.pack(pady=10)

            #* \\ Button to save the edited task
            save_button = GTG.Button(
                edit_window,
                text="Save",
                command=lambda: self.save_task(selected_task_index, edit_entry.get(), edit_window)
            )
            save_button.pack(pady=5)

#* \\ Adding GTG custom message box pop ups
        except IndexError:
            GTG.showwarning(self, "No Selection", "Please select a task to edit.")

    def save_task(self, index, new_task, window):
        """Save the edited task and close the edit window."""
        if new_task:
            self.tasks[index] = new_task
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, new_task)
            window.destroy()
            GTG.showinfo(self, "Success", "Task updated successfully!")
        else:
            GTG.showerror(self, "Empty Task", "Task cannot be empty.")


#* \\ Adding the to do list to a tkinter window 
root = tk.Tk()
root.title("Main Window")

todo_list = TodoList(root, bg="#2b2b2b")
todo_list.pack(fill="both", expand=True)

root.mainloop()

#! ----------------------- END of To Do List App -----------------------------------------------------



#! ----------------------- Stop Watch App -----------------------------------------------------

class Stopwatch(GTG.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        #* \\ Variables to track time
        self.running = False
        self.start_time = None
        self.elapsed_time = GTGDateTime(0, 1, 1, 0, 0, 0)  #* \\ Initialize elapsed time to 00:00:00
        #* \\ Frame to hold the buttons
        self.button_frame = GTG.Frame(self)
        self.button_frame.pack(pady=5)
        #* \\ Label to display the time
        self.time_label = GTG.Label(self, text="00:00:00", font=("Arial", 24), bg="#2b2b2b", fg="white")
        self.time_label.pack(pady=10)

        self.start_button = GTG.Button(self.button_frame, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=5)  #* \\ Place the Start button on the left

        self.stop_button = GTG.Button(self.button_frame, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=5)  #* \\ Place the Stop button next to the Start button

        self.reset_button = GTG.Button(self.button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=5) #* \\ Place the reset button next to the Stop button
    
    def start(self):
        """Start the stopwatch."""
        if not self.running:
            self.running = True
            self.start_time = GTGDateTime.now()  #* \\ Use GTGDateTime.now() to get the current time
            self.update_time()

    def stop(self):
        """Stop the stopwatch."""
        if self.running:
            self.running = False
            current_time = GTGDateTime.now()
            elapsed_seconds = self.calculate_elapsed_seconds(self.start_time, current_time)
            self.elapsed_time = self.add_seconds_to_time(self.elapsed_time, elapsed_seconds)

    def reset(self):
        """Reset the stopwatch."""
        self.running = False
        self.elapsed_time = GTGDateTime(0, 1, 1, 0, 0, 0)  #* \\ Reset elapsed time to 00:00:00
        self.time_label.config(text="00:00:00")

    def update_time(self):
        """Update the displayed time."""
        if self.running:
            current_time = GTGDateTime.now()
            elapsed_seconds = self.calculate_elapsed_seconds(self.start_time, current_time)
            total_time = self.add_seconds_to_time(self.elapsed_time, elapsed_seconds)
            self.time_label.config(text=f"{total_time.time.hour:02}:{total_time.time.minute:02}:{total_time.time.second:02}")
            self.after(1000, self.update_time)  #* \\ Update every second

    def calculate_elapsed_seconds(self, start_time, end_time):
        """Calculate the elapsed time in seconds between two GTGDateTime objects."""
        start_seconds = (
            start_time.time.hour * 3600
            + start_time.time.minute * 60
            + start_time.time.second
        )
        end_seconds = (
            end_time.time.hour * 3600
            + end_time.time.minute * 60
            + end_time.time.second
        )
        return end_seconds - start_seconds

    def add_seconds_to_time(self, time_obj, seconds):
        """Add seconds to a GTGDateTime object and return a new GTGDateTime object."""
        total_seconds = (
            time_obj.time.hour * 3600
            + time_obj.time.minute * 60
            + time_obj.time.second
            + seconds
        )
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return GTGDateTime(0, 1, 1, hours, minutes, seconds)  #* \\ Date part is irrelevant for stopwatch 


# Adding the stop watch to a tkinter window 
root = tk.Tk()
root.title("Stopwatch")

#* \\ Create an instance of the Stopwatch class and add it to the window
stopwatch = Stopwatch(root)
stopwatch.pack()

root.mainloop()

#! ----------------------- END of Stop Watch Example -----------------------------------------------------


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        #* \\ Variable to store the current input
        self.input_var = tk.StringVar(value="")

        #* \\ Create the display
        self.display = GTG.Entry(root, enable_hover=False, font=("Arial", 18), justify="right")
        self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.display.configure(textvariable=self.input_var)

        #* \\ Create buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0, 1, 4)  
        ]

        #* \\ Create a frame for the buttons
        button_frame = GTG.Frame(root, enable_hover=False)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        #* \\ Add buttons to the frame
        for button in buttons:
            text, row, col = button[0], button[1], button[2]
            colspan = button[3] if len(button) > 3 else 1
            rowspan = button[4] if len(button) > 4 else 1

            btn = GTG.Button(
                button_frame,
                text=text,
                enable_hover=True,
                bg="red" if text == "C" else "#f0f0f0",
                fg="black",
                hover_bg="#ff7d7d" if text == "C" else "#d9d9d9",
                hover_fg="lime",
                font=("Arial", 14),
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky="nsew", padx=5, pady=5)

         #* \\ Configure grid weights
        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)

    def on_button_click(self, text):
        """Handle button clicks."""
        current_input = self.input_var.get()

        if text == "C":
            self.input_var.set("")   #* \\ Clear the input
        elif text == "=":
            try:
                result = str(eval(current_input))  #* \\ Evaluate the expression
                self.input_var.set(result)
            except Exception as e:
                self.input_var.set("Error")   #* \\ Handle errors
        else:
            self.input_var.set(current_input + text)   #* \\ Append the button text to the input


#! Adding to a tkinter window 
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()



# #! ----------------------- Text Editor Example -----------------------------------------------------


import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        #* \\ Variable to store the current file path
        self.current_file = None

        #* \\ Create the menu bar
        self.menu_bar = GTG.Menu(root, enable_hover=True)
        self.root.configure(menu=self.menu_bar)

        #* \\ File menu
        file_menu = GTG.Menu(self.menu_bar, enable_hover=True , hover_bg="lime")
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        #* \\ Edit menu
        edit_menu = GTG.Menu(self.menu_bar, enable_hover=True, hover_bg="lime")
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Clear", command=self.clear_text)

        #* \\ Format menu
        format_menu = GTG.Menu(self.menu_bar, enable_hover=True,hover_bg="lime")
        self.menu_bar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Bold", command=self.toggle_bold)
        format_menu.add_command(label="Font Size", command=self.change_font_size)

        #* \\ Create the text area
        self.text_area = GTG.Text(root, enable_hover=True, wrap="word")
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        #* \\ Configure default font
        self.current_font = ("Arial", 12)
        self.text_area.configure(font=self.current_font)

    def open_file(self):
        """Open a text file and load its content into the text area."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)  #* \\ Clear the text area
                    self.text_area.insert(tk.END, file.read())  #* \\ Insert file content
                self.current_file = file_path
                self.status_bar.configure(text=f"Opened: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    def save_file(self):
        """Save the current text to a file."""
        if self.current_file:
            file_path = self.current_file
        else:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))  #* \\ Write text to file
                self.current_file = file_path
                self.status_bar.configure(text=f"Saved: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def clear_text(self):
        """Clear the text area."""
        self.text_area.delete(1.0, tk.END)
        self.status_bar.configure(text="Text cleared")

    def toggle_bold(self):
        """Toggle bold formatting for selected text."""
        current_font = self.text_area.cget("font")
        new_font = ("Arial", 12, "bold") if "bold" not in current_font else ("Arial", 12)
        self.text_area.configure(font=new_font)

    def change_font_size(self):
        """Change the font size of the text."""
        new_size = simpledialog.askinteger("Font Size", "Enter font size:", minvalue=8, maxvalue=72)
        if new_size:
            self.current_font = ("Arial", new_size)
            self.text_area.configure(font=self.current_font)


#* \\ Run the text editor 
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()


