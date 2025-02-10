from GTG_imports import tk , ttk 
from GTG_imports import *
from PyGTG.Modules.GTG_DateTime_Module import *

#! ----------------------------------- Start of Main Widgets (tk ,ttk) ----------------------------------------------------------------      
   
class GTG:
  
    class Button(tk.Button):
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, frame=None, image_path=None, font=None, borderwidth=10, link=None, **kwargs):
            super().__init__(parent, **kwargs)
            
            # \\ Default values \\ 
            self.default_bg = "#7f7f7f"
            self.default_fg = "Black"
            self.default_hover_bg = "light gray"
            self.default_hover_fg = "white"
            self.default_frame = "ridge"  
            self.default_font = ("Arial", 12, "bold")  # \\ Default font
            self.default_borderwidth = 10  # \\ Default borderwidth
            
            # \\ Customizable values \\ 
            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
            self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg
            self.frame = frame if frame is not None else self.default_frame
            self.font = font if font is not None else self.default_font
            self.borderwidth = borderwidth  # \\ Custom borderwidth
            
            # \\ Image handling \\ 
            self.image = None
            self.image_path = image_path
            if self.image_path:
                self.load_image()  
            
            self.link = link  # \\ Store the link 
            self.enable_hover = enable_hover
            
            # \\ Configure the button style \\ 
            self.configure(
                bg=self.bg,  
                fg=self.fg,   
                relief=self.frame,
                font=self.font,  
                activebackground="darkgray",  
                activeforeground="white",  
                borderwidth=self.borderwidth,
                highlightthickness=0, 
                pady=5, padx=10,
                **kwargs 
            )
            
            # \\ Bind hover events if enabled \\ 
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover) 
                self.bind("<Leave>", self.on_leave)
            
            # \\ Bind Click event to open link \\ 
            if self.link:
                self.bind("<Button>" , self.on_click)

        def load_image(self):
            """Load and resize the image to fit the button size."""
            try:
                pil_image = Image.open(self.image_path)
                pil_image = pil_image.resize((self["width"], self["height"]))
                self.image = ImageTk.PhotoImage(pil_image)
                self.config(image=self.image)
            except Exception as e:
                print(f"Error loading image: {e}")

        def on_hover(self, event):
            """Change button appearance on hover."""
            if self.enable_hover:
                self.configure(bg=self.hover_bg, fg=self.hover_fg, relief="raised", borderwidth=self.borderwidth)  

        def on_leave(self, event):
            """Revert button appearance when not hovering."""
            if self.enable_hover:
                self.configure(bg=self.bg, fg=self.fg, relief=self.frame, borderwidth=self.borderwidth)  
        
        def on_click(self, event):
            """Open the link in the default web browser when the button is clicked."""
            if self.link:
                webbrowser.open(self.link)
        
        def toggle_text(self, new_text):
            """Change the button's text.""" 
            self.config(text=new_text)

