from GTG_Widgets import GTG 
from GTG_DateTime_Module import *
from GTG_imports import *
from GTG_Random_Modules import GTG_Random
from GTG_Extended_Widgets import GTGScrolledText


#! -------------- 

class FloatingDot:
    def __init__(self, canvas, x, y, radius, color, widget_class):
        """
        Represents a floating dot on the canvas.
        - canvas: The canvas where the dot is drawn.
        - x, y: The initial coordinates of the dot.
        - radius: The radius of the dot.
        - color: The color of the dot.
        - widget_class: The class of the widget (e.g., GTG.Button).
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.widget_class = widget_class
        self.name = widget_class.__name__  # Name of the widget to be displayed in a dot
        self.vx = GTG_Random.uniform(-2, 2)  # Horizontal velocity
        self.vy = GTG_Random.uniform(-2, 2)  # Vertical velocity

        # Create the dot
        self.id = canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius, fill=color, outline="black"
        )

        self.label = GTG.Label(
            canvas,  
            text=self.name,
            font=("Arial", 10, "bold"),
            fg="Black",
            bg=color,  # Match the dot's color
            padx=5,
            pady=2,
        )

        # Place the label on the canvas using create_window
        self.label_id = canvas.create_window(x, y, window=self.label)
        self.canvas.tag_bind(self.id, "<Button-1>", self.on_click)
        self.label.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        """Display a pop-up with the widget's source code and an example."""
        self.show_popup()

    def show_popup(self):
        """Create a pop-up window to display the widget's source code and an example."""
        popup = GTG.Toplevel(
            parent=self.canvas,
            enable_hover=False,  # Enable hover effects
            default_bg="#2b2b2b",  # Match the background color of your app
            hover_bg="#3b3b3b",  # Hover background color
            hover_highlight="#808080",  # Hover highlight color
            relief="ridge",  # Border style
            borderwidth=10,  # Border width
            highlightthickness=2  # Highlight thickness
        )
        popup.title(f"Source Code and Example: {self.widget_class.__name__}")
        popup.geometry("1200x600")

        # Frame for the source code
        code_frame = GTG.Frame(popup, bg="#2b2b2b")
        code_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        title_label = GTG.Label(
            code_frame,
            text=f"Source Code for {self.widget_class.__name__}",
            font=("Arial", 14, "bold"),
            background="#2b2b2b",
            foreground="white",
        )
        title_label.pack(pady=10)

        code_text = scrolledtext.ScrolledText(
            code_frame,
            wrap="word",
            font=("Courier New", 10),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            selectbackground="#3e3e3e",
        )
        code_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Retrieve and display the source code with syntax highlighting
        source_code = inspect.getsource(self.widget_class)
        self.highlight_syntax(code_text, source_code)

        # Generate and display example code for the widget
        example_code_frame = GTG.Frame(popup, bg="#2b2b2b")
        example_code_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        example_title_label = GTG.Label(
            example_code_frame,
            text=f"Example for {self.widget_class.__name__}",
            font=("Arial", 14, "bold"),
            background="#2b2b2b",
            foreground="white",
        )
        example_title_label.pack(pady=10)

        example_code_text = scrolledtext.ScrolledText(
            example_code_frame,
            wrap="word",
            font=("Courier New", 10),
            bg="#1e1e1e",
            fg="white",
            insertbackground="white",
            selectbackground="#3e3e3e",
        )
        example_code_text.pack(fill="both", expand=True, padx=10, pady=10)

        # Generate and display the example code
        example_code = self.generate_example_code()
        example_code_text.insert("end", example_code)

    def highlight_syntax(self, text_widget, source_code):
        """Highlight the syntax of the source code using Pygments."""
        lexer = PythonLexer()
        style = get_style_by_name('monokai')

        for token, content in lex(source_code, lexer):
            if token in Token.Comment:
                text_widget.insert("end", content, "comment")
            elif token in Token.Keyword:
                text_widget.insert("end", content, "keyword")
            elif token in Token.String:
                text_widget.insert("end", content, "string")
            elif token in Token.Name:
                text_widget.insert("end", content, "name")
            elif token in Token.Number:
                text_widget.insert("end", content, "number")
            else:
                text_widget.insert("end", content)

        # Configure tags for syntax highlighting
        text_widget.tag_configure("comment", foreground="#75715e")
        text_widget.tag_configure("keyword", foreground="#f92672")
        text_widget.tag_configure("string", foreground="#e6db74")
        text_widget.tag_configure("name", foreground="#a6e22e")
        text_widget.tag_configure("number", foreground="#ae81ff")

    def generate_example_code(self):
        """Dynamically generate an example usage code for the widget."""
        widget_class = self.widget_class
        example_code = ""

        # Inspect the widget's constructor (i.e., its parameters)
        constructor_params = inspect.signature(widget_class).parameters
        args = list(constructor_params.keys())

        # Start building the example based on constructor params
        example_code = f"# Example for {self.widget_class.__name__} widget\n"
        # example_code += f"# Instantiating {self.widget_class.__name__} with default values\n"
        
        # Generate the widget instantiation code dynamically
        example_code += f"{self.widget_class.__name__.lower()} = {widget_class.__name__}("

        # Iterate through constructor parameters to auto-generate the example
        for i, param in enumerate(args):
            if param == 'self':
                continue
            default_value = constructor_params[param].default
            if default_value is inspect.Parameter.empty:
                default_value = 'None'  # If no default value is specified, use None
            example_code += f"\n    {param}={default_value},"

        # Remove last comma and add closing parentheses
        example_code = example_code.rstrip(',') + "\n)"
        example_code += f"\n# {self.widget_class.__name__} example completed"

        return example_code
    
    def move(self):
        """Update the dot's position based on its velocity."""
        self.x += self.vx
        self.y += self.vy

        # Bounce off the walls
        if self.x - self.radius < 0 or self.x + self.radius > self.canvas.winfo_width():
            self.vx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > self.canvas.winfo_height():
            self.vy *= -1

        self.canvas.coords(self.id, self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)
        self.canvas.coords(self.label_id, self.x, self.y)

