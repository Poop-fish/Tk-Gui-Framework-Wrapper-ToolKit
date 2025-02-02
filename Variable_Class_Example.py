from GTG_imports import *  
from GTG_Widgets import *


#! int and double variable use case  
def on_change(value):
    print(f"Value changed to: {value}")

def validate_input(new_value, variable_type):
    """Validate the input based on the variable type."""
    try:
        if variable_type == "int":
            int(new_value)
        elif variable_type == "double":
            float(new_value)
        return True
    except ValueError:
        return False


root = tk.Tk()

# \\ Register validation functions
validate_int_cmd = root.register(lambda new_value: validate_input(new_value, "int"))
validate_double_cmd = root.register(lambda new_value: validate_input(new_value, "double"))

#  \\ Using the custom IntVar with validation
int_var = GTG.IntVar(value=10, callback=on_change)
entry_int = GTG.Entry(root, textvariable=int_var, validate="key", validatecommand=(validate_int_cmd, "%P"))
entry_int.pack()

# \\ Using the custom DoubleVar with validation
double_var = GTG.DoubleVar(value=10.5, callback=on_change)
entry_double = GTG.Entry(root, textvariable=double_var, validate="key", validatecommand=(validate_double_cmd, "%P"))
entry_double.pack()

root.mainloop() 

#!----------------------------------------------------------------------------------------------------------------------------------------------------------------

#! Enum Variable use case 
# \\ Define the Enum
class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"


root = tk.Tk()

# C\\ reate an EnumVar with the Color enum
enum_var = GTG.EnumVar(enum_type=Color, value=Color.RED.value)

# \\ Create a label and an OptionMenu
label = GTG.Label(root, text="Choose a color:")
label.pack()

option_menu = tk.OptionMenu(root, enum_var, *[e.value for e in Color])
option_menu.pack()

# \\ Create a button to print the selected color
def print_selected_color():
    selected_color = enum_var.get_value()
    print(f"Selected color: {selected_color}")

button = GTG.Button(root, text="Print Selected Color", command=print_selected_color)
button.pack()

# \\ Set the value to Color.GREEN programmatically
enum_var.set_value(Color.GREEN)

root.mainloop()
