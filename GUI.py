from tkinter import ttk
from tkinter import *



root = Tk()
root.title('BVBS-Viewer')
root.geometry('1200x800')

container = ttk.Frame(root, width=1000, height=1000)
canvas = Canvas(container)

scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

Label(scrollable_frame, text="    PRĘTY\n").pack()


container.pack(fill="both", expand=True)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
root.mainloop()
