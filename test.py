import tkinter as tk

# Answers for each digit position
answers = [
   ['', '好', '幾好', '一般', '幾差', '差'],
    ['', '好好多', '稍好', '差唔多', '稍差', '差好多'],
    ['', '好', '幾好', '一般', '幾差', '差'],
    ['', '好好多', '稍好', '差唔多', '稍差', '差好多'],
    ['', '滿意', '稍滿意', '一般', '唔太滿意', '唔滿意'],
    ['', '下降好多', '稍微下降', '差唔多', '稍為上漲', '上漲好多'],
    ['', '滿意', '稍滿意', '一般', '唔太好', '非常唔好'],
    ['', '好好多', '稍好', '差唔多', '稍差', '差好多'],
    ['', '好好', '稍好', '一般', '唔太好', '非常唔好'],
    ['', '好好', '稍好', '一般', '唔太好', '非常唔好'],  # 10th
    ['', '好好', '稍好', '一般', '唔太好', '非常唔好'],  
    ['', '好好', '稍好', '一般', '唔太好', '非常唔好'],  
    ['', 'Uneducated', 'primary school', 'form 3', 'form 5', 'form 7', 'Tertiary education', 'Degree', 'rejected'],  # 13th
    ['', '18-25', '26-35', '36-45', '46-55', '56-65', '65 above', 'rejected'],  # 14th
    ['', '0-5000', '5001-10000', '10001-15000', '15001-20000', '20000-30000', '30000-40000', 'above 40000', 'rejected'],  # 15th
    ['', '0-10000', '10000-20000', '20001-30000', '30001-40000', '40001-50000', '50001-60000', 'above 60000', 'rejected'],
]

class App:
    def __init__(self, root):
        self.root = root
        self.current_digit = 0
        self.current_number_index = 0
        self.user_inputs = []  # Store multiple entries
        
        self.root.title("Digit Response Program")
        
        self.entry = tk.Entry(root, width=20)
        self.entry.grid(row=0, column=0, columnspan=2)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.grid(row=0, column=2)
        
        self.numbers_listbox = tk.Listbox(root, height=5)
        self.numbers_listbox.grid(row=1, column=0, columnspan=3, sticky="ew")
        self.numbers_listbox.bind('<<ListboxSelect>>', self.select_number)
        
        self.display_label = tk.Label(root, text="", height=2)
        self.display_label.grid(row=2, column=0, columnspan=3)
        
        tk.Button(root, text="Previous", command=self.previous_digit).grid(row=3, column=0)
        tk.Button(root, text="Next", command=self.next_digit, width=10).grid(row=3, column=1)
        tk.Button(root, text="Clear", command=self.clear).grid(row=3, column=2)

    def submit(self):
        number = self.entry.get()
        if len(number) == 16 and number.isdigit():
            self.user_inputs.append(number)
            entry_label = f"{len(self.user_inputs)}: {number}"
            self.numbers_listbox.insert(tk.END, entry_label)
            self.entry.delete(0, tk.END)
        else:
            self.display_label.config(text="Invalid input, please enter 16 digits.")

    def select_number(self, event=None):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            self.current_number_index = index
            self.current_digit = 0
            self.update_display()

    def next_digit(self):
        if self.current_digit < 15:  # Since we are dealing with 16 digits
            self.current_digit += 1
            self.update_display()

    def previous_digit(self):
        if self.current_digit > 0:
            self.current_digit -= 1
            self.update_display()

    def clear(self):
        self.user_inputs = []
        self.numbers_listbox.delete(0, tk.END)
        self.display_label.config(text="")
        self.current_digit = 0
        self.current_number_index = 0

    def update_display(self):
        if self.user_inputs:
            current_number = self.user_inputs[self.current_number_index]
            digit = int(current_number[self.current_digit])
            # Adjust the index in your answers lookup if necessary
            answer = answers[self.current_digit % len(answers)][digit]
            # Show the current digit number next to the answer
            display_text = f"{self.current_digit + 1}: {answer}"
            self.display_label.config(text=display_text)
        else:
            self.display_label.config(text="No numbers entered.")


root = tk.Tk()
app = App(root)
root.mainloop()
