import open_screen
import sys, getopt

class todo:

    def main(self, argv):
        pass
    #    # inputfile = ''
    #    # outputfile = ''
    #    # try:
    #    #    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    #    # except getopt.GetoptError:
    #    #    print 'test.py -i <inputfile> -o <outputfile>'
    #    #    sys.exit(2)
    #    # for opt, arg in opts:
    #    #    if opt == '-h':
    #    #       print 'test.py -i <inputfile> -o <outputfile>'
    #    #       sys.exit()
    #    #    elif opt in ("-i", "--ifile"):
    #    #       inputfile = arg
    #    #    elif opt in ("-o", "--ofile"):
    #    #       outputfile = arg
    #    # print 'Input file is "', inputfile
    #    # print 'Output file is "', outputfile
    #

    def read_file(self):
        f = open('todo_storage.csv', 'r')
        self.todo_list = f.readlines()
        f.close()

    def write_file(self):
        f = open('todo_storage.csv', 'w')
        f.writelines(self.todo_list)
        f.close()

    def print_todo_list(self):
        print(file_ops(read))



if __name__ == "__main__":
   main(sys.argv[1:])

open_screen.draw_screen()
