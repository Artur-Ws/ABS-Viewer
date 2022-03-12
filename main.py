from abs import ABS
from natsort import natsorted
from GUI import GUI

abs_path = "example_abs/1.abs"
gui = GUI()
rebar_values = []
mesh_values = []

# ---- NUMBERS FOR SPECIFIC VALUES ----
# "4" - for length
# "5" - for number of pieces
# "7" - for diameter


def fill_value_list(datatype, value_list):
    """
    Gets empty list of values and appends sub-lists with data for each position from bvbs.

    :param datatype: Datatype string, for rebars it will be "bf2d"
    :param value_list: Empty list for specific datatype - rebars or meshes for example.
    :return:
    """

    abs = ABS(abs_path)
    abs.get_value(5, datatype, do_sum=True)

    def refresh():
        if datatype == 'bf2d':
            abs_dict = abs.bf2d
        elif datatype == 'bfma':
            abs_dict = abs.bfma
        elif datatype == 'bf3d':
            abs_dict = abs.bf3d
        elif datatype == 'bfgt':
            abs_dict = abs.bfgt
        elif datatype == 'bfwe':
            abs_dict = abs.bfwe
        elif datatype == 'bfau':
            abs_dict = abs.bfau
        return abs_dict

    # ADD POSITION NUMBER LIST
    abs_dict = refresh()
    for pos in natsorted(abs_dict):
        value_list.append([str(pos)])

    # ADD NUMBER OF PIECES FOR EACH POSITION
    i = 0
    for pos in natsorted(abs_dict):
        value_list[i].append(str(abs_dict[pos]))
        i += 1

    # ADD DIAMETER FOR EACH POSITION
    i = 0
    abs.get_value(7, datatype)
    abs_dict = refresh()
    for pos in natsorted(abs_dict):
        value_list[i].append(str(abs_dict[pos]))
        i += 1

    # ADD LENGTH FOR EACH POSITION
    i = 0
    abs.get_value(4, datatype)
    abs_dict = refresh()
    for pos in natsorted(abs_dict):
        value_list[i].append(str(abs_dict[pos]))
        i += 1


fill_value_list('bf2d', rebar_values)
print(rebar_values)
