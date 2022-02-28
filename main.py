temp1 = "example_abs/1.abs"


class ABS:
    """
    Create ABS object, that has a methods for .abs files maintenance.
    It takes path with .abs file name as an input
    """

    def __init__(self, abs_file_loc):

        self.abs_file_loc = abs_file_loc
        self.abs_file = open(abs_file_loc)
        self.list_of_lines = []

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

    def search_ats(self, line):
        """
        It will search index of each "@" in given string and append it to at_indexes list.
        :param line:
        :return:
        """
        at_indexes =[]
        for index, char in enumerate(line):
            if char == "@":
                at_indexes.append(index)
        return at_indexes



ind = []
abs = ABS(temp1)
abs.getlines()

# test whether search_ats method works
for line in abs.list_of_lines:
    index = abs.search_ats(line)
    ind.append(index)

for i in ind:
    print(i)

