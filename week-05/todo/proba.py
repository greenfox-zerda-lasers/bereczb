def file_ops(op):
    f = open('todo_storage.csv', 'r+')
    todo_list = f.readlines()
    f.close()
    f2 = open('todo_storage2.csv', 'r+')
    f2.writelines(todo_list)
    f2.close()

file_ops(0)
