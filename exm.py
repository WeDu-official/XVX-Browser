import tkinter as tk
import os
import subprocess
# Define the path to the extensions folder

class ExtensionManager:

    def __init__(self):
        # Initialize the list of extension names
        self.extension_names = []

        # Find all the Python files in the extensions folder
        EXTENSIONS_PATH = "extensions"
        for file_name in os.listdir(EXTENSIONS_PATH):
            if file_name.endswith(".html"):
                self.extension_names.append(file_name[:-5])

        # Create the GUI
        self.root = tk.Tk()
        self.root.title("Extension Manager")
        self.root.geometry('350x400')
        # Create the listbox
        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        for name in self.extension_names:
            self.listbox.insert(tk.END, name)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.LEFT, padx=5)

        select_button = tk.Button(button_frame, text="Select All", command=self.select_all)
        select_button.pack(pady=5)

        deselect_button = tk.Button(button_frame, text="Deselect All", command=self.deselect_all)
        deselect_button.pack(pady=5)

        delete_selected_button = tk.Button(button_frame, text="Delete Selected", command=self.delete_selected)
        delete_selected_button.pack(pady=5)

        delete_all_button = tk.Button(button_frame, text="Delete All", command=self.delete_all)
        delete_all_button.pack(pady=5)

        open_selected_button = tk.Button(button_frame, text="Open Selected", command=self.open_selected)
        open_selected_button.pack(pady=5)

        # Start the mainloop
        self.root.mainloop()

    def select_all(self):
        self.listbox.select_set(0, tk.END)

    def deselect_all(self):
        self.listbox.selection_clear(0, tk.END)

    def delete_selected(self):
        selected_indices = self.listbox.curselection()
        for index in reversed(selected_indices):
            name = self.extension_names[index]
            file_path = os.path.join(EXTENSIONS_PATH, name + ".py")
            os.remove(file_path)
            self.extension_names.pop(index)
            self.listbox.delete(index)

    def delete_all(self):
        for name in self.extension_names:
            file_path = os.path.join(EXTENSIONS_PATH, name + ".py")
            os.remove(file_path)
        self.extension_names.clear()
        self.listbox.delete(0, tk.END)

    def open_selected(self):
        selected_indices = self.listbox.curselection()
        for index in selected_indices:
            name = self.extension_names[index]
            file_path = os.path.join(EXTENSIONS_PATH, name + ".py")
            file_abs_path = os.path.abspath(file_path)
            # check if the file has a GUI
            with open(file_abs_path, "r") as f:
                first_line = f.readline().strip()
            has_gui = "Tkinter" in first_line or "tkinter" in first_line or "PyQt" in first_line or "wx" in first_line

            # open the file using os.startfile or subprocess.Popen
            if has_gui:
                subprocess.Popen(["python", file_abs_path], creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                os.startfile(file_abs_path)

# Create an instance of the ExtensionManager class
extension_manager = ExtensionManager()
