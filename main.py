from abs import ABS
from natsort import natsorted
from GUI import GUI

temp1 = "example_abs/2.abs"

abs =ABS(temp1)
abs.get_value(5, 'bf2d', True)
abs.get_value(5, 'bfma', True)


for pos in natsorted(abs.bf2d):
    text = str(pos) + "  liczba sztuk: " + str(abs.bf2d[pos])
    # label = Label(scrollable_frame, text=text)
    # label.pack()
    print(text)
#
# Label(scrollable_frame, text="\n    SIATKI\n").pack()
for pos in abs.bfma:
    text = str(pos) + "  liczba sztuk: " + str(abs.bfma[pos])
    # label = Label(scrollable_frame, text=text)
    # label.pack()


class Parameter:
    def __init__(self, path, param):
        self.path = path
        self.param = param

        self.position_nr = []
        self.quantity = []
        self.diameter = []
        self.diameter = []



