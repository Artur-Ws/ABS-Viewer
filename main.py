temp1 = "example_abs/1.abs"


class ABS:

    def __init__(self, abs_file_loc):

        self.abs_file_loc = abs_file_loc
        self.abs_file = open(abs_file_loc)

    def getlines(self):

        for line in self.abs_file.readlines():
            print(line)
            print("####################")
            linelist = []
            for i in line:
                linelist.append(i)
                print(linelist)


abs = ABS(temp1)
abs.getlines()