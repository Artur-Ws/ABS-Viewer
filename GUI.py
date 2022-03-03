from tkinter import ttk
from tkinter import *



root = Tk()
root.title('BVBS-Viewer')
root.geometry('1200x800')
first = ttk.Frame(root, borderwidth=3, width=100, height=1000)
first.grid_propagate(0)
first["width"]=100
container = ttk.Frame(root, width=100, height=1000)
canvas = Canvas(first)

scrollbar = ttk.Scrollbar(first, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
    Label(scrollable_frame, text="    PRĘTY\n").pack()


first.pack(side="left", fill="both", expand=True)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
root.mainloop()
