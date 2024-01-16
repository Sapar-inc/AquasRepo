import tkinter as tk
from tkinter import ttk


from plotdata import regression_plot
from stats import stats_columns

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.winfo_toplevel().title("Application")
        self.create_labels()
        self.create_entries()
        self.create_text_boxes()
        self.create_buttons()

    def create_labels(self):
        self.l1 = tk.Label(self.master, text="Filename")
        self.l2 = tk.Label(self.master, text="X Label")
        self.l3 = tk.Label(self.master, text="Y Label")

        self.l1.grid(row=0)
        self.l2.grid(row=1)
        self.l3.grid(row=2)

    def create_entries(self):
        self.eFname = tk.Entry(self.master, width=40)
        self.eX = tk.Entry(self.master, width=40)
        self.eY = tk.Entry(self.master, width=40)

        self.eFname.grid(row=0, column=1, sticky=tk.W)
        self.eX.grid(row=1, column=1, sticky=tk.W)
        self.eY.grid(row=2, column=1, sticky=tk.W)

    def create_text_boxes(self):
        self.txtX = tk.Text(self.master, width=30)
        self.txtY = tk.Text(self.master, width=30)

        self.txtX.grid(row=3, column=0, sticky=tk.W)
        self.txtY.grid(row=3, column=1, sticky=tk.W)

    def create_buttons(self):
        self.style = ttk.Style()
        self.style.map('D.TButton',
                       foreground=[('pressed', 'red'), ('active', 'green')],
                       background=[('pressed', '!disabled', 'black'), ('active', 'white')]
                       )

        self.btn = ttk.Button(self.master, text='Show Regression Graph', style="D.TButton", command=self.show_graph)
        self.btn.grid(row=4, column=0, sticky=tk.W)

        self.stats = ttk.Button(self.master, text='Show Stats', style='D.TButton', command=self.show_stats)
        self.stats.grid(row=4, column=1, sticky=tk.W)

        self.quit = ttk.Button(self.master, text='Quit', style='D.TButton', command=self.master.destroy)
        self.quit.grid(row=4, column=1, sticky=tk.E)

    def show_graph(self):
        regression_plot(self.eFname.get(), self.eX.get(), self.eY.get())

    def show_stats(self):
        xstats, ystats = stats_columns(self.eFname.get(), self.eX.get(), self.eY.get())
        self.txtX.insert(tk.INSERT, xstats)
        self.txtY.insert(tk.INSERT, ystats)