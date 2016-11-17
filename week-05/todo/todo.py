import open_screen, sys, csv

class Todo:

    def argument_function(self, argv):

        self.argument = argv
        self.read_file()

        if self.argument[0] == '-l':
            self.print_todo_list()

        elif self.argument[0] == '-a':
            if len(self.argument) == 1:
                print('\nNo task is provided')
            else:
                self.add_task(self.argument[1])
                self.write_file()

        elif self.argument[0] == '-r':
            if len(self.argument) == 1:
                print('\nUnable to remove: No index is provided')
            else:
                try:
                    if int(self.argument[1]) < 1 or int(self.argument[1]) > len(self.todo_list):
                        print('\nUnable to remove: Index is out of bound')
                    else:
                        self.remove_task(int(self.argument[1]))
                        self.write_file()
                except:
                    print('\nIndex is not a number!')

        elif self.argument[0] == '-c':
            if len(self.argument) == 1:
                print('\nUnable to check: No index is provided')
            else:
                try:
                    if int(self.argument[1]) < 1 or int(self.argument[1]) > len(self.todo_list):
                        print('\nUnable to check: Index is out of bound')
                    else:
                        self.argument[0] == '-c'
                        self.check_task(int(self.argument[1]))
                        self.write_file()
                except:
                    print('\nIndex is not a number!')

        else:
            print('\n___!!! Unsupported argument !!!___')
            open_screen.draw_screen()

    def read_file(self):
        try:
            f = open('todo_storage.csv', 'r')
            self.todo_list = f.readlines()
            f.close()
        except:
            self.todo_list = []

    def write_file(self):
        f = open('todo_storage.csv', 'w')
        f.writelines(self.todo_list)
        f.close()

    def add_task(self, new_task):
        self.todo_list.append('[ ] ' + new_task + '\n')

    def remove_task(self, nth):
        self.todo_list.pop(nth - 1)

    def print_todo_list(self):
        print()
        if len(self.todo_list) == 0:
            print('No todos for today! :)')
        else:
            for i in range(len(self.todo_list)):
                print(i + 1, ' - ', self.todo_list[i][:-1])

    def check_task(self, nth):
        self.todo_list[nth-1] = '[X]' + self.todo_list[nth-1][3:]

my_todo = Todo()

if len(sys.argv) != 1:
    my_todo.argument_function(sys.argv[1:])

else:
    open_screen.draw_screen()
