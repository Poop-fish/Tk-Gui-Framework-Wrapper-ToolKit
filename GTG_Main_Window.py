from GTG_imports import *
from GTG_Widgets import *
#! ------------------------  init / Main Window -------------------------------------------------------------    
class MainWindow():
    def __init__(self, title="GTG Application", width=800, height=600):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.configure(bg="#2b2b2b")

        #* \\ Main frame to hold widgets \\
        self.main_frame = GTG.Frame(self.root, bg="#2b2b2b" , enable_hover=False , relief="flat")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def RunWindow(self):
        """Start the main event loop."""
        self.root.mainloop()
    
    def add_widget(self, widget_class, *args, **kwargs):
        """
        Add a widget to the main frame.
        
        Parameters:
        - widget_class: The class of the widget to be added.
        - *args, **kwargs: Additional arguments to pass to the widget constructor.
        """
        widget = widget_class(self.main_frame, *args, **kwargs)
        widget.pack(pady=10)
        return widget
    
    def root_widget(self, widget_class, *args, **kwargs):
        """
        Add a widget directly to the root window.
        
        Parameters:
        - widget_class: The class of the widget to be added.
        - *args, **kwargs: Additional arguments to pass to the widget constructor.
        """
        widget = widget_class(self.root, *args, **kwargs)
        widget.pack(pady=10)
        return widget
#! -------------------------------------------------------------------------------------------------------------------------
