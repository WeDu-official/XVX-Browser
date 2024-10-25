import os
x = open('coc.txt','r')
folder_to_remove:str = x.read().strip('\n')
x.close()
def remove_folder_recursively(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a directory.")
        return
    for root, dirs, files in os.walk(folder_path):
        print(f"Folder: {root}")
        for dir in dirs:
            print(f"  Subfolder: {os.path.join(root, dir)}")
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except (PermissionError,OSError):
                pass
        for dir in dirs:
            try:
                os.rmdir(os.path.join(root,dir))
            except (PermissionError,OSError):
                pass
    print(f"Folder '{folder_path}' and its contents have been removed.")
remove_folder_recursively(folder_to_remove)
o = open('chi2.txt','r')
d = o.read()
o.close()
if d == '':
    os.startfile('main.py')