# GTG Widget Descriptions

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
My custom Tkinter button class improves the default `Button` widget by adding hover effects and customization options, making it more interactive and visually appealing 


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## GTG.Label Overview

The `GTG.Label` class is a subclass of `tk.Label` that introduces additional features such as hover effects and customizable styling. It allows developers to easily configure the appearance of labels in a `tkinter` application, including background color, text color, font, padding, and more.


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
My  Label class provides a flexible and reusable way to create custom labels with hover effects in tkinter applications. By allowing customization of various properties, it simplifies the process of creating visually appealing user interfaces. 


-----------------------------------------------------------------------------------------------------------------------------------------------------



## GTG.Frame Overview

`GTG.Frame` class is a subclass of `tk.Frame` that introduces additional features such as hover effects, customizable padding, border width, and smooth color transitions. It allows developers to create visually appealing and interactive frames in a `tkinter` application.

---

## Class Definition

```python
class Frame(tk.Frame):
    def __init__(self, parent, enable_hover=False, bg=None, highlightbackground=None, hover_bg=None, 
                 hover_highlight=None, relief="ridge", borderwidth=None, hover_borderwidth=None, 
                 padx=None, pady=None, hover_padx=None, hover_pady=None, cursor=None, 
                 animation_speed=10, **kwargs):
        super().__init__(parent, **kwargs)
        
        # \\ Default values
        self.default_bg = "#d9d9d9"
        self.default_highlight = "#a0a0a0"
        self.default_hover_bg = "#c0c0c0"
        self.default_hover_highlight = "#808080"
        self.default_borderwidth = 5
        self.default_padx = 0
        self.default_pady = 0
        self.default_cursor = "arrow"
        
        # \\ Customizable properties
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
        
        # \\ Bind hover events if enabled
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
``` 

## Customizable Properties
The following properties can be customized during initialization:

`bg:` Background color.

`highlightbackground:` Highlight color.

`hover_bg:` Background color on hover.

`hover_highlight:` Highlight color on hover.

`borderwidth:` Width of the border.

`hover_borderwidth:` Border width on hover.

`padx:` Horizontal padding.

`pady:` Vertical padding.

`hover_padx:` Horizontal padding on hover.

`hover_pady:` Vertical padding on hover.

`cursor:` Cursor style.

`animation_speed:` Speed of the color animation (in milliseconds).

## Hover Effect
The enable_hover parameter determines whether the hover effect is enabled. If True, the frame's background color, highlight color, padding, and border width will change when the mouse hovers over it. 


## Methods
`__init__`

The constructor method initializes the Frame object. It sets default values for properties and configures the frame based on the provided or default values. If hover effects are enabled, it binds the <Enter> and <Leave> events to the on_hover and on_leave methods, respectively.

`configure_frame`
This method configures the frame's appearance, including its background color, border width, highlight color, padding, and cursor style.

`on_hover`
This method is triggered when the mouse enters the frame's area. It initiates a smooth color transition to the hover colors and adjusts padding and border width if hover effects are enabled.

`on_leave`
This method is triggered when the mouse leaves the frame's area. It reverts the frame's appearance to its default state, including colors, padding, and border width.

`animate_color`
This method smoothly animates the transition between two background and highlight colors over a specified number of steps.

`calculate_color_delta`
This helper method calculates the color delta (change in RGB values) for each step of the animation.

`interpolate_color`
This helper method interpolates between two colors based on the current step of the animation. 


## Usage Example

```python
root = tk.Tk()

# \\ Create a custom frame with hover effect
frame = Frame(
    root,
    enable_hover=True,
    bg="lightblue",
    highlightbackground="blue",
    hover_bg="darkblue",
    hover_highlight="navy",
    borderwidth=2,
    hover_borderwidth=4,
    padx=10,
    pady=10,
    hover_padx=15,
    hover_pady=15,
    cursor="hand2",
    animation_speed=20
)
frame.pack(pady=20, padx=20)

root.mainloop()
```
***In this example, the frame will smoothly transition its colors, padding, and border width when the mouse hovers over it.***

## Conclusion
My `GTG.Frame` class provides a flexible and reusable way to create custom frames with hover effects and smooth animations in `tkinter` applications. By allowing customization of various properties, it simplifies the process of creating visually appealing and interactive user interfaces. 


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## GTG.Canvas Overview

