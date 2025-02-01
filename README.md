### Note: 
Everything is a work in progress and some widgets might be buggy and may not work as intended.
That being said i am by no means a expert on Gui or frameworks but making projects like this helps me improve my coding skills :) 


# Custom GUI Framework

My GUI framework **(GTG)** is a custom-built toolkit based on Tkinter (Python's standard GUI library). It provides a wide range of customizable widgets and advanced features that enable the creation of modern, interactive, and visually appealing applications.

## 1. Core Features
- **Custom Widgets:** Enhanced versions of standard Tkinter widgets (e.g., Button, Label, Entry, Canvas, Frame, etc.).
- **Hover Effects:** Interactive UI with widgets responding to mouse hover.
- **Custom Styling:** Background colors, foreground colors, borders, fonts, and more can be customized.
- **Dynamic Updates:** Widgets update dynamically based on user interactions or program logic.

## 2. Widgets Available
GTG Gui framework includes the following custom widgets:
- **Buttons:** Customizable buttons with hover effects, text toggling, and dynamic styling.
- **Labels:** Customizable text and colors with hover effects.
- **Frames:** Containers with hover effects and customizable borders/backgrounds.
- **Canvas:** Drawing area with methods for shapes, text, and hover effects.
- **Entry:** Text input fields with hover effects and customizable styling.
- **Toplevel:** Customizable pop-up windows with hover effects.
- **Scale:** Sliders with hover effects, click effects, and customizable colors.
- **MessageBox:** Pre-built dialog boxes for displaying messages, errors, warnings, or confirmations.
- **Spinbox:** Numeric input widgets with hover effects.
- **Menu:** Customizable menus with hover effects, commands, cascades, and separators.
- **Radiobutton:** Customizable radio buttons with hover effects.
- **Notebook:** Tabbed interfaces with hover effects.
- **Checkbutton:** Customizable checkboxes with hover effects.
- **Scrollbar:** Custom scrollbars with adjustable styling.
- **Listbox:** Lists with hover effects and customizable colors.
- **Text:** Multi-line text input with hover effects and styling options.
- **Progressbar:** Progress bars with customizable colors and styles.
- **SidePanel:** A collapsible side panel with drag-and-drop functionality for the toggle button and you can add widgets to it.

  
## 3. Advanced Features
- **Dynamic Variables:** Custom variable classes (e.g., `StringVar`, `IntVar`, `BooleanVar`, `DateTimeVar`, etc.) for dynamic updates and data binding.
  - Example: Automatically update a Label when a `StringVar` changes.
- **Error Handling:** `VallurErrorVar` and `VallurErrorException` for error management in the UI.
- **DateTime Support:** `DateTimeVar` for handling and displaying date/time data.
- **File Handling:** `FileVar` simplifies working with file paths.
- **Color Management:** `ColorVar` enables easy hex color code handling.

## 4. Use Cases
GTG GUI framework is suitable for a variety of applications, including:
- **Desktop Applications:** To-do lists, calculators, text editors, file explorers, etc.
- **Data Visualization Tools:** Charts, graphs, and dashboards.
- **Interactive Tools:** Drawing apps, image viewers, and games.
- **Utility Apps:** Unit converters, timers, password managers, etc.
- **Custom Forms:** Input forms with validation and dynamic updates.
**ideas are almost endless**

## 5. Strengths
- **Modern Look:** Customizable colors, hover effects, and styling create a polished appearance.
- **Ease of Use:** Pre-built, customizable widgets simplify UI development.
- **Extensibility:** Easily add new widgets or modify existing ones.
- **Interactivity:** Hover effects, dynamic updates, and event handling enhance user experience.

## 6. Limitations
- **Performance:** May experience slowdowns with very complex UIs containing many widgets.
- **Cross-Platform Consistency:** UI appearance may vary slightly across operating systems.
- **Advanced Graphics:** For high-end graphics or animations, additional libraries (e.g., Pygame, Matplotlib) may be required.

## 7. Ideal For
- **Rapid Prototyping:** Quickly build and test UI concepts.
- **Small to Medium-Sized Applications:** Ideal for tools, utilities, and desktop apps.
- **Educational Projects:** Perfect for learning GUI development and Python programming.
- **Custom Solutions:** Suitable for building tailored applications.

## Conclusion
**GTG** is a powerful, flexible, and modern toolkit for building desktop applications in Python. By enhancing Tkinter with hover effects, dynamic variables, and custom styling, it provides an excellent solution for various projects, from simple utilities to interactive applications. 


## How to import from GTG_Widgets\
![Screenshot 2025-02-01 181726](https://github.com/user-attachments/assets/6964a7b4-2a09-4b7f-9fc2-4ba4566669f9)


## Example Files
- **widget_example_1.py**
- **widget_example_2.py**
- **Example_Apps.py**
- **Variable_Class_Example.py**
- **Variable_Class_Example2.py**


# GTG Widgets Usage Examples


# Basic Examples

## Button
```python
button = GTG.Button(app.root, text="Click Me", command=lambda: print("Button clicked"))
button.pack()
```

## Label
```python
label = GTG.Label(app.root, text="Hello, World!", fg="white", bg="black")
label.pack()
```

## Frame
```python
frame = GTG.Frame(app.root, bg="gray")
frame.pack()
```

## Canvas
```python
canvas = GTG.Canvas(app.root)
canvas.pack()
canvas.draw_rectangle(10, 10, 100, 100, fill="red")
```

## Entry
```python
entry = GTG.Entry(app.root)
entry.pack()
```

## Toplevel (New Window)
```python
toplevel = GTG.Toplevel(app.root, bg="white")
```

## Scale
```python
scale = GTG.Scale(app.root, from_=0, to=100)
scale.pack()
```

## MessageBox
```python
GTG.showinfo(app.root, "Info", "This is an information message.")
```

## Spinbox
```python
spinbox = GTG.Spinbox(app.root, from_=0, to=10)
spinbox.pack()
```

## Menu
```python
menu = GTG.Menu(app.root)
app.root.config(menu=menu)
file_menu = GTG.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=app.root.quit)
```

## Radiobutton
```python
var = GTG.StringVar()
radio1 = GTG.Radiobutton(app.root, text="Option 1", variable=var, value="1")
radio2 = GTG.Radiobutton(app.root, text="Option 2", variable=var, value="2")
radio1.pack()
radio2.pack()
```

## Notebook
```python
notebook = GTG.Notebook(app.root)
notebook.pack()
frame1 = GTG.Frame(notebook)
frame2 = GTG.Frame(notebook)
notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")
```

## Checkbutton
```python
check_var = GTG.BooleanVar()
checkbox = GTG.Checkbutton(app.root, text="Check Me", variable=check_var)
checkbox.pack()
```

## Scrollbar
```python
scrollbar = GTG.Scrollbar(app.root)
scrollbar.pack()
```

## Listbox
```python
listbox = GTG.Listbox(app.root)
listbox.pack()
listbox.insert(0, "Item 1")
listbox.insert(1, "Item 2")
```

## Text
```python
text_widget = GTG.Text(app.root)
text_widget.pack()
```

## Progressbar
```python
progress = GTG.Progressbar(app.root, length=200, mode='determinate')
progress.pack()
progress.start()
```

## OptionMenu
```python
option_var = GTG.StringVar()
option_menu = GTG.OptionMenu(app.root, option_var, "Option 1", "Option 2", "Option 3")
option_menu.pack()
```

## PanedWindow
```python
paned = GTG.PanedWindow(app.root, orientation='horizontal')
paned.pack()
frame1 = GTG.Frame(paned)
frame2 = GTG.Frame(paned)
paned.add_pane(frame1)
paned.add_pane(frame2)
```

## Variables
```python
string_var = GTG.StringVar(value="Hello")
boolean_var = GTG.BooleanVar(value=True)
int_var = GTG.IntVar(value=10)
double_var = GTG.DoubleVar(value=5.5)
list_var = GTG.ListVar(value=["Item1", "Item2"])
```

## Custom File Dialog
```python
file_dialog = GTG.CustomFileDialog(app.root)
selected_file = file_dialog.get_file_path()
```

## Tooltip
```python
tooltip = GTG.Tooltip(button, "This is a button")
```

## Custom Color Picker
```python
def color_selected(color):
    print("Selected Color:", color)
color_picker = GTG.CustomColorPicker(color_selected)
color_picker.open_picker()
```

## Side Panel
```python
side_panel = GTG.SidePanel(app.root, width=250, bg="darkgray")
side_panel._build()
```

app.RunWindow()




