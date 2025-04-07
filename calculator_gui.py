import tkinter as tk
from tkinter import messagebox

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
            input_var.set("")
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Global variables
expression = ""
input_var = tk.StringVar()

# Entry widget to display the current expression
entry = tk.Entry(root, textvar=input_var, font=("Arial", 20), justify="right", bd=10, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Create buttons dynamically
for row in buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(button_row, text=btn_text, font=("Arial", 18), relief=tk.RAISED, bd=5)
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", click)

# Run the main loop
root.mainloop()