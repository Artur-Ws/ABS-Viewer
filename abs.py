import numpy as np


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

    def search_symbol_index(self, line, symbol):
        """
        It will search index of each appearance of given symbol in passed (line) and append it to symbol_indexes list.
        :param symbol: symbol which indexes you want to search for
        :param line: list of elements from one line (one bar/mesh from .abs).
        :return: list with indexes of each appearance of chosen symbol
        """
        symbol_indexes = []
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
            index = self.search_symbol_index(line, '@')
            self.numbers.append(''.join(line[index[3]+2:index[4]]))
        return np.unique(self.numbers)

    def get_value(self, at_before, data_type, do_sum=False, delete_first=True):
        """
        Get values of given parameter passed by 'at_before' and assign it to one of specific datatype lists.\n
        Possible datatypes:
            bf2d - 2d shapes,\n
            bfma - meshes,\n
            bf3d - 3d shapes,\n
            bfgt - lattice girders,\n
            bfwe - helixes and spirals,\n
            bfau - spacers an supporting cages.
        :param at_before: value after wchich "@" in a row (starts with "0" value).
        :param data_type: one of datatype shown above.
        :param do_sum: warning - pass True only for summable values like number of pieces, or if you want i.e. total mass.
        :param delete_first: Whether or not to delete first sign of value (it is usually letter irrelevant for value).
        :return:
        """
        # decide whether or not to skip first sign (if it is a letter before number for example)
        if delete_first:
            factor = 2
        else:
            factor = 1

        # number of pieces appears after 6th "@" symbol

        unique_positions = self.get_pos_numbers()
        pos_dict = {}
        # for each position in table
        for nr in unique_positions:
            current_value = 0
            # for each line in .abs file
            for line in self.list_of_lines:
                index = self.search_symbol_index(line, '@')   # list of "@" index
                # if datatype of that line (first 4 letters) match with given datatype
                if ''.join(line[0:4]) == str(data_type.upper()):
                    # if position number in table from top loop match position number of actual line
                    if ''.join(line[index[3]+2:index[4]]) == nr:
                        if do_sum:
                            # print(line[index[at_before]+factor:index[at_before+1]])
                            current_value += float(''.join(line[index[at_before]+factor:index[at_before+1]]))
                        elif not do_sum:
                            current_value = ''.join(line[index[at_before]+factor:index[at_before+1]])
            if current_value != 0:
                pos_dict[nr] = current_value
        # return pos_dict
        if data_type == 'bf2d':
            self.bf2d = pos_dict
        elif data_type == 'bfma':
            self.bfma = pos_dict
        elif data_type == 'bf3d':
            self.bf3d = pos_dict
        elif data_type == 'bfgt':
            self.bfgt = pos_dict
        elif data_type == 'bfwe':
            self.bfwe = pos_dict
        elif data_type == 'bfau':
            self.bfau = pos_dict