#! -------------------------------------------------------------------------------------------------------------------------
    
    class Label(tk.Label):
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, 
                    font=None, borderwidth=None, frame=None, padx=None, pady=None, **kwargs):
            super().__init__(parent, **kwargs)
            
            #* \\ Default values \\
            self.default_bg = "#7f7f7f"
            self.default_fg = "Black"
            self.default_hover_bg = "#e0e0e0"
            self.default_hover_fg = fg if fg is not None else self.default_fg
            self.default_font = ("Arial", 12)
            self.default_borderwidth = 5
            self.default_frame = "sunken"
            self.default_padx = 10
            self.default_pady = 5
            
            #* \\ Customizable properties \\
            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
            self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg
            self.font = font if font is not None else self.default_font
            self.borderwidth = borderwidth if borderwidth is not None else self.default_borderwidth
            self.relief = frame if frame is not None else self.default_frame
            self.padx = padx if padx is not None else self.default_padx
            self.pady = pady if pady is not None else self.default_pady
            
            self.enable_hover = enable_hover
            
            #* \\ Configure the label \\
            self.configure(
                bg=self.bg,
                fg=self.fg,
                font=self.font,
                borderwidth=self.borderwidth,
                relief=self.relief,
                padx=self.padx,
                pady=self.pady
            )
            
            #* \\ Bind hover events if enabled \\
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg=self.hover_bg, fg=self.hover_fg)

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg, fg=self.fg)

    
#! -------------------------------------------------------------------------------------------------------------------------   
    
    class Frame(tk.Frame):
        def __init__(self, parent, enable_hover=False, bg=None, highlightbackground=None, hover_bg=None, 
                    hover_highlight=None, relief="ridge", borderwidth=None, hover_borderwidth=None, 
                    padx=None, pady=None, hover_padx=None, hover_pady=None, cursor=None, 
                    animation_speed=10, **kwargs):
            super().__init__(parent, **kwargs)
            
            #* \\ Default values \\ 
            self.default_bg = "#d9d9d9"
            self.default_highlight = "#a0a0a0"
            self.default_hover_bg = "#c0c0c0"
            self.default_hover_highlight = "#808080"
            self.default_borderwidth = 5
            self.default_padx = 0
            self.default_pady = 0
            self.default_cursor = "arrow"
            
            #* \\ Customizable properties \\
            self.bg_color = bg if bg is not None else self.default_bg
            self.highlight_color = highlightbackground if highlightbackground is not None else self.default_highlight
            self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
            self.hover_highlight = hover_highlight if hover_highlight is not None else self.default_hover_highlight
            self.borderwidth = borderwidth if borderwidth is not None else self.default_borderwidth
            self.hover_borderwidth = hover_borderwidth if hover_borderwidth is not None else self.borderwidth
            self.padx = padx if padx is not None else self.default_padx
            self.pady = pady if pady is not None else self.default_pady
            self.hover_padx = hover_padx if hover_padx is not None else self.padx
            self.hover_pady = hover_pady if hover_pady is not None else self.pady
            self.cursor = cursor if cursor is not None else self.default_cursor
            self.animation_speed = animation_speed
            self.enable_hover = enable_hover
        
            self.configure_frame()
            
            #* \\ Bind hover events if enabled
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def configure_frame(self):
            """Configure the frame's appearance."""
            self.configure(
                bg=self.bg_color,
                relief="ridge",
                borderwidth=self.borderwidth,
                highlightthickness=2,
                highlightbackground=self.highlight_color,
                padx=self.padx,
                pady=self.pady,
                cursor=self.cursor
            )

        def on_hover(self, event):
            """Handle hover events."""
            if self.enable_hover:
                self.animate_color(self.bg_color, self.hover_bg, self.highlight_color, self.hover_highlight)
                self.configure(padx=self.hover_padx, pady=self.hover_pady, borderwidth=self.hover_borderwidth)

        def on_leave(self, event):
            """Handle leave events."""
            if self.enable_hover:
                self.animate_color(self.hover_bg, self.bg_color, self.hover_highlight, self.highlight_color)
                self.configure(padx=self.padx, pady=self.pady, borderwidth=self.borderwidth)

        def animate_color(self, from_bg, to_bg, from_highlight, to_highlight):
            """Smoothly animate the background and highlight colors."""
            steps = 10
            delta_bg = self.calculate_color_delta(from_bg, to_bg, steps)
            delta_highlight = self.calculate_color_delta(from_highlight, to_highlight, steps)
            
            def update_step(step):
                if step < steps:
                    new_bg = self.interpolate_color(from_bg, delta_bg, step)
                    new_highlight = self.interpolate_color(from_highlight, delta_highlight, step)
                    self.configure(bg=new_bg, highlightbackground=new_highlight)
                    self.after(self.animation_speed, update_step, step + 1)
            
            update_step(0)

        def calculate_color_delta(self, from_color, to_color, steps):
            """Calculate the color delta for each step."""
            return [
                (int(to_color[i:i+2], 16) - int(from_color[i:i+2], 16)) / steps
                for i in range(1, 7, 2)
            ]

        def interpolate_color(self, start, delta, step):
            """Interpolate between two colors."""
            return "#{:02x}{:02x}{:02x}".format(
                int(start[1:3], 16) + int(delta[0] * step),
                int(start[3:5], 16) + int(delta[1] * step),
                int(start[5:7], 16) + int(delta[2] * step)
            )
#! -------------------------------------------------------------------------------------------------------------------------  

    class Canvas(tk.Canvas):
        def __init__(self, parent, enable_hover=False, hover_bg="#c0c0c0", default_bg="#d9d9d9", width=400, height=400, **kwargs):
            super().__init__(parent, **kwargs)
            self.enable_hover = enable_hover
            self.hover_bg = hover_bg
            self.default_bg = default_bg
            self.configure(
                bg=self.default_bg,  
                bd=5,           
                relief="ridge", 
                width=width,      
                height=height      
            )
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)
        
        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg=self.hover_bg)  

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.default_bg)  

        def draw_rectangle(self, x1, y1, x2, y2, **kwargs):
            """Draws a rectangle on the canvas.

            Args:
                x1, y1, x2, y2 (int): Coordinates of the rectangle.
                **kwargs: Additional arguments for the rectangle (e.g., fill, outline).
            
            Returns:
                int: The ID of the rectangle object.
            """
            return self.create_rectangle(x1, y1, x2, y2, **kwargs)

        def draw_circle(self, x, y, radius, **kwargs):
            """Draws a circle on the canvas.
            
            Args:
                x, y (int): Coordinates of the center of the circle.
                radius (int): Radius of the circle.
                **kwargs: Additional arguments for the circle (e.g., fill, outline).
            
            Returns:
                int: The ID of the circle object.
            """
            return self.create_oval(x-radius, y-radius, x+radius, y+radius, **kwargs)

        def draw_line(self, x1, y1, x2, y2, **kwargs):
            """Draws a line on the canvas.
            
            Args:
                x1, y1, x2, y2 (int): Coordinates of the line.
                **kwargs: Additional arguments for the line (e.g., fill, width).
            
            Returns:
                int: The ID of the line object.
            """
            return self.create_line(x1, y1, x2, y2, **kwargs)

        def draw_polygon(self, points, **kwargs):
            """Draws a polygon on the canvas.
            
            Args:
                points (list of tuples): List of (x, y) coordinates for the polygon.
                **kwargs: Additional arguments for the polygon (e.g., fill, outline).
            
            Returns:
                int: The ID of the polygon object.
            """
            return self.create_polygon(points, **kwargs)

        def draw_text(self, x, y, text, **kwargs):
            """Draws text on the canvas.
            
            Args:
                x, y (int): Coordinates of the text.
                text (str): The text to display.
                **kwargs: Additional arguments for the text (e.g., font, fill).
            
            Returns:
                int: The ID of the text object.
            """
            return self.create_text(x, y, text=text, **kwargs)

        def clear_canvas(self):
            """Clears all objects from the canvas."""
            self.delete("all")

        def set_background_color(self, color):
            """Sets the background color of the canvas.
            
            Args:
                color (str): The color to set as the background.
            """
            self.configure(bg=color)

        def set_hover_color(self, color):
            """Sets the hover color of the canvas.
            
            Args:
                color (str): The color to set as the hover background.
            """
            self.hover_bg = color

        def set_default_color(self, color):
            """Sets the default color of the canvas.
            
            Args:
                color (str): The color to set as the default background.
            """
            self.default_bg = color
            self.configure(bg=color)


