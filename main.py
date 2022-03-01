from abs import ABS
from tkinter import *
temp1 = "example_abs/1.abs"

abs =ABS(temp1)
abs.get_value(5, 'bf2d', True)


root = Tk()
for pos in abs.bf2d:
    text = str(pos) + "  liczba sztuk: " + str(abs.bf2d[pos])
    label = Label(root, text=text)
    label.pack()

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
