import os

def draw_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Python Todo application')
    print('=======================')
    print('')
    print('Command line arguments:')
    print('-l   Lists all the tasks')
    print('-a   Adds a new task')
    print('-r   Removes a task')
    print('-c   Completes a task')
    print('')