#! -------------------------------------------------------------------------------------------------------------------------   
    
    class Entry(tk.Entry):
        def __init__(self, parent, enable_hover=True, **kwargs):
        
            self.hover_bg = kwargs.pop("hover_bg", None)
            self.hover_fg = kwargs.pop("hover_fg", None)
            self.hover_highlightbackground = kwargs.pop("hover_highlightbackground", None)
            self.hover_highlightcolor = kwargs.pop("hover_highlightcolor", None)

            super().__init__(parent, **kwargs)

            #* \\ Default styles
            self.default_bg = self.cget("bg")
            self.default_fg = self.cget("fg")
            self.default_highlightbackground = self.cget("highlightbackground")
            self.default_highlightcolor = self.cget("highlightcolor")

            #* \\ Enable hover effects
            self.enable_hover = enable_hover
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                if self.hover_bg:
                    self.configure(bg=self.hover_bg)
                if self.hover_fg:
                    self.configure(fg=self.hover_fg)
                if self.hover_highlightbackground:
                    self.configure(highlightbackground=self.hover_highlightbackground)
                if self.hover_highlightcolor:
                    self.configure(highlightcolor=self.hover_highlightcolor)

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(
                    bg=self.default_bg,
                    fg=self.default_fg,
                    highlightbackground=self.default_highlightbackground,
                    highlightcolor=self.default_highlightcolor
                )
    
#! -------------------------------------------------------------------------------------------------------------------------
    
    class Toplevel(tk.Toplevel):
        def __init__(self, parent, enable_hover=False, default_bg="#7f7f7f", default_highlight="#a0a0a0",
                    hover_bg="#e0e0e0", hover_highlight="#808080", relief="ridge", borderwidth=10,
                    highlightthickness=2, **kwargs):
            super().__init__(parent, **kwargs)
 
            # \\ Customizable attributes
            self.default_bg = default_bg
            self.default_highlight = default_highlight
            self.hover_bg = hover_bg
            self.hover_highlight = hover_highlight
            self.iconbitmap('Assets/FaceLogo.ico')
            # \\ Configure the window's appearance
            self.configure(
                bg=self.default_bg,
                relief=relief,
                borderwidth=borderwidth,
                highlightthickness=highlightthickness,
                highlightbackground=self.default_highlight
            )
            self.enable_hover = enable_hover

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            """Hover effect: Change background color on mouse enter"""
            if self.enable_hover:
                self.configure(bg=self.hover_bg, highlightbackground=self.hover_highlight)

        def on_leave(self, event):
            """Reset background color when mouse leaves"""
            if self.enable_hover:
                self.configure(bg=self.default_bg, highlightbackground=self.default_highlight)
#! -------------------------------------------------------------------------------------------------------------------------
    
    class Scale(tk.Scale):
        def __init__(self, parent, enable_hover=True, enable_click_effect=True, show_value=True, **kwargs):
            super().__init__(parent, **kwargs)

            self.default_bg = "#d9d9d9"
            self.default_fg = "black"
            self.default_highlight = "#a0a0a0"
            self.hover_bg = "#e0e0e0"
            self.hover_highlight = "#808080"
            self.click_bg = "#c0c0c0"
            self.click_highlight = "#606060"

            self.configure(
                bg=self.default_bg,
                fg=self.default_fg,
                relief="ridge",
                troughcolor="#cccccc",
                highlightthickness=2,
                highlightbackground=self.default_highlight,
                font=("Arial", 12),
                sliderrelief="raised",
                sliderlength=20,
                orient=tk.HORIZONTAL,
                showvalue=show_value  
            )

            self.enable_hover = enable_hover
            self.enable_click_effect = enable_click_effect

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

            if self.enable_click_effect:
                self.bind("<ButtonPress-1>", self.on_click)
                self.bind("<ButtonRelease-1>", self.on_release)

        def on_hover(self, event):
            self.configure(bg=self.hover_bg, highlightbackground=self.hover_highlight)

        def on_leave(self, event):
            self.configure(bg=self.default_bg, highlightbackground=self.default_highlight)

        def on_click(self, event):
            self.configure(bg=self.click_bg, highlightbackground=self.click_highlight)

        def on_release(self, event):
            if self.enable_hover:
                self.configure(bg=self.hover_bg, highlightbackground=self.hover_highlight)
            else:
                self.configure(bg=self.default_bg, highlightbackground=self.default_highlight)

        def set_orientation(self, orientation):
            """Set the orientation of the Scale (horizontal or vertical)"""
            self.configure(orient=orientation)

        def set_colors(self, bg=None, fg=None, troughcolor=None, hover_bg=None, hover_highlight=None, click_bg=None, click_highlight=None):
            """Customize the colors of the Scale"""
            if bg:
                self.default_bg = bg
                self.configure(bg=bg)
            if fg:
                self.default_fg = fg
                self.configure(fg=fg)
            if troughcolor:
                self.configure(troughcolor=troughcolor)
            if hover_bg:
                self.hover_bg = hover_bg
            if hover_highlight:
                self.hover_highlight = hover_highlight
            if click_bg:
                self.click_bg = click_bg
            if click_highlight:
                self.click_highlight = click_highlight

        def toggle_value_display(self, show_value):
            """Toggle the display of the slider's value"""
            self.configure(showvalue=show_value)

