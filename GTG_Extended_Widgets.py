from GTG_imports import * 
from GTG_Widgets import GTG , GTGDateTime

#! ------------------------------------ Custom Widgets Made With GTG Gui ----------------------------------------------------------------------------------
    
class FileDialog(GTG.Toplevel):
    def __init__(self, parent, initialdir=None, title="Select File"):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x300")
        self.file_path = None

        self.initialdir = initialdir if initialdir else os.getcwd()
        self.current_dir = self.initialdir

        self.create_widgets()

    def create_widgets(self):
        # \\ Frame for directory navigation
        nav_frame = GTG.Frame(self)
        nav_frame.pack(fill=tk.X, padx=5, pady=5)

        self.up_button = GTG.Button(nav_frame, text="Up", command=self.go_up)
        self.up_button.pack(side=tk.LEFT, padx=5)

        self.dir_label = GTG.Label(nav_frame, text=self.current_dir)
        self.dir_label.pack(side=tk.LEFT, expand=True, fill=tk.X)

        # \\ Listbox to display files and directories
        self.listbox = GTG.Listbox(self)
        self.listbox.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.listbox.bind("<Double-Button-1>", self.on_double_click)

        # \\ Buttons for selection
        button_frame = GTG.Frame(self)
        button_frame.pack(fill=tk.X, padx=5, pady=5)

        self.select_button = GTG.Button(button_frame, text="Select", command=self.on_select)
        self.select_button.pack(side=tk.RIGHT, padx=5)

        self.cancel_button = GTG.Button(button_frame, text="Cancel", command=self.destroy)
        self.cancel_button.pack(side=tk.RIGHT, padx=5)

        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, "..")  # \\ Add "up" directory
        for item in os.listdir(self.current_dir):
            self.listbox.insert(tk.END, item)

    def go_up(self):
        new_dir = os.path.dirname(self.current_dir)
        if os.path.exists(new_dir):
            self.current_dir = new_dir
            self.dir_label.config(text=self.current_dir)
            self.update_listbox()

    def on_double_click(self, event):
        selected = self.listbox.get(self.listbox.curselection())
        new_path = os.path.join(self.current_dir, selected)
        if os.path.isdir(new_path):
            self.current_dir = new_path
            self.dir_label.config(text=self.current_dir)
            self.update_listbox()

    def on_select(self):
        selected = self.listbox.get(self.listbox.curselection())
        self.file_path = os.path.join(self.current_dir, selected)
        self.destroy()

    def get_file_path(self):
        return self.file_path

#! ----------------------------------------------------------------------------------------------------------------------
    


#! -------------------------------------------- Extended Widgets (GT) Made With GTG -----------------------------------------------------------------------------

class Tooltip:
    def __init__(self, widget, text, delay=500, bg="#ffffe0", fg="black", font=("Arial", 10), borderwidth=1, relief="solid"):
        """
        Initialize the Tooltip.

        Parameters:
            widget: The widget to which the tooltip is attached.
            text (str): The text to display in the tooltip.
            delay (int): Delay in milliseconds before the tooltip appears.
            bg (str): Background color of the tooltip.
            fg (str): Foreground (text) color of the tooltip.
            font (tuple): Font style and size for the tooltip text.
            borderwidth (int): Border width of the tooltip.
            relief (str): Border style of the tooltip (e.g., "solid", "raised").
        """
        self.widget = widget
        self.text = text
        self.delay = delay
        self.bg = bg
        self.fg = fg
        self.font = font
        self.borderwidth = borderwidth
        self.relief = relief
        self.tooltip = None
        self.tooltip_id = None

        # \\ Bind events
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)
        self.widget.bind("<ButtonPress>", self.on_leave)

    def on_enter(self, event=None):
        """Schedule the tooltip to appear after a delay."""
        self.tooltip_id = self.widget.after(self.delay, self.show_tooltip)

    def on_leave(self, event=None):
        """Hide the tooltip and cancel the scheduled appearance."""
        if self.tooltip_id:
            self.widget.after_cancel(self.tooltip_id)
            self.tooltip_id = None
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    def show_tooltip(self):
        """Display the tooltip."""
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)  # Remove window decorations
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = GTG.Label(
            self.tooltip,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            relief=self.relief,
            borderwidth=self.borderwidth
        ) 
        label.pack()

#! ----------------------------------------------------------------------------------------------------------------------
class SidePanel:
    def __init__(self, root, width=200, height=500, x=0, y=0, bg="gray", open_state=True, Frame="raised"):
        self.root = root
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.bg = bg
        self.open_state = open_state
        self.relief = Frame  
        self.panel = None
        self.toggle_button = None
        self.animating = False
        self.dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0

    def _build(self):
        self.panel = GTG.Frame(self.root, width=self.width, height=self.height, bg=self.bg,
                            relief=self.relief, borderwidth=10 , enable_hover=False)
        self.panel.place(x=self.x if self.open_state else -self.width, y=self.y)

        self.toggle_button = GTG.Button(self.root, text="☰", command=self.toggle_panel, bg=self.bg)
        self.toggle_button.place(x=self.x + self.width + 500, y=self.y + 10)


        self.toggle_button.bind("<ButtonPress-1>", self.start_drag)
        self.toggle_button.bind("<B1-Motion>", self.on_drag)
        self.toggle_button.bind("<ButtonRelease-1>", self.stop_drag)

    def toggle_panel(self):
        if self.animating:
            return

        target_x = self.x if not self.open_state else -self.width
        self.animate_panel(target_x)
        self.open_state = not self.open_state

    def animate_panel(self, target_x):
        self.animating = True
        current_x = self.panel.winfo_x()

        if current_x == target_x:
            self.animating = False
            return

        step = 20 if target_x > current_x else -20
        next_x = current_x + step

        if (step > 0 and next_x > target_x) or (step < 0 and next_x < target_x):
            next_x = target_x

        self.panel.place(x=next_x, y=self.y)
        self.root.after(10, lambda: self.animate_panel(target_x))

    def add_widget(self, widget):
        widget._build(self.panel)

    def start_drag(self, event):
        self.dragging = True
        self.drag_offset_x = event.x
        self.drag_offset_y = event.y

    def on_drag(self, event):
        if self.dragging:
            new_x = self.toggle_button.winfo_x() + (event.x - self.drag_offset_x)
            new_y = self.toggle_button.winfo_y() + (event.y - self.drag_offset_y)
            self.toggle_button.place(x=new_x, y=new_y)

    def stop_drag(self, event):
        self.dragging = False 

