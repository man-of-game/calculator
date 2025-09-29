import tkinter as tk

# --- Functions ---

def button_click(item):
    """Appends the clicked button's value to the entry field."""
    entry.insert(tk.END, item)

def button_clear():
    """clears the entire entry field."""
    entry.delete(0, tk.END)

def button_equal():
    """Calculates the expression in the entry field."""
    try:
        result = str(eval(entry.get()))
        button_clear()
        entry.insert(0, result)
    except Exception as e:
        # If there's an error, show 'ERROR'
        button_clear()
        entry.insert(0, "ERROR")

def button_backspace():
    #Deletes the last character in the entry field.
    current_text = entry.get()
    if current_text:
        new_text = current_text[:-1] #Slice the string to remove the last character 
        entry.delete(0, tk.END)
        entry.insert(0, new_text)

# ---Main window setup ---

# creating main window
root = tk.Tk()
root.title("simple calculator")
root.geometry("450x550") #Set window size
root.resizable(False, False) #Make window not resizable
root.iconbitmap("calculator ico.ico")

# frame for the entry field
entry_frame = tk.Frame(root)
entry_frame.grid(row=0, column=0, sticky='news')

# frame to hold the widgets
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, sticky='news')

# ---configure the grid col and rows to have equal weight---
# this makes all cells in the grid the same size

for i in range(4):  #for 4 columns
    button_frame.grid_columnconfigure(i, weight =1, uniform='group1')

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1,  uniform='group2')


# ---widgets---

# entry field
entry = tk.Entry(entry_frame, width=16, font=("arial", 24), borderwidth=2, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

#Define the button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# ---create and place buttons---

#set initial row and column for the grid
row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == '=':
        # create the '=' button
        # link it to the button_equal function
        tk.Button(button_frame, text=button_text, font=("Arial", 18), command=button_equal).grid(row=row_val, column=col_val, sticky='news') #'news' makes the button fill the cell
    else:
        # create all other butons, linking them to the button_click function
        # The lambda function is used to pass the button's text to the function
        tk.Button(button_frame, text=button_text, font=('Arial', 18), command=lambda b=button_text: button_click(b)).grid(row=row_val, column= col_val, sticky='news')
   
    # move to nxt coloumn
    col_val+=1
    # if the column exceeds 3 (0,1,2,3), reset to 0 and move to the nxt row
    if col_val > 3:
        col_val = 0
        row_val+=1

# create and place the 'Clear' button separately
tk.Button(button_frame, text='Clear', font=('Arial', 15), command=button_clear).grid(row=0, column=0, columnspan=2, sticky='news')

# backspacce button
tk.Button(button_frame, text="DEL", font=('Arial', 15), command=button_backspace).grid(row=0, column=2,  columnspan=2, sticky='news' )

# ---Start the GUI---

#This line keeps the window open and listening for events (like button clicks)
root.mainloop()