#! -------------------------------------------------------------------------------------------------------------------------
    
    class MessageBox(Toplevel):
        def __init__(self, parent, title, message, message_type="info", buttons=["OK"], **kwargs):
            super().__init__(parent, **kwargs)
            self.parent = parent
            self.title(title)
            self.message = message
            self.message_type = message_type
            self.buttons = buttons

            self.configure(bg="#7f7f7f", padx=20, pady=20)
            self.resizable(False, False)

            self.create_widgets()

        def create_widgets(self):
            message_label = GTG.Label(self, text=self.message, bg="#7f7f7f", fg="red", font=("Arial", 12))
            message_label.pack(pady=10)

            button_frame = GTG.Frame(self, bg="#7f7f7f" , enable_hover=False)
            button_frame.pack(pady=10)

            for button_text in self.buttons:
                button = GTG.Button(button_frame, text=button_text, command=lambda bt=button_text: self.on_button_click(bt) ,bg="red")
                button.pack(side=tk.LEFT, padx=5)

        def on_button_click(self, button_text):
            """Handle button clicks and close the message box."""
            self.destroy()
            return button_text

    # \\ Helper methods for common message box types
    @staticmethod
    def showinfo(parent, title, message):
        """Display an info message box."""
        dialog = GTG.MessageBox(parent, title, message, message_type="info")
        parent.wait_window(dialog)

    @staticmethod
    def showerror(parent, title, message):
        """Display an error message box."""
        dialog = GTG.MessageBox(parent, title, message, message_type="error")
        parent.wait_window(dialog)

    @staticmethod
    def showwarning(parent, title, message):
        """Display a warning message box."""
        dialog = GTG.MessageBox(parent, title, message, message_type="warning")
        parent.wait_window(dialog)

    @staticmethod
    def askyesno(parent, title, message):
        """Display a yes/no confirmation dialog."""
        dialog = GTG.MessageBox(parent, title, message, buttons=["Yes", "No"])
        return dialog.on_button_click("Yes") if dialog.on_button_click("Yes") else False

    @staticmethod
    def askokcancel(parent, title, message):
        """Display an OK/Cancel confirmation dialog."""
        dialog = GTG.MessageBox(parent, title, message, buttons=["OK", "Cancel"])
        return dialog.on_button_click("OK") if dialog.on_button_click("OK") else False



#! -------------------------------------------------------------------------------------------------------------------------
    
    class Spinbox(tk.Spinbox):
        def __init__(self, parent, enable_hover=True, **kwargs):
            super().__init__(parent, **kwargs)
            self.enable_hover = enable_hover
            self.configure(
                bg="white",
                fg="black",
                font=("Arial", 12),
                relief="sunken",
                borderwidth=5
            )
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg="#f0f0f0")

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg="white")

#! -------------------------------------------------------------------------------------------------------------------------
    
    class Menu(tk.Menu):
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, **kwargs):
            super().__init__(parent, **kwargs)

            self.default_bg = "#7f7f7f"
            self.default_fg = "Black"
            self.default_hover_bg = "light gray"
            self.default_hover_fg = "white"

            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
            self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg

            self.enable_hover = enable_hover
            self.configure(tearoff=0) 
            self.configure(
                bg=self.bg,
                fg=self.fg,
                activebackground=self.hover_bg,
                activeforeground=self.hover_fg,
                relief="raised",
                font=("Arial", 12)
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg=self.hover_bg, fg=self.hover_fg)

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg, fg=self.fg)

        def add_command(self, label, command=None, **kwargs):
            """Add a command to the menu."""
            super().add_command(label=label, command=command, **kwargs) 
            
        def add_cascade(self, label, menu=None, **kwargs):
            """Add a cascade menu."""
            super().add_cascade(label=label, menu=menu, **kwargs)  

        def add_separator(self):
            """Add a separator to the menu."""
            super().add_separator()  
        
        def add_checkbutton(self, label, command=None, **kwargs):
            """Add a checkbutton to the menu."""
            super().add_checkbutton(label=label, command=command, **kwargs)  

        def add_radiobutton(self, label, command=None, **kwargs):
            """Add a radiobutton to the menu."""
            super().add_radiobutton(label=label, command=command, **kwargs) 


#! -------------------------------------------------------------------------------------------------------------------------   
    
    class Radiobutton(tk.Radiobutton):
        def __init__(self, parent, text, variable, value, enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, **kwargs):
            super().__init__(parent, text=text, variable=variable, value=value, **kwargs)
            
            self.default_bg = "#7f7f7f"
            self.default_fg = "black"
            self.default_hover_bg = "light gray"
            self.default_hover_fg = "white"

            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
            self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg

            self.enable_hover = enable_hover

            self.configure(
                bg=self.bg,
                fg=self.fg,
                activebackground=self.hover_bg,
                activeforeground=self.hover_fg,
                font=("Arial", 12),
                selectcolor=self.bg
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg=self.hover_bg, fg=self.hover_fg)

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg, fg=self.fg)
    
