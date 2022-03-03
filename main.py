from abs import ABS

from natsort import natsorted
temp1 = "example_abs/2.abs"

abs =ABS(temp1)
abs.get_value(5, 'bf2d', True)
abs.get_value(5, 'bfma', True)


for pos in natsorted(abs.bf2d):
    text = str(pos) + "  liczba sztuk: " + str(abs.bf2d[pos])
    # label = Label(scrollable_frame, text=text)
    # label.pack()
#
# Label(scrollable_frame, text="\n    SIATKI\n").pack()
for pos in abs.bfma:
    text = str(pos) + "  liczba sztuk: " + str(abs.bfma[pos])
    # label = Label(scrollable_frame, text=text)
    # label.pack()


class Position(ABS):
    def __init__(self):
        pass


