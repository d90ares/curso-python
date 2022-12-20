import os

cwd = os.getcwd()
full_list = os.listdir(cwd)
file_list = [i for i in full_list if os.path.isfile[i] and '.py' not in i]
types = list(set([i.split('.')[1] for i in file_list]))

for file in file_list:
    from_path = os.path.join(cwd, file)
    to_path = os.path.join(cwd, file.split('.')[-1], file)

    os.replace(from_path, to_path)
