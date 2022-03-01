import numpy as np
temp1 = "example_abs/1.abs"


class ABS:
    """
    Create ABS object, that has a methods for .abs files maintenance.
    It takes path with .abs file name as an input
    """
    # DATA TYPES:
    # • BF2D two dimensional bending shapes
    # • BF3D three dimensional bending shapes
    # • BFWE helixes and spirals
    # • BFMA reinforcing steel meshes
    # • BFGT lattice girders
    # • BFAU spacers an supporting cages
    def __init__(self, abs_file_loc):

        self.abs_file_loc = abs_file_loc
        self.abs_file = open(abs_file_loc)
        self.list_of_lines = []
        self.numbers = []
        self.bf2d = {}
        self.bf3d = {}
        self.bfwe = {}
        self.bfma = {}
        self.bfgt = {}
        self.bfau = {}

        self.getlines()

    def getlines(self):
        """
        Appends each line of .abs as a single element to self.list_of_lines list.
        :return:
        """

        for line in self.abs_file.readlines():
            char_list = []
            for i in line:
                char_list.append(i)
            self.list_of_lines.append(char_list)

    def search_symbol(self, line, symbol):
        """
        It will search index of each appearance of given symbol in passed (line) and append it to symbol_indexes list.
        :param symbol: symbol which indexes you want to search for
        :param line: list of elements from one line (one bar/mesh from .abs).
        :return: list with indexes of each appearance of chosen symbol
        """
        symbol_indexes =[]
        for index, char in enumerate(line):
            if str(char) == str(symbol):
                symbol_indexes.append(index)
        return symbol_indexes

    def get_pos_numbers(self):
        """
        Get position numbers and append unique ones to self.numbers list, for all positions in file.
        :return:
        """
        # position number appears after 4th "@" symbol
        for line in self.list_of_lines:
            index = self.search_symbol(line, '@')
            self.numbers.append(''.join(line[index[3]+1:index[4]]))
        return np.unique(self.numbers)

    def get_value(self, at_before, data_type, do_sum=False, delete_first=True):
        # decide whether or not to skip first sign (if it is a letter before number for example)
        if delete_first:
            factor = 2
        else:
            factor = 1

        # number of pieces appears after 6th "@" symbol

        unique_positions = self.get_pos_numbers()
        pos_dict = {}
        for nr in unique_positions:
            current_value = 0
            for line in self.list_of_lines:
                index = self.search_symbol(line, '@')   #list of "@" index
                if ''.join(line[0:4]) == str(data_type.upper()):
                    if ''.join(line[index[3]+1:index[4]]) == nr:
                        if do_sum == True:
                            print(line[index[at_before]+factor:index[at_before+1]])
                            current_value += float(''.join(line[index[at_before]+factor:index[at_before+1]]))
                        elif do_sum == False:
                            current_value = ''.join(line[index[at_before]+factor:index[at_before+1]])
            if current_value != 0:
                pos_dict[nr] = current_value
        # return pos_dict
        if data_type == 'bf2d':
            self.bf2d = pos_dict
        elif data_type == 'bfma':
            self.bfma = pos_dict





#line[index[first_at]+1:index[last_at]]
ind = []
abs = ABS(temp1)
abs.get_value(5, 'bfma', True, True)
abs.get_value(5, 'bf2d', True, True)
x = abs.bfma
y = abs.bf2d
print('MESHES:')
for i in x:
    print(i, ' number of pieces: ', x[i])
print('REBARS:')
for i in y:
    print(i, ' number of pieces: ', y[i])
x=[1,2,3,4,5,6,7,8,9]

# print(x[2:5])

# # test whether search_symbol method works
# for line in abs.list_of_lines:
#     index = abs.search_symbol(line)
#     ind.append(index)
#
# for i in ind:
#     print(i)

