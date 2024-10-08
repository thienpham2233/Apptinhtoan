import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Tính Toán")

        self.create_menu()

        self.create_input_frame()

        self.create_tabs()

        self.create_result_frame()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Thoát", command=self.root.quit)

    def create_input_frame(self):
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Số thứ nhất:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_num1 = ttk.Entry(input_frame, width=15)
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Số thứ hai:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_num2 = ttk.Entry(input_frame, width=15)
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)

    def create_tabs(self):
        notebook = ttk.Notebook(self.root)
        notebook.grid(row=1, column=0, padx=10, pady=10)

        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Cộng & Trừ")

        btn_add = ttk.Button(tab1, text="Cộng", command=lambda: self.calculate('+'))
        btn_add.grid(row=0, column=0, padx=10, pady=10)

        btn_subtract = ttk.Button(tab1, text="Trừ", command=lambda: self.calculate('-'))
        btn_subtract.grid(row=0, column=1, padx=10, pady=10)

        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Nhân & Chia")

        btn_multiply = ttk.Button(tab2, text="Nhân", command=lambda: self.calculate('*'))
        btn_multiply.grid(row=0, column=0, padx=10, pady=10)

        btn_divide = ttk.Button(tab2, text="Chia", command=lambda: self.calculate('/'))
        btn_divide.grid(row=0, column=1, padx=10, pady=10)

    def create_result_frame(self):       
        result_frame = ttk.Frame(self.root, padding="10")
        result_frame.grid(row=2, column=0, padx=10, pady=10)

        self.result_label = ttk.Label(result_frame, text="Kết quả: ", font=('Arial', 14))
        self.result_label.grid(row=0, column=0)

    def calculate(self, operation):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    self.result_label.config(text="Không thể chia cho 0!")
                    return
                result = num1 / num2

            self.result_label.config(text=f"Kết quả: {result}")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()