`GTG.Canvas` class is a subclass of `tk.Canvas` that introduces additional features such as hover effects and helper methods for drawing rectangles and text. It allows developers to create interactive and visually appealing canvases in a `tkinter` application.

---

## Class Definition

```python
class Canvas(tk.Canvas):
    def __init__(self, parent, enable_hover=True, **kwargs):
        super().__init__(parent, **kwargs)
        self.enable_hover = enable_hover
        self.configure(
            bg="#d9d9d9",  
            bd=5,           
            relief="ridge", 
            width=400,      
            height=400      
        )
        if self.enable_hover:
            self.bind("<Enter>", self.on_hover)
            self.bind("<Leave>", self.on_leave)
    
    def on_hover(self, event):
        if self.enable_hover:
            self.configure(bg="#c0c0c0")  

    def on_leave(self, event):
        if self.enable_hover:
            self.configure(bg="#d9d9d9")  

    def draw_rectangle(self, x1, y1, x2, y2, **kwargs):
        """Draws a rectangle on the canvas."""
        return self.create_rectangle(x1, y1, x2, y2, **kwargs)

    def draw_text(self, x, y, text, **kwargs):
        """Draws text on the canvas."""
        return self.create_text(x, y, text=text, **kwargs) 
``` 

## Class Properties

### Default Configuration

The Canvas class is initialized with the following default configuration:

`bg:` Background color (#d9d9d9).

`bd:` Border width (5).

`relief:` Border relief style (ridge).

`width:` Canvas width (400).

`height:` Canvas height (400).

## Hover Effect
`enable_hover` parameter determines whether the hover effect is enabled. If `True`, the canvas's background color will change when the mouse hovers over it. 


## Methods
`__init__`

The constructor method initializes the Canvas object. It sets up the canvas with default properties and binds hover events if enable_hover is True.

`on_hover`

This method is triggered when the mouse enters the canvas's area. It changes the background color to the hover color (#c0c0c0) if hover effects are enabled.

`on_leave`

This method is triggered when the mouse leaves the canvas's area. It reverts the background color to the default color (#d9d9d9) if hover effects are enabled.

`draw_rectangle`

This method draws a rectangle on the canvas. It accepts the coordinates of the rectangle (x1, y1, x2, y2) and additional keyword arguments for customization (e.g., fill color, outline color).

`draw_text`

This method draws text on the canvas. It accepts the coordinates (x, y), the text to display, and additional keyword arguments for customization (e.g., font, fill color). 



## Usage Example

```python
root = tk.Tk()

# \\ Create a custom canvas with hover effect
canvas = Canvas(root, enable_hover=True)
canvas.pack(pady=20, padx=20)

# \\ Draw a rectangle on the canvas
canvas.draw_rectangle(50, 50, 150, 150, fill="lightblue", outline="blue")

# \\ Draw text on the canvas
canvas.draw_text(100, 100, text="Hello, Canvas!", font=("Arial", 14), fill="darkblue")

root.mainloop() 
```
**In this example:**
**The canvas will change its background color when the mouse hovers over it.**
**A rectangle and text are drawn on the canvas using the draw_rectangle and draw_text methods.** 


## Conclusion
`GTG.Canvas` class provides a flexible and reusable way to create custom canvases with hover effects and helper methods for drawing shapes and text in `tkinter` applications. By allowing customization of properties and providing intuitive methods, it simplifies the process of creating interactive and visually appealing user interfaces 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


## GTG.Entry Overview
`GTG.Entry` widget extends the standard `tk.Entry` in Tkinter to provide hover effects. It allows users to define background and foreground colors that change when the mouse enters and leaves the widget.

## Features
- **Customizable Hover Effects**: Supports changing the background, foreground, highlight background, and highlight color on hover.
- **Retains Default Styles**: Stores the original styles and restores them when the mouse leaves.
- **Toggle Hover Effects**: The hover functionality can be enabled or disabled using the `enable_hover` parameter.

## Implementation
```python
import tkinter as tk

class Entry(tk.Entry):
    def __init__(self, parent, enable_hover=True, **kwargs):
        self.hover_bg = kwargs.pop("hover_bg", None)
        self.hover_fg = kwargs.pop("hover_fg", None)
        self.hover_highlightbackground = kwargs.pop("hover_highlightbackground", None)
        self.hover_highlightcolor = kwargs.pop("hover_highlightcolor", None)

        super().__init__(parent, **kwargs)

        # Store default styles
        self.default_bg = self.cget("bg")
        self.default_fg = self.cget("fg")
        self.default_highlightbackground = self.cget("highlightbackground")
        self.default_highlightcolor = self.cget("highlightcolor")

        # Enable hover effects
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
```

## Usage Example
```python
root = tk.Tk()
entry = Entry(root, hover_bg="lightgray", hover_fg="blue", enable_hover=True)
entry.pack(pady=10)
root.mainloop()
```

## Customization Options
The widget accepts the following optional hover-related parameters:
- `hover_bg`: Background color on hover.
- `hover_fg`: Foreground (text) color on hover.
- `hover_highlightbackground`: Border highlight color on hover.
- `hover_highlightcolor`: Highlight color inside the entry on hover.
- `enable_hover`: Boolean flag to enable or disable hover effects.

## Conclusion
The enhanced `GTG.Entry` widget provides a simple yet effective way to add hover effects in Tkinter applications. It improves user interaction and allows for easy customization.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


## GTG.Toplevel Overview
My custom `GTG.Toplevel` widget extends Tkinter's standard `tk.Toplevel` to provide hover effects. It modifies the window's background and highlight colors when the mouse enters and leaves.

## Features
- **Customizable Hover Effects**: Changes background and highlight colors on hover.
- **Styled Appearance**: Default ridge border with a custom background and highlight.
- **Toggle Hover Effects**: Can be enabled or disabled with the `enable_hover` parameter.

## Implementation
```python
import tkinter as tk

class Toplevel(tk.Toplevel):
    def __init__(self, parent, enable_hover=True, **kwargs):
        super().__init__(parent, **kwargs)

        self.default_bg = "#7f7f7f"
        self.default_highlight = "#a0a0a0"
        
        self.configure(
            bg=self.default_bg, 
            relief="ridge", 
            borderwidth=10, 
            highlightthickness=2,
            highlightbackground=self.default_highlight
        )

        self.enable_hover = enable_hover

        if self.enable_hover:
            self.bind("<Enter>", self.on_hover)
            self.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        """Hover effect: Change background color on mouse enter"""
        if self.enable_hover:
            self.configure(bg="#e0e0e0", highlightbackground="#808080")

    def on_leave(self, event):
        """Reset background color when mouse leaves"""
        if self.enable_hover:
            self.configure(bg=self.default_bg, highlightbackground=self.default_highlight)
```

## Usage Example
```python
root = tk.Tk()
top = Toplevel(root, enable_hover=True)
top.geometry("300x200")
root.mainloop()
```

## Customization Options
The widget supports the following optional parameters:
- `enable_hover`: Boolean flag to enable or disable hover effects.

## Conclusion
`GTG.Toplevel` widget enhances the default Tkinter window by adding hover effects, improving the user interface with interactive visual feedback.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


## GTG.Scale Overview
`GTG.Scale` widget extends Tkinter's `tk.Scale` by adding hover and click effects. It also allows dynamic customization of colors and orientation.

## Features
- **Hover Effects**: Changes background and highlight color when the mouse hovers over the widget.
- **Click Effects**: Adjusts background and highlight color when clicked.
- **Customizable Appearance**: Supports dynamic modification of colors and orientation.
- **Toggle Value Display**: Allows enabling or disabling the display of the current value.

## Implementation
```python
import tkinter as tk

class MyScale(tk.Scale):
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
```

## Usage Example
```python
root = tk.Tk()
scale = GTGScale(root, enable_hover=True, enable_click_effect=True)
scale.pack(pady=10)
root.mainloop()
```

## Customization Options
The widget allows customization of the following properties:
- **Hover and Click Colors**: Modify background and highlight colors for different states.
- **Orientation**: Switch between horizontal and vertical scale.
- **Value Display**: Toggle the display of the scale's value.

## Conclusion
`GTG.Scale` widget enhances the standard `tk.Scale` by adding interactive hover and click effects, making it more visually responsive and customizable.