#! -------------------------------------------------------------------------------------------------------------------------   
    
    class Notebook(ttk.Notebook):
        def __init__(self, parent, enable_hover=True, hover_background="light gray", 
                    default_background="#7f7f7f", foreground="black", font=("Arial", 12), **kwargs):
            super().__init__(parent, **kwargs)
            self.enable_hover = enable_hover
            self.hover_background = hover_background
            self.default_background = default_background
            self.foreground = foreground
            self.font = font

            # \\ Configure the style for the notebook
            self.style = ttk.Style()
            self.style.theme_use("alt")
            # \\ Configure the default tab style
            self.style.configure("Custom.TNotebook", background=self.default_background)
            self.style.configure("Custom.TNotebook.Tab", 
                                background=self.default_background, 
                                foreground=self.foreground, 
                                font=self.font,
                                padding=[10, 5])  # \\ Add padding to tabs

            # \\ Configure the hover effect for tabs
            if self.enable_hover:
                self.style.map("Custom.TNotebook.Tab",
                            background=[("active", self.hover_background),
                                        ("!active", self.default_background)])

            # \\ Apply the custom style to the notebook
            self.configure(style="Custom.TNotebook")

            # \\ Bind events for dragging tabs
            self.bind("<ButtonPress-1>", self.on_tab_press)
            self.bind("<ButtonRelease-1>", self.on_tab_release)
            self.bind("<B1-Motion>", self.on_tab_drag)

            # \\ Bind double-click event for renaming tabs
            self.bind("<Double-1>", self.on_tab_double_click)

            self.dragged_tab = None

        def on_tab_press(self, event):
            """Called when a tab is clicked."""
            tab_index = self.index(f"@{event.x},{event.y}")
            if tab_index != -1:
                self.dragged_tab = tab_index

        def on_tab_release(self, event):
            """Called when the mouse button is released."""
            self.dragged_tab = None

        def on_tab_drag(self, event):
            """Called when a tab is being dragged."""
            if self.dragged_tab is not None:
                target_tab_index = self.index(f"@{event.x},{event.y}")
                if target_tab_index != -1 and target_tab_index != self.dragged_tab:
                    self.insert(target_tab_index, self.tabs()[self.dragged_tab])
                    self.dragged_tab = target_tab_index

        def on_tab_double_click(self, event):
            """Called when a tab is double-clicked."""
            tab_index = self.index(f"@{event.x},{event.y}")
            if tab_index != -1:
                self.rename_tab(tab_index)

        def rename_tab(self, tab_index):
            """Rename the tab at the given index."""
            current_name = self.tab(tab_index, "text")
            new_name = simpledialog.askstring("Rename Tab", "Enter new tab name:", initialvalue=current_name)
            if new_name:
                self.tab(tab_index, text=new_name)

#! -------------------------------------------------------------------------------------------------------------------------   
    
    class Checkbutton(tk.Checkbutton):
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, selectcolor=None, **kwargs):
            super().__init__(parent, **kwargs)
            
            self.default_bg = "#d9d9d9"
            self.default_fg = "black"
            self.default_selectcolor = "#a0a0a0"

            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.selectcolor = selectcolor if selectcolor is not None else self.default_selectcolor

            self.enable_hover = enable_hover

            self.configure(
                bg=self.bg,
                fg=self.fg,
                font=("Arial", 12),
                selectcolor=self.selectcolor,
                relief="flat",
                padx=5, pady=5
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg="#c0c0c0")

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg)
#! -------------------------------------------------------------------------------------------------------------------------    
    
    class Scrollbar(tk.Scrollbar):
        def __init__(self, parent, **kwargs):
            super().__init__(parent, **kwargs)
            self.configure(
                bg="#a0a0a0",
                troughcolor="#d9d9d9",
                relief="flat",
                borderwidth=2
        )
#! -------------------------------------------------------------------------------------------------------------------------    
    
    class Listbox(tk.Listbox):
        
        def __init__(self, parent, enable_hover=True, bg=None, fg=None, **kwargs):
            super().__init__(parent, **kwargs)

            self.default_bg = "#ffffff"
            self.default_fg = "black"
            
            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.enable_hover = enable_hover

            self.configure(
                bg=self.bg,
                fg=self.fg,
                font=("Arial", 12),
                selectbackground="gray",
                selectforeground="white",
                relief="sunken",
                borderwidth=5
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg="#f0f0f0")

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg)
    
#! -------------------------------------------------------------------------------------------------------------------------
    class Text(tk.Text):
        def __init__(self, parent, enable_hover=True, **kwargs):
            super().__init__(parent, **kwargs)
            self.enable_hover = enable_hover

            # \\ Default configuration
            default_config = {
                "bg": "white",
                "fg": "black",
                "font": ("Arial", 12),
                "wrap": "word",
                "borderwidth": 5,
                "relief": "sunken",
                "insertbackground": "black",
                "highlightthickness": 2,
                "highlightbackground": "#a0a0a0",
                "highlightcolor": "#808080"
            }

            default_config.update(kwargs)
            self.configure(**default_config)

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(highlightbackground="#808080", highlightcolor="#505050")

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(highlightbackground="#a0a0a0", highlightcolor="#808080")

