import open_screen
import sys, getopt
import csv

class Todo:

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
        for i in range(len(self.todo_list)):
            print(i + 1, ' - ', self.todo_list[i][4:-1])

    def add_task(self):
        self.todo_list.append('[ ] ' + self.new_task + '\n')

    def remove_task(self, nth):
        self.nth = nth
        self.todo_list.pop(self.nth - 1)

    def checked_state(self):
        for i in range(len(self.todo_list)):
            print(i + 1, ' - ', self.todo_list[i][:-1])

    def proba(self):
        self.new_task = 'qwerty'
        self.read_file()
        print(self.todo_list)
        self.print_todo_list()
        self.add_task()
        print('')
        self.print_todo_list()
        print(self.todo_list)
        print('')
        self.remove_task(2)
        self.print_todo_list()
        print(self.todo_list)
        self.checked_state()


my_todo = Todo()

if __name__ == "__main__":
   my_todo.main(sys.argv[1:])

open_screen.draw_screen()

# my_todo.print_todo_list()

my_todo.proba()
