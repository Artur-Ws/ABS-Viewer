from tkinter import ttk
from tkinter import filedialog
from tkinter import *


class GUI:

    def __init__(self):
        self.root = Tk()

        # Config:
        self.headings = ['pos_nr', 'diameter', 'pieces', 'shape']
        self.head_names = ['Numer pozycji', 'Średnica', 'Liczba sztuk', 'Kształt']
        self.root.title('BVBS-Viewer')
        # self.root.geometry('1400x800')
        self.label = Label(self.root, text=" Przykładowa lokalizacja pliku")
        self.abs_path = ' '

        self.main_process()

    def main_process(self):

        button = ttk.Button(self.root, text='Wybierz plik', command=self.search_path)
        button.grid(row=0, column=0, sticky="w")

        self.label.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.make_tree()

        self.root.mainloop()

    def make_tree(self):

        tree = ttk.Treeview(self.root, columns=self.headings, show='headings')

        for heading, heading_name in zip(self.headings, self.head_names):
            tree.heading(heading, text=heading_name)
        tree.grid(row=1, column=0, columnspan=2, sticky="nsew")

        scroll = ttk.Scrollbar(self.root)
        scroll.grid(row=1, column=2, sticky="nse")
        scroll.configure(command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)

        # for i in range(50):
        e = [[1, 2, 3], [4, 5, 6]]
        tree.insert('', END, values=e)

    def search_path(self):
        self.abs_path = filedialog.askdirectory()
        self.label.configure(text='Wybrany plik: ' + str(self.abs_path))

    def spacer(self, amount):
        space = ''
        for i in range(amount):
            space  += ' '
        return space


x = GUI()




#
# root = Tk()
# top_frame = Frame(root, bg='blue', height=50)
# bottom_frame = Frame(root, bg='black')
# top_frame.pack_propagate(0)
# # bottom_frame.pack_propagate(0)
#
#
# label = Label(top_frame, text = 'qwertuiop')
# b_label = Label(bottom_frame, text='    5   ')
# top_frame.pack(fill='x')
# bottom_frame.pack(fill='both')
# label.pack()
# b_label.pack()
# root.mainloop()











# root = Tk()
# root.title('BVBS-Viewer')
# root.geometry('1200x800')
# first = ttk.Frame(root, borderwidth=3, width=100, height=1000)
# first.grid_propagate(0)
# first["width"]=100
# container = ttk.Frame(root, width=100, height=1000)
# canvas = Canvas(first)
#
# scrollbar = ttk.Scrollbar(first, orient="vertical", command=canvas.yview)
# scrollable_frame = ttk.Frame(canvas)
# scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# canvas.configure(yscrollcommand=scrollbar.set)
#
# for i in range(50):
#     Label(scrollable_frame, text="    PRĘTY\n").pack()
#
#
# first.pack(side="left", fill="both", expand=True)
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")
# root.mainloop()
