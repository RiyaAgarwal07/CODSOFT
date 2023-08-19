import tkinter as tk
from math import sqrt, factorial

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry = tk.Entry(root, width=45, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=15)
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('C', 6, 0), ('←', 6, 1), ('!', 6, 2), ('√', 6, 3),
        ]
        
        for button_text, row, col in buttons:
            button = tk.Button(self.root, text=button_text, padx=25, pady=25, command=lambda text=button_text: self.handle_button_click(text))
            button.grid(row=row, column=col)
    
    def handle_button_click(self, text):
        if text == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        elif text == '<-':
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current_text[:-1])
        elif text == '!':
            try:
                num = int(self.entry.get())
                result = factorial(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == '√':
            try:
                num = float(self.entry.get())
                result = sqrt(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