#! -------------------------------------------------------------------------------------------------------------------------
    class Progressbar(ttk.Progressbar):
        def __init__(self, parent, length=200, mode="determinate", style_name="Custom.Horizontal.TProgressbar", **kwargs):
            super().__init__(parent, length=length, mode=mode, **kwargs)
            
            # \\ Default style configuration
            self.style_name = style_name
            self.style = ttk.Style()
            self.style.theme_use("clam")
            
            # \\ Apply default or custom style
            self.configure(style=self.style_name)
            self.set_style(
                troughcolor="#d9d9d9",
                background="#7f7f7f",
                bordercolor="#a0a0a0",
                lightcolor="#c0c0c0",
                darkcolor="#808080"
            )

        def set_style(self, **kwargs):
            """
            Customize the progress bar style.
            Available options: troughcolor, background, bordercolor, lightcolor, darkcolor, etc.
            """
            self.style.configure(
                self.style_name,
                **kwargs
            )

#! -------------------------------------------------------------------------------------------------------------------------
    class OptionMenu(tk.OptionMenu):
        def __init__(self, parent, variable, *options, enable_hover=True, bg="#7f7f7f", fg="black", hover_bg="light gray", hover_fg="white", font=("Arial", 12), **kwargs):
            super().__init__(parent, self.variable, *self.options, **kwargs)
            """
            Initialize the OptionMenu widget.

            Parameters:
                parent: The parent widget.
                variable: A tk.StringVar to store the selected option.
                *options: A list of options to display in the dropdown.
                enable_hover (bool): Whether to enable hover effects.
                bg (str): Background color of the widget.
                fg (str): Foreground (text) color of the widget.
                hover_bg (str): Background color on hover.
                hover_fg (str): Foreground color on hover.
                font (tuple): Font style and size.
                **kwargs: Additional arguments to pass to the OptionMenu widget.
            """
            self.variable = variable
            self.options = options
            self.enable_hover = enable_hover
            self.bg = bg
            self.fg = fg
            self.hover_bg = hover_bg
            self.hover_fg = hover_fg
            self.font = font
            
            self.configure(
                bg=self.bg,
                fg=self.fg,
                activebackground=self.hover_bg,
                activeforeground=self.hover_fg,
                font=self.font,
                relief="raised",
                borderwidth=2
            )

            # \\ Add hover effects
            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            """Change appearance on hover."""
            if self.enable_hover:
                self.configure(bg=self.hover_bg, fg=self.hover_fg)

        def on_leave(self, event):
            """Revert appearance when not hovering."""
            if self.enable_hover:
                self.configure(bg=self.bg, fg=self.fg)

        def update_options(self, *new_options):
            """
            Update the options in the dropdown menu.

            Parameters:
                *new_options: A list of new options to display.
            """
            self.options = new_options
            self["menu"].delete(0, "end")  # \\ Clear existing options
            for option in self.options:
                self["menu"].add_command(label=option, command=lambda opt=option: self.variable.set(opt))

        def bind_selection_event(self, callback):
            """
            Bind a callback function to the selection event.

            Parameters:
                callback: A function to call when an option is selected.
            """
            self.variable.trace_add("write", lambda *args: callback(self.variable.get()))

#! -------------------------------------------------------------------------------------------------------------------------

    class PanedWindow(ttk.PanedWindow):
        def __init__(self, parent, enable_hover=True, orientation="horizontal", sash_color=None, hover_sash_color=None, **kwargs):
            super().__init__(parent, orient=orientation, **kwargs)
            self.enable_hover = enable_hover
            self.orientation = orientation
            self.default_sash_color = "#a0a0a0"
            self.default_hover_sash_color = "#808080"
            self.sash_color = sash_color if sash_color else self.default_sash_color
            self.hover_sash_color = hover_sash_color if hover_sash_color else self.default_hover_sash_color

            # \\ Configure the style for the PanedWindow
            self.style = ttk.Style()
            self.style.configure("Custom.TPanedwindow", background="#d9d9d9")
            self.style.configure("Custom.TPanedwindow.Sash", background=self.sash_color)

            # \\  Apply the custom style
            self.configure(style="Custom.TPanedwindow")

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)
                self.bind("<Motion>", self.on_sash_hover)

        def on_hover(self, event):
            """Change background color on hover."""
            if self.enable_hover:
                self.style.configure("Custom.TPanedwindow", background="#c0c0c0")

        def on_leave(self, event):
            """Revert background color when not hovering."""
            if self.enable_hover:
                self.style.configure("Custom.TPanedwindow", background="#d9d9d9")

        def on_sash_hover(self, event):
            """Change sash color when hovering over it."""
            if self.enable_hover:
                sash_width = 5  # \\  Width of the sash
                sash_positions = self.get_sash_positions()

                for pos in sash_positions:
                    if self.orientation == "horizontal":
                        # \\ Check if the mouse is near a horizontal sash
                        if abs(event.y - pos) < sash_width:
                            self.style.configure("Custom.TPanedwindow.Sash", background=self.hover_sash_color)
                            return
                    else:
                        # \\ Check if the mouse is near a vertical sash
                        if abs(event.x - pos) < sash_width:
                            self.style.configure("Custom.TPanedwindow.Sash", background=self.hover_sash_color)
                            return

                # \\ If not near any sash, revert to the default sash color
                self.style.configure("Custom.TPanedwindow.Sash", background=self.sash_color)

        def get_sash_positions(self):
            """Get the positions of all sashes in the PanedWindow."""
            sash_positions = []
            num_panes = len(self.panes())  
            for i in range(num_panes - 1):  # \\ Number of sashes is one less than the number of panes
                sash_positions.append(self.sashpos(i))
            return sash_positions

        def set_sash_color(self, color):
            """Set the color of the sash."""
            self.sash_color = color
            self.style.configure("Custom.TPanedwindow.Sash", background=self.sash_color)

        def add_pane(self, widget, **kwargs):
            """Add a new pane to the PanedWindow."""
            self.add(widget, **kwargs)

        def remove_pane(self, widget):
            """Remove a pane from the PanedWindow."""
            self.forget(widget)

        def set_orientation(self, orientation):
            """Set the orientation of the PanedWindow (horizontal or vertical)."""
            self.orientation = orientation
            self.configure(orient=self.orientation)

        def set_sash_width(self, width):
            """Set the width of the sash."""
            self.configure(width=width)

        def set_sash_relief(self, relief):
            """Set the relief style of the sash."""
            self.style.configure("Custom.TPanedwindow.Sash", relief=relief)

