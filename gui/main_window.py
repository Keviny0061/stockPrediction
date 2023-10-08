from tkinter import Frame, Label, Entry, Button, StringVar, Toplevel, ttk
from data.fetch_data import get_stock_data

class MainWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(padx=20, pady=20)  # Added some padding
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Enter Stock Ticker:")  # Using ttk.Label
        self.label.grid(row=0, column=0, padx=10, pady=10)  # Added some padding

        self.entry = ttk.Entry(self, font=('Arial', 12))  # Using ttk.Entry and added a font
        self.entry.grid(row=0, column=1, padx=10, pady=10)  # Added some padding

        self.submit_btn = ttk.Button(self, text="Fetch Data", command=self.fetch_data)  # Using ttk.Button
        self.submit_btn.grid(row=0, column=2, padx=10, pady=10)  # Added some padding

        self.output_label = StringVar()
        self.output_display = ttk.Label(self, textvariable=self.output_label, font=('Arial', 12))  # Using ttk.Label and added a font
        self.output_display.grid(row=1, column=0, columnspan=3, padx=10, pady=10)  # Added some padding

    def fetch_data(self):
        ticker = self.entry.get()
        data = get_stock_data(ticker)
        
        if data:
            output = f"Price: {data['price']} | Volume: {data['volume']}"
        else:
            output = "Invalid ticker or data not available."
        
        self.output_label.set(output)
