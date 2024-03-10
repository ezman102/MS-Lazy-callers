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
    ['', '0-10000', '10000-20000', '20001-30000', '30001-40000', '40001-50000', '50001-60000', 'above 60000', 'rejected'],  # 16th
]

class App:
    def __init__(self, root):
        self.root = root
        self.current_digit = 0
        self.user_input = ''
        
        self.root.title("Digit Response Program")
        
        self.entry = tk.Entry(root, width=20)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        self.display_label = tk.Label(root, text="", height=2)
        self.display_label.grid(row=1, column=0, columnspan=4)
        
        tk.Button(root, text="Submit", command=self.submit).grid(row=2, column=0)
        tk.Button(root, text="Previous", command=self.previous_digit).grid(row=2, column=1)
        tk.Button(root, text="Next", command=self.next_digit, width=10).grid(row=2, column=2)  # Increased width for easier press
        tk.Button(root, text="Clear", command=self.clear).grid(row=2, column=3)

    def submit(self):
        self.user_input = self.entry.get()
        self.current_digit = 0
        self.update_display()

    def next_digit(self):
        if self.current_digit < len(self.user_input) - 1:
            self.current_digit += 1
            self.update_display()

    def previous_digit(self):
        if self.current_digit > 0:
            self.current_digit -= 1
            self.update_display()

    def clear(self):
        self.entry.delete(0, tk.END)
        self.display_label.config(text="")
        self.user_input = ''
        self.current_digit = 0

    def update_display(self):
        if self.user_input and len(self.user_input) == 16:
            digit = int(self.user_input[self.current_digit])
            answer = answers[self.current_digit][digit]
            self.display_label.config(text=answer)
        else:
            self.display_label.config(text="Invalid input, please enter 16 digits.")

root = tk.Tk()
root.attributes("-topmost", True)

app = App(root)

root.mainloop()