#! -------------------------------------------------------------------------------------------------------------------------
    
    class SplitView(ttk.PanedWindow):
        def __init__(self, parent, orientation="horizontal", **kwargs):
            super().__init__(parent, orient=orientation, **kwargs)
            self.pane1 = GTG.Frame(self,bg="#868686", relief="groove", borderwidth=20)
            self.pane2 = GTG.Frame(self, bg="#868686")
            self.add(self.pane1)
            self.add(self.pane2)

        def add_widget(self, widget, pane=1):
            if pane == 1:
                widget.pack(in_=self.pane1, fill="both", expand=True)
            else:
                widget.pack(in_=self.pane2, fill="both", expand=True)
#! -------------------------------------------------------------------------------------------------------------------------   
    
    class Combobox(ttk.Combobox):
        def __init__(self, parent, values, default_index=0, bg="#7f7f7f", fg="black", hover_bg="light gray", hover_fg="white", **kwargs):
            super().__init__(parent, values=values, state="readonly", **kwargs)
            
            self.default_bg = bg
            self.default_fg = fg
            self.hover_bg = hover_bg
            self.hover_fg = hover_fg
            
            self.current(default_index)
            self.bind("<Enter>", self.on_hover)
            self.bind("<Leave>", self.on_leave)
            
        def on_hover(self, event):
            self.configure(background=self.hover_bg, foreground=self.hover_fg)
        
        def on_leave(self, event):
            self.configure(background=self.default_bg, foreground=self.default_fg)

#! -------------------------------------------------------------------------------------------------------------------------

    class Treeview(ttk.Treeview):
        def __init__(self, parent, columns, show_headers=True, **kwargs):
            super().__init__(parent, columns=columns, show="tree headings" if show_headers else "tree", **kwargs)
            self.columns = columns
            self.headings = [col.capitalize() for col in columns]
            self.configure_columns()
            self.apply_styles()
        
            self.bind("<Motion>", self.on_hover) 
            self.bind("<Leave>", self.on_leave)
            self.bind("<Double-1>", self.toggle_item)  # \\ Double-click to expand/collapse
            self.last_hovered = None
            self.tag_configure("hover", background="gray")  

        def configure_columns(self):
            """Configure columns with default width and alignment."""
            for col, heading in zip(self.columns, self.headings):
                self.heading(col, text=heading)
                self.column(col, width=120, anchor="center")

        def apply_styles(self):
            """Apply a modern theme with relief effects."""
            style = ttk.Style()
            style.theme_use("alt")  
            style.configure("Treeview",
                            background="black",
                            foreground="lime",
                            rowheight=25,
                            fieldbackground="#f8f8f8",
                            relief="groove")  
            style.map("Treeview",
                    background=[("selected", "lightgray")],  
                    foreground=[("selected", "lime")])
            style.configure("Treeview.Heading", font=("Arial", 10, "bold"), relief="raised", background="#dddddd" , borderwidth=5)

        def add_item(self, parent="", text="", values=(), open_state=False):
            """Add a new item with optional parent-child hierarchy."""
            return self.insert(parent, "end", text=text, values=values, open=open_state)

        def on_hover(self, event):
            """Highlight row on mouse hover."""
            row = self.identify_row(event.y)
            if row != self.last_hovered:
                if self.last_hovered:
                    self.item(self.last_hovered, tags=())
                if row:
                    self.item(row, tags=("hover",))
                    self.last_hovered = row

        def on_leave(self, event):
            """Remove hover highlight when cursor leaves the widget."""
            if self.last_hovered:
                self.item(self.last_hovered, tags=())
                self.last_hovered = None

        def toggle_item(self, event):
            """Expand or collapse a row on double-click."""
            item = self.identify_row(event.y)
            if item:
                is_open = self.item(item, "open")
                self.item(item, open=not is_open)
