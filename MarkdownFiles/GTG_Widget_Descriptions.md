# GTG Widget Descriptions
-------------------------------

## GTG.Button Overview
This is a custom `Button` class for Tkinter that extends `tk.Button`. It adds hover effects and customizable styles, making it more visually appealing and functional than the default Tkinter button.

## Features
- Customizable background, foreground, and hover colors
- Customizable border and relief styles
- Hover effects that change button appearance
- A method to toggle button text dynamically

## Class Definition
```python
class Button(tk.Button):
    def __init__(self, parent, enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, frame=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.default_bg = "#7f7f7f"
        self.default_fg = "Black"
        self.default_hover_bg = "light gray"
        self.default_hover_fg = "white"
        self.default_frame = "ridge"  
        
        self.bg = bg if bg is not None else self.default_bg
        self.fg = fg if fg is not None else self.default_fg
        self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
        self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg
        self.frame = frame if frame is not None else self.default_frame
        
        self.enable_hover = enable_hover
    
        self.configure(
            bg=self.bg,  
            fg=self.fg,   
            relief=self.frame, 
            font=("Arial", 12, "bold"), 
            activebackground="darkgray",  
            activeforeground="white",  
            borderwidth=10,
            highlightthickness=0, 
            pady=5, padx=10 
        )
        
        if self.enable_hover:
            self.bind("<Enter>", self.on_hover) 
            self.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        """Change button appearance on hover."""
        if self.enable_hover:
            self.configure(bg=self.hover_bg, fg=self.hover_fg, relief="raised", borderwidth=10)  

    def on_leave(self, event):
        """Revert button appearance when not hovering."""
        if self.enable_hover:
            self.configure(bg=self.bg, fg=self.fg, relief=self.frame, borderwidth=10)  
    
    def toggle_text(self, new_text):
        """Change the button's text."""
        self.config(text=new_text)
```

## How to Use

### Create a Tkinter Window and Use the Button
```python
root = tk.Tk()
root.title("Custom Button Example")

# Create a button instance
btn = GTG.Button(root, text="Click Me", bg="blue", fg="white", hover_bg="red", hover_fg="yellow")
btn.pack(pady=20)

# Change text dynamically
def change_text():
    btn.toggle_text("New Text")

change_text_button = GTG.Button(root, text="Change Button Text", command=change_text)
change_text_button.pack()

root.mainloop()
```

### Customization Options
When creating a button, you can pass the following parameters:
- `bg`: Background color (default: `#7f7f7f`)
- `fg`: Foreground (text) color (default: `Black`)
- `hover_bg`: Background color on hover (default: `light gray`)
- `hover_fg`: Foreground color on hover (default: `white`)
- `frame`: Button relief style (default: `ridge`)
- `enable_hover`: Enable or disable hover effect (default: `True`)

### Methods
- `on_hover(event)`: Changes button appearance when hovered over.
- `on_leave(event)`: Restores button appearance when hover is removed.
- `toggle_text(new_text)`: Updates the button's text.

## Conclusion
This custom Tkinter button class improves the default `Button` widget by adding hover effects and customization options, making it more interactive and visually appealing 


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## GTG.Label Overview

The `Label` class is a subclass of `tk.Label` that introduces additional features such as hover effects and customizable styling. It allows developers to easily configure the appearance of labels in a `tkinter` application, including background color, text color, font, padding, and more.


## Class Definition

```python
class Label(tk.Label):
    def __init__(self, parent, enable_hover=True, bg=None, fg=None, hover_bg=None, hover_fg=None, 
                 font=None, borderwidth=None, relief=None, padx=None, pady=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        # \\ Default values
        self.default_bg = "#7f7f7f"
        self.default_fg = "Black"
        self.default_hover_bg = "#e0e0e0"
        self.default_hover_fg = fg if fg is not None else self.default_fg
        self.default_font = ("Arial", 12)
        self.default_borderwidth = 5
        self.default_relief = "sunken"
        self.default_padx = 10
        self.default_pady = 5
        
        # \\ Customizable properties
        self.bg = bg if bg is not None else self.default_bg
        self.fg = fg if fg is not None else self.default_fg
        self.hover_bg = hover_bg if hover_bg is not None else self.default_hover_bg
        self.hover_fg = hover_fg if hover_fg is not None else self.default_hover_fg
        self.font = font if font is not None else self.default_font
        self.borderwidth = borderwidth if borderwidth is not None else self.default_borderwidth
        self.relief = relief if relief is not None else self.default_relief
        self.padx = padx if padx is not None else self.default_padx
        self.pady = pady if pady is not None else self.default_pady
        
        # \\ Enable/disable hover effect
        self.enable_hover = enable_hover
        
        # \\ Configure the label
        self.configure(
            bg=self.bg,
            fg=self.fg,
            font=self.font,
            borderwidth=self.borderwidth,
            relief=self.relief,
            padx=self.padx,
            pady=self.pady
        )
        
        # \\ Bind hover events if enabled
        if self.enable_hover:
            self.bind("<Enter>", self.on_hover)
            self.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        if self.enable_hover:
            self.configure(bg=self.hover_bg, fg=self.hover_fg)

    def on_leave(self, event):
        if self.enable_hover:
            self.configure(bg=self.bg, fg=self.fg) 
``` 

### Customizable Options

The following properties can be customized during initialization:

`bg:` Background color.

`fg:` Text color.

`hover_bg:` Background color on hover.

`hover_fg:` Text color on hover.

`font:` Font style and size.

`borderwidth:` Width of the border.

`relief:` Border relief style.

`padx:` Horizontal padding.

`pady:` Vertical padding.



### Methods

`__init__`

The constructor method initializes the Label object. It sets default values for properties and configures the label based on the provided or default values. If hover effects are enabled, it binds the <Enter> and <Leave> events to the on_hover and on_leave methods, respectively.

`on_hover:`

- This method is triggered when the mouse enters the label's area. It changes the background and text colors to the hover colors if hover effects are enabled.

`on_leave:`

- This method is triggered when the mouse leaves the label's area. It reverts the background and text colors to their default values if hover effects are enabled. 




### Usage Example

```python
root = tk.Tk()

# Create a custom label with hover effect
label = Label(
    root,
    text="Hover over me!",
    bg="lightblue",
    fg="darkblue",
    hover_bg="darkblue",
    hover_fg="lightblue",
    font=("Helvetica", 14),
    borderwidth=2,
    relief="raised",
    padx=20,
    pady=10
)
label.pack(pady=20)

root.mainloop()
```
***In this example, the label will change its background and text colors when the mouse hovers over it.***


### Conclusion
The Label class provides a flexible and reusable way to create custom labels with hover effects in tkinter applications. By allowing customization of various properties, it simplifies the process of creating visually appealing user interfaces.
