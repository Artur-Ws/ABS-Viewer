from abs import ABS
from natsort import natsorted
from GUI import GUI

abs_path = "example_abs/2.abs"
gui = GUI()
rebar_values = []
mesh_values = []


abs = ABS(abs_path)
# Get number of pieces
abs.get_value(5, 'bf2d', do_sum=True)
abs.get_value(5, 'bfma', do_sum=True)


def fill_value_list(datatype, value_list):
    """
    Gets empty list of values and appends sub-lists with data for each position from bvbs.
    :param datatype: Datatype dictionary from ABS class. For example "ABS.bf2d"
    :param value_list: Empty list for specific datatype - rebars or meshes for example.
    :return:
    """

    # ADD POSITION NUMBER LIST
    for pos in natsorted(datatype):
        value_list.append([str(pos)])

    # ADD DIAMETER FOR EACH POSITION
    i = 0
    for pos in natsorted(datatype):
        value_list[i].append(str(datatype[pos]))
        i += 1
        # text = str(pos) + "  liczba sztuk: " + str(abs.bf2d[pos])

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


fill_value_list(abs.bf2d, rebar_values)
print(rebar_values)
