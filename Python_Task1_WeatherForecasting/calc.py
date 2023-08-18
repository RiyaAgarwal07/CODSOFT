import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operator_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                result = "Error: Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numeric values.")
    except Exception as e:
        result_label.config(text=str(e))


# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Create widgets
entry_num1 = tk.Entry(app)
entry_num2 = tk.Entry(app)
operator_var = tk.StringVar()
operator_var.set("Addition")
operation_menu = tk.OptionMenu(app, operator_var, "Addition", "Subtraction", "Multiplication", "Division")
calculate_button = tk.Button(app, text="Calculate", command=calculate)
result_label = tk.Label(app, text="Result: ")

# Grid layout for widgets
entry_num1.grid(row=0, column=0, padx=5, pady=5)
operation_menu.grid(row=0, column=1, padx=5, pady=5)
entry_num2.grid(row=0, column=2, padx=5, pady=5)
calculate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Start the main event loop
app.mainloop()
