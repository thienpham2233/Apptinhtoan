import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng dụng Tính Toán")

        # Responsive
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)

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
        input_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        
        input_frame.columnconfigure(1, weight=1)

        ttk.Label(input_frame, text="Số thứ nhất:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_num1 = ttk.Entry(input_frame, width=15)
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(input_frame, text="Số thứ hai:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_num2 = ttk.Entry(input_frame, width=15)
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    def create_tabs(self):
        notebook = ttk.Notebook(self.root)
        notebook.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # tab Phép tính cơ bản
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Phép tính cơ bản")
        tab1.columnconfigure(0, weight=1)
        tab1.columnconfigure(1, weight=1)
        
        btn_add = ttk.Button(tab1, text="Cộng", command=lambda: self.calculate('+'))
        btn_add.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        btn_subtract = ttk.Button(tab1, text="Trừ", command=lambda: self.calculate('-'))
        btn_subtract.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        btn_multiply = ttk.Button(tab1, text="Nhân", command=lambda: self.calculate('*'))
        btn_multiply.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        btn_divide = ttk.Button(tab1, text="Chia", command=lambda: self.calculate('/'))
        btn_divide.grid(row=1, column=1, padx=10, pady=10, sticky="ew")


        # Tab Phép tính nâng cao
        tab3 = ttk.Frame(notebook)
        notebook.add(tab3, text="Phép tính nâng cao")
        tab3.columnconfigure(0, weight=1)
        tab3.columnconfigure(1, weight=1)
        
        btn_square = ttk.Button(tab3, text="Bình phương", command=lambda: self.calculate('^2'))
        btn_square.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        btn_sqrt = ttk.Button(tab3, text="Căn bậc 2", command=lambda: self.calculate('sqrt'))
        btn_sqrt.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        btn_factorial = ttk.Button(tab3, text="Giai thừa", command=lambda: self.calculate('factorial'))
        btn_factorial.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def create_result_frame(self):       
        result_frame = ttk.Frame(self.root, padding="10")
        result_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        
        result_frame.columnconfigure(0, weight=1)

        self.result_label = ttk.Label(result_frame, text="Kết quả: ", font=('Arial', 14))
        self.result_label.grid(row=0, column=0, sticky="w")

    def format_result(self, result):
        # xuống dòng sau mỗi 10 ký tự
        result_str = str(result)
        formatted_result = "\n".join(result_str[i:i+20] for i in range(0, len(result_str), 20))
        return f"Kết quả:\n{formatted_result}"

    def calculate(self, operation):
        try:
            num1 = float(self.entry_num1.get())
            if operation in ['+', '-', '*', '/']:
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
            elif operation == '^2':
                result = num1 ** 2
            elif operation == 'sqrt':
                if num1 < 0:
                    self.result_label.config(text="Không thể lấy căn bậc 2 của số âm!")
                    return
                result = math.sqrt(num1)
            elif operation == 'factorial':
                if num1 < 0 or not num1.is_integer():
                    self.result_label.config(text="Giai thừa chỉ xác định cho số nguyên không âm!")
                    return
                result = math.factorial(int(num1))

            # Định dạng kết quả để hiển thị theo yêu cầu
            self.result_label.config(text=self.format_result(result))
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300") 
    app = CalculatorApp(root)
    root.mainloop()