#! ----------------------------------------------------------------------------------------------------------------------

class GTGScrolledText(GTG.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        # \\ Create a Text widget
        self.text = GTG.Text(self, **kwargs)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # \\ Create a Scrollbar
        self.scrollbar = GTG.Scrollbar(self, command=self.text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # \\ Link the scrollbar to the text widget
        self.text.config(yscrollcommand=self.scrollbar.set)

    def insert(self, *args):
        """Forward the insert method to the Text widget."""
        self.text.insert(*args)

    def delete(self, *args):
        """Forward the delete method to the Text widget."""
        self.text.delete(*args)

    def get(self, *args):
        """Forward the get method to the Text widget."""
        return self.text.get(*args) 
 #! ----------------------------------------------------------------------------------------------------------------------   
import math
class CircularSlider(tk.Canvas):
    def __init__(self, parent, radius=50, min_value=0, max_value=100, start_angle=-90, tick_count=10, knob_shape="circle", knob_image=None, **kwargs):
        super().__init__(parent, width=2*radius+20, height=2*radius+20, bg=kwargs.get('bg', 'white'), highlightthickness=0)
        
        self.radius = radius
        self.min_value = min_value
        self.max_value = max_value
        self.start_angle = start_angle
        self.angle = start_angle
        self.knob_radius = kwargs.get('knob_radius', 10)
        self.value = min_value
        self.tick_count = tick_count
        self.knob_shape = knob_shape
        self.knob_image_path = knob_image
        self.knob_image = None
        
        if self.knob_image_path:
            image = Image.open(self.knob_image_path)
            image = image.resize((2*self.knob_radius, 2*self.knob_radius), Image.LANCZOS)
            self.knob_image = ImageTk.PhotoImage(image)
        
        self.center = (self.radius + 10, self.radius + 10)
        
        self.track_color = kwargs.get('track_color', '#7f7f7f')
        self.knob_color = kwargs.get('knob_color', 'black')
        self.tick_color = kwargs.get('tick_color', 'black')
        
        self.draw_slider()
        self.bind("<B1-Motion>", self.move_knob)
        self.bind("<Button-1>", self.move_knob)
    
    def draw_slider(self):
        self.delete("all")
        
        self.create_oval(10, 10, 10 + 2*self.radius, 10 + 2*self.radius, outline=self.track_color, width=5)
        self.draw_ticks()
        
        knob_x = self.center[0] + self.radius * math.cos(math.radians(self.angle))
        knob_y = self.center[1] + self.radius * math.sin(math.radians(self.angle))
        
        if self.knob_image:
            self.create_image(knob_x, knob_y, image=self.knob_image, tags="knob")
        elif self.knob_shape == "circle":
            self.create_oval(knob_x - self.knob_radius, knob_y - self.knob_radius,
                             knob_x + self.knob_radius, knob_y + self.knob_radius,
                             fill=self.knob_color, outline="black", width=2, tags="knob")
        elif self.knob_shape == "square":
            self.create_rectangle(knob_x - self.knob_radius, knob_y - self.knob_radius,
                                  knob_x + self.knob_radius, knob_y + self.knob_radius,
                                  fill=self.knob_color, outline="black", width=2, tags="knob")
    
    def draw_ticks(self):
        for i in range(self.tick_count):
            tick_angle = self.start_angle + (i / (self.tick_count - 1)) * 360
            inner_x = self.center[0] + (self.radius - 10) * math.cos(math.radians(tick_angle))
            inner_y = self.center[1] + (self.radius - 10) * math.sin(math.radians(tick_angle))
            outer_x = self.center[0] + self.radius * math.cos(math.radians(tick_angle))
            outer_y = self.center[1] + self.radius * math.sin(math.radians(tick_angle))
            self.create_line(inner_x, inner_y, outer_x, outer_y, fill=self.tick_color, width=2)
    
    def move_knob(self, event):
        dx, dy = event.x - self.center[0], event.y - self.center[1]
        angle = math.degrees(math.atan2(dy, dx))
        
        if angle < 0:
            angle += 360
        
        self.angle = angle
        self.value = self.min_value + ((self.angle - self.start_angle) % 360) / 360 * (self.max_value - self.min_value)
        
        self.draw_slider()
        print(f"Value: {self.get_value()}")
    
    def get_value(self):
        return round(self.value)