class FloatingDotApp:
    def __init__(self, root, width=1000, height=600):
        """
        Initialize the application.
        - root: The root Tkinter window.
        - width, height: Dimensions of the window.
        """
        self.root = root
        self.root.title("Work in progress")
        self.root.geometry(f"{width}x{height}")
        
        self.main_frame = GTG.Frame(self.root, bg="#353535")
        self.main_frame.pack(fill="both", expand=True)
       
        self.split_view = GTG.SplitView(self.main_frame, orientation="horizontal")
        self.split_view.pack(fill="both", expand=True)
        
        self.sidebar = GTG.Frame(self.split_view.pane1, width=200, bg="#434343", cursor="cross")
        self.sidebar.pack(side="left", fill="y", expand=False)
         
        self.canvas = GTG.Canvas(self.split_view.pane2, enable_hover=False, default_bg="#434343")
        self.canvas.pack(side="right", fill="both", expand=True)
        
        self.mouse_pos_label = GTG.Label(self.sidebar, text="Mouse Position: (0, 0)")
        self.mouse_pos_label.pack(pady=10)
        
        self.dot_positions_label = GTG.Label(self.sidebar, text="Dot Positions:")
        self.dot_positions_label.pack(pady=10)
        
        self.dot_positions_text = GTGScrolledText(
            self.sidebar,
            wrap="word",
            font=("Courier New", 10),
            height=10,
            width=25,
        )
        self.dot_positions_text.pack(pady=10, padx=5, fill="both", expand=True)

        self.canvas.bind("<Motion>", self.update_mouse_position)

        self.dots = []
        self.lines = []  # To store line IDs

        # Add dots for each widget in the GTG framework
        self.add_dot(100, 100, color="#ff0000", widget_class=GTG.Button) # \\ Red
        self.add_dot(200, 200, color="#0000ff", widget_class=GTG.Frame) # \\ Blue 
        self.add_dot(300, 300, color="#4eff41", widget_class=GTG.Label) # \\ Neon Green
        self.add_dot(400, 400, color="#b0b81e", widget_class=GTG.Entry) # Yellow
        self.add_dot(500, 500, color="#8b3eff", widget_class=GTG.Canvas) # \\ Purple 
        self.add_dot(300, 500, color="#aa5500", widget_class=GTG.Listbox) # \\ Brown
        self.add_dot(500, 500, color="#ff00ff", widget_class=GTG.Checkbutton) # \\ orange 
        self.add_dot(200, 320, color="#7d0002", widget_class=GTG.Toplevel) # \\Black
        self.add_dot(100, 400, color="#7a7a7a", widget_class=GTG.Scale) # \\ Gray
        self.add_dot(100, 200, color="#005500", widget_class=GTG.Scrollbar) # \\ Grass Green
        self.add_dot(100, 430, color="#aaaaff", widget_class=GTG.SplitView) # \\ Light Purple
        self.add_dot(100, 430, color="#ffbbf8", widget_class=GTG.Text) # \\ Light Pink 
        self.add_dot(100, 430, color="#ffedb5", widget_class=GTG.Notebook)
        self.add_dot(100, 430, color="#00ffff", widget_class=GTG.StringVar)

        # FPS control
        self.fps = 120  # Default FPS
        self.fps_scale = GTG.Scale(self.sidebar, from_=10, to=120, orient="horizontal", label="FPS", command=self.update_fps)
        self.fps_scale.set(self.fps)
        self.fps_scale.pack(pady=10)
        
        self.size_scale = GTG.Scale(self.sidebar, from_=5, to=35, orient="horizontal", label="Size Scale", command=self.update_dot_size)
        self.size_scale.pack(pady=10)
        
        self.animate()

    def update_fps(self, value):
        """Update the FPS based on the slider value."""
        self.fps = int(value)

    def update_dot_size(self, value):
        """Update the size of the dots based on the slider value."""
        new_radius = int(value)
        for dot in self.dots:
            dot.radius = new_radius
            dot.canvas.coords(dot.id, dot.x - new_radius, dot.y - new_radius, dot.x + new_radius, dot.y + new_radius)

    def add_dot(self, x, y, radius=10, color="red", widget_class=None):
        """
        Add a floating dot to the canvas.
        - x, y: Initial coordinates of the dot.
        - radius: Radius of the dot.
        - color: Color of the dot.
        - widget_class: The class of the widget (e.g., GTG.Button).
        """
        if widget_class is None:
            raise ValueError("widget_class must be provided")
        dot = FloatingDot(self.canvas, x, y, radius, color, widget_class)
        self.dots.append(dot)

    def animate(self):
        """Update the positions of all dots and redraw the canvas."""
        for dot in self.dots:
            dot.move()

        self.update_dot_positions()
        self.draw_lines()

        self.root.after(int(1000 / self.fps), self.animate)

    def draw_lines(self):
        """Draw lines between the dots."""
        self.canvas.delete("line")  # Clear previous lines
        for i in range(len(self.dots)):
            for j in range(i + 1, len(self.dots)):
                x1, y1 = self.dots[i].x, self.dots[i].y
                x2, y2 = self.dots[j].x, self.dots[j].y
                self.canvas.create_line(x1, y1, x2, y2, fill="gray", tags="line")

    def update_mouse_position(self, event):
        """Update the mouse position label."""
        self.mouse_pos_label.config(text=f"Mouse Position: ({event.x}, {event.y})")

    def update_dot_positions(self):
        """Update the dot positions in the sidebar."""
        self.dot_positions_text.delete(1.0, tk.END)  # Clear previous content
        for dot in self.dots:
            self.dot_positions_text.insert(
                tk.END,
                f"{dot.name}: ({int(dot.x)}, {int(dot.y)})\n"
            )

def Example():
    root = tk.Tk()
    app = FloatingDotApp(root)
    root.mainloop()

if __name__ == "__main__":
    Example()