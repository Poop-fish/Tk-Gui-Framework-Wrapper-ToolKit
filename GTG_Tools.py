from GTG_iterables import GTGenumerate
from GTG_imports import *  
from GTG_Widgets import *
from GTG_Extended_Widgets import *
from GTG_Random_Modules import GTG_Random
from GTG_iterables import GTG_range

#! ------------------------------------------------- Gui Tools -------------------------------------------------------------

class PyExE:
    def __init__(self, root, x=0, y=0, width=400, height=250, bg=None, relief="groove", borderwidth=5, padding=(0, 0), sticky=""):
        self.root = root
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg = bg
        self.relief = relief
        self.borderwidth = borderwidth
        self.padding = padding
        self.sticky = sticky
        self.frame = None
        self.script_path = GTG.StringVar()
        self.output_folder = GTG.StringVar()
        self.icon_path = GTG.StringVar()
        self.onefile_var = GTG.BooleanVar()
        self.console_var = GTG.BooleanVar()
        self.drag_data = {}

        self._build()

    def _build(self):
        """Build the main UI components."""
        
        self.frame = GTG.Frame(self.root,
                            width=self.width,
                            height=self.height,
                            bg=self.bg,
                            relief=self.relief,
                            borderwidth=self.borderwidth)
        self.frame.place(x=self.x, y=self.y)

        self.frame.bind("<ButtonPress-1>", self.on_drag_start)
        self.frame.bind("<B1-Motion>", self.on_drag_motion)
        self.frame.bind("<ButtonRelease-1>", self.on_drag_release)

        self.side_panel = GTG.Frame(self.frame, width=100, height=self.height, bg="#f0f0f0")
        self.side_panel.grid(row=0, column=0, rowspan=5, sticky="nsew")

        self.main_area = GTG.Frame(self.frame, width=self.width - 120, height=self.height, bg="#ffffff")
        self.main_area.grid(row=0, column=1, rowspan=5, sticky="nsew", padx=20, pady=10)

        self.script_label = GTG.Label(self.main_area, text="Select Python Script:")
        self.script_label.grid(row=0, column=0, pady=5, sticky="w")

        self.script_entry = GTG.Entry(self.main_area, textvariable=self.script_path, width=40, bg="gray")
        self.script_entry.grid(row=0, column=1, pady=5)

        self.browse_button = GTG.Button(self.main_area, text="Browse", command=self.browse_file,image_path="Assets/icon_2.png", width=25 , height=25, frame="flat")
        self.browse_button.grid(row=0, column=2, pady=5)

        self.folder_label = GTG.Label(self.main_area, text="Select Output Folder:")
        self.folder_label.grid(row=1, column=0, pady=5, sticky="w")

        self.folder_entry = GTG.Entry(self.main_area, textvariable=self.output_folder, width=40, bg="gray")
        self.folder_entry.grid(row=1, column=1, pady=5)

        self.folder_button = GTG.Button(self.main_area, text="Browse", command=self.browse_folder,image_path="Assets/icon_2.png", width=25 , height=25, frame="flat")
        self.folder_button.grid(row=1, column=2, pady=5)

        self.icon_label = GTG.Label(self.main_area, text="Select Icon (.ico):")
        self.icon_label.grid(row=2, column=0, pady=5, sticky="w")

        self.icon_entry = GTG.Entry(self.main_area, textvariable=self.icon_path, width=40,bg="gray")
        self.icon_entry.grid(row=2, column=1, pady=5)

        self.icon_button = GTG.Button(self.main_area, text="Browse", command=self.browse_icon,image_path="Assets/icon_2.png", width=25 , height=25, frame="flat")
        self.icon_button.grid(row=2, column=2, pady=5)

        self.onefile_check = GTG.Checkbutton(self.main_area, text="One-file executable", variable=self.onefile_var)
        self.onefile_check.grid(row=3, column=0, pady=5)

        self.console_check = GTG.Checkbutton(self.main_area, text="Hide console window", variable=self.console_var)
        self.console_check.grid(row=3, column=1, pady=5)

        self.convert_button = GTG.Button(self.main_area, text="Convert to EXE", command=self.convert_to_exe, borderwidth=5)
        self.convert_button.grid(row=4, column=0, columnspan=3, pady=20)

        self.status_label = GTG.Label(self.main_area, text="", fg="Lime")
        self.status_label.grid(row=5, column=0, columnspan=3, pady=5)

        self.side_button_1 = GTG.Button(self.side_panel, text="Help", command=self.show_help, borderwidth=5)
        self.side_button_1.grid(row=0, column=0, pady=10)

        self.side_button_2 = GTG.Button(self.side_panel, text="About", command=self.show_about, borderwidth=5)
        self.side_button_2.grid(row=1, column=0, pady=10)

    # -- Dragging Logic --
    def on_drag_start(self, event):
        """Record the initial mouse position when dragging starts."""
        self.is_dragging = True
        self.drag_data['x'] = event.x
        self.drag_data['y'] = event.y

    def on_drag_motion(self, event):
        """Move the frame as the mouse is dragged."""
        if self.is_dragging:
            delta_x = event.x - self.drag_data['x']
            delta_y = event.y - self.drag_data['y']
            new_x = self.frame.winfo_x() + delta_x
            new_y = self.frame.winfo_y() + delta_y
            self.frame.place(x=new_x, y=new_y)

    def on_drag_release(self, event):
        """Stop dragging when the mouse is released."""
        self.is_dragging = False


    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if file_path:
            self.script_path.set(file_path)

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.output_folder.set(folder_path)

    def browse_icon(self):
        icon_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
        if icon_path:
            self.icon_path.set(icon_path)

    def convert_to_exe(self):
        script = self.script_path.get()
        output_folder = self.output_folder.get()
        icon = self.icon_path.get()

        if not script:
            messagebox.showerror("Error", "Please select a Python script.")
            return

        if not os.path.exists(script):
            messagebox.showerror("Error", "The selected script does not exist.")
            return

        if not output_folder:
            messagebox.showerror("Error", "Please select an output folder.")
            return

        if not os.path.exists(output_folder):
            messagebox.showerror("Error", "The selected output folder does not exist.")
            return

        if icon and not os.path.exists(icon):
            messagebox.showerror("Error", "The selected icon file does not exist.")
            return

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        dist_dir = os.path.join(output_folder, 'dist')
        build_dir = os.path.join(output_folder, 'build')
        spec_file = os.path.join(output_folder, os.path.basename(script).replace('.py', '.spec'))

        # \\ Build the PyInstaller command
        command = ["pyinstaller", script]

        # \\ Add --onefile option if selected
        if self.onefile_var.get():
            command.append("--onefile")

        # \\ Add --noconsole option if selected
        if self.console_var.get():
            command.append("--noconsole")

        # \\ Specify the custom directories for dist, build, and spec files
        command.append(f"--distpath={dist_dir}")  # \\ Output EXE to the dist folder
        command.append(f"--workpath={build_dir}")  # \\ Temporary files for building
        command.append(f"--specpath={output_folder}")  # \\ Save .spec file to the output folder

        if icon:
            command.append(f"--icon={icon}")

        try:
            self.status_label.config(text="Generating EXE... Please wait.")
            self.frame.update()

            subprocess.run(command, check=True)

            if os.path.exists(spec_file):
                shutil.move(spec_file, os.path.join(output_folder, os.path.basename(spec_file)))

            self.status_label.config(text="EXE created successfully!", fg="green")
            messagebox.showinfo("Success", f"EXE and build files created successfully in: {output_folder}")

        except subprocess.CalledProcessError:
            self.status_label.config(text="An error occurred.", fg="red")
            messagebox.showerror("Error", "Failed to create EXE. Check the console for errors.")

    def show_help(self):
       GTG.showinfo(self.root, title="Help", message="This tool converts Python scripts into EXE files using PyInstaller.\nSelect your Python script, output folder, and any desired options.")
    
    def show_about(self):
        GTG.showinfo(self.root, title="About", message="ExeFileMaker v1.0\n Created by GamerTag") 

#! Example
if __name__ == "__main__":
    root = tk.Tk()
    root.title("GExeFileMaker")
    root.geometry("800x650")
    app = PyExE(root)
    
    root.mainloop() 

#! -----------------------------------------------------------------------------------------------------------------------------

#! ------------ CPU / GPU/ Memory / Performance Bars --------------

class SystemPerformanceWidget(GTG.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(bg="#f0f0f0")
       
        # \\ CPU Frame
        cpu_frame = GTG.Frame(self)
        cpu_frame.pack(fill=tk.X, pady=5)

        self.cpu_label = GTG.Label(cpu_frame, text="CPU Usage: -", font=("Arial", 12))
        self.cpu_label.pack(anchor=tk.W)

        self.cpu_progress = GTG.Progressbar(cpu_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.cpu_progress.pack(fill=tk.X)

        # \\ GPU Frame
        gpu_frame = GTG.Frame(self)
        gpu_frame.pack(fill=tk.X, pady=5)

        self.gpu_label = GTG.Label(gpu_frame, text="GPU Usage: -", font=("Arial", 12))
        self.gpu_label.pack(anchor=tk.W)

        self.gpu_progress = GTG.Progressbar(gpu_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.gpu_progress.pack(fill=tk.X)

        # \\ Memory Frame
        memory_frame = GTG.Frame(self)
        memory_frame.pack(fill=tk.X, pady=5)

        self.memory_label = GTG.Label(memory_frame, text="Memory Usage: -", font=("Arial", 12))
        self.memory_label.pack(anchor=tk.W)

        self.memory_progress = GTG.Progressbar(memory_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.memory_progress.pack(fill=tk.X)

        # \\ Start updating the dashboard
        self.update_dashboard()

    def get_system_stats(self):
        # \\ CPU Usage
        cpu_usage = psutil.cpu_percent(interval=0.1)

        # \\ Memory Usage
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        # \\ GPU Usage (if available)
        gpu_usage = "N/A"
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_usage = f"{gpus[0].load * 100:.1f}%"

        return {
            "CPU": f"{cpu_usage}%",
            "GPU": gpu_usage,
            "Memory": f"{memory_usage}%"
        }

    def update_dashboard(self):
        stats = self.get_system_stats()

        # \\ Update CPU progress bar and label
        self.cpu_label.config(text=f"CPU Usage: {stats['CPU']}")
        self.cpu_progress['value'] = float(stats['CPU'].strip('%'))

        # \\ Update GPU progress bar and label
        self.gpu_label.config(text=f"GPU Usage: {stats['GPU']}")
        if stats['GPU'] != "N/A":
            self.gpu_progress['value'] = float(stats['GPU'].strip('%'))
        else:
            self.gpu_progress['value'] = 0

        # \\ Update Memory progress bar and label
        self.memory_label.config(text=f"Memory Usage: {stats['Memory']}")
        self.memory_progress['value'] = float(stats['Memory'].strip('%'))

        # \\ Schedule the next update
        self.after(1000, self.update_dashboard)  

class SystemPerformance(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Performance")
        self.geometry("500x400")
        self.configure(bg='#868686')
        self.iconbitmap('Assets/FaceLogo.ico')
        performance_widget = SystemPerformanceWidget(self)
        performance_widget.pack(fill=tk.BOTH, expand=True)

# #! Example
# if __name__ == "__main__":
#     app = SystemPerformance()
#     app.mainloop() 

#! -----------------------------------------------------------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cryptography.fernet import Fernet

class GFileEncrypter:
    def __init__(self, root=None, x=0, y=0, width=400, height=300):
        self.root = root
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.file_path = None
        self.key = None
        self.drag_data = {}
        self.create_widgets()

    def create_widgets(self):
        self.frame = GTG.Frame(self.root, width=self.width, height=self.height, relief="groove", borderwidth=3)
        self.frame.place(x=self.x, y=self.y)

        # \\ Bind events for dragging and resizing
        self.frame.bind("<ButtonPress-1>", self.on_drag_start)
        self.frame.bind("<B1-Motion>", self.on_drag_motion)
        self.frame.bind("<ButtonRelease-1>", self.on_drag_release)

        # self.frame.bind("<ButtonPress-3>", self.on_resize_start)
        # self.frame.bind("<B3-Motion>", self.on_resize_motion)
        # self.frame.bind("<ButtonRelease-3>", self.on_resize_release)

        title = GTG.Label(self.frame, text="File Encrypter/Decrypter", font=("Arial", 16), bg="lightgray")
        title.pack(pady=10)

        # Buttons for file operations
        select_btn = GTG.Button(self.frame, text="Select File", command=self.select_file)
        select_btn.pack(pady=10, anchor="w")

        encrypt_btn = GTG.Button(self.frame, text="Encrypt File", command=self.encrypt_file, bg="green", fg="white")
        encrypt_btn.pack(pady=5, anchor="ne")

        decrypt_btn = GTG.Button(self.frame, text="Decrypt File", command=self.decrypt_file, bg="blue", fg="white")
        decrypt_btn.pack(pady=5, anchor="w")

        generate_key_btn = GTG.Button(self.frame, text="Generate Key", command=self.generate_key, bg="orange")
        generate_key_btn.pack(pady=5, anchor="ne")

        save_key_btn = GTG.Button(self.frame, text="Save Key", command=self.save_key, bg="purple", fg="white")
        save_key_btn.pack(pady=5, anchor="w")

        load_key_btn = GTG.Button(self.frame, text="Load Key", command=self.load_key, bg="brown", fg="white")
        load_key_btn.pack(pady=5, anchor="ne")

        self.file_label = GTG.Label(self.frame, text="No file selected", bg="lightgray", wraplength=350)
        self.file_label.pack(pady=10)

    def on_drag_start(self, event):
        """Record the initial mouse position when dragging starts."""
        self.drag_data['x'] = event.x
        self.drag_data['y'] = event.y

    def on_drag_motion(self, event):
        """Move the frame as the mouse is dragged."""
        delta_x = event.x - self.drag_data['x']
        delta_y = event.y - self.drag_data['y']
        new_x = self.frame.winfo_x() + delta_x
        new_y = self.frame.winfo_y() + delta_y
        self.frame.place(x=new_x, y=new_y)

    def on_drag_release(self, event):
        """Stop dragging when the mouse is released."""
        self.drag_data = {}

    # def on_resize_start(self, event):
    #     """Start resizing the frame by right-clicking anywhere on the frame."""
    #     self.is_resizing = True
    #     self.drag_data['x'] = event.x
    #     self.drag_data['y'] = event.y
    #     self.width = self.frame.winfo_width()
    #     self.height = self.frame.winfo_height()

    # def on_resize_motion(self, event):
    #     """Resize the frame as the mouse is dragged."""
    #     if self.is_resizing:
    #         delta_x = event.x - self.drag_data['x']
    #         delta_y = event.y - self.drag_data['y']
    #         new_width = max(100, self.width + delta_x)  
    #         new_height = max(100, self.height + delta_y)  

    #         self.frame.place(width=new_width, height=new_height)
    #         self.width = new_width
    #         self.height = new_height

    # def on_resize_release(self, event):
    #     """Stop resizing when the right mouse button is released."""
    #     self.is_resizing = False

    def select_file(self):
        """Select a file to encrypt or decrypt."""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            self.file_label.config(text=f"Selected File: {file_path}")
        else:
            messagebox.showwarning("No File", "Please select a file!")

    def generate_key(self):
        """Generate a new encryption key."""
        self.key = Fernet.generate_key()
        messagebox.showinfo("Key Generated", "A new key has been generated!")
        print(f"Generated Key: {self.key.decode()}") 

    def save_key(self):
        """Save the generated key to a file."""
        if not self.key:
            messagebox.showwarning("No Key", "Please generate or load a key first!")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".key", filetypes=[("Key Files", "*.key")])
        if file_path:
            with open(file_path, "wb") as key_file:
                key_file.write(self.key)
            messagebox.showinfo("Key Saved", f"Key saved to: {file_path}")

    def load_key(self):
        """Load an encryption key from a file."""
        file_path = filedialog.askopenfilename(filetypes=[("Key Files", "*.key")])
        if file_path:
            with open(file_path, "rb") as key_file:
                self.key = key_file.read()
            messagebox.showinfo("Key Loaded", "Encryption key has been loaded!")

    def encrypt_file(self):
        """Encrypt the selected file."""
        if not self.file_path:
            messagebox.showwarning("No File", "Please select a file to encrypt!")
            return
        if not self.key:
            messagebox.showwarning("No Key", "Please generate or load a key first!")
            return
        try:
            with open(self.file_path, "rb") as file:
                data = file.read()
            cipher = Fernet(self.key)
            encrypted_data = cipher.encrypt(data)

            save_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Encrypted Files", "*.enc")])
            if save_path:
                with open(save_path, "wb") as enc_file:
                    enc_file.write(encrypted_data)
                messagebox.showinfo("File Encrypted", f"File encrypted and saved to: {save_path}")
        except Exception as e:
            messagebox.showerror("Encryption Error", f"An error occurred: {e}")

    def decrypt_file(self):
        """Decrypt the selected file."""
        if not self.file_path:
            messagebox.showwarning("No File", "Please select a file to decrypt!")
            return
        if not self.key:
            messagebox.showwarning("No Key", "Please generate or load a key first!")
            return
        try:
            with open(self.file_path, "rb") as file:
                encrypted_data = file.read()
            cipher = Fernet(self.key)
            decrypted_data = cipher.decrypt(encrypted_data)

            save_path = filedialog.asksaveasfilename(filetypes=[("All Files", "*.*")])
            if save_path:
                with open(save_path, "wb") as dec_file:
                    dec_file.write(decrypted_data)
                messagebox.showinfo("File Decrypted", f"File decrypted and saved to: {save_path}")
        except Exception as e:
            messagebox.showerror("Decryption Error", f"An error occurred: {e}")

# #! Example
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("500x600")
#     app = GFileEncrypter(root, x=50, y=50)
#     root.mainloop() 

#! -----------------------------------------------------------------------------------------------------------------------------

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.iconbitmap('Assets/FaceLogo.ico')
        # \\ Variable to store the current input
        self.input_var = GTG.StringVar(value="")

        # \\ Create the display
        self.display = GTG.Entry(root, font=("Arial", 18), justify="right")
        self.display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.input_var.bind_to_widget(self.display) 

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0, 1, 4)  
        ]

        # \\ Create a frame for the buttons
        button_frame = GTG.Frame(root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # \\ Add buttons to the frame
        for button in buttons:
            text, row, col = button[0], button[1], button[2]
            colspan = button[3] if len(button) > 3 else 1
            rowspan = button[4] if len(button) > 4 else 1

            btn = GTG.Button(
                button_frame,
                text=text,
                bg="red" if text == "C" else "#f0f0f0",
                fg="black",
                font=("Arial", 14),
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky="nsew", padx=5, pady=5)

        # \\ Configure grid weights using GTG_range
        for i in GTG_range(0, 6):  
            button_frame.grid_rowconfigure(i, weight=1)
        for j in GTG_range(0, 4):  
            button_frame.grid_columnconfigure(j, weight=1)

    def on_button_click(self, text):
        """Handle button clicks."""
        current_input = self.input_var.get()

        if text == "C":
            self.input_var.set("")   
        elif text == "=":
            try:
                result = str(eval(current_input))  
                self.input_var.set(result)
            except Exception as e:
                self.input_var.set("Error")   
        else:
            self.input_var.set(current_input + text) 

# #! Example adding to a tk window 
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = Calculator(root)
#     root.mainloop()

#! -----------------------------------------------------------------------------------------------------------------------------

class Calendar:
    def __init__(self, master, x=0, y=0, width=100, height=300, bg="#4a4a4a", fg="white"):
        self.master = master
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg = bg
        self.fg = fg
        self.frame = None
        self.current_date = datetime.now() 
        self.selected_date = None
        self.events = {}  
        self._build()

    def _build(self):
        self.frame = GTG.Frame(self.master, width=self.width, height=self.height, bg=self.bg)
        self.frame.place(x=self.x, y=self.y)
        
        self.title_label = GTG.Label(self.frame, text="", font=("Arial", 16), fg=self.fg, bg=self.bg)
        self.title_label.grid(row=0, column=0, columnspan=7)
        
        self.prev_button = GTG.Button(self.frame, text="<", command=self.prev_month, bg="Gray", fg="white", font=("Arial", 10))
        self.prev_button.grid(row=0, column=0, sticky="w", padx=10)
        
        self.next_button = GTG.Button(self.frame, text=">", command=self.next_month, bg="Gray", fg="white", font=("Arial", 10))
        self.next_button.grid(row=0, column=6, sticky="e", padx=10)
        
        self.day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day in GTGenumerate(self.day_names):
            day_label = GTG.Label(self.frame, text=day, font=("Arial", 10), fg=self.fg, bg=self.bg)
            day_label.grid(row=1, column=col)
        
        self.create_calendar()

    def create_calendar(self):
        for widget in self.frame.winfo_children():
            if isinstance(widget, GTG.Button) and widget != self.prev_button and widget != self.next_button:
                widget.destroy()
        year = self.current_date.year
        month = self.current_date.month
        cal = calendar.monthcalendar(year, month)
        self.title_label.config(text=f"{calendar.month_name[month]} {year}")

        # \\ Create buttons for each day of the month
        row = 2
        col = 0
        for week in cal:
            for day in week:
                if day != 0:
                    day_button = GTG.Button(self.frame, text=str(day), width=1, height=1, 
                                        command=lambda d=day: self.select_date(d), 
                                        bg=self.bg, fg="white", font=("Arial", 10))
                    # \\ Highlight the current date
                    if day == self.current_date.day and self.current_date.month == month and self.current_date.year == year:
                        day_button.config(bg="red", fg="white")
                    day_button.grid(row=row, column=col)
                    # \\ If there are events on the day, add an event indicator
                    if (year, month, day) in self.events:
                        event_button = GTG.Button(self.frame, text="E", width=2, height=1, 
                                                command=lambda d=day: self.view_event(d), 
                                                bg="red", fg="white", font=("Arial", 5))
                        event_button.grid(row=row, column=col, sticky="e", padx=3, pady=3)
                col += 1
            row += 1
            col = 0
    
    def prev_month(self):
        """Show the previous month."""
        if self.current_date.month == 1:
            self.current_date = self.current_date.replace(year=self.current_date.year - 1, month=12)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month - 1)
        self.create_calendar()

    def next_month(self):
        """Show the next month."""
        if self.current_date.month == 12:
            self.current_date = self.current_date.replace(year=self.current_date.year + 1, month=1)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month + 1)
        self.create_calendar()

    def select_date(self, day):
        """Select a date and show a message box to add or view events."""
        self.selected_date = f"{calendar.month_name[self.current_date.month]} {day}, {self.current_date.year}"
        
        # Ask for the action: Add Event or View Events
        action = messagebox.askquestion("Event Management", 
                                        f"Would you like to add or view events for {self.selected_date}?", 
                                        icon='question')
        
        if action == "yes":
            self.add_event(day)
        else:
            self.view_event(day)

    def add_event(self, day):
        """Add an event to the selected day."""
        event_title = askstring("Event Title", "Enter the title of the event:")
        if event_title:
            event_description = askstring("Event Description", "Enter a description of the event:")
            event_date = (self.current_date.year, self.current_date.month, day)
            
            if event_date not in self.events:
                self.events[event_date] = []
            self.events[event_date].append({"title": event_title, "description": event_description})
            
            messagebox.showinfo("Event Added", f"Event '{event_title}' has been added for {self.selected_date}.")
            self.create_calendar()

    def view_event(self, day):
        """View and remove events for the selected day."""
        event_date = (self.current_date.year, self.current_date.month, day)
        
        if event_date in self.events:
            events = self.events[event_date]
            event_details = "\n".join([f"{i+1}. {event['title']}: {event['description']}" for i, event in enumerate(events)])
            
            remove = messagebox.askquestion("Remove Events", 
                                            f"Events for {self.selected_date}:\n\n{event_details}\n\nWould you like to remove these events?", 
                                            icon='question')
            
            if remove == "yes":
                del self.events[event_date]
                messagebox.showinfo("Events Removed", f"All events for {self.selected_date} have been removed.")
                self.create_calendar()
        else:
            messagebox.showinfo("No Events", f"There are no events for {self.selected_date}.")

#! Example
# def main():
#     root = tk.Tk()
#     root.title("Calendar Widget Example")
#     root.geometry("600x500") 

#     # \\ Instantiate the CalendarWidget and pass the root window
#     calendar = Calendar(root, x=50, y=50, width=300, height=300)

#     root.mainloop()

# if __name__ == "__main__":
#     main()

#! -----------------------------------------------------------------------------------------------------------------------------

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Clicker")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#868686')
        self.root.iconbitmap('Assets/FaceLogo.ico')
        self.clicking = False
        self.click_interval = GTG.DoubleVar(value=0.0001) 
        self.start_key = "f6"
        self.stop_key = "f7"
        self.start_key_press_count = 0

        self.title_label = GTG.Label(root, text="Auto Clicker")
        self.title_label.pack(pady=10)

        self.interval_label = GTG.Label(root, text="Click Interval (seconds):")
        self.interval_label.pack(pady=5)

        self.interval_options = [1.0, 0.9, 0.08, 0.007, 0.0006, 0.0005, 0.0004, 0.0003, 0.0002, 0.0001]
        self.interval_dropdown = GTG.Combobox(root, values=self.interval_options, textvariable=self.click_interval , fg="lime", hover_fg="lime")
        self.interval_dropdown.pack(pady=5)
        self.interval_dropdown.current(0)  

        self.custom_interval_entry = GTG.Entry(root, textvariable=self.click_interval, bg="#b0b0b0" , fg="black")
        self.custom_interval_entry.pack(pady=5)

        self.start_button = GTG.Button(root, text=f"Start ({self.start_key.upper()})", command=self.start_clicking)
        self.start_button.place(x=425 , y=350)
        self.start_button.bind("<Button-3>", self.change_start_key)

        self.stop_button = GTG.Button(root, text=f"Stop ({self.stop_key.upper()})", command=self.stop_clicking, state=tk.DISABLED)
        self.stop_button.place(x=50 , y=350)
        self.stop_button.bind("<Button-3>", self.change_stop_key)

        self.status_label = GTG.Label(root, text="Status: Stopped")
        self.status_label.pack(pady=20)

        self.info_label = GTG.Label(root, text="""Press Your Start Key 
        Keybind Multiply times to increase click speed""")
        self.info_label.pack(pady=5)
            
        self.info_label2 = GTG.Label(root, text="Right Click the Start/Stop Button then click a key to set a custom keybind")
        self.info_label2.pack(pady=5)
    
        keyboard.add_hotkey(self.start_key, self.start_clicking)
        keyboard.add_hotkey(self.stop_key, self.stop_clicking)
    
    def change_start_key(self, event):
        """Change the start keybind."""
        self.status_label.config(text="Press a key for Start")
        new_key = keyboard.read_event().name
        self.start_key = new_key
        self.start_button.config(text=f"Start ({self.start_key.upper()})")
        keyboard.add_hotkey(self.start_key, self.start_clicking)
        self.status_label.config(text="Status: Stopped")
    
    def change_stop_key(self, event):
        """Change the stop keybind."""
        self.status_label.config(text="Press a key for Stop")
        new_key = keyboard.read_event().name
        self.stop_key = new_key
        self.stop_button.config(text=f"Stop ({self.stop_key.upper()})")
        keyboard.add_hotkey(self.stop_key, self.stop_clicking)
        self.status_label.config(text="Status: Stopped")

    def start_clicking(self):
        """Start the auto-clicker."""
        self.start_key_press_count += 1
        if self.start_key_press_count > 1:
            new_interval = max(self.click_interval.get() - 0.0001, 0.00001)  
            self.click_interval.set(new_interval)

        try:
            self.click_interval.set(float(self.custom_interval_entry.get())) 
        except ValueError:
            self.click_interval.set(0.0001)  

        self.clicking = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Clicking...")

        self.click_thread = threading.Thread(target=self.auto_click)
        self.click_thread.start()

    def stop_clicking(self):
        """Stop the auto-clicker."""
        self.clicking = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Stopped")

    def auto_click(self):
        """Auto-clicker logic."""
        while self.clicking:
            pyautogui.click()
            time.sleep(self.click_interval.get())

# #! Example
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AutoClickerApp(root)
#     root.mainloop()

#! ---------------------------------------------------------------------------------------------

    class Clocky(GTG.Frame):
        def __init__(self, master=None, **kwargs):
            super().__init__(master, **kwargs)
            self.master = master
            self.clock_canvas = GTG.Canvas(self, width=200, height=200, highlightthickness=0 , default_bg="black")
            self.clock_canvas.pack(padx=10, pady=10)

            self._draw_clock_face()
            self._update_clock()

        def _draw_clock_face(self):
            """Draw the static elements of the clock face with enhanced design."""
            radius = 90
            center = 100, 100
            self.clock_canvas.create_oval(10, 10, 190, 190, outline="#333", width=3)

            self.clock_canvas.create_oval(15, 15, 185, 185, fill="#eea284", outline="#c0d6e4", width=1)

            for hour in range(1, 13):
                angle = math.radians(hour * 30)
                x = center[0] + radius * 0.75 * math.cos(angle - math.pi / 2)
                y = center[1] + radius * 0.75 * math.sin(angle - math.pi / 2)
                self.clock_canvas.create_text(x, y, text=str(hour), font=("Arial", 14, "bold"), fill="#333")

            for tick in range(60):
                angle = math.radians(tick * 6)
                outer_x = center[0] + radius * math.cos(angle - math.pi / 2)
                outer_y = center[1] + radius * math.sin(angle - math.pi / 2)
                inner_x = center[0] + (radius - 5 if tick % 5 == 0 else radius - 2) * math.cos(angle - math.pi / 2)
                inner_y = center[1] + (radius - 5 if tick % 5 == 0 else radius - 2) * math.sin(angle - math.pi / 2)
                color = "#555" if tick % 5 == 0 else "#aaa"
                self.clock_canvas.create_line(outer_x, outer_y, inner_x, inner_y, fill=color, width=1)

            self.clock_canvas.create_oval(95, 95, 105, 105, fill="#333", outline="#111")

            self.left_eye = self.clock_canvas.create_oval(70, 70, 90, 90, fill="white", outline="#333")  # \\ Left eye
            self.right_eye = self.clock_canvas.create_oval(110, 70, 130, 90, fill="white", outline="#333")  # \\ Right eye

            self.left_pupil = self.clock_canvas.create_oval(78, 78, 82, 82, fill="black")  # \\ Left pupil
            self.right_pupil = self.clock_canvas.create_oval(118, 78, 122, 82, fill="black")  # \\ Right pupil
            self.clock_canvas.create_arc(65, 90, 135, 140, start=200, extent=140, style="arc", outline="#333", width=2)

            self._update_googly_eyes()

        def _update_googly_eyes(self):
            """Update the position of the googly eyes dynamically."""

            def move_pupil(eye_center, pupil_radius, eye_radius):
                max_offset = eye_radius - pupil_radius
                offset_x = random.randint(-max_offset, max_offset)
                offset_y = random.randint(-max_offset, max_offset)
                return eye_center[0] + offset_x, eye_center[1] + offset_y

            left_eye_center = (80, 80)
            right_eye_center = (120, 80)
            pupil_radius = 4
            eye_radius = 10
            left_pupil_pos = move_pupil(left_eye_center, pupil_radius, eye_radius)
            right_pupil_pos = move_pupil(right_eye_center, pupil_radius, eye_radius)

            self.clock_canvas.coords(
                self.left_pupil,
                left_pupil_pos[0] - pupil_radius,
                left_pupil_pos[1] - pupil_radius,
                left_pupil_pos[0] + pupil_radius,
                left_pupil_pos[1] + pupil_radius,
            )

            self.clock_canvas.coords(
                self.right_pupil,
                right_pupil_pos[0] - pupil_radius,
                right_pupil_pos[1] - pupil_radius,
                right_pupil_pos[0] + pupil_radius,
                right_pupil_pos[1] + pupil_radius,
            )

            self.clock_canvas.after(200, self._update_googly_eyes)

        def _update_clock(self):
            """Update the analog clock hands with cooler visuals."""
            self.clock_canvas.delete("hands")
            self.clock_canvas.delete("hands_shadow")

            center = 100, 100
            radius = 90
            current_time = datetime.now()
            hour, minute, second = current_time.hour % 12, current_time.minute, current_time.second

            hour_angle = math.radians((hour + minute / 60) * 30)
            hour_x = center[0] + radius * 0.5 * math.cos(hour_angle - math.pi / 2)
            hour_y = center[1] + radius * 0.5 * math.sin(hour_angle - math.pi / 2)
            self.clock_canvas.create_line(center[0], center[1], hour_x, hour_y, fill="#333", width=6, tags="hands")

            minute_angle = math.radians((minute + second / 60) * 6)
            minute_x = center[0] + radius * 0.7 * math.cos(minute_angle - math.pi / 2)
            minute_y = center[1] + radius * 0.7 * math.sin(minute_angle - math.pi / 2)
            self.clock_canvas.create_line(center[0], center[1], minute_x, minute_y, fill="lime", width=4, tags="hands")

            second_angle = math.radians(second * 6)
            second_x = center[0] + radius * 0.85 * math.cos(second_angle - math.pi / 2)
            second_y = center[1] + radius * 0.85 * math.sin(second_angle - math.pi / 2)
            self.clock_canvas.create_line(center[0], center[1], second_x, second_y, fill="#ff5555", width=2, tags="hands")

            shadow_offset = 1
            self.clock_canvas.create_line(center[0] + shadow_offset, center[1] + shadow_offset, hour_x, hour_y,
                                        fill="#888", width=6, tags="hands_shadow")
            self.clock_canvas.create_line(center[0] + shadow_offset, center[1] + shadow_offset, minute_x, minute_y,
                                        fill="#aaa", width=4, tags="hands_shadow")
            self.clock_canvas.create_line(center[0] + shadow_offset, center[1] + shadow_offset, second_x, second_y,
                                        fill="#faa", width=2, tags="hands_shadow")

            self.clock_canvas.after(1000, self._update_clock)

    # #! Example 
    # if __name__ == "__main__":
    #     root = tk.Tk()
    #     root.title("Analog Clock Widget")
    #     clock_widget = Clocky(master=root)
    #     clock_widget.pack(padx=20, pady=20)
    #     root.mainloop()