#! ---------------------------------------------------------------------------------------------------------------------------------
    
    class LabelFrame(tk.LabelFrame):
        def __init__(self, parent, text="", enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, **kwargs):
            super().__init__(parent, text=text, **kwargs)
            
            # \\ Default values \\ 
            self.default_bg = "#7f7f7f"
            self.default_fg = "black"
            self.default_hover_bg = "light gray"
            self.default_hover_fg = "white"

            self.bg = bg if bg is not None else self.default_bg
            self.fg = fg if fg is not None else self.default_fg
            self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
            self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg

            self.enable_hover = enable_hover

            self.configure(
                bg=self.bg,
                fg=self.fg,
                relief="ridge",
                borderwidth=5
            )

            if self.enable_hover:
                self.bind("<Enter>", self.on_hover)
                self.bind("<Leave>", self.on_leave)

        def on_hover(self, event):
            if self.enable_hover:
                self.configure(bg=self.hover_bg, fg=self.hover_fg)

        def on_leave(self, event):
            if self.enable_hover:
                self.configure(bg=self.bg, fg=self.fg)
    
  

    class Bitmap(tk.Label):
        def __init__(self, parent, bitmap, **kwargs):
            super().__init__(parent, bitmap=bitmap, **kwargs)

#! ------------------------------------------  END of Main Widgets ------------------------------------------------------------------------------------------------


#!-------------------------------------------------Start Of VARIABLES-------------------------------------------------------------------------------------------------------

    class StringVar(tk.StringVar):
        def __init__(self, value="", callback=None, **kwargs):
            super().__init__(**kwargs)
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            self.set(new_value)
#! -------------------------------------------------------------------------------------------------------------------------   
    
    class BooleanVar(tk.BooleanVar):
        def __init__(self, value=False, callback=None, **kwargs):
            super().__init__(**kwargs)
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(variable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            self.set(bool(new_value))
    
 #! -------------------------------------------------------------------------------------------------------------------------  
    class ListVar(tk.Variable):
        def __init__(self, value=None, callback=None, **kwargs):
            super().__init__(**kwargs)
            if value is None:
                value = []
            self._value = value  # \\ Store the list as an attribute
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get_value())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self._value 

        def set_value(self, new_value):
            if not isinstance(new_value, list):
                raise ValueError("Value must be a list")
            self._value = new_value  
            self.set(str(new_value))  

        def append(self, item):
            self._value.append(item) 
            self.set(str(self._value)) 

        def remove(self, item):
            if item in self._value:
                self._value.remove(item)  
                self.set(str(self._value))  

#! -------------------------------------------------------------------------------------------------------------------------   
    class IntVar(tk.IntVar):
        def __init__(self, value=0, callback=None, **kwargs):
            super().__init__(**kwargs)
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            self.set(int(new_value))
 #! -------------------------------------------------------------------------------------------------------------------------   
    class DoubleVar(tk.DoubleVar):
        def __init__(self, value=0.0, callback=None, **kwargs):
            super().__init__(**kwargs)
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            self.set(float(new_value)) 

#! -------------------------------------------------------------------------------------------------------------------------   
    class FileVar(tk.Variable):
        def __init__(self, value=None, callback=None, **kwargs):
            super().__init__(**kwargs)
            if value is None:
                value = ""
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            if not isinstance(new_value, str):
                raise ValueError("Value must be a file path string")
            self.set(new_value)
    
#! -------------------------------------------------------------------------------------------------------------------------    
    class DateTimeVar(tk.Variable):
        def __init__(self, value=None, callback=None, **kwargs):
            super().__init__(**kwargs)
            if value is None:
                value = GTGDateTime.now()
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            if not isinstance(new_value,GTGDateTime):
                raise ValueError("Value must be a datetime object")
            self.set(new_value)
    
#! -------------------------------------------------------------------------------------------------------------------------    
    class ColorVar(tk.Variable):
        def __init__(self, value=None, callback=None, **kwargs):
            super().__init__(**kwargs)
            if value is None:
                value = "#000000"  # \\ Default to black
            self.set(value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self.get()

        def set_value(self, new_value):
            if not isinstance(new_value, str) or not new_value.startswith("#"):
                raise ValueError("Value must be a hex color code (e.g., '#RRGGBB')")
            self.set(new_value)
   
#! -------------------------------------------------------------------------------------------------------------------------
    class EnumVar(tk.StringVar):
        def __init__(self, value=None, enum_type=None, callback=None, **kwargs):
            super().__init__(**kwargs)
            if enum_type is None:
                raise ValueError("enum_type must be specified")
            self.enum_type = enum_type
            self.set(value if value is not None else list(enum_type)[0].value)
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self.enum_type(self.get())

        def set_value(self, new_value):
            if isinstance(new_value, self.enum_type):
                new_value = new_value.value
            if new_value not in [e.value for e in self.enum_type]:
                raise ValueError(f"Value must be one of {[e.value for e in self.enum_type]}")
            self.set(new_value)

#! ------------------------------------------------------------------------------------------------------------------------- 

#! need to look this Var over and clean it up 
    class ValueErrorVar(tk.Variable):
        def __init__(self, value=None, callback=None, **kwargs):
            super().__init__(**kwargs)
            if value is None:
                value = ""
            self._value = value  #* \\ Store the error message as an attribute
            self.callback = callback
            self.trace_add("write", self.on_change)

        def on_change(self, *args):
            if self.callback:
                self.callback(self.get_value())

        def bind_to_widget(self, widget):
            widget.configure(textvariable=self)

        def get_value(self):
            return self._value

        def set_value(self, new_value):
            if not isinstance(new_value, str):
                raise ValueError("Value must be a string")
            self._value = new_value
            self.set(new_value)

        def clear(self):
            self.set_value("")  #* \\ Clear the error message


    class ValueErrorException(Exception):
        def __init__(self, message, error_var=None):
            super().__init__(message)
            self.message = message
            self.error_var = error_var

        def __str__(self):
            return self.message

#!------------------------------------------------------------------------------------------------------------------------------
