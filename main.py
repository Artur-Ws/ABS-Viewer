from abs import ABS
from tkinter import ttk
from tkinter import *
# from natsort import natsorted
temp1 = "example_abs/2.abs"

abs =ABS(temp1)
abs.get_value(5, 'bf2d', True)
abs.get_value(5, 'bfma', True)


root = Tk()
root.title('BVBS-Viewer')
# root.geometry('300x800')

container = ttk.Frame(root)
canvas = Canvas(container)

scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

Label(scrollable_frame, text="    PRĘTY\n").pack()
for pos in sorted(abs.bf2d):
    text = str(pos) + "  liczba sztuk: " + str(abs.bf2d[pos])
    label = Label(scrollable_frame, text=text)
    label.pack()

Label(scrollable_frame, text="\n    SIATKI\n").pack()
for pos in abs.bfma:
    text = str(pos) + "  liczba sztuk: " + str(abs.bfma[pos])
    label = Label(scrollable_frame, text=text)
    label.pack()

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
root.mainloop()

# #line[index[first_at]+1:index[last_at]]
# ind = []
# abs = ABS(temp1)
# abs.get_value(5, 'bfma', True, True)
# abs.get_value(5, 'bf2d', True, True)
# x = abs.bfma
# y = abs.bf2d
# print('MESHES:')
# for i in x:
#     print(i, ' number of pieces: ', x[i])
# print('REBARS:')
# for i in y:
#     print(i, ' number of pieces: ', y[i])
# x = [1,2,3,4,5,6,7,8,9]
#
# # print(x[2:5])
#
# # # test whether search_symbol_index method works
# # for line in abs.list_of_lines:
# #     index = abs.search_symbol_index(line)
# #     ind.append(index)
# #
# # for i in ind:
# #     print(i)
